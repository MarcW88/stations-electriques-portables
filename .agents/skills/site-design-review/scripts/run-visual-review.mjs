#!/usr/bin/env node

import { chromium } from '@playwright/test';
import { spawn } from 'node:child_process';
import { mkdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';

// Discover real HTML routes in this repository, instead of inheriting routes
// from the Bloc-notes numérique reference project.
import { existsSync, readdirSync } from 'node:fs';

function discoverRoutes(section) {
  const routes = [];
  const walk = (directory, route) => {
    if (!existsSync(directory)) return;
    if (existsSync(path.join(directory, 'index.html'))) routes.push(route);
    for (const entry of readdirSync(directory, { withFileTypes: true })) {
      if (entry.isDirectory()) walk(path.join(directory, entry.name), route + entry.name + '/');
    }
  };
  walk(section, '/' + section + '/');
  return routes;
}

const SCOPES = {
  brands: discoverRoutes('marques'),
  comparisons: discoverRoutes('comparatifs'),
  usages: discoverRoutes('usages'),
  guides: discoverRoutes('guides'),
  deals: discoverRoutes('bons-plans')
};

const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'mobile', width: 390, height: 844 }
];

function parseArgs(argv) {
  const options = {
    baseUrl: '',
    output: '.artifacts/design-review',
    port: 4173,
    routes: [],
    scope: ''
  };

  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    const next = argv[index + 1];
    if (value === '--base-url') options.baseUrl = next, index += 1;
    else if (value === '--output') options.output = next, index += 1;
    else if (value === '--port') options.port = Number(next), index += 1;
    else if (value === '--route') options.routes.push(next), index += 1;
    else if (value === '--scope') options.scope = next, index += 1;
    else if (value === '--help') options.help = true;
    else throw new Error(`Option inconnue : ${value}`);
  }

  if (options.scope && !SCOPES[options.scope]) {
    throw new Error(`Scope inconnu : ${options.scope}. Scopes disponibles : ${Object.keys(SCOPES).join(', ')}`);
  }
  if (!options.routes.length && options.scope) options.routes = SCOPES[options.scope];
  if (!options.routes.length && options.scope) throw new Error(`Aucune page trouvée pour le scope ${options.scope}`);
  if (!options.routes.length) options.routes = ['/guides/'];
  return options;
}

function slug(route) {
  return route.replace(/^\/+|\/+$/g, '').replaceAll('/', '--') || 'home';
}

