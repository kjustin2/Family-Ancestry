import { readdir, readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '_site');
async function walk(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const results = [];
  for (const entry of entries) {
    const full = path.join(directory, entry.name);
    if (entry.isDirectory()) results.push(...await walk(full));
    else results.push(full);
  }
  return results;
}
const files = await walk(root);
const missing = [];
const contentsByFile = new Map(await Promise.all(files.filter(name => /\.(html|svg)$/i.test(name)).map(async file => [file, await readFile(file, 'utf8')])));
const idsByFile = new Map();
const timelineStates = new Set([... (await readFile(path.join(root, 'explore', 'timeline.js'), 'utf8')).matchAll(/item\("([^"]+)"/g)].map(match => match[1]));
for (const [file, contents] of contentsByFile) {
  const ids = [...contents.matchAll(/\bid=(['"])([^'"]+)\1/g)].map(match => match[2]);
  idsByFile.set(file, new Set(ids));
  if (new Set(ids).size !== ids.length) missing.push(`${path.relative(root, file)} has duplicate element IDs`);
  if (file.endsWith('.html')) {
    if (/<p>\|/.test(contents)) missing.push(`${path.relative(root, file)} contains unrendered table rows`);
    const headings = [...contents.matchAll(/<h1\b/g)];
    if (headings.length !== 1) missing.push(`${path.relative(root, file)} has ${headings.length} main headings`);
    for (const image of contents.matchAll(/<img\b[^>]*>/g)) {
      if (!/\balt=(['"])[\s\S]*?\1/.test(image[0])) missing.push(`${path.relative(root, file)} has an image without alt text`);
    }
  }
}
const ledgerMarkdown = await readFile(path.resolve(root, '..', 'research', 'sources.md'), 'utf8');
const sourceLabels = [...ledgerMarkdown.matchAll(/^\| ([A-Z][A-Z0-9-]*(?: \/ [A-Z][A-Z0-9-]*)?) \|/gm)].flatMap(match => match[1] === 'ID' ? [] : match[1].split(' / '));
if (new Set(sourceLabels).size !== sourceLabels.length) missing.push('Source ledger has colliding record labels');
for (const file of files.filter(name => /\.(html|svg)$/i.test(name))) {
  const contents = await readFile(file, 'utf8');
  for (const match of contents.matchAll(/\b(?:href|src)=(['"])([^'"]+)\1/g)) {
    const url = match[2].replaceAll('&amp;', '&');
    if (/^(?:[a-z]+:|\/\/)/i.test(url)) continue;
    const local = decodeURIComponent(url.split(/[?#]/, 1)[0]);
    const target = local ? path.resolve(path.dirname(file), local) : file;
    if (!target.startsWith(`${root}${path.sep}`) && target !== root) {
      missing.push(`${path.relative(root, file)} → ${url} (outside site)`);
      continue;
    }
    try {
      if (!(await stat(target)).isFile()) missing.push(`${path.relative(root, file)} → ${url}`);
      const fragment = url.includes('#') ? decodeURIComponent(url.slice(url.indexOf('#') + 1)) : '';
      // The explorer stores selected person IDs in its URL; these are application state, not DOM anchors.
      const validState = path.relative(root, target).replaceAll('\\', '/') === 'explore/timeline.html' && timelineStates.has(fragment);
      if (fragment && !fragment.startsWith('person=') && !validState && idsByFile.has(target) && !idsByFile.get(target).has(fragment)) {
        missing.push(`${path.relative(root, file)} → ${url} (missing section)`);
      }
    } catch {
      missing.push(`${path.relative(root, file)} → ${url}`);
    }
  }
}
// Story links assembled by the interactive views are not present in their initial HTML.
for (const file of files.filter(name => name.endsWith('.js'))) {
  const contents = await readFile(file, 'utf8');
  for (const match of contents.matchAll(/['"]((?:\.\.\/|branches\/|context\/|maps\/|media\/|sources\/)[^'"\n]+\.(?:html|svg|jpg|png)(?:#[^'"\n]*)?)['"]/g)) {
    const [local, fragment] = match[1].split('#');
    const target = path.resolve(local.startsWith('../') ? path.dirname(file) : root, decodeURIComponent(local));
    try {
      if (!(await stat(target)).isFile()) throw new Error('Missing file');
      if (fragment && idsByFile.has(target) && !idsByFile.get(target).has(fragment)) missing.push(`${path.relative(root, file)} → ${match[1]} (missing section)`);
    } catch {
      missing.push(`${path.relative(root, file)} → ${match[1]}`);
    }
  }
}
if (missing.length) {
  console.error(`Broken local site links (${missing.length}):\n${missing.join('\n')}`);
  process.exitCode = 1;
} else {
  console.log(`Checked files, section links, unique IDs, main headings and image descriptions across ${contentsByFile.size} HTML and SVG files.`);
}
