(() => {
  const menu=document.querySelector('.site-nav'), button=document.querySelector('.burger');
  if(menu&&button){
    menu.id='site-navigation'; button.type='button'; button.setAttribute('aria-controls',menu.id);
    const close=(focus=false)=>{menu.dataset.open='false';button.setAttribute('aria-expanded','false');button.setAttribute('aria-label','Ouvrir le menu');if(focus)button.focus();};close();
    button.addEventListener('click',()=>{const open=menu.dataset.open!=='true';menu.dataset.open=String(open);button.setAttribute('aria-expanded',String(open));button.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');if(open)menu.querySelector('a')?.focus();});
    document.addEventListener('keydown',e=>{if(e.key==='Escape'){if(menu.dataset.open==='true')close(true);else document.activeElement?.blur();}});
    document.addEventListener('click',e=>{if(!e.target.closest('.site-header'))close();});
    window.matchMedia('(max-width:768px)').addEventListener('change',()=>close());
  }
  document.querySelectorAll('figure img').forEach(img=>{
    const figure=img.closest('figure');
    const failed=()=>{if(!figure)return;figure.classList.add('image-unavailable');if(!figure.querySelector('.image-status')){const p=document.createElement('p');p.className='image-status';p.textContent='Illustration indisponible. La légende et les informations ci-dessous restent accessibles.';figure.prepend(p);}};
    img.addEventListener('error',failed);if(img.complete&&!img.naturalWidth)failed();
  });
  document.querySelectorAll('.table-scroll,.table-wrap,.table-wrapper').forEach(el=>{el.tabIndex=0;el.setAttribute('role','region');el.setAttribute('aria-label','Tableau — défilement horizontal');});
  const mobile=matchMedia('(max-width:1024px)');
  const toc=document.querySelector('.content-sidebar .sidebar-box:has(.toc-list)');
  if(toc){const copy=toc.cloneNode(true);copy.classList.add('mobile-toc');copy.querySelectorAll('[id]').forEach(el=>el.removeAttribute('id'));document.querySelector('.content-layout')?.before(copy);const update=()=>{toc.hidden=mobile.matches;};mobile.addEventListener('change',update);update();}
  const specs=document.querySelector('.model-specs'),aside=document.querySelector('.content-sidebar');
  if(specs&&aside){const marker=document.createComment('specification position');specs.before(marker);const update=()=>{if(mobile.matches)document.querySelector('.content-main')?.prepend(specs);else marker.after(specs);};mobile.addEventListener('change',update);update();}
})();
