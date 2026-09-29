const search = document.querySelector('#page-search');
const category = document.querySelector('#page-category');
const results = document.querySelector('#page-results');
const count = document.querySelector('#page-count');
const labels = { branches: 'Family branch', context: 'Story & setting', research: 'Research notes', sources: 'Saved record guide', media: 'Image provenance', maps: 'Map guide', README: 'Atlas guide', 'FAMILY-TREE': 'Family guide', timeline: 'Research timeline' };
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase();
let pages = [];
function render() {
  const terms = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
  const matches = pages.filter(page => (category.value === 'all' || page.category === category.value) && terms.every(term => normalize(`${page.title} ${page.text}`).includes(term)))
    .sort((a, b) => {
      const score = p => terms.filter(term => normalize(p.title).includes(term)).length;
      return score(b) - score(a) || a.title.localeCompare(b.title);
    });
  count.textContent = `${matches.length} ${matches.length === 1 ? 'page' : 'pages'}${terms.length ? ' found' : ' to explore'}`;
  results.replaceChildren();
  if (!matches.length) {
    const empty = document.createElement('p'); empty.textContent = 'No pages match. Try a surname or place variant, or choose all research pages.'; results.append(empty);
  }
  for (const page of matches) {
    const link = document.createElement('a'); link.href = `../${page.url}`;
    const tag = document.createElement('span'); tag.className = 'eyebrow'; tag.textContent = labels[page.category] ?? 'Family research';
    const title = document.createElement('h2'); title.textContent = page.title;
    const snippet = document.createElement('p');
    const body = page.text.startsWith(page.title) ? page.text.slice(page.title.length).trim() : page.text;
    const at = terms.length ? Math.max(0, normalize(body).indexOf(terms[0]) - 65) : 0;
    snippet.textContent = `${at ? '…' : ''}${body.slice(at, at + 225)}${body.length > at + 225 ? '…' : ''}`;
    const open = document.createElement('strong'); open.textContent = 'Open the page ↗';
    link.append(tag, title, snippet, open); results.append(link);
  }
}
fetch('../search-index.json').then(response => { if (!response.ok) throw new Error('Directory unavailable'); return response.json(); }).then(data => {
  pages = data; render(); search.addEventListener('input', render); category.addEventListener('change', render);
}).catch(() => { count.textContent = 'The search directory could not load. Open the written family guide or reload this page.'; });
