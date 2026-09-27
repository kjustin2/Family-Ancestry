"""Generate compact, evidence-labeled family storyboards from the cited atlas notes.

The SVGs are reading aids. Source links and limits live in
context/family-storyboards.md and research/assets-by-generation.md.
"""

from pathlib import Path
from xml.sax.saxutils import escape


OUT = Path(__file__).resolve().parent


BOARDS = [
    {
        "slug": "justin-paternal",
        "title": "Justin's paternal lines · rope, coal and technical study",
        "subtitle": "Two immigrant branches meet at Fred Kramer and Patricia Cordaro; the older Baden match is still open.",
        "columns": ("Kramer · Bosch", "Cordaro · Caucci"),
        "bands": [
            ("1870–1900 · older arrivals", [
                ("Martin / Matthew? · Wilkes-Barre", "Mason → rope-factory worker", "$3,000 real estate + $700 personal (1870)", "Lena + Katie marked at school (1880)", "STRONG IDENTITY LEAD", "proposed"),
                ("Antonio · Sutera to Pennsylvania", "Farm worker (1899); later miner", "No land value or earnings yet found", "No named school yet found", "RECORDS + OPEN ASSETS", "recorded"),
            ]),
            ("1938–1962 · industrial households", [
                ("Ferdinand (c. 1882) · rope", "Wire-rope foreman (1940)", "Home $2,400; 1939 wages $1,996", "Eighth grade; Hilda at G.A.R. (1940)", "ORIGINAL CENSUS", "recorded"),
                ("Joseph, Dina + Patricia · coal", "Coal-company worker; Patricia secretary", "No comparable home or wage amount", "Joseph H2; Dina grade 8 (1940)", "CENSUS + MARRIAGE FORM", "recorded"),
            ]),
            ("1962–2021 · marriage and learning", [
                ("Ferdinand Louis → Fred → Paul → sons", "Rope work continued to Bridon (obituary)", "Later wages and transfers unrecorded", "NRI → RIT → Penn State / GT + Pitt", "OBITUARY + FAMILY ACCOUNTS", "family"),
                ("Fred + Patricia · branches meet", "Marriage recorded in 1962", "No inherited-asset chain established", "School path for Fred and Patricia open", "RECORDED UNION; OPEN DETAILS", "recorded"),
            ]),
        ],
    },
    {
        "slug": "justin-maternal",
        "title": "Justin's maternal lines · farms, Berwick work and later learning",
        "subtitle": "Miller / Reese and Raber / Kreischer / Sponenberg stories meet through Paul, Sonya and Melissa.",
        "columns": ("Miller · Gower · Reese", "Raber · Kreischer · Sponenberg"),
        "bands": [
            ("1827–1915 · farms and trades", [
                ("Marshall Miller → Amos", "Farming; Union service strongly matched", "$600 real estate on 1870 census", "No named school found for Marshall", "HOUSEHOLD + VETERAN MATCH", "recorded"),
                ("Daniel? → John L. → Edward", "Canal lead; foundry → store purchasing", "1907 Berwick home reported, value unknown", "Common / country schools in 1915 profile", "RETROSPECTIVE BIOGRAPHY", "proposed"),
            ]),
            ("1915–1956 · Berwick households", [
                ("Lester + Mabel / Pearl → Paulene", "Cleaning, ironing and labor in memoir", "$1,500 home sale recalled after 1954", "Paulene: Millville; Marqueen: 1956 yearbook", "FIRST-PERSON MEMORY", "family"),
                ("Kreischer + Sponenberg kin", "Factory and purchasing work in profiles", "No comparable family wealth figure", "No school register for Aletha yet checked", "RETROSPECTIVE PROFILES", "proposed"),
            ]),
            ("1980s–2000s · later paths", [
                ("Paul Miller → Melissa Miller Kramer", "Melissa's PA real-estate work reported", "No wage, deed or estate chain checked", "Modern school details not yet sourced", "FAMILY ACCOUNT", "family"),
                ("Shirley Kreischer Raber", "Cigar plant → school crossing guard", "No wage or home value in obituary", "GED in 1987, later in life", "FAMILY OBITUARY", "family"),
            ]),
        ],
    },
    {
        "slug": "ashley-paternal",
        "title": "Ashley's paternal lines · Virginia work and a Fairfax home",
        "subtitle": "Weatherford / Neathery and Morrison / Hollinger meet with Garnett and Florence in 1954.",
        "columns": ("Weatherford · Neathery", "Morrison · Hollinger · Straub"),
        "bands": [
            ("1850–1900 · older households", [
                ("Samuel + Jane · Halifax candidate", "Planter / farmer in census returns", "$375 RE (1850); $786 RE (1870)", "Caroline listed at school, fields conflict", "OLDER LINK UNRESOLVED", "proposed"),
                ("Thomas + Isophena · Indiana lead", "Farmer in a probable 1900 household", "Farm owned with mortgage; no balance", "Children's schooling needs closer check", "GRANDPARENT LINK PROPOSED", "proposed"),
            ]),
            ("1930–1950 · Depression and widowhood", [
                ("Duffy + Annie Weatherford", "Carpenter → city cleaner", "Home $1,000 (1930 and 1940); wage $1,078", "School record for Duffy not found", "ORIGINAL CENSUSES", "recorded"),
                ("Roscoe + Eleanor Morrison", "Sheet metal; Eleanor: 'family work'", "$15 monthly rent (1940); no estate", "Edwin and Paul working by 1950", "CENSUS + DEATH RECORD", "recorded"),
            ]),
            ("1954–2019 · converging Fairfax family", [
                ("Garnett + Florence Weatherford", "Navy / bus; Florence bank bookkeeper", "1980 purchase $104,500; 2019 sale $645,000", "John: Edison High (family account)", "RECORDS + FAMILY SCHOOL", "family"),
                ("Florence → John Sr. → Ashley", "Florence: bank; John: Navy Yard IT", "No personal wealth estimate", "Ashley: Virginia Tech 2015–19 (family)", "BRANCHES JOINED IN 1954", "family"),
            ]),
        ],
    },
    {
        "slug": "ashley-maternal",
        "title": "Ashley's maternal lines · trades, homes and the Navy Yard",
        "subtitle": "Smith / Mulhall and Blevins / Hines paths have promising early records but two crucial parent links remain open.",
        "columns": ("Smith · Mulhall · Corbett", "Blevins · Hines · Cowan"),
        "bands": [
            ("1680s–1920 · older leads", [
                ("John Mulhall → DC Smith candidate", "Gardener → brass molder → water foreman", "Rented in 1900; no earnings stated", "Named schools not found", "ASHLEY LINK STILL OPEN", "proposed"),
                ("James Blevin · Northeast lead", "Oyster Bay sailor (1686/7)", "£20 tax rate (1683); £14 land sale", "No childhood school evidence", "NOT LINKED TO ASHLEY", "proposed"),
            ]),
            ("1920–1940 · skilled work and housing", [
                ("Raymond Smith · DC candidate", "Optician, 1930 and 1950", "$35.50 monthly rent (1930)", "No named school found", "JAMES PARENT LINK OPEN", "proposed"),
                ("Hines + William Howard Blevins", "Rail-yard machinist; varnish sprayer", "Hines home $4,000 (1930); Howard rent $12", "No named school for Howard", "DIFFERENT HOUSEHOLDS / YEARS", "recorded"),
            ]),
            ("1957–2019 · Fairfax and university", [
                ("James + Gladys → Alice Smith", "Alice: Navy Yard admin (family account)", "Smith home sold $360,000 (2010)", "Alice: Hayfield + cosmetology (family)", "RECORDS + FAMILY ACCOUNTS", "family"),
                ("Gladys → Alice → Ashley", "Three-generation recent path", "No inheritance or net-worth record", "Timothy + Ashley: Virginia Tech (family)", "PARENT LINKS; SCHOOL FAMILY", "family"),
            ]),
        ],
    },
]


