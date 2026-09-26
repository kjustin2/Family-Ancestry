"""Regenerate the small evidence diagrams embedded in the family pages."""

from pathlib import Path
from xml.sax.saxutils import escape


HERE = Path(__file__).resolve().parent


def txt(x, y, value, *, size=20, fill="#163348", weight=400, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="Segoe UI, Arial, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{escape(value)}</text>')


def save(name, body, width, height, title, description):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">'
           f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>'
           + body + '</svg>')
    (HERE / name).write_text(svg, encoding="utf-8")


def lineage():
    w, h = 1100, 805
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="805" fill="#127f82"/>',
         txt(54, 62, 'The Kramer names, one generation at a time', size=32, weight=700),
         txt(54, 93, 'Solid = recorded or family-supplied link     Dashed = chart/proposed link', size=16, fill="#52616a")]
    people = [
        ("Matthew / Matthias Kramer", "charted 1840–1918 · mason, later ropemaker", "CHART / INDEX", "#547487"),
        ("Ferdinand (c. 1882)", "older foreman · 146 Prospect · 1940 census", "CENSUS", "#127f82"),
        ("Ferdinand Louis (1913)", "younger machine operator · 1950 census match", "STRONG MATCH", "#127f82"),
        ("Fred / Ferdinand Francis (1939)", "Techneglas · Army Reserve · obituary", "OBITUARY", "#b46827"),
        ("Paul Joseph Kramer", "Army Reserve · family account", "FAMILY", "#5c6ba0"),
        ("Justin Paul Kramer", "son of Paul and Melissa Miller Kramer", "FAMILY", "#5c6ba0"),
    ]
    ys = [124 + i * 105 for i in range(len(people))]
    for i, (name, detail, label, color) in enumerate(people):
        y = ys[i]
        if i:
            prev = ys[i-1] + 73
            dash = ' stroke-dasharray="7 7"' if i in (1, 2, 3) else ''
            b.append(f'<line x1="102" y1="{prev}" x2="102" y2="{y}" stroke="{color}" stroke-width="3"{dash}/>')
            b.append(f'<circle cx="102" cy="{y}" r="5" fill="{color}"/>')
        b.extend([f'<rect x="54" y="{y}" width="990" height="73" rx="13" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="54" y="{y}" width="8" height="73" rx="4" fill="{color}"/>',
                  txt(85, y+31, name, size=23, weight=700),
                  txt(85, y+57, detail, size=16, fill="#52616a"),
                  f'<rect x="850" y="{y+18}" width="165" height="35" rx="17" fill="{color}"/>',
                  txt(932, y+42, label, size=13, fill="#fff", weight=700, extra='text-anchor="middle"')])
    b += [txt(54, 774, 'Open: Matthew → 1882 Ferdinand; 1882 → 1913 Ferdinand; 1913 record → Fred’s father.', size=16, fill="#52616a")]
    save('kramer-lineage.svg', ''.join(b), w, h,
         'Kramer working lineage',
         'Six people from Matthew Kramer to Justin Kramer. Two early parent-child links are proposed; three successive Ferdinand generations have distinct labels.')


