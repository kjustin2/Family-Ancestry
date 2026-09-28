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
for (const file of files.filter(name => /\.(html|svg)$/i.test(name))) {
  const contents = await readFile(file, 'utf8');
  for (const match of contents.matchAll(/\b(?:href|src)=(['"])([^'"]+)\1/g)) {
    const url = match[2].replaceAll('&amp;', '&');
    if (/^(?:[a-z]+:|\/\/|#)/i.test(url)) continue;
    const local = decodeURIComponent(url.split(/[?#]/, 1)[0]);
    if (!local) continue;
    const target = path.resolve(path.dirname(file), local);
    if (!target.startsWith(`${root}${path.sep}`) && target !== root) {
      missing.push(`${path.relative(root, file)} → ${url} (outside site)`);
      continue;
    }
    try {
      if (!(await stat(target)).isFile()) missing.push(`${path.relative(root, file)} → ${url}`);
    } catch {
      missing.push(`${path.relative(root, file)} → ${url}`);
    }
  }
}
if (missing.length) {
  console.error(`Broken local site links (${missing.length}):\n${missing.join('\n')}`);
  process.exitCode = 1;
} else {
  console.log(`Checked local links across ${files.filter(name => /\.(html|svg)$/i.test(name)).length} HTML and SVG files.`);
}
