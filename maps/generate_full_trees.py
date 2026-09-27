"""Generate the four compact, evidence-marked long family trees.

Each lane follows one ancestral path, not every descendant. An edge's evidence
level belongs to the parent-child step ending at the next card. The linked
branch notes give the underlying records and the unresolved identity tests.
"""

from html import escape
from pathlib import Path
from textwrap import wrap


OUT = Path(__file__).parent
COLORS = {"record": "#147d78", "account": "#6557a0", "lead": "#b16a39"}
LABELS = {"record": "record", "account": "family", "lead": "proposed"}


def person(name, detail, step="record"):
    return {"name": name, "detail": detail, "step": step}


TREES = [
    {
        "slug": "full-tree-paternal-kramer-cordaro",
        "title": "Justin's paternal lines: Kramer + Cordaro",
        "subtitle": "From an 1806 Baden couple toward Justin; the German-to-Pennsylvania identity bridge remains open.",
        "left_label": "KRAMER · Baden → Pennsylvania",
        "right_label": "CORDARO · Sicily → Pennsylvania",
        "left_link": "../branches/kramer.md",
        "right_link": "../branches/cordaro-passport-lead.md",
        "left": [
            person("Blasius Kramer + Agathe Huber", "1806 marriage index · Unadingen"),
            person("Bernhard Kramer + Maria Huber", "1812 baptism + 1839 marriage originals"),
            person("Matthäus Kramer (1840)", "Unadingen birth original"),
            person("Matthew / Matthias + Lena", "Wilkes-Barre 1900 census; German match open", "lead"),
            person("Ferdinand (c. 1882) + Rose Bosch", "1900/1930 censuses; 1951 certificate"),
            person("Ferdinand Louis (1913) + Mary Andrews", "1930/1950 censuses; 1976 obituary"),
            person("Fred / Ferdinand Francis (1939)", "1950 household; later obituary"),
        ],
        "right": [
            person("Giuseppe Cordaro + Maria Tona", "Named in Antonio's 1878 + 1899 originals"),
            person("Antonio Cordaro + Pietra Magro", "1899 marriage; 1909/1927 migration records"),
            person("Joseph Cordaro + Dina Caucci", "1938 marriage; 1940 household"),
            person("Patricia Cordaro Kramer", "1962 marriage names Joseph + Dina"),
        ],
        "shared": [
            person("Paul Kramer", "Fred + Patricia's son · family account", "account"),
            person("Justin Kramer", "Paul + Melissa's son · family account", "account"),
        ],
        "merge": ("account", "account"),
        "caveat": "The 1840 German Matthäus and Pennsylvania Matthew are not yet proved to be one man. The Italian passport holder remains unidentified.",
    },
    {
        "slug": "full-tree-maternal-miller-sponenberg",
        "title": "Justin's maternal lines: Miller + Sponenberg",
        "subtitle": "The two Berwick paths meet at Melissa; the oldest Sponenberg parents come from a 1915 biography.",
        "left_label": "MILLER · Sugarloaf → Berwick",
        "right_label": "SPONENBERG → KREISCHER → RABER",
        "left_link": "../branches/miller-gower-reese.md",
        "right_link": "../branches/raber-kreisher-fairchild.md",
        "left": [
            person("Gad Marshall Miller + Elizabeth Hess", "1870/1880 farm censuses"),
            person("Amos Miller + Mary Gower", "1880 son label; 1910 household"),
            person("Lester Miller + Velma Wilson", "1937 marriage; 1950 family household"),
            person("Paul Miller", "1950 child; Paulene's memoir"),
        ],
        "right": [
            person("John Shellhammer + Mary Culp", "Named by Edward's 1915 biography", "lead"),
            person("Hannah Shellhammer + Daniel Sponenberg", "1915 parent claim; family Bible", "lead"),
            person("John Leonard Sponenberg + Emma Hartman", "Bible birth entry; 1915 biography"),
            person("Edward Sponenberg + Jennie Mensinger", "1915 biography; daughter Aletha named", "lead"),
            person("Aletha Sponenberg + William Kreischer", "1940 Shirley household; 2018 obituary"),
            person("Shirley Kreischer Raber (1932–2018)", "2018 obituary names daughter Sonya"),
            person("Sonya Raber / Balliet", "Obituary + family account"),
        ],
        "shared": [
            person("Melissa Miller Kramer", "Paul + Sonya's daughter · family account", "account"),
            person("Justin Kramer", "Melissa + Paul Kramer's son · family account", "account"),
        ],
        "merge": ("account", "account"),
        "caveat": "Velma's proposed Mabel Reese identity is not proved. Ruth Kreischer Fairchild is a collateral lead; the remembered direct Fairchild ancestor remains unplaced.",
    },
    {
        "slug": "full-tree-weatherford-morrison",
        "title": "Ashley's paternal lines: Weatherford + Morrison",
        "subtitle": "Two paths toward John Weatherford; uncertain nineteenth-century identity links stay dashed.",
        "left_label": "WEATHERFORD · Virginia → Fairfax",
        "right_label": "MORRISON · Indiana → Fairfax",
        "left_link": "../branches/weatherford-early-virginia.md",
        "right_link": "../branches/morrison-hollinger.md",
        "left": [
            person("Samuel Weatherford + Jane Ricketts", "1829 marriage index; 1850 household"),
            person("Asa / Thomas Weatherford + Julia / Ann", "1850–84 records disagree on names", "lead"),
            person("George C. Weatherford + Ella Lumpkin", "1884 marriage; father named Thomas A.", "lead"),
            person("Doctor Duffy + Annie Neathery", "1966/1969 certificates name parents"),
            person("Garnett B. Weatherford Sr. (1927–2007)", "1930/1940 censuses; 1954 marriage"),
        ],
        "right": [
            person("Thomas Morrison + Isophena Bennett", "1900/1910 Indiana households"),
            person("Delia / Celia Morrison", "1900/1910 child; 1923 parent-naming index"),
            person("Roscoe Morrison + Eleanor Hollinger", "1920 marriage names Celia; birth link open", "lead"),
            person("Florence Ruth Morrison (1937–2019)", "1940/1950 household; 1954 marriage"),
        ],
        "shared": [
            person("John Weatherford Sr. + Alice Smith", "Garnett + Florence's son; 1986 marriage"),
            person("Ashley Weatherford", "John + Alice's daughter · family account", "account"),
        ],
        "merge": ("record", "record"),
        "caveat": "The Asa/Thomas name conflict and Roscoe's exact Celia birth link need original records. The older Samuel line is a strong candidate, not a closed pedigree.",
    },
    {
        "slug": "full-tree-smith-blevins",
        "title": "Ashley's maternal lines: Smith/Mulhall + Blevins",
        "subtitle": "Ten visible generations on the longest Blevins proposal; the colonial and recent bridges are visibly open.",
        "left_label": "MULHALL → SMITH · Ireland → DC",
        "right_label": "BLEVINS · Virginia / Carolinas → DC",
        "left_link": "../branches/smith-mulhall-corbett.md",
        "right_link": "../branches/blevins-deep-lineage.md",
        "left": [
            person("John Mulhall + Mary (surname open)", "Ireland-born; 1850–80 DC household"),
            person("John T. Mulhall + Margaret Corbett", "1880 parent household; 1894 child return"),
            person("Alice Mulhall + Raymond J. Smith", "1894/1937 parent indexes; 1920 in-law link"),
            person("James A. Smith (DC son)", "1940/1950 son; 1957 groom identity open"),
        ],
        "right": [
            person("James Blevins (c. 1708)", "Linked tree; immigrant origin unknown", "lead"),
            person("James Blevins (c. 1740)", "Parentage disputed; colonial names repeat", "lead"),
            person("Joseph Blevins Sr. (c. 1770)", "Tree-only parent step", "lead"),
            person("Daniel Blevins + Elizabeth Brackins", "1850–70 households; older parent open", "lead"),
            person("Shubiel Blevins + Ada Thompson", "Households; 1906 sworn kin account", "lead"),
            person("William Elkanah Blevins (1876–1929)", "1929 certificate names Shubiel + Ada"),
            person("William Howard Blevins + Mary Hines", "1920 candidate household; parent gap", "lead"),
            person("Gladys Louise Blevins Smith", "1940 child; 1957 marriage to James"),
        ],
        "shared": [
            person("Alice Marie Smith Weatherford", "James + Gladys's daughter · 1986 return"),
            person("Ashley Weatherford", "Alice + John's daughter · family account", "account"),
        ],
        "merge": ("lead", "record"),
        "caveat": "The colonial Blevins links are tree leads. William Howard's parent link and the 1957 James Smith groom's DC identity are still unproved.",
    },
]


