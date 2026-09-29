/* A static, file://-friendly view of the repo's researched ancestral paths.
   Update a card only after checking its branch page and the source behind it. */
const person = (id, title, era, place, story, evidence, read, image = '', map = '', edge = 'recorded') => ({ id, title, era, place, story, evidence, read, image, map, edge });
const groups = [
  {
    key: 'justin-paternal', title: 'Justin · paternal', sub: 'Baden, Sicily & Pennsylvania', color: '#c8754c', parent: person('paul-kramer', 'Paul Kramer', 'c. 1980s · college', 'Pennsylvania', 'Justin’s father studied electrical engineering at LCCC and RIT, served in the Army Reserve, and continued the family’s interest in technical work.', 'Family account; school dates are approximate.', '../context/recent-generations.md', '', '../maps/europe-family-places.svg', 'family'),
    lanes: [
      { label: 'Kramer', nodes: [
        person('kramer-blasius', 'Blasius Kramer + Agathe Huber', '1806 marriage', 'Unadingen, Baden', 'An original index places this couple in Unadingen. Their line through Bernhard and an 1840 Matthäus is documented in German records.', 'Original marriage and baptism indexes; the later U.S. link is open.', '../branches/kramer-unadingen-household.md', '', '../maps/europe-family-places.svg'),
        person('kramer-bernhard', 'Bernhard Kramer + Maria Huber', '1812–1878', 'Unadingen, Baden', 'Bernhard’s 1812 baptism and 1839 marriage identify a German household with twelve indexed children. An 1878 memorial preserves a glimpse of his community.', 'German original records and translated memorial.', '../branches/kramer-unadingen-household.md', '../sources/records/bernhard-kramer-huber-unadingen-memorial-1878.jpg', '../maps/europe-family-places.svg'),
        person('kramer-matthaus', 'Matthäus Kramer (1840)', 'Born 1840', 'Unadingen, Baden', 'This child is named in the Unadingen records. Whether he is Pennsylvania’s Matthew Kramer remains unproved.', 'German birth original; identity bridge to Pennsylvania is proposed.', '../branches/kramer-baden-candidate.md', '', '../maps/europe-family-places.svg', 'proposed'),
        person('kramer-pa', 'Matthew Kramer + Lena', '1900 census · 1865 reported arrival', 'Wilkes-Barre, Pennsylvania', 'The 1900 census describes Matthew and Lena as German-born and reports 1865 U.S. arrivals. It does not give Matthew’s German town or parents.', '1900 census; proposed match to Unadingen Matthäus.', '../branches/kramer.md', '../sources/records/kramer-matthew-lena-census-1900.jpg', '../maps/europe-family-places.svg'),
        person('kramer-ferdinand1', 'Ferdinand Kramer + Rose Bosch', 'c. 1882–1951', 'Wilkes-Barre, Pennsylvania', 'The first of three generations called Ferdinand in this path. He appears as Matthew and Lena’s son in 1900 and with sons Ferdinand Louis and Emil in 1930.', '1900 and 1930 censuses; death certificate.', '../branches/kramer.md', '../sources/records/kramer-matthew-lena-census-1900.jpg'),
        person('kramer-ferdinand2', 'Ferdinand Louis + Mary Andrews', '1913–1976', 'Wilkes-Barre, Pennsylvania', 'The second Ferdinand was 16 when the 1930 census marked a radio set in his parents’ home at 146 Prospect. His obituary later reported National Radio Institute graduation. His own draft card puts him and Mary at 19 Flick Street and names American Chain & Cable’s Hazard Division; the 1950 census calls him a wire-rope machine operator. Why he studied radio and what he built remain unknown.', '1930 original documents a household radio; 1976 obituary reports NRI graduation; signed draft card and 1950 census establish his work, but no NRI project.', '../context/education-across-generations.md#a-radio-lesson-by-mail', '../sources/records/ferdinand-louis-kramer-obituary-1976.jpg', '../maps/ferdinand-louis-nri-evidence.svg'),
        person('kramer-ferdinand3', 'Fred / Ferdinand Francis Kramer', 'Born 1939', 'Pennsylvania', 'The third Ferdinand, generally called Fred, links the earlier Pennsylvania household to Paul Kramer and Justin.', '1950 household and later obituary; parent-to-Paul link supplied by family.', '../branches/kramer.md', '', '', 'family')
      ]},
      { label: 'Cordaro · Caucci', nodes: [
        person('cordaro-giuseppe', 'Giuseppe Cordaro + Maria Tona', 'Late 1800s', 'Sutera, Sicily', 'Sicilian original acts name Giuseppe and Maria as Antonio Cordaro’s parents. This is the currently documented older Cordaro generation.', 'Antonio’s 1878 birth and 1899 marriage originals.', '../branches/cordaro-passport-lead.md', '', '../maps/cordaro-sutera-places.svg'),
        person('cordaro-antonio', 'Antonio Cordaro + Pietra Magro', '1878 birth · 1899 marriage', 'Sutera → Pennsylvania', 'Marriage and migration records trace a staged move from Sutera. A 1927 naturalization petition bears Antonio’s signature. The 1905 Sutera landslide belongs to the town’s context; his own motive is unknown.', '1899 marriage act, manifests and 1927 petition.', '../branches/cordaro-passport-lead.md', '../sources/records/antonio-cordaro-petition-1927.jpg', '../maps/cordaro-crossing-evidence.svg'),
        person('cordaro-joseph', 'Joseph Cordaro + Dina Caucci', '1938 marriage', 'Pennsylvania', 'Their marriage application joins the Sicilian Cordaro line to Dina’s Caucci and Belardinelli family, whose parents were born in Italy.', '1938 original marriage application and 1940 household.', '../branches/caucci-belardinelli.md', '../sources/records/cordaro-caucci-marriage-1938.jpg', '../maps/europe-family-places.svg'),
        person('cordaro-patricia', 'Patricia Cordaro Kramer', 'Mid-1900s', 'Pennsylvania', 'Patricia’s marriage record names Joseph and Dina. Family accounts name her sisters Joan, Mary and Toni; their individual records are still being assembled.', '1962 marriage record; sibling names from family account.', '../branches/cordaro-passport-lead.md', '', '../maps/cordaro-sutera-places.svg', 'family')
      ]}
    ]
  },
  {
    key: 'justin-maternal', title: 'Justin · maternal', sub: 'Pennsylvania farms, mills & Berwick', color: '#b29a54', parent: person('melissa-kramer', 'Melissa Miller Kramer', 'c. 1980s · college', 'Pennsylvania', 'Justin’s mother, daughter of Paul Miller and Sonya Raber, earned an associate degree at LCCC and worked in real estate in the 2000s.', 'Family account; college years are approximate.', '../context/recent-generations.md', '', '../maps/america-family-places.svg', 'family'),
    lanes: [
      { label: 'Miller', nodes: [
        person('miller-marshall', 'Gad Marshall Miller + Elizabeth Hess', '1870 & 1880 censuses', 'Pennsylvania', 'Censuses place this family on a Pennsylvania farm. A veterans schedule strongly matches Marshall with Union service, but the exact service story needs careful reading.', '1870 and 1880 censuses; veterans-schedule analysis.', '../branches/miller-gower-reese.md', '../sources/records/marshall-elizabeth-miller-census-1880.jpg'),
        person('miller-amos', 'Amos Miller + Mary Gower', '1880 & 1910 censuses', 'Pennsylvania', 'Amos appears with the older Miller household and later with Mary. Their records provide the next step toward Lester.', '1880 son label and 1910 household.', '../branches/miller-gower-reese.md'),
        person('miller-lester', 'Lester Miller + Velma Wilson', '1937 marriage · 1950 census', 'Berwick area, Pennsylvania', 'The 1950 household shows Lester’s weaving-mill work and Velma’s private-home housework, a useful snapshot of a family economy.', '1937 marriage index and 1950 census sheets.', '../branches/miller-gower-reese.md', '../sources/records/miller-berwick-household-census-1950-sheet15.jpg'),
        person('miller-paul', 'Paul Miller', '1950 household · later years', 'Berwick area, Pennsylvania', 'Paul is named in his sister Paulene’s memoir. Her account preserves small family scenes, including a birthday cruise he gave to their mother.', '1950 household and Paulene’s family memoir.', '../branches/maternal-kramer-side.md')
      ]},
      { label: 'Sponenberg · Kreischer · Raber', nodes: [
        person('sponenberg-shellhammer', 'John Shellhammer + Mary Culp', 'Early 1800s', 'Pennsylvania', 'A 1915 Berwick biography traces the Sponenberg family through this older couple. It is a retrospective claim to check against earlier originals.', '1915 biography; older parent step not independently closed.', '../branches/raber-kreisher-fairchild.md', '../sources/records/edward-sponenberg-biography-1915-187.jpg', '', 'proposed'),
        person('sponenberg-hannah', 'Hannah Shellhammer + Daniel Sponenberg', 'Early 1800s', 'Pennsylvania', 'Family Bible pages and a later biography preserve names and family events across this generation.', 'Family Bible and 1915 biography.', '../branches/raber-kreisher-fairchild.md', '../sources/records/hannah-sponenberg-family-bible-births.jpg'),
        person('sponenberg-john', 'John Leonard Sponenberg + Emma Hartman', '1800s', 'Columbia County, Pennsylvania', 'A Bible birth entry and the 1915 biography help follow the family toward Edward and Berwick.', 'Family Bible and biography; test each generational link.', '../branches/raber-kreisher-fairchild.md', '../sources/records/hannah-sponenberg-family-bible-births.jpg'),
        person('sponenberg-edward', 'Edward Sponenberg + Jennie Mensinger', '1915 biography', 'Berwick, Pennsylvania', 'Edward’s 1915 biography describes his work and ancestry. The family also identifies a Berwick burial place and house images associated with this line.', '1915 biography; house identifications from family account.', '../branches/raber-kreisher-fairchild.md', '../sources/records/edward-sponenberg-biography-1915-187.jpg', '../maps/sponenberg-pennsylvania-places.svg'),
        person('sponenberg-aletha', 'Aletha Sponenberg + William Kreischer', 'Early–mid 1900s', 'Berwick, Pennsylvania', 'Shirley’s 1940 household and later obituary place Aletha and William on the path to Sonya. William reportedly supervised at the Duplan silk mill.', '1940 household and obituary; mill role from family account.', '../branches/raber-kreisher-fairchild.md', '', '../maps/sponenberg-pennsylvania-places.svg'),
        person('raber-shirley', 'Shirley Kreischer Raber', '1932–2018', 'Berwick area, Pennsylvania', 'Her obituary names daughter Sonya. The family’s Fairchild story needs care: Ruth Kreischer married a Fairchild, while an earlier Fairchild-born ancestor is not yet placed.', '2018 obituary and family account.', '../branches/raber-kreisher-fairchild.md'),
        person('raber-sonya', 'Sonya Raber / Balliet', '1950 household · later years', 'Pennsylvania', 'Sonya connects the Kreischer–Sponenberg and Raber lines to Melissa. Her father William John Raber appears in a 1950 household; her marriage to Floyd Balliet is family supplied. A signed card now names her Raber grandfather William Glenmore and his mother Mary Rebecca.', '1950 household, parent index, signed WWII card and family account; William A. father link remains open.', '../branches/raber-shadle-household.md', '', '../maps/raber-glenmore-record-bridge.svg', 'family')
      ]}
    ]
  },
  {
    key: 'ashley-paternal', title: 'Ashley · paternal', sub: 'Southside Virginia, Indiana & Fairfax', color: '#688b91', parent: person('john-weatherford', 'John Weatherford Sr.', '1986 marriage · Navy Yard career', 'Franconia, Fairfax County', 'Born at Alexandria Hospital, John grew up in Fairfax, attended Edison High School and worked with IT equipment at the Washington Navy Yard for many years.', 'Family account; 1986 marriage return anchors the adult household.', '../branches/weatherford-smith-generations.md', '', '../maps/colette-neighborhood.svg', 'family'),
    lanes: [
      { label: 'Weatherford', nodes: [
        person('weatherford-samuel', 'Samuel Weatherford + Jane Ricketts', '1829 marriage · 1880 census', 'Halifax County, Virginia', 'An 1829 marriage lead and 1850–1880 households place a Weatherford family in Southside Virginia. Their exact bridge to George remains unsettled.', 'Marriage index and census originals; later parent step disputed.', '../branches/weatherford-early-virginia.md', '../sources/records/samuel-jane-weatherford-census-1850.jpg', '../maps/america-family-places.svg', 'proposed'),
        person('weatherford-asa', 'Asa / Thomas Weatherford + Julia / Ann', '1855 index · 1875 court case', 'Halifax County, Virginia', 'A Halifax court petition names Julia A. Oakes as Edward Oakes’s heir and Thomas Weatherford’s wife. An older case names Amy Adams Oakes’s father William Adams. The court sale of Edward’s Black Walnut tract describes a house and outbuildings.', 'Original court files support Julia’s Oakes line; the Thos E / A. T. / Asa and Ann / Julia identity path toward George remains proposed.', '../branches/weatherford-early-virginia.md#julia-oakess-older-family-two-court-files', '../sources/records/oakes-black-walnut-auction-1875.jpg', '../maps/oakes-adams-court-chain.svg', 'proposed'),
        person('weatherford-george', 'George C. Weatherford + Ella Lumpkin', '1884 marriage', 'Virginia', 'Their 1884 marriage gives a firmer early Weatherford anchor. Later certificates connect them to Doctor Duffy Weatherford.', '1884 marriage and 1966 death certificate.', '../branches/weatherford-early-virginia.md'),
        person('weatherford-duffy', 'Doctor Duffy + Annie Neathery', 'Early 1900s–1960s', 'Danville area, Virginia', 'Death certificates name this generation and their parents. Census pages show their household before the family’s Fairfax years.', '1930/1940 censuses and parent-naming certificates.', '../branches/weatherford-smith-generations.md', '../sources/records/duffy-annie-weatherford-census-1930.jpg'),
        person('weatherford-garnett', 'Garnett B. Weatherford Sr.', '1927–2007', 'Virginia → Fairfax County', 'Family memory says Garnett joined the Navy at 17 after misstating his age. His 1946 card records an honorable discharge; an obituary reports Pacific service and a long bus-driving career.', '1946 Navy card and obituary; age story from family account.', '../branches/weatherford.md', '../sources/records/garnett-florence-marriage-1954.jpg', '../maps/colette-neighborhood.svg')
      ]},
      { label: 'Morrison · Hollinger', nodes: [
        person('morrison-thomas', 'Thomas Morrison + Isophena Bennett', '1900 & 1910 censuses', 'Indiana', 'Indiana census households show the older Morrison family in a farming setting. Their precise link to Roscoe runs through a name variation that remains under review.', '1900 and 1910 censuses; proposed later bridge.', '../branches/morrison-hollinger.md', '', '../maps/america-family-places.svg'),
        person('morrison-delia', 'Delia / Celia Morrison', 'Early 1900s', 'Indiana', 'Celia or Delia appears in older households and on a later parent-naming record. The naming variation is central to Roscoe’s birth question.', 'Censuses and 1923 parent-naming index; same-person question open.', '../branches/morrison-hollinger.md', '', '', 'proposed'),
        person('morrison-roscoe', 'Roscoe Morrison + Eleanor Hollinger', '1920 marriage', 'Indiana → Virginia', 'Roscoe’s marriage names Celia. Eleanor’s Hollinger line points toward an immigrant Straub family, with France and Germany conflicting in the sources.', '1920 marriage; Hollinger death certificate and census comparison.', '../branches/morrison-hollinger.md', '../sources/records/louisa-straub-hollinger-death-certificate-1941.jpg'),
        person('morrison-florence', 'Florence Ruth Morrison Weatherford', '1937–2019', 'Indiana → Fairfax County', 'Florence married Garnett in 1954, worked at Burke & Herbert Bank according to family memory, and later lived near her son John’s family in Franconia.', '1940/1950 households, 1954 marriage; work from family account.', '../branches/weatherford-smith-generations.md', '../sources/records/garnett-florence-marriage-1954.jpg', '../maps/colette-neighborhood.svg', 'family')
      ]}
    ]
  },
  {
    key: 'ashley-maternal', title: 'Ashley · maternal', sub: 'Ireland, Virginia & the Washington area', color: '#8b75a4', parent: person('alice-weatherford', 'Alice Smith Weatherford', '1986 marriage · Navy Yard career', 'Prince George’s County → Fairfax', 'Alice was born in Prince George’s County, attended Hayfield High School, studied cosmetology, and spent more than 25 years in administration at the Washington Navy Yard.', 'Family account; 1986 marriage return names her parents.', '../branches/smith.md', '', '../maps/colette-neighborhood.svg', 'family'),
    lanes: [
      { label: 'Smith · Mulhall · Corbett', nodes: [
        person('mulhall-ireland', 'John Mulhall + Mary', 'Mid-1800s', 'Ireland → Washington, DC', 'Censuses describe John and Mary as Ireland-born. Their exact Irish counties, voyage and reasons for moving are not yet known.', '1850–1880 DC household records.', '../branches/smith-mulhall-corbett.md', '', '../maps/europe-family-places.svg'),
        person('mulhall-johnt', 'John T. Mulhall + Margaret Corbett', 'Late 1800s', 'Washington, DC', 'Household and child records link this DC generation. The Corbett name opens another Irish research path, but no town of origin is established.', '1880 household and 1894 child return.', '../branches/smith-mulhall-corbett.md'),
        person('smith-raymond', 'Alice Mulhall + Raymond J. Smith', '1894 & 1937 parent indexes', 'Washington, DC', 'Parent indexes and an in-law household identify this couple in the DC Smith path.', '1894/1937 parent indexes and 1920 in-law link.', '../branches/smith-mulhall-corbett.md'),
        person('smith-dc-james', 'James A. Smith (DC household)', '1940 & 1950 censuses', 'Washington, DC', 'A son James A. appears in the DC household. Matching him to Alice’s father, the 1957 groom James Allen Smith, remains an identity lead.', '1940/1950 household; parent-naming bridge to groom missing.', '../branches/smith-mulhall-corbett.md', '', '', 'proposed'),
        person('smith-james-allen', 'James Allen Smith', '1957 marriage', 'Washington area → Fairfax', 'The 1957 marriage to Gladys Louise Blevins and Alice’s 1986 marriage return securely name this more recent Smith generation.', '1957 marriage notice and 1986 parent-naming return.', '../branches/smith.md')
      ]},
      { label: 'Blevins · Hines', nodes: [
        person('blevins-james1708', 'James Blevins (c. 1708)', '1700s', 'Colonial America', 'An older tree places this James at the start of a long Blevins route. Multiple men of this name lived in the colonies; his connection to Ashley’s line is unproved.', 'Compiled-tree lead only; original parent chain open.', '../branches/blevins-rhode-island-lead.md', '', '../maps/america-family-places.svg', 'proposed'),
        person('blevins-james1740', 'James Blevins (c. 1740)', '1700s', 'Virginia region', 'A second James appears in the proposed colonial chain. Deeds involving a James Blevin show land transactions, but cannot yet identify this person as the same man.', 'Tree hypothesis; distinguish same-name colonial records.', '../branches/blevins-colonial-james.md', '', '', 'proposed'),
        person('blevins-joseph', 'Joseph Blevins Sr.', 'Late 1700s', 'Virginia / North Carolina region', 'This proposed parent step is useful for searching, but no original record yet closes it.', 'Compiled-tree parent link only.', '../branches/blevins-deep-lineage.md', '', '', 'proposed'),
        person('blevins-daniel', 'Daniel Blevins + Elizabeth Brackins', '1850–1870 censuses', 'North Carolina', 'Original census households document Daniel and Elizabeth. Their link into the older Joseph/Jamess sequence is still under test.', '1850–1870 household originals; older parent gap.', '../branches/blevins-deep-lineage.md', '../sources/records/daniel-elizabeth-blevins-census-1850.jpg'),
        person('blevins-shubiel', 'Shubiel Blevins + Ada Thompson', 'c. 1844–1913 · 1941 headstone form', 'North Carolina / Virginia', 'A federal headstone application records Shubiel’s Confederate service. Ada’s family appears in a sworn kin account. This is a documented generation, with older ancestry still open.', 'Censuses, 1906 account and 1941 headstone application.', '../branches/blevins-deep-lineage.md', '../sources/records/shubiel-blevins-headstone-application-1941.jpg'),
        person('blevins-elkanah', 'William Elkanah Blevins', '1876–1929', 'North Carolina / Virginia', 'His 1929 death certificate names Shubiel and Ada as parents. The later link to William Howard needs a decisive record.', '1929 parent-naming death certificate; next step proposed.', '../branches/blevins-deep-lineage.md', '', '', 'proposed'),
        person('blevins-howard', 'William Howard Blevins + Mary Hines', '1920s–1930s', 'Virginia / Washington area', 'A 1931 marriage joins William Howard and Mary. Mary’s Hines and Cowan ancestors have their own original-record trail.', '1931 marriage; William Elkanah parent link open.', '../branches/blevins-deep-lineage.md', '../sources/records/william-howard-blevins-candidate-census-1930.jpg'),
        person('blevins-gladys', 'Gladys Louise Blevins Smith', '1940 census · died 2008', 'Virginia → Fairfax County', 'Gladys’s memorial names her children, including Alice, Buck, Jane, Timothy and Carolyn. The family recalls their long connection to the Franconia neighborhood.', '1940 census, 1957 marriage and 2008 memorial.', '../branches/smith.md', '../sources/records/blevins-household-census-1940.jpg', '../maps/colette-neighborhood.svg')
      ]}
    ]
  }
];

