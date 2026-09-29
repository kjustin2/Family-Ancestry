// Progressive enhancement: every branch link is readable without JavaScript.
for (const browser of document.querySelectorAll('[data-line-browser]')) {
  const search = browser.querySelector('[data-line-search]');
  const side = browser.querySelector('[data-line-side]');
  const cards = [...browser.querySelectorAll('[data-line-card]')];
  const normalize = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase();
  const update = () => {
    const terms = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    let count = 0;
    for (const card of cards) {
      card.hidden = !(side.value === 'all' || side.value === card.dataset.side) || !terms.every(term=>normalize(card.dataset.search).includes(term));
      if (!card.hidden) count++;
    }
    for (const group of browser.querySelectorAll('[data-line-group]')) group.hidden = !group.querySelector('[data-line-card]:not([hidden])');
    browser.querySelector('[data-line-count]').textContent = `${count} of ${cards.length} family lines${terms.length ? ` matching “${search.value.trim()}”` : ''}`;
    browser.querySelector('[data-line-empty]').hidden = count !== 0;
  };
  search.addEventListener('input', update);
  side.addEventListener('change', update);
}
