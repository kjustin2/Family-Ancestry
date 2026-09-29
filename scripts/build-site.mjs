import { execFileSync } from 'node:child_process';
import { copyFile, mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';
import { gfmHeadingId } from 'marked-gfm-heading-id';
import { buildLines, branchBrowser, articleBranchLinks } from './build-lines.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const output = path.resolve(root, '_site');
if (path.dirname(output) !== root || path.basename(output) !== '_site') {
  throw new Error('Refusing to replace a directory outside this repository');
}

marked.use(gfmHeadingId());
const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
})[char]);

const plainText = html => html.replace(/<[^>]+>/g, ' ').replace(/&(?:amp|lt|gt|quot|#39);/g, s => ({'&amp;':'&','&lt;':'<','&gt;':'>','&quot;':'"','&#39;':"'"})[s]).replace(/\s+/g, ' ').trim();
const views = [['Branches', 'explore/branches.html'], ['Tree', 'explore/family-explorer.html'], ['Timeline', 'explore/timeline.html'], ['Homes', 'explore/family-homes.html'], ['Maps', 'context/geography-atlas.html'], ['Gallery', 'context/faces-and-places.html'], ['Find a page', 'explore/library.html']];
const navigation = prefix => `<nav aria-label="Site views">${views.map(([label, url]) => `<a href="${prefix}${url}">${label}</a>`).join('')}</nav>`;
const header = prefix => `<header class="site-header"><a class="brand" href="${prefix}index.html"><span class="brand-symbol" aria-hidden="true">✳</span> Family Atlas</a>${navigation(prefix)}</header>`;
const searchIndex = [];

function prepareArticle(markdown) {
  let html = rewriteHtmlLinks(marked.parse(markdown, { gfm: true }));
  // Keep images readable at their natural proportions; reserve eager loading for the first visual.
  let imageCount = 0;
  html = html.replace(/<img\b[^>]*>/g, tag => imageCount++ === 0 || /loading=/.test(tag) ? tag : tag.replace('<img ', '<img loading="lazy" '));
  html = html.replace(/<p>(<img\b[^>]*>)<\/p>/g, (whole, image) => {
    const source = image.match(/\bsrc="([^"]+)"/)?.[1];
    return source ? `<figure class="record-visual"><a href="${source}">${image}<span>Open full image ↗</span></a></figure>` : whole;
  });
  html = html.replace(/<table>/g, '<div class="table-scroll" role="region" aria-label="Research comparison" tabindex="0"><table>').replace(/<\/table>/g, '</table></div>');
  const headings = [...html.matchAll(/<h([23]) id="([^"]+)">([\s\S]*?)<\/h\1>/g)];
  const toc = headings.length > 1 ? `<details class="page-toc" open><summary>On this page</summary><nav aria-label="Page sections">${headings.map(m => `<a class="toc-level-${m[1]}" href="#${m[2]}">${plainText(m[3])}</a>`).join('')}</nav></details>` : '';
  return { html, toc };
}

function rewriteHtmlLinks(html) {
  return html.replace(/\b(href|src)=(['"])([^'"]+)\2/g, (whole, attr, quote, url) => {
    if (/^(?:[a-z]+:|\/\/|#)/i.test(url)) return whole;
    return `${attr}=${quote}${url.replace(/\.md(?=($|[?#]))/i, '.html')}${quote}`;
  });
}

function documentPage(markdown, sourcePath) {
  markdown = markdown.replace(/^\uFEFF/, '');
  const title = markdown.match(/^#\s+(.+)$/m)?.[1] ?? path.basename(sourcePath, '.md');
  const relativeRoot = '../'.repeat(sourcePath.split('/').length - 1);
  const { html: article, toc } = prepareArticle(markdown);
  const ledger = sourcePath === 'research/sources.md';
  const description = plainText(article).slice(title.length).trim().slice(0, 180);
  searchIndex.push({ title, url: sourcePath.replace(/\.md$/, '.html'), category: sourcePath.split('/')[0].replace('.md', ''), text: plainText(article) });
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#142a31">
  <title>${escapeHtml(title)} · Family Atlas</title>
  <meta name="description" content="${escapeHtml(description)}">
  <link rel="stylesheet" href="${relativeRoot}site.css">
  <link rel="stylesheet" href="${relativeRoot}lines.css">
  <script src="${relativeRoot}site.js" defer></script>
</head>
<body class="document-page${ledger ? ' ledger-page' : ''}">
  <a class="skip" href="#main">Skip to research</a>
  ${header(relativeRoot)}
  <div class="document-shell"><aside class="document-rail"><p class="eyebrow">Research notebook</p><a href="${relativeRoot}explore/branches.html">← Choose a family line</a><a href="${relativeRoot}explore/family-explorer.html">Combined tree</a><a href="${relativeRoot}research/sources.html">Source ledger</a><p>Names, dates and family links are labeled by their supporting records or as open research leads.</p></aside>
  <main id="main" class="document-main">${articleBranchLinks(sourcePath,relativeRoot)}${toc}${ledger ? '<div class="ledger-tools" hidden><label>Find a source <input type="search" id="source-search" placeholder="Name, source ID, place or record…"></label><p id="source-count" role="status"></p><button id="source-more" type="button">Show more sources</button></div>' : ''}<article class="prose">${article}</article><footer>Family Atlas · <a href="${relativeRoot}index.html">Home</a> · <a href="${relativeRoot}research/open-questions.html">Open questions</a></footer></main></div>
</body>
</html>`;
}

await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });
const tracked = execFileSync('git', ['ls-files', '-z'], { cwd: root })
  .toString('utf8').split('\0').filter(Boolean);
// Include new authored pages in a preview before staging; never copy ignored working files.
const authored = execFileSync('git', ['ls-files', '--others', '--exclude-standard', '-z'], { cwd: root })
  .toString('utf8').split('\0').filter(file => /\.(?:md|html|css|js|svg)$/.test(file));
const roots = new Set(['branches', 'context', 'explore', 'maps', 'media', 'research', 'sources']);
const rootDocs = new Set(['README.md', 'FAMILY-TREE.md', 'timeline.md']);
let pages = 0;
let assets = 0;
for (const file of [...tracked, ...authored]) {
  const normalized = file.replaceAll('\\', '/');
  if (!roots.has(normalized.split('/')[0]) && !rootDocs.has(normalized)) continue;
  const destination = path.join(output, normalized.replace(/\.md$/i, '.html'));
  await mkdir(path.dirname(destination), { recursive: true });
  if (normalized.endsWith('.md')) {
    const source = await readFile(path.join(root, normalized), 'utf8');
    await writeFile(destination, documentPage(source, normalized), 'utf8');
    pages += 1;
  } else if (/\.(?:html|svg)$/i.test(normalized)) {
    const source = await readFile(path.join(root, normalized), 'utf8');
    const prefix = '../'.repeat(normalized.split('/').length - 1);
    const rendered = normalized.startsWith('explore/') && normalized.endsWith('.html') ? source.replace(/<nav aria-label="Site views">([\s\S]*?)<\/nav>/, (_, original) => `<nav aria-label="Site views">${original.includes('Family Atlas') ? `<a href="${prefix}index.html">✳ Family Atlas</a>` : ''}${views.map(([label,url])=>`<a class="nav-link" href="${prefix}${url}">${label}</a>`).join('')}</nav>`) : source;
    await writeFile(destination, rewriteHtmlLinks(rendered), 'utf8');
    assets += 1;
  } else if (normalized.endsWith('.js')) {
    const source = await readFile(path.join(root, normalized), 'utf8');
    await writeFile(destination, source.replace(/\.md(?=(?:#[^'"]*)?['"])/g, '.html'), 'utf8');
    assets += 1;
  } else {
    await copyFile(path.join(root, normalized), destination);
    assets += 1;
  }
}
const home = await readFile(path.join(root, 'site', 'index.html'), 'utf8');
await writeFile(path.join(output, 'index.html'), home.replace(/<nav aria-label="Site views">[\s\S]*?<\/nav>/, navigation('')).replace('<!-- BRANCH_DIRECTORY -->', branchBrowser('', 'Choose the branch you came to see')));
for (const file of await readdir(path.join(root, 'site'))) {
  if (/\.(?:css|js)$/.test(file)) await copyFile(path.join(root, 'site', file), path.join(output, file));
}
pages += await buildLines(output, header, searchIndex);
await writeFile(path.join(output, 'search-index.json'), JSON.stringify(searchIndex));
const stories = await readFile(path.join(root, 'context', 'people-and-stories.md'), 'utf8');
const storySections = stories.split(/^## /m).slice(1).map(section => {
  const { html } = prepareArticle(`## ${section}`);
  const relocated = html.replace(/\b(href|src)="([^"]+)"/g, (whole, attr, url) => /^(?:[a-z]+:|\/|#|\.\.\/)/i.test(url) ? whole : `${attr}="../context/${url}"`);
  return `<article class="life-card">${relocated}</article>`;
}).join('\n');
await writeFile(path.join(output, 'explore', 'stories.html'), `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>People behind the records · Family Atlas</title><meta name="description" content="Eight short family stories about work, music, learning and home, with the evidence beside each one."><link rel="stylesheet" href="../site.css"></head><body><a class="skip" href="#main">Skip to stories</a>${header('../')}<main id="main" class="stories-main"><section class="stories-intro"><p class="eyebrow">The people behind the records</p><h1>Small details. Whole lives.</h1><p>Meet a musician, a purchasing agent, a bookkeeper and the families around them. Each scene keeps the record—or the person who remembered it—close at hand.</p><p class="evidence-note">Family memories and biographies are attributed accounts. A job or a household value gives a glimpse, never a complete measure of character or wealth.</p><a class="outline-link" href="../context/family-storyboards.html">Follow all four family sides ↗</a></section><div class="life-grid">${storySections}</div><section class="next-path"><h2>Follow the thread that caught your eye.</h2><a href="family-explorer.html">Connect the people ↗</a><a href="family-homes.html">See their streets ↗</a><a href="../context/education-across-generations.html">Follow the schools ↗</a><a href="../research/assets-by-generation.html">Read the money records ↗</a></section></main><footer><span>Eight scenes · source-linked throughout</span><a href="../index.html">Home</a><a href="library.html">Find any research page</a></footer></body></html>`);
pages += 1;
await writeFile(path.join(output, '.nojekyll'), '');
console.log(`Built ${pages} readable research pages and copied ${assets} atlas assets to _site.`);