const focal = [
  person('justin', 'Justin Kramer', '2017–2021 · Pitt', 'Pennsylvania', 'Justin studied computer science at the University of Pittsburgh, completing a combined bachelor’s and master’s program in 2021.', 'Family account.', '../context/recent-generations.md', '', '', 'family'),
  person('ashley', 'Ashley Weatherford', '2015–2019 · Virginia Tech', 'Virginia / Pennsylvania', 'Ashley attended Virginia Tech from about 2015 to 2019. Her parents are John Weatherford Sr. and Alice Smith Weatherford.', 'Family account.', '../context/recent-generations.md', '', '', 'family')
];

const WIDTH = 2940, HEIGHT = 1400, CARD_W = 278, CARD_H = 72, ROW_GAP = 91, MAX_ROWS = 11;
const windowEl = document.querySelector('#tree-window');
const canvas = document.querySelector('#tree-canvas');
const nodesEl = document.querySelector('#tree-nodes');
const linesEl = document.querySelector('#connections');
const detailEl = document.querySelector('#detail');
const searchEl = document.querySelector('#search');
const resultsEl = document.querySelector('#search-results');
const branchEl = document.querySelector('#branch');
const all = new Map();
const positions = new Map();
let scale = 1, offsetX = 0, offsetY = 0, selected = '', dragging = null, moved = false;

