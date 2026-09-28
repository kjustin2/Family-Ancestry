const buttons = [...document.querySelectorAll('[data-filter]')];
const homes = [...document.querySelectorAll('.home[data-line]')];
const count = document.querySelector('#count');

function applyFilter(line) {
  let visible = 0;
  for (const home of homes) {
    home.hidden = line !== 'all' && home.dataset.line !== line;
    if (!home.hidden) visible += 1;
  }
  for (const button of buttons) {
    const active = button.dataset.filter === line;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  }
  count.textContent = `Showing ${visible} ${visible === 1 ? 'place' : 'places'}`;
  history.replaceState(null, '', line === 'all' ? location.pathname : `#${line}`);
}

for (const button of buttons) button.addEventListener('click', () => applyFilter(button.dataset.filter));
const initial = location.hash.slice(1);
if (buttons.some(button => button.dataset.filter === initial)) applyFilter(initial);