def property_assessments():
    w, h = 1010, 535
    years = [2000, 2005, 2008, 2016, 2026]
    vals = [234650, 620700, 597560, 471700, 850640]
    x0, x1, y0, y1 = 100, 940, 155, 405
    x = lambda year: x0 + (year - 2000) / 26 * (x1-x0)
    y = lambda value: y1 - value / 900000 * (y1-y0)
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="535" fill="#b46827"/>',
         txt(55, 62, 'One property, five county assessments', size=31, weight=700),
         txt(55, 92, '6307 Colette Drive · nominal dollars · selected years', size=17, fill="#52616a")]
    for value in (0, 300000, 600000, 900000):
        yy = y(value)
        b += [f'<line x1="{x0}" y1="{yy:.1f}" x2="{x1}" y2="{yy:.1f}" stroke="#d8dedc"/>',
              txt(78, yy+5, '$0' if value == 0 else f'${value//1000}k', size=15, fill="#52616a", extra='text-anchor="end"')]
    points = ' '.join(f'{x(yr):.1f},{y(v):.1f}' for yr,v in zip(years, vals))
    b.append(f'<polyline points="{points}" fill="none" stroke="#b46827" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    for yr, val in zip(years, vals):
        xx, yy = x(yr), y(val)
        b += [f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="8" fill="#fff" stroke="#b46827" stroke-width="4"/>',
              txt(xx, yy-19 if yr != 2000 else yy-20, f'${val:,}', size=16, weight=700, extra='text-anchor="middle"'),
              txt(xx, 433, str(yr), size=17, fill="#52616a", extra='text-anchor="middle"')]
    b += ['<rect x="55" y="465" width="900" height="44" rx="9" fill="#e9e2d5"/>',
          txt(72, 493, 'Assessments are estimates of this parcel; they are not equity, income, or family net worth.', size=17, fill="#344954")]
    save('colette-assessments.svg', ''.join(b), w, h,
         'Fairfax County assessments for 6307 Colette Drive',
         'Line chart of nominal county assessments: 2000 $234,650; 2005 $620,700; 2008 $597,560; 2016 $471,700; 2026 $850,640. These are property estimates, not family wealth.')


def kramer_work():
    w, h = 1050, 615
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="615" fill="#127f82"/>',
         txt(52, 59, 'Work recorded along the Wilkes-Barre line', size=30, weight=700),
         txt(52, 89, 'Different people and sources; this is a sequence of records, not one continuous job.', size=16, fill="#52616a")]
    rows = [
        ('1871–1900', 'Matthew / Matthias', 'mason → laborer → ropemaker', 'city directories; identity proposed'),
        ('1889–1904', 'Same-address Kramers', 'silk beamer · book sewer · dressmaker · bottler', 'directories; kinship unproved'),
        ('1940', 'Ferdinand (c. 1882)', 'wire-rope foreman · $1,996 wages in 1939', 'census; owned home estimated $2,400'),
        ('1950', 'Ferdinand Louis (1913)', 'wire-rope machine operator', 'census match; no income on sheet'),
        ('Later', 'Fred (1939) and Paul', 'Techneglas / Army Reserve; Army Reserve', 'Fred obituary / Paul family account'),
    ]
    for i,(period,name,work,note) in enumerate(rows):
        y=115+i*92
        b.extend([f'<rect x="52" y="{y}" width="946" height="78" rx="12" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="52" y="{y}" width="155" height="78" rx="12" fill="#127f82"/>',
                  txt(129, y+45, period, size=17, fill="#fff", weight=700, extra='text-anchor="middle"'),
                  txt(230, y+29, name, size=19, weight=700),
                  txt(230, y+55, work, size=17),
                  txt(976, y+27, note, size=13, fill="#52616a", extra='text-anchor="end"')])
    b.append(txt(52, 599, 'Money figures are one 1940 census snapshot. They cannot establish a family wealth trend.', size=15, fill="#52616a"))
    save('kramer-work.svg', ''.join(b), w, h,
         'Recorded Kramer work in Wilkes-Barre',
         'A dated sequence of occupations from city directories, censuses, obituary and family account. The only income figures are a 1939 wage and 1940 home estimate for the older Ferdinand.')


def weatherford_smith_generations():
    w, h = 1080, 660
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="660" fill="#127f82"/>',
         txt(54, 62, 'Four layers of the Weatherford–Smith family', size=31, weight=700),
         txt(54, 92, 'Marriage returns name Alice’s parents; their own parents and dates remain open.', size=16, fill="#52616a")]

    def card(x, y, width, color, layer, name, detail):
        b.extend([f'<rect x="{x}" y="{y}" width="{width}" height="88" rx="13" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="{x}" y="{y}" width="8" height="88" rx="4" fill="{color}"/>',
                  txt(x+23, y+25, layer, size=14, fill=color, weight=700),
                  txt(x+23, y+51, name, size=21, weight=700),
                  txt(x+23, y+75, detail, size=15, fill="#52616a")])

    card(54, 125, 464, '#127f82', 'GREAT-GRANDPARENTS', 'D.D. + Annie Neatherly', 'Helen’s notice names her and 12 siblings')
    card(562, 125, 464, '#b46827', 'EARLIER SMITH / BLEVINS', 'Four grandparents unknown', 'James’s and Gladys’s parents need records')
    card(54, 255, 464, '#127f82', 'GRANDPARENTS', 'Garnett Sr. + Florence', 'Garnett Sr. is D.D. and Annie’s son')
    card(562, 255, 464, '#b46827', 'GRANDPARENTS', 'James A. Smith + Gladys Blevins', '1986 return names both; Jane and Buck linked')
    card(218, 385, 644, '#5c6ba0', 'PARENTS', 'John Gordon Weatherford Sr. + Alice Smith', 'John: three named siblings · Alice: four reported siblings')
    card(218, 515, 644, '#5c6ba0', 'CHILDREN', 'Ashley · John Jr. · Tancy Weatherford', 'Family-supplied sibling group; dates not established')
    b.append('<line x1="285" y1="213" x2="285" y2="255" stroke="#85979b" stroke-width="3"/>')
    b.append('<line x1="794" y1="213" x2="794" y2="255" stroke="#85979b" stroke-width="3" stroke-dasharray="7 7"/>')
    b.extend(['<path d="M286 343 L286 367 L540 367 L540 385 M794 343 L794 367 L540 367" fill="none" stroke="#85979b" stroke-width="3"/>',
              '<line x1="540" y1="473" x2="540" y2="515" stroke="#85979b" stroke-width="3"/>',
              txt(54, 634, 'Solid: recorded or family links. Dashed: earlier Smith and Blevins parents unknown.', size=15, fill="#52616a")])
    save('weatherford-smith-generations.svg', ''.join(b), w, h,
         'Weatherford and Smith family generations',
         'Four layers from D.D. and Annie Weatherford and unknown earlier Smith and Blevins relatives to Garnett and Florence, James and Gladys, John and Alice, then Ashley, John Jr. and Tancy. The dashed earlier Smith and Blevins connection has not been identified.')


