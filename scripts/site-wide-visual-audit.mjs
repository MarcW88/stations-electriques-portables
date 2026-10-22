import { chromium } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const root = process.cwd();
const paths = execFileSync('git', ['ls-files', '--', '**/index.html', 'index.html'], { encoding: 'utf8' })
  .trim().split('\n').filter(p => p && !p.startsWith('.agents/')).sort();
const routes = [...new Set(paths.map(p => p === 'index.html' ? '/' : '/' + p.slice(0, -'index.html'.length)))];
const base = (process.env.AUDIT_BASE_URL || 'https://stations-electriques-portables.fr').replace(/\/$/, '');
const dir = path.resolve('.artifacts/design-review/site-wide');
const viewports = [{name:'desktop',width:1440,height:1000},{name:'mobile',width:390,height:844}];
await mkdir(dir, {recursive:true});
const browser=await chromium.launch({headless:true});
const results=[];
for (const viewport of viewports) {
  const context=await browser.newContext({viewport:{width:viewport.width,height:viewport.height},reducedMotion:'reduce'});
  for(const route of routes){
    const page=await context.newPage(), errors=[], failedResources=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.on('requestfailed',r=>failedResources.push({url:r.url(),error:r.failure()?.errorText}));
    let status=null, navigationError=null;
    try{
      const response=await page.goto(base+route,{waitUntil:'domcontentloaded',timeout:25000});
      status=response?.status()??null;
      await page.waitForTimeout(400);
      const facts=await page.evaluate(()=>{
        const imgs=[...document.images],header=document.querySelector('.site-header'),toc=document.querySelector('.toc-list');
        const links=[...document.querySelectorAll('.toc-list a')];
        const scroll=document.documentElement.scrollWidth,client=document.documentElement.clientWidth;
        return {title:document.title,h1:document.querySelectorAll('h1').length,headings:document.querySelectorAll('h2').length,
          missingH2Ids:[...document.querySelectorAll('h2')].filter(x=>!x.id).map(x=>x.textContent.trim().slice(0,80)),
          tocLinks:links.length,invalidToc:links.filter(a=>a.hash&&!document.getElementById(decodeURIComponent(a.hash.slice(1)))).length,
          horizontalOverflow:scroll>client,scrollWidth:scroll,clientWidth:client,
          overflowElements:[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.right>window.innerWidth+2||r.left< -2)&&getComputedStyle(e).position!=='fixed'}).slice(0,12).map(e=>({tag:e.tagName,cls:String(e.className||'').slice(0,100),width:Math.round(e.getBoundingClientRect().width),right:Math.round(e.getBoundingClientRect().right)})),
          images:imgs.length,brokenImages:imgs.filter(img=>!img.complete||img.naturalWidth===0).map(img=>img.src).slice(0,12),
          missingAlts:imgs.filter(img=>!img.hasAttribute('alt')).length,
          headerHeight:header?.getBoundingClientRect().height??null,
          sidebarWidth:document.querySelector('.content-sidebar')?.getBoundingClientRect().width??null,
          tables:document.querySelectorAll('table').length,
          placeholder:document.body.innerText.includes('Contenu à rédiger')};
      });
      const safe=(route.replace(/^\/+|\/+$/g,'').replaceAll('/','--')||'home');
      await page.screenshot({path:path.join(dir,safe+'--'+viewport.name+'.png'),fullPage:true});
      results.push({route,viewport:viewport.name,status,...facts,errors,failedResources:failedResources.slice(0,12)});
    }catch(e){navigationError=String(e);results.push({route,viewport:viewport.name,status,navigationError,errors,failedResources:failedResources.slice(0,12)});}
    await page.close();
  }
  await context.close();
}
await browser.close();
const summary={routes:routes.length,checks:results.length,failedNavigation:results.filter(x=>x.navigationError||!x.status||x.status>=400).length,overflow:results.filter(x=>x.horizontalOverflow).length,brokenImagePages:results.filter(x=>x.brokenImages?.length).length,missingAltPages:results.filter(x=>x.missingAlts).length,invalidTocPages:results.filter(x=>x.invalidToc).length};
await writeFile(path.join(dir,'report.json'),JSON.stringify({base,viewports,routes,summary,results},null,2));
await writeFile(path.join(dir,'summary.md'),['# Audit automatique desktop/mobile', '', 'Attention : les captures nécessitent une revue humaine pour juger du design.','',...Object.entries(summary).map(([k,v])=>'- '+k+': '+v),'', '## Pages avec anomalies','',...results.filter(x=>x.navigationError||x.status>=400||x.horizontalOverflow||x.brokenImages?.length||x.invalidToc).map(x=>'- '+x.route+' '+x.viewport+': HTTP '+x.status+', overflow '+!!x.horizontalOverflow+', images cassées '+(x.brokenImages?.length??'n/a')+', TOC '+(x.invalidToc??'n/a'))].join('\n'));
console.log(JSON.stringify(summary));
