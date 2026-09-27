"""Build a compact coverage map for the cited family asset ledger."""

from pathlib import Path
from xml.sax.saxutils import escape


ROWS = [
    ("Disqué / Schaaf", [("1684 mill rights", "work"), ("1839 mill sale", "work"), ("No record", "empty"), ("No record", "empty")]),
    ("Kramer / Bosch", [("No record", "empty"), ("1870 $3k land + work", "work"), ("1940 home + wages", "value"), ("1975 Bridon work", "work")]),
    ("Miller / Gower", [("No record", "empty"), ("No record", "empty"), ("1954 $1,500 sale*", "memoir"), ("No record", "empty")]),
    ("Raber / Fairchild", [("No record", "empty"), ("No record", "empty"), ("No record", "empty"), ("No record", "empty")]),
    ("Weatherford", [("No record", "empty"), ("No record", "empty"), ("No record", "empty"), ("1980–2019 sales", "value")]),
    ("Smith / Blevins", [("1737 land?", "lead"), ("1860 $150?", "lead"), ("1930–40 rent + pay", "work"), ("2010 $360k sale", "value")]),
    ("Cordaro / Caucci", [("No record", "empty"), ("No record", "empty"), ("1938 laborer", "work"), ("1962 secretary", "work")]),
]

COLORS = {
    "value": ("#dceee8", "#176c59"),
    "work": ("#e5edf6", "#3e6080"),
    "memoir": ("#fff0cc", "#885f1d"),
    "lead": ("#fae7dc", "#99533b"),
    "empty": ("#f1f2ef", "#829092"),
}


def t(x, y, value, size=16, fill="#17343d", weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{escape(value)}</text>')


def main():
    width, height = 1200, 690
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             '<title id="title">Economic evidence across family lines and eras</title>',
             '<desc id="desc">Seven family lines across four periods. Colored cells show dated prices, asset rights, work records, family memories, or candidate records. Gray cells mean no usable record found. This is source coverage, not a wealth curve.</desc>',
             f'<rect width="{width}" height="{height}" fill="#f8f6f0"/>',
             '<rect width="12" height="690" fill="#a27432"/>',
             t(48, 55, "Where the economic evidence is", 30, weight=700),
             t(48, 85, "By family line and period · source coverage, not a wealth curve", 17, fill="#59696c")]
    labels = ["1650–1799", "1800–1899", "1900–1959", "1960–2026"]
    x0, step, cw = 280, 224, 210
    for col, label in enumerate(labels):
        parts.append(t(x0 + col * step + cw / 2, 138, label, 15, fill="#516569", weight=700, anchor="middle"))
    for row, (name, cells) in enumerate(ROWS):
        y = 158 + row * 61
        parts.append(t(48, y + 33, name, 17, weight=700))
        for col, (label, kind) in enumerate(cells):
            x = x0 + col * step
            fill, ink = COLORS[kind]
            parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="49" rx="9" fill="{fill}"/>')
            parts.append(t(x + cw / 2, y + 30, label, 14, fill=ink, weight=700 if kind != "empty" else 400, anchor="middle"))
    parts.append(t(48, 612, "Colored cells show the kind of evidence; amounts are from different years and cannot be compared directly.", 15, fill="#506368"))
    parts.append(t(48, 639, "? = candidate Blevins record, descent unproved    * = Paulene's recollection, deed unexamined", 14, fill="#765f47"))
    parts.append(t(48, 665, "Sources and precise limits: research/assets-by-generation.md", 13, fill="#66787a"))
    parts.append('</svg>')
    Path(__file__).with_name('asset-evidence-over-time.svg').write_text(''.join(parts), encoding='utf-8')


if __name__ == '__main__':
    main()