async function waitForServer(url) {
  for (let attempt = 0; attempt < 50; attempt += 1) {
    try {
      const response = await fetch(url);
      if (response.ok) return;
    } catch {}
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  throw new Error(`Le serveur local ne répond pas : ${url}`);
}

const options = parseArgs(process.argv.slice(2));
if (options.help) {
  console.log('Usage: run-visual-review.mjs [--scope brands|comparisons|usages|guides|deals] [--route /chemin/] [--base-url URL] [--output dossier] [--port 4173]');
  process.exit(0);
}

const outputRoot = path.resolve(options.output);
await rm(outputRoot, { recursive: true, force: true });
await mkdir(outputRoot, { recursive: true });

let server;
let baseUrl = options.baseUrl.replace(/\/$/, '');
if (!baseUrl) {
  baseUrl = `http://127.0.0.1:${options.port}`;
  server = spawn('python3', ['-m', 'http.server', String(options.port), '--bind', '127.0.0.1', '--directory', '.'], {
    stdio: ['ignore', 'pipe', 'pipe']
  });
  await waitForServer(`${baseUrl}/`);
}

const report = {
  generatedAt: new Date().toISOString(),
  baseUrl,
  scope: options.scope || null,
  routes: options.routes,
  viewports: VIEWPORTS,
  pages: []
};

let browser;
try {
  browser = await chromium.launch({ headless: true });

  for (const viewport of VIEWPORTS) {
    const context = await browser.newContext({
      viewport: { width: viewport.width, height: viewport.height },
      reducedMotion: 'reduce'
    });

    for (const route of options.routes) {
      const page = await context.newPage();
      const consoleErrors = [];
      const pageErrors = [];
      page.on('console', message => {
        if (message.type() === 'error') consoleErrors.push(message.text());
      });
      page.on('pageerror', error => pageErrors.push(error.message));

      const response = await page.goto(`${baseUrl}${route}`, { waitUntil: 'networkidle' });
      if (!response || response.status() >= 400) throw new Error(`Route inaccessible: ${route} (HTTP ${response?.status() ?? 'aucune réponse'})`);
      await page.evaluate(() => document.fonts?.ready);

      const measurements = await page.evaluate(() => {
        const sidebar = document.querySelector('.content-sidebar');
        const headings = [...document.querySelectorAll('.content-main h2, .content-main h3')];
        const toc = document.querySelector('.sidebar-toc, .toc-list');
        const tocLinks = [...document.querySelectorAll('.sidebar-toc a, .toc-list a')];
        const fixedHeader = document.querySelector('.site-header');
        const tables = [...document.querySelectorAll('.table-wrapper, .table-wrap')];
        const articleAnswer = document.querySelector('.article-answer');
        const firstEditorialLink = document.querySelector('.content-main a:not(.btn)');
        return {
          title: document.title,
          statusReady: document.readyState,
          horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          headingCount: headings.length,
          tocLinkCount: tocLinks.length,
          tocParentClass: toc?.parentElement?.className || null,
          missingHeadingIds: headings.filter(heading => !heading.id).map(heading => heading.textContent.trim()),
          tableCount: tables.length,
          rawTableCount: document.querySelectorAll('.content-main table:not(.comp-table)').length,
          overflowingTables: tables
            .filter(wrapper => wrapper.scrollWidth > wrapper.clientWidth)
            .map(wrapper => ({ scrollWidth: wrapper.scrollWidth, clientWidth: wrapper.clientWidth })),
          articleAnswer: articleAnswer ? {
            height: Math.round(articleAnswer.getBoundingClientRect().height),
            background: getComputedStyle(articleAnswer).backgroundColor,
            borderLeftWidth: getComputedStyle(articleAnswer).borderLeftWidth
          } : null,
          firstEditorialLink: firstEditorialLink ? {
            color: getComputedStyle(firstEditorialLink).color,
            decoration: getComputedStyle(firstEditorialLink).textDecorationLine
          } : null,
          sidebar: sidebar ? {
            height: Math.round(sidebar.getBoundingClientRect().height),
            top: Math.round(sidebar.getBoundingClientRect().top),
            position: getComputedStyle(sidebar).position
          } : null,
          headerHeight: fixedHeader ? Math.round(fixedHeader.getBoundingClientRect().height) : 0
        };
      });

      const viewportFolder = path.join(outputRoot, viewport.name);
      await mkdir(viewportFolder, { recursive: true });
      const screenshot = path.join(viewportFolder, `${slug(route)}.png`);
      await page.screenshot({ path: screenshot, fullPage: true, animations: 'disabled' });

      if (viewport.name === 'mobile' && route === options.routes[0]) {
        const burger = page.locator('.burger');
        if (await burger.count()) {
          await burger.click();
          await page.screenshot({
            path: path.join(viewportFolder, `${slug(route)}--menu-open.png`),
            fullPage: false,
            animations: 'disabled'
          });
        }
      }

      report.pages.push({
        route,
        viewport: viewport.name,
        httpStatus: response?.status() ?? null,
        screenshot: path.relative(process.cwd(), screenshot),
        consoleErrors,
        pageErrors,
        ...measurements
      });
      if (pageErrors.length || consoleErrors.length) {
        console.warn(`Erreurs navigateur sur ${route} (${viewport.name}):`, { pageErrors, consoleErrors });
      }
      await page.close();
    }
    await context.close();
  }
} finally {
  if (browser) await browser.close();
  if (server) server.kill('SIGTERM');
}

await writeFile(path.join(outputRoot, 'report.json'), `${JSON.stringify(report, null, 2)}\n`);
console.log(`Captures créées : ${report.pages.length}`);
console.log(`Rapport : ${path.join(outputRoot, 'report.json')}`);