def esc(value):
    return escape(value, quote=True)


def line(x1, y1, x2, y2, tier):
    dash = ' stroke-dasharray="7 6"' if tier == "lead" else ''
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{COLORS[tier]}" stroke-width="3"{dash}/>'


def card(x, y, width, item, href, incoming=None):
    color = COLORS[incoming or "record"]
    parts = [f'<a href="{esc(href)}"><rect x="{x}" y="{y}" width="{width}" height="72" rx="12" fill="#ffffff" stroke="#d7e1e1"/>',
             f'<rect x="{x}" y="{y}" width="6" height="72" rx="3" fill="{color}"/>',
             f'<text x="{x+18}" y="{y+28}" class="person">{esc(item["name"])}</text>',
             f'<text x="{x+18}" y="{y+51}" class="detail">{esc(item["detail"])}</text></a>']
    if incoming:
        parts.append(f'<text x="{x+width-12}" y="{y+63}" class="tag" text-anchor="end" fill="{color}">{LABELS[incoming]}</text>')
    return "".join(parts)


def render(tree):
    left, right, shared = tree["left"], tree["right"], tree["shared"]
    rows = max(len(left), len(right))
    row_h, card_h, first_y = 96, 72, 178
    shared_y = first_y + rows * row_h + 50
    height = shared_y + len(shared) * row_h + 107
    left_x, right_x, width, center_x, center_width = 42, 638, 520, 340, 520
    top_left = rows - len(left)
    top_right = rows - len(right)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">',
             f'<title id="title">{esc(tree["title"])}</title>',
             f'<desc id="desc">{esc(tree["subtitle"] + " " + tree["caveat"])}</desc>',
             '<style>.heading{font:700 30px Segoe UI,Arial,sans-serif;fill:#183343}.subtitle{font:16px Segoe UI,Arial,sans-serif;fill:#526875}.lane{font:700 15px Segoe UI,Arial,sans-serif;letter-spacing:1px;fill:#183343}.person{font:700 18px Segoe UI,Arial,sans-serif;fill:#183343}.detail{font:14px Segoe UI,Arial,sans-serif;fill:#556a73}.tag{font:700 11px Segoe UI,Arial,sans-serif}.foot{font:13px Segoe UI,Arial,sans-serif;fill:#526875}</style>',
             f'<rect width="1200" height="{height}" fill="#f4f7f6"/>',
             '<rect width="1200" height="8" fill="#147d78"/>',
             f'<text x="42" y="52" class="heading">{esc(tree["title"])}</text>',
             f'<text x="42" y="81" class="subtitle">{esc(tree["subtitle"])}</text>',
             '<path d="M42 102 H1158" stroke="#d7e1e1"/>',
             f'<text x="42" y="137" class="lane">{esc(tree["left_label"])}</text>',
             f'<text x="638" y="137" class="lane">{esc(tree["right_label"])}</text>',
             '<text x="42" y="158" class="detail">Older ↑ · later ↓ · click a card for records</text>']
    for data, x, offset, href in ((left, left_x, top_left, tree["left_link"]),
                                  (right, right_x, top_right, tree["right_link"])):
        for i, item in enumerate(data):
            y = first_y + (offset + i) * row_h
            if i:
                parts.append(line(x + width/2, y-row_h+card_h, x+width/2, y, item["step"]))
            first_tier = item["step"] if item["step"] == "lead" else None
            parts.append(card(x, y, width, item, href, item["step"] if i else first_tier))
    last_y = first_y + (rows-1)*row_h + card_h
    merge_y = shared_y - 19
    for x, tier in zip((left_x+width/2, right_x+width/2), tree["merge"]):
        parts.append(line(x, last_y, x, merge_y, tier))
        parts.append(line(x, merge_y, 600, merge_y, tier))
    parts.append(line(600, merge_y, 600, shared_y, shared[0]["step"]))
    for i, item in enumerate(shared):
        y = shared_y + i*row_h
        if i:
            parts.append(line(600, y-row_h+card_h, 600, y, item["step"]))
        parts.append(card(center_x, y, center_width, item, "../README.md", item["step"]))
    foot_y = shared_y + len(shared)*row_h + 5
    parts.append(f'<text x="42" y="{foot_y}" class="foot">Solid teal = record-backed · purple = family account · dashed ochre = proposed link.</text>')
    for i, piece in enumerate(wrap(tree["caveat"], 135)):
        parts.append(f'<text x="42" y="{foot_y+23+i*20}" class="foot">{esc(piece)}</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    for tree in TREES:
        path = OUT / f'{tree["slug"]}.svg'
        path.write_text(render(tree), encoding="utf-8")
        print(path)
