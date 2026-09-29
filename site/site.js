// Source filtering is progressive enhancement: the complete ledger remains in the HTML.
const sourceTools = document.querySelector('.ledger-tools');
if (sourceTools) {
  const rows = [...document.querySelectorAll('.prose tbody tr')];
  const search = document.querySelector('#source-search');
  const more = document.querySelector('#source-more');
  const count = document.querySelector('#source-count');
  let limit = 40;
  for (const row of rows) {
    const id = row.cells[0]?.textContent.trim();
    if (id) row.id = `source-${id.replace(/[^a-zA-Z0-9-]/g, '-')}`;
  }
  function filterSources() {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let matched = 0;
    for (const row of rows) {
      const text = row.textContent.toLocaleLowerCase();
      const matches = terms.every(term => text.includes(term));
      row.hidden = !matches || matched >= limit;
      if (matches) matched++;
    }
    count.textContent = `${Math.min(matched, limit)} of ${matched} sources${terms.length ? ' match your search' : ''}`;
    more.hidden = matched <= limit;
    for (const table of document.querySelectorAll('.prose .table-scroll')) {
      table.hidden = !table.querySelector('tbody tr:not([hidden])');
    }
  }
  search.addEventListener('input', () => { limit = 40; filterSources(); });
  more.addEventListener('click', () => { limit += 80; filterSources(); });
  sourceTools.hidden = false;
  filterSources();
}