OVERVIEW = [
    ("Justin · paternal", "Mason → rope / Sicily farm → coal", "1870 values; 1940 home + wage", "NRI → RIT → Penn State / GT + Pitt", "justin-paternal"),
    ("Justin · maternal", "Farm, canal, factory and care work", "1870 value; 1954 sale remembered", "Berwick yearbook; Shirley's GED", "justin-maternal"),
    ("Ashley · paternal", "Farm, carpentry, transit and bank", "1930/40 home; 1980/2019 parcel", "Edison; Ashley at Virginia Tech", "ashley-paternal"),
    ("Ashley · maternal", "Optician, furniture, rail and Navy Yard", "1930 home / rent; 1940 rent", "Hayfield; Timothy at Virginia Tech", "ashley-maternal"),
]


def txt(x, y, value, cls, extra=""):
    return f'<text x="{x}" y="{y}" class="{cls}" {extra}>{escape(value)}</text>'


STYLE = """<style>
text{font-family:Arial,sans-serif;fill:#19363e}.title{font-size:27px;font-weight:700}.sub{font-size:14px}.column{font-size:18px;font-weight:700}.band{font-size:14px;font-weight:700;fill:#4b6268}.person{font-size:17px;font-weight:700}.key{font-size:11px;font-weight:700;letter-spacing:.04em}.value{font-size:14px}.badge{font-size:10px;font-weight:700;letter-spacing:.03em}.foot{font-size:12px;fill:#50666b}.card{fill:#fff;stroke:#c7d6d1;stroke-width:1.5;rx:12}.bar{fill:#e7efea}.recorded{fill:#327c67}.family{fill:#5675a2}.proposed{fill:#ac743b}
</style>"""


