import { execFileSync } from 'node:child_process';
import { copyFile, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';
import { gfmHeadingId } from 'marked-gfm-heading-id';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const output = path.resolve(root, '_site');
if (path.dirname(output) !== root || path.basename(output) !== '_site') {
  throw new Error('Refusing to replace a directory outside this repository');
}

marked.use(gfmHeadingId());
const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
})[char]);

function rewriteHtmlLinks(html) {
  return html.replace(/\b(href|src)=(['"])([^'"]+)\2/g, (whole, attr, quote, url) => {
    if (/^(?:[a-z]+:|\/\/|#)/i.test(url)) return whole;
    return `${attr}=${quote}${url.replace(/\.md(?=($|[?#]))/i, '.html')}${quote}`;
  });
}

function documentPage(markdown, sourcePath) {
  const title = markdown.match(/^#\s+(.+)$/m)?.[1] ?? path.basename(sourcePath, '.md');
  const relativeRoot = '../'.repeat(sourcePath.split('/').length - 1);
  const article = rewriteHtmlLinks(marked.parse(markdown, { gfm: true }));
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#142a31">
  <title>${escapeHtml(title)} · Family Atlas</title>
  <link rel="stylesheet" href="${relativeRoot}site.css">
</head>
<body class="document-page">
  <a class="skip" href="#main">Skip to story</a>
  <header class="site-header">
    <a class="brand" href="${relativeRoot}index.html"><span class="brand-symbol" aria-hidden="true">✳</span> Family Atlas</a>
    <nav aria-label="Site views"><a href="${relativeRoot}explore/family-explorer.html">Explore tree</a><a href="${relativeRoot}explore/timeline.html">Timeline</a><a href="${relativeRoot}context/geography-atlas.html">Maps</a><a href="${relativeRoot}context/faces-and-places.html">Gallery</a></nav>
  </header>
  <div class="document-shell"><aside class="document-rail"><p class="eyebrow">Research notebook</p><a href="${relativeRoot}explore/family-explorer.html">← Back to the tree</a><a href="${relativeRoot}FAMILY-TREE.html">All four family sides</a><a href="${relativeRoot}research/sources.html">Source ledger</a><p>Names, dates and family links are labeled by their supporting records or as open research leads.</p></aside>
  <main id="main" class="document-main"><article class="prose">${article}</article><footer>Family Atlas · <a href="${relativeRoot}index.html">Home</a> · <a href="${relativeRoot}research/open-questions.html">Open questions</a></footer></main></div>
</body>
</html>`;
}

await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });
const tracked = execFileSync('git', ['ls-files', '-z'], { cwd: root })
  .toString('utf8').split('\0').filter(Boolean);
const roots = new Set(['branches', 'context', 'explore', 'maps', 'media', 'research', 'sources']);
const rootDocs = new Set(['README.md', 'FAMILY-TREE.md', 'timeline.md']);
let pages = 0;
let assets = 0;
for (const file of tracked) {
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
    await writeFile(destination, rewriteHtmlLinks(source), 'utf8');
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
await copyFile(path.join(root, 'site', 'index.html'), path.join(output, 'index.html'));
await copyFile(path.join(root, 'site', 'site.css'), path.join(output, 'site.css'));
await writeFile(path.join(output, '.nojekyll'), '');
console.log(`Built ${pages} readable research pages and copied ${assets} atlas assets to _site.`);