def miller_raber_family():
    w, h = 1180, 645
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="645" fill="#127f82"/>',
         txt(48, 56, 'Melissa’s two Berwick branches', size=31, weight=700),
         txt(48, 85, 'Left: Paulene Miller Beach’s memoir + Justin   ·   Right: Justin’s family account', size=16, fill='#52616a')]

    def card(x, y, width, color, heading, detail, note):
        b.extend([f'<rect x="{x}" y="{y}" width="{width}" height="82" rx="12" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="{x}" y="{y}" width="8" height="82" rx="4" fill="{color}"/>',
                  txt(x+22, y+26, heading, size=20, weight=700),
                  txt(x+22, y+50, detail, size=16),
                  txt(x+22, y+71, note, size=13, fill='#52616a')])

    card(48, 112, 515, '#127f82', 'Amos Miller + Mary Gower', 'Lester’s parents · memoir dates 1867–1943 / 1884–1954', 'Family memoir; vital records pending')
    card(618, 112, 515, '#b46827', 'Fairchild great-grandmother', 'Shirley’s mother · given name unknown', 'Justin’s account; record pending')
    card(48, 216, 515, '#127f82', 'Lester Miller + Mabel/Pearl Reese', 'Mabel raised by William + Clementine Wilson', 'Memoir; six named children')
    card(618, 216, 515, '#b46827', 'Shirley Kreisher Raber', 'Sonya’s mother · husband’s name unknown', 'Justin’s account; record pending')
    card(48, 320, 515, '#127f82', 'Paul Miller', 'Siblings: Marqueen, Paulene, Shirley, Gladys, Carl', 'Justin + Paulene’s memoir; Gladys lifespan disputed')
    card(618, 320, 515, '#b46827', 'Sonya Raber', 'Alice, Bill, Wendy, Tim, Tom on Sonya’s side', 'Sibling versus married-in roles unresolved')
    for x in (304, 874):
        for y in (194, 298):
            b.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+22}" stroke="#85979b" stroke-width="3"/>')
    b.extend(['<path d="M304 402 L304 429 L590 429 M874 402 L874 429 L590 429 L590 449" fill="none" stroke="#85979b" stroke-width="3"/>'])
    card(310, 449, 560, '#5c6ba0', 'Melissa Miller Kramer', 'Daughter of Paul + Sonya · mother of Justin', 'Parent links supplied by Justin')
    b.extend([txt(48, 577, 'Earlier Miller, Reese and Corderman relatives appear in the branch page.', size=17, fill='#344954'),
              txt(48, 607, 'Fairchild dairy in Paulene’s memoir is not linked to Sonya’s Fairchild ancestor.', size=15, fill='#52616a')])
    save('miller-raber-family.svg', ''.join(b), w, h,
         'Melissa Miller Kramer’s Miller and Raber family lines',
         'Two Berwick branches join at Paul Miller and Sonya Raber, whose daughter is Melissa. The Miller branch uses Paulene Beach’s family memoir and Justin’s account. The Raber, Kreisher and Fairchild branch currently rests on Justin’s account; the Fairchild ancestor is unnamed.')


if __name__ == '__main__':
    lineage()
    property_assessments()
    kramer_work()
    weatherford_smith_generations()
    miller_raber_family()