const escapeHtml = value => String(value).replace(/[&<>"']/g, character => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[character]);
const safeHref = path => /^(?:\.\.\/|lines\/[a-z-]+\.html$|https:\/\/)/.test(path) ? path : '#';
const statusLabel = status => status === 'family' ? 'Family account' : status === 'proposed' ? 'Proposed link' : 'Record supported';
function putNode(item, x, y, groupIndex, laneLabel) {
  all.set(item.id, { ...item, groupIndex, laneLabel });
  positions.set(item.id, { x, y });
  const button = document.createElement('button');
  button.type = 'button';
  button.className = `tree-card ${item.edge}`;
  button.style.left = `${x}px`;
  button.style.top = `${y}px`;
  button.dataset.id = item.id;
  button.setAttribute('aria-label', `${item.title}, ${item.era}. ${statusLabel(item.edge)}. Open details.`);
  button.innerHTML = `<span class="card-era">${escapeHtml(item.era)}</span><strong>${escapeHtml(item.title)}</strong>`;
  button.addEventListener('click', () => { if (!moved) selectNode(item.id); });
  nodesEl.append(button);
}
function addLine(fromId, toId, status) {
  const a = positions.get(fromId), b = positions.get(toId);
  if (!a || !b) return;
  const x1 = a.x + CARD_W / 2, y1 = a.y + CARD_H, x2 = b.x + CARD_W / 2, y2 = b.y;
  const bend = y1 + (y2 - y1) * .52;
  const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  path.setAttribute('d', `M ${x1} ${y1} C ${x1} ${bend}, ${x2} ${bend}, ${x2} ${y2}`);
  path.setAttribute('class', `connection ${status}`);
  linesEl.append(path);
}
function renderTree() {
  canvas.style.width = `${WIDTH}px`; canvas.style.height = `${HEIGHT}px`;
  linesEl.setAttribute('viewBox', `0 0 ${WIDTH} ${HEIGHT}`);
  linesEl.setAttribute('width', WIDTH); linesEl.setAttribute('height', HEIGHT);
  groups.forEach((group, gi) => {
    const baseX = 40 + gi * 750;
    const groupTitle = document.createElement('div');
    groupTitle.className = 'group-title'; groupTitle.style.left = `${baseX}px`;
    groupTitle.style.setProperty('--group-color', group.color);
    groupTitle.innerHTML = `<strong>${escapeHtml(group.title)}</strong><span>${escapeHtml(group.sub)}</span>`;
    nodesEl.append(groupTitle);
    group.lanes.forEach((lane, li) => {
      const x = baseX + li * 310;
      const label = document.createElement('div'); label.className = 'lane-label'; label.style.left = `${x}px`; label.textContent = lane.label; nodesEl.append(label);
      lane.nodes.forEach((node, ni) => {
        const y = 105 + (MAX_ROWS - lane.nodes.length + ni) * ROW_GAP;
        putNode(node, x, y, gi, lane.label);
        if (ni) addLine(lane.nodes[ni - 1].id, node.id, lane.nodes[ni - 1].edge);
      });
    });
    putNode(group.parent, baseX + 155, 1178, gi, 'Next generation');
    group.lanes.forEach(lane => addLine(lane.nodes.at(-1).id, group.parent.id, lane.nodes.at(-1).edge));
  });
  putNode(focal[0], 570, 1300, 0, 'Present');
  putNode(focal[1], 2070, 1300, 2, 'Present');
  addLine(groups[0].parent.id, 'justin', 'family'); addLine(groups[1].parent.id, 'justin', 'family');
  addLine(groups[2].parent.id, 'ashley', 'family'); addLine(groups[3].parent.id, 'ashley', 'family');
  document.querySelector('#node-count').textContent = all.size;
  groups.forEach((group, i) => {
    branchEl.add(new Option(group.title, `g${i}`));
    group.lanes.forEach((lane, li) => branchEl.add(new Option(`  ↳ ${lane.label}`, `l${i}-${li}`)));
  });
  const branchChoices = document.createElement('optgroup');
  branchChoices.label = 'Open a smaller family tree';
  for (const line of window.FAMILY_LINES ?? []) branchChoices.append(new Option(`${line.name} line`, `line:${line.url}`));
  branchEl.append(branchChoices);
}
function transform() { canvas.style.transform = `translate(${offsetX}px, ${offsetY}px) scale(${scale})`; }
function clampScale(value) { return Math.max(.08, Math.min(2.2, value)); }
function fit() {
  const w = windowEl.clientWidth, h = windowEl.clientHeight;
  scale = clampScale(Math.min((w - 46) / WIDTH, (h - 46) / HEIGHT));
  offsetX = (w - WIDTH * scale) / 2; offsetY = (h - HEIGHT * scale) / 2;
  transform();
}
function centerAt(x, y, wantedScale = Math.max(scale, .82)) {
  scale = clampScale(wantedScale);
  offsetX = windowEl.clientWidth / 2 - (x + CARD_W / 2) * scale;
  offsetY = windowEl.clientHeight / 2 - (y + CARD_H / 2) * scale;
  transform();
}
function zoomAt(multiplier, clientX = windowEl.getBoundingClientRect().left + windowEl.clientWidth / 2, clientY = windowEl.getBoundingClientRect().top + windowEl.clientHeight / 2) {
  const rect = windowEl.getBoundingClientRect();
  const px = clientX - rect.left, py = clientY - rect.top;
  const worldX = (px - offsetX) / scale, worldY = (py - offsetY) / scale;
  scale = clampScale(scale * multiplier);
  offsetX = px - worldX * scale; offsetY = py - worldY * scale;
  transform();
}
function selectedPath(item) {
  const group = groups[item.groupIndex];
  const lane = group.lanes.find(l => l.label === item.laneLabel);
  if (!lane) return '';
  return lane.nodes.map(n => n.id === item.id ? `<b>${escapeHtml(n.title)}</b>` : `<button type="button" data-jump="${escapeHtml(n.id)}">${escapeHtml(n.title)}</button>`).join('<span aria-hidden="true"> → </span>');
}
function selectNode(id, center = false, updateUrl = true) {
  const item = all.get(id); if (!item) return;
  selected = id;
  if (updateUrl) {
    const hash = `#person=${encodeURIComponent(id)}`;
    try { history.replaceState(null, '', hash); }
    catch { location.hash = hash; }
  }
  document.querySelectorAll('.tree-card').forEach(card => card.classList.toggle('selected', card.dataset.id === id));
  const group = groups[item.groupIndex];
  const status = statusLabel(item.edge);
  const read = safeHref(item.read);
  const image = item.image ? `<a class="artifact" href="${safeHref(item.image)}" target="_blank" rel="noopener"><img src="${safeHref(item.image)}" alt="Record or period image associated with ${escapeHtml(item.title)}; see branch notes for identification" loading="lazy"><span>Open the related image ↗</span></a>` : '';
  const map = item.map ? `<a href="${safeHref(item.map)}" target="_blank" rel="noopener">See the related visual ↗</a>` : '';
  detailEl.innerHTML = `<div class="detail-top"><span class="detail-branch">${escapeHtml(group.title)} / ${escapeHtml(item.laneLabel)}</span><span class="detail-status ${item.edge}">${status}</span></div><h3>${escapeHtml(item.title)}</h3><p class="detail-era">${escapeHtml(item.era)} <span>·</span> ${escapeHtml(item.place)}</p><p class="detail-story">${escapeHtml(item.story)}</p><div class="detail-evidence"><strong>What supports this</strong><p>${escapeHtml(item.evidence)}</p></div>${image}<div class="detail-links"><a href="${read}">Read this branch &amp; its sources ↗</a>${map}</div>${selectedPath(item) ? `<div class="detail-path"><strong>Follow this path</strong><div>${selectedPath(item)}</div></div>` : ''}`;
  detailEl.querySelectorAll('[data-jump]').forEach(button => button.addEventListener('click', () => selectNode(button.dataset.jump, true)));
  document.querySelector('#tree-tip').textContent = `${item.title} · ${status}`;
  if (center) { const p = positions.get(id); centerAt(p.x, p.y); }
}
function markSearch() {
  const term = searchEl.value.trim().toLocaleLowerCase();
  const matches = [];
  document.querySelectorAll('.tree-card').forEach(card => {
    const item = all.get(card.dataset.id);
    const match = !term || [item.title, item.place, item.era, item.story, item.laneLabel].some(v => v.toLocaleLowerCase().includes(term));
    card.classList.toggle('dimmed', Boolean(term) && !match);
    card.classList.toggle('match', Boolean(term) && match);
    if (term && match) matches.push(item.id);
  });
  document.querySelector('#tree-tip').textContent = term ? `${matches.length} matching cards${matches.length ? ' · press Enter to jump to the first' : ''}` : selected ? `${all.get(selected).title} · ${statusLabel(all.get(selected).edge)}` : 'Select a card to explore a life';
  resultsEl.hidden = !term;
  if (term) {
    const normalized = term.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    const branches = (window.FAMILY_LINES ?? []).filter(line => [line.name,line.aliases,line.origin].join(' ').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase().includes(normalized));
    document.querySelector('#tree-tip').textContent = `${branches.length} family lines · ${matches.length} canvas cards · select a result`;
    const shown = matches.slice(0, 12);
    resultsEl.innerHTML = `<span>${branches.length} family line${branches.length === 1 ? '' : 's'} · ${matches.length} canvas card${matches.length === 1 ? '' : 's'}${matches.length > shown.length ? ' · showing first 12 cards' : ''}</span>` + branches.map(line=>`<a class="tree-branch-result" href="${safeHref(line.url)}"><strong>${escapeHtml(line.name)} line · small tree &amp; timeline ↗</strong><small>${escapeHtml(line.side)} · ${escapeHtml(line.origin)}</small></a>`).join('') + shown.map(id => {
      const item = all.get(id);
      return `<button type="button" data-result="${escapeHtml(id)}"><strong>${escapeHtml(item.title)}</strong><small>${escapeHtml(item.laneLabel)} · ${escapeHtml(item.place)}</small></button>`;
    }).join('');
    resultsEl.querySelectorAll('[data-result]').forEach(button => button.addEventListener('click', () => {
      searchEl.value = '';
      markSearch();
      selectNode(button.dataset.result, true);
    }));
  }
  return matches;
}

renderTree();
function personFromHash() {
  const match = location.hash.match(/^#person=(.+)$/);
  if (!match) return '';
  try { return decodeURIComponent(match[1]); } catch { return ''; }
}
requestAnimationFrame(() => {
  fit();
  const initial = personFromHash();
  selectNode(all.has(initial) ? initial : 'justin', Boolean(initial), false);
});
window.addEventListener('hashchange', () => {
  const id = personFromHash();
  if (all.has(id)) selectNode(id, true, false);
});
document.querySelector('#fit').addEventListener('click', () => { branchEl.value = 'all'; fit(); });
document.querySelector('#zoom-in').addEventListener('click', () => zoomAt(1.25));
document.querySelector('#zoom-out').addEventListener('click', () => zoomAt(.8));
branchEl.addEventListener('change', () => {
  if (branchEl.value === 'all') return fit();
  if (branchEl.value.startsWith('line:')) { location.href = safeHref(branchEl.value.slice(5)); return; }
  const isLane = branchEl.value.startsWith('l');
  const [gi, li] = (isLane ? branchEl.value.slice(1).split('-') : [branchEl.value.slice(1), '0']).map(Number);
  const x = 40 + gi * 750 + (isLane ? li * 310 + CARD_W / 2 : 310);
  const firstRow = isLane ? MAX_ROWS - groups[gi].lanes[li].nodes.length : MAX_ROWS - Math.max(...groups[gi].lanes.map(lane => lane.nodes.length));
  const targetY = 105 + firstRow * ROW_GAP + 180;
  scale = clampScale(isLane ? Math.min((windowEl.clientWidth - 32) / CARD_W, 1.05) : Math.min((windowEl.clientWidth - 40) / 710, windowEl.clientWidth < 600 ? .72 : .91));
  offsetX = windowEl.clientWidth / 2 - x * scale; offsetY = windowEl.clientHeight / 2 - targetY * scale;
  transform();
});
searchEl.addEventListener('input', markSearch);
searchEl.addEventListener('keydown', event => {
  if (event.key !== 'Enter') return;
  const normalize = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase().trim();
  const line = (window.FAMILY_LINES ?? []).find(line=>normalize(line.name) === normalize(searchEl.value));
  if (line) { event.preventDefault(); location.href = safeHref(line.url); return; }
  const first = markSearch()[0];
  if (first) { searchEl.value = ''; markSearch(); selectNode(first, true); document.querySelector('#tree-heading').scrollIntoView({ behavior: 'smooth' }); event.preventDefault(); }
});
document.querySelectorAll('[data-story]').forEach(button => button.addEventListener('click', () => { selectNode(button.dataset.story, true); document.querySelector('#tree-heading').scrollIntoView({ behavior: 'smooth' }); }));
windowEl.addEventListener('wheel', event => { event.preventDefault(); zoomAt(event.deltaY < 0 ? 1.12 : 1 / 1.12, event.clientX, event.clientY); }, { passive: false });
windowEl.addEventListener('pointerdown', event => {
  if (event.button !== 0 || event.target.closest('a, .tree-card')) return;
  dragging = { x: event.clientX, y: event.clientY, startX: offsetX, startY: offsetY };
  moved = false; windowEl.setPointerCapture(event.pointerId); windowEl.classList.add('dragging');
});
windowEl.addEventListener('pointermove', event => {
  if (!dragging) return;
  const dx = event.clientX - dragging.x, dy = event.clientY - dragging.y;
  if (Math.hypot(dx, dy) > 5) moved = true;
  if (moved) { offsetX = dragging.startX + dx; offsetY = dragging.startY + dy; transform(); }
});
function stopDrag() { dragging = null; windowEl.classList.remove('dragging'); setTimeout(() => { moved = false; }, 0); }
windowEl.addEventListener('pointerup', stopDrag);
windowEl.addEventListener('pointercancel', stopDrag);
window.addEventListener('resize', () => { if (!selected) fit(); });