def card(x, y, item):
    person, work, asset, school, badge, status = item
    parts = [f'<rect class="card" x="{x}" y="{y}" width="516" height="132"/>',
             f'<rect class="{status}" x="{x}" y="{y}" width="6" height="132" rx="3"/>',
             txt(x + 17, y + 25, person, "person"),
             txt(x + 18, y + 49, "WORK", "key"), txt(x + 90, y + 49, work, "value"),
             txt(x + 18, y + 72, "ASSET", "key"), txt(x + 90, y + 72, asset, "value"),
             txt(x + 18, y + 95, "SCHOOL", "key"), txt(x + 90, y + 95, school, "value"),
             f'<rect x="{x+17}" y="{y+106}" width="{min(297, 25+len(badge)*6.2):.0f}" height="18" rx="9" fill="#eff2ed"/>',
             txt(x + 27, y + 119, badge, "badge")]
    return "".join(parts)


def board_svg(board):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 670" role="img" aria-labelledby="title desc">',
             f'<title id="title">{escape(board["title"])}</title><desc id="desc">{escape(board["subtitle"])} Three generation bands compare dated work, assets and education across two branches. Colors distinguish recorded, family-reported and proposed details.</desc>',
             STYLE, '<rect width="1120" height="670" fill="#f8faf7"/>',
             txt(25, 43, board["title"], "title", 'id="visible-title"'),
             txt(25, 68, board["subtitle"], "sub"),
             f'<rect class="bar" x="25" y="88" width="1070" height="38" rx="9"/>',
             txt(42, 113, board["columns"][0], "column"), txt(585, 113, board["columns"][1], "column")]
    for index, (band, items) in enumerate(board["bands"]):
        y = 139 + index * 163
        parts.append(txt(27, y, band, "band"))
        parts.append(card(25, y + 12, items[0]))
        parts.append(card(579, y + 12, items[1]))
    parts.extend([
        f'<rect x="25" y="633" width="1070" height="24" rx="7" fill="#eaf0ed"/>',
        txt(37, 650, "Teal = record detail  ·  Blue = family account  ·  Ochre = identity or lineage lead. Money fields are different measures, never a wealth curve.", "foot"),
        '</svg>'])
    return "\n".join(parts) + "\n"


def overview_svg():
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 505" role="img" aria-labelledby="title desc">',
             '<title id="title">Four family paths through work, assets and education</title>',
             '<desc id="desc">Each of Justin and Ashley\'s four main family arms has a brief work story, dated asset clue and education trail. Values are from different sources and cannot be compared as net worth.</desc>',
             STYLE, '<rect width="1120" height="505" fill="#f8faf7"/>',
             txt(25, 44, "Four family paths, three ways to look", "title"),
             txt(25, 69, "Choose a row below, then open its two-branch storyboard and short source-linked scenes.", "sub"),
             '<rect class="bar" x="25" y="89" width="1070" height="37" rx="8"/>',
             txt(40, 113, "FAMILY ARM", "key"), txt(255, 113, "WORK", "key"),
             txt(530, 113, "ASSET CLUES", "key"), txt(817, 113, "EDUCATION", "key")]
    for i, (name, work, asset, school, slug) in enumerate(OVERVIEW):
        y = 137 + i * 83
        parts += [f'<rect class="card" x="25" y="{y}" width="1070" height="71"/>',
                  f'<rect x="25" y="{y}" width="6" height="71" fill="{["#317a67", "#ad7741", "#5379a2", "#826e9b"][i]}" rx="3"/>',
                  txt(40, y + 30, name, "column"),
                  txt(255, y + 29, work, "value"),
                  txt(530, y + 29, asset, "value"),
                  txt(817, y + 29, school, "value"),
                  txt(255, y + 50, "Open the paired line below for generations and records", "foot")]
    parts += [txt(25, 490, "Sources and caveats: context/family-storyboards.md. Blank amounts mean no figure found, not no property or income.", "foot"), '</svg>']
    return "\n".join(parts) + "\n"


for board in BOARDS:
    (OUT / f'family-storyboard-{board["slug"]}.svg').write_text(board_svg(board), encoding="utf-8")
(OUT / "family-storyboard-overview.svg").write_text(overview_svg(), encoding="utf-8")
