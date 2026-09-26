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
         txt(54, 93, 'Solid = census or family-reported link     Dashed = strong identity match', size=16, fill="#52616a")]
    people = [
        ("Matthew Kramer (c. 1840)", "1900 census father · Matthias identity open", "CENSUS", "#547487"),
        ("Ferdinand (c. 1882)", "1900 son · 1930 father · later foreman", "CENSUS", "#127f82"),
        ("Ferdinand Louis (1913)", "1930 son · 1950 machine-operator match", "CENSUS", "#127f82"),
        ("Fred / Ferdinand Francis (1939)", "Techneglas · Army Reserve · obituary", "OBITUARY", "#b46827"),
        ("Paul Joseph Kramer", "Army Reserve · family account", "FAMILY", "#5c6ba0"),
        ("Justin Paul Kramer", "son of Paul and Melissa Miller Kramer", "FAMILY", "#5c6ba0"),
    ]
    ys = [124 + i * 105 for i in range(len(people))]
    for i, (name, detail, label, color) in enumerate(people):
        y = ys[i]
        if i:
            prev = ys[i-1] + 73
            dash = ' stroke-dasharray="7 7"' if i == 3 else ''
            b.append(f'<line x1="102" y1="{prev}" x2="102" y2="{y}" stroke="{color}" stroke-width="3"{dash}/>')
            b.append(f'<circle cx="102" cy="{y}" r="5" fill="{color}"/>')
        b.extend([f'<rect x="54" y="{y}" width="990" height="73" rx="13" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="54" y="{y}" width="8" height="73" rx="4" fill="{color}"/>',
                  txt(85, y+31, name, size=23, weight=700),
                  txt(85, y+57, detail, size=16, fill="#52616a"),
                  f'<rect x="850" y="{y+18}" width="165" height="35" rx="17" fill="{color}"/>',
                  txt(932, y+42, label, size=13, fill="#fff", weight=700, extra='text-anchor="middle"')])
    b += [txt(54, 774, 'Open: Matthew = Matthias? 1913 Ferdinand L. = Fred’s father? Bernhard parent link?', size=16, fill="#52616a")]
    save('kramer-lineage.svg', ''.join(b), w, h,
         'Kramer working lineage',
         'Six people from Matthew Kramer to Justin Kramer. The 1900 and 1930 census households record the first two links; the next identity match needs a certificate. Three Ferdinand generations have distinct labels.')


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
    w, h = 1050, 710
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="710" fill="#127f82"/>',
         txt(52, 59, 'Work recorded along the Wilkes-Barre line', size=30, weight=700),
         txt(52, 89, 'Different people and sources; this is a sequence of records, not one continuous job.', size=16, fill="#52616a")]
    rows = [
        ('1871–1900', 'Matthew / Matthias', 'mason → laborer → ropemaker', 'city directories; identity proposed'),
        ('1889–1904', 'Same-address Kramers', 'silk beamer · book sewer · dressmaker · bottler', 'directories; kinship unproved'),
        ('1940', 'Ferdinand (c. 1882)', 'wire-rope foreman · $1,996 wages in 1939', 'census; owned home estimated $2,400'),
        ('1940–43', 'Emil Carl (1915)', 'ACCO strander → Army enlistment', 'draft card; marriage; enlistment'),
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
    b.append(txt(52, 690, 'Money figures are one 1940 census snapshot. They cannot establish a family wealth trend.', size=15, fill="#52616a"))
    save('kramer-work.svg', ''.join(b), w, h,
         'Recorded Kramer work in Wilkes-Barre',
         'A dated sequence of occupations from directories, censuses, Emil Carl Kramers signed draft card, marriage and enlistment records, obituary and family account. The only income figures are a 1939 wage and 1940 home estimate for the older Ferdinand.')


def bosch_connection():
    w, h = 1040, 480
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="480" fill="#b46827"/>',
         txt(48, 59, 'The Bosch link, across a census page break', size=30, weight=700),
         txt(48, 87, '1920: sheet 8A ends with the parents; sheet 8B continues their household.', size=16, fill="#52616a")]

    def box(x, y, width, color, title, detail):
        b.extend([f'<rect x="{x}" y="{y}" width="{width}" height="76" rx="12" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="{x}" y="{y}" width="8" height="76" rx="4" fill="{color}"/>',
                  txt(x + 22, y + 31, title, size=20, weight=700),
                  txt(x + 22, y + 57, detail, size=16, fill="#52616a")])

    box(48, 116, 440, '#b46827', 'Amiel + Hildegard Bosch', 'Baden-born · reported arrival c. 1880')
    box(552, 116, 440, '#127f82', 'Ferdinand + Rose A. Kramer', '1920 household head + wife')
    b += ['<path d="M268 192 L268 222 L520 222 L520 245 M772 192 L772 222 L520 222" fill="none" stroke="#85979b" stroke-width="3"/>',
          txt(520, 242, 'in-laws to Ferdinand = Rose’s parents', size=15, fill="#52616a", extra='text-anchor="middle"')]
    box(48, 259, 944, '#127f82', 'Ferdinand L. (1913) + Emil Carl (1915)', 'Sons on 1920 sheet 8B · Hilda joined the household by 1930')
    b += ['<line x1="520" y1="245" x2="520" y2="259" stroke="#85979b" stroke-width="3"/>',
          txt(48, 377, 'Rose’s Bosch surname is named in Emil’s 1941 marriage application.', size=17),
          txt(48, 408, 'Greener as Hildegard’s maiden name and an exact immigration date still need records.', size=16, fill="#52616a")]
    save('bosch-1920-connection.svg', ''.join(b), w, h,
         'The Bosch and Kramer households in the 1920 census',
         'The 1920 census spans two sheets. Ferdinand and Rose Kramer are on sheet 8A. Rose’s parents Amiel and Hildegard Bosch and the two sons are on sheet 8B. The Bosch couple reported birth in Baden and immigration about 1880; their exact arrival and Hildegard’s maiden name remain open.')


def weatherford_smith_generations():
    w, h = 1080, 660
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="660" fill="#127f82"/>',
         txt(54, 62, 'Four layers of the Weatherford–Smith family', size=31, weight=700),
         txt(54, 92, 'Census and marriage records now identify Gladys’s parents; James’s earlier link remains open.', size=16, fill="#52616a")]

    def card(x, y, width, color, layer, name, detail):
        b.extend([f'<rect x="{x}" y="{y}" width="{width}" height="88" rx="13" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="{x}" y="{y}" width="8" height="88" rx="4" fill="{color}"/>',
                  txt(x+23, y+25, layer, size=14, fill=color, weight=700),
                  txt(x+23, y+51, name, size=21, weight=700),
                  txt(x+23, y+75, detail, size=15, fill="#52616a")])

    card(54, 125, 464, '#127f82', 'GREAT-GRANDPARENTS', 'Doctor Duffy + Annie Neathery', '1930 household and original death records')
    card(562, 125, 464, '#b46827', 'GLADYS’S PARENTS', 'W. Howard Blevins + Mary Hines', '1931 marriage · 1940 census household')
    card(54, 255, 464, '#127f82', 'GRANDPARENTS', 'Garnett Sr. + Florence', 'Garnett Sr. is D.D. and Annie’s son')
    card(562, 255, 464, '#b46827', 'GRANDPARENTS', 'James A. Smith + Gladys Blevins', '2008 memorial names all five children')
    card(218, 385, 644, '#5c6ba0', 'PARENTS', 'John Gordon Weatherford Sr. + Alice Smith', 'John: three named siblings · Alice: four memorial-named siblings')
    card(218, 515, 644, '#5c6ba0', 'CHILDREN', 'Ashley · John Jr. · Tancy Weatherford', 'Family-supplied sibling group; dates not established')
    b.append('<line x1="285" y1="213" x2="285" y2="255" stroke="#85979b" stroke-width="3"/>')
    b.append('<line x1="905" y1="213" x2="905" y2="255" stroke="#85979b" stroke-width="3"/>')
    b.extend(['<path d="M286 343 L286 367 L540 367 L540 385 M794 343 L794 367 L540 367" fill="none" stroke="#85979b" stroke-width="3"/>',
              '<line x1="540" y1="473" x2="540" y2="515" stroke="#85979b" stroke-width="3"/>',
              txt(54, 634, 'Gladys’s parent link is recorded; James’s parents and Florence’s parents remain unproved.', size=15, fill="#52616a")])
    save('weatherford-smith-generations.svg', ''.join(b), w, h,
         'Weatherford and Smith family generations',
         'Four layers from D.D. and Annie Weatherford and the documented parents of Gladys Blevins to Garnett and Florence, James and Gladys, John and Alice, then Ashley, John Jr. and Tancy. James Smith’s parents remain unconfirmed.')


def smith_blevins_lineage():
    w, h = 1080, 660
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="660" fill="#b46827"/>',
         txt(54, 62, 'Alice’s Smith and Blevins evidence map', size=31, weight=700),
         txt(54, 91, 'Solid: census, marriage or memorial link  ·  Dashed: candidate or member-tree lead', size=15, fill='#52616a')]

    def card(x, y, width, color, heading, detail, note):
        b.extend([f'<rect x="{x}" y="{y}" width="{width}" height="93" rx="13" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="{x}" y="{y}" width="8" height="93" rx="4" fill="{color}"/>',
                  txt(x+22, y+27, heading, size=20, weight=700),
                  txt(x+22, y+53, detail, size=16),
                  txt(x+22, y+77, note, size=14, fill='#52616a')])

    card(54, 122, 463, '#547487', 'Raymond J. + Allice Maulhall', 'Candidate parents of James', '1990 Social Security record; spouse unlinked')
    card(562, 122, 463, '#b46827', 'W. Howard Blevins + Mary E. Hines', 'Gladys’s parents · married 1931', '1940 household has G. Louise Blevins')
    card(54, 275, 463, '#547487', 'James Allen Smith', '1933–1990 on shared grave marker', '1986 return names him as Alice’s father')
    card(562, 275, 463, '#b46827', 'Gladys Louise Blevins Smith', '1938–2008 · born Bristol, Virginia', '2008 memorial names husband and five children')
    card(185, 451, 710, '#5c6ba0', 'Five children, including Alice', 'Jane · James “Buck” · Timothy · Alice · Carolyn', '2008 memorial; Jane, Buck and Alice: original marriage returns')
    b.extend(['<line x1="285" y1="215" x2="285" y2="275" stroke="#547487" stroke-width="3" stroke-dasharray="7 7"/>',
              '<line x1="794" y1="215" x2="794" y2="275" stroke="#b46827" stroke-width="3"/>',
              '<path d="M285 368 L285 412 L540 412 L540 451 M794 368 L794 412 L540 412" fill="none" stroke="#85979b" stroke-width="3"/>',
              txt(54, 593, 'Further Blevins: William E.’s certificate names Shubiel + Ada; his 1918 marriage names Tancy.', size=16, fill='#344954'),
              txt(54, 624, 'William Howard → William E. remains a 1920-household lead; see deeper evidence ladder.', size=15, fill='#52616a')])
    save('smith-blevins-lineage.svg', ''.join(b), w, h,
         'Evidence map of Alice Smith Weatherford’s ancestry',
         'Alice’s parents James Allen Smith and Gladys Louise Blevins had five named children. Gladys’s parents William Howard Blevins and Mary Elizabeth Hines are linked by a 1931 marriage and 1940 census. A same-name Social Security record proposes James’s parents Raymond J. Smith and Allice Maulhall, but the identity needs a spouse or child bridge. William Elkanah’s 1929 certificate names Shubiel and Ada; his 1918 marriage names Tancy Barker; his proposed son William Howard still needs a direct record.')


def weatherford_deep_lineage():
    w, h = 1080, 790
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         '<rect x="0" y="0" width="12" height="790" fill="#127f82"/>',
         txt(54, 62, 'Ashley’s Weatherford line, five generations', size=31, weight=700),
         txt(54, 91, 'Death certificates and censuses connect the older relatives; living links use family accounts.', size=15, fill="#52616a")]

    def card(x, y, width, color, layer, name, detail):
        b.extend([f'<rect x="{x}" y="{y}" width="{width}" height="88" rx="13" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="{x}" y="{y}" width="8" height="88" rx="4" fill="{color}"/>',
                  txt(x+22, y+24, layer, size=13, fill=color, weight=700),
                  txt(x+22, y+51, name, size=20, weight=700),
                  txt(x+22, y+73, detail, size=14, fill="#52616a")])

    card(54, 122, 464, '#127f82', 'DUFFY’S PARENTS', 'George C. + Ella Lumpkin', 'Duffy’s 1966 certificate names both')
    card(562, 122, 464, '#b46827', 'ANNIE’S PARENTS', 'John R. Neathery + Annie Phelps', 'Annie’s 1969 certificate names both')
    card(192, 257, 696, '#127f82', 'GREAT-GRANDPARENTS', 'Doctor Duffy + Annie Lillian', 'Duffy: Caswell County, NC → Dan River, VA')
    card(192, 392, 696, '#127f82', 'GRANDPARENTS', 'Garnett Sr. + Florence Morrison', 'Garnett: 1930 household; 1946 Navy-discharge card')
    card(192, 527, 696, '#5c6ba0', 'PARENTS', 'John Gordon + Alice Smith', '1986 marriage return; Fairfax County homes')
    card(192, 662, 696, '#5c6ba0', 'ASHLEY’S GENERATION', 'Ashley · John Jr. · Tancy', 'Sibling group supplied by Justin')
    b.extend(['<path d="M286 210 L286 233 L540 233 L540 257 M794 210 L794 233 L540 233" fill="none" stroke="#85979b" stroke-width="3"/>'])
    for y1, y2 in ((345, 392), (480, 527), (615, 662)):
        b.append(f'<line x1="540" y1="{y1}" x2="540" y2="{y2}" stroke="#85979b" stroke-width="3"/>')
    b.append(txt(54, 773, 'Earlier: George and Ella’s 1884 register names parents; the 1880 census has a name conflict.', size=14, fill='#52616a'))
    save('weatherford-deep-lineage.svg', ''.join(b), w, h,
         'Five generations of Ashley Weatherford’s paternal family',
         'George C. Weatherford and Ella Lumpkin, and John R. Neathery and Annie Phelps, precede Doctor Duffy Weatherford and Annie Lillian Neathery, Garnett and Florence Weatherford, John and Alice Weatherford, and Ashley with siblings John Jr. and Tancy. Original certificates and censuses support the older generations; the most recent links are family supplied.')


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


def blevins_deep_lineage():
    w, h = 1120, 930
    b = [f'<rect width="{w}" height="{h}" fill="#f6f3eb"/>',
         f'<rect width="12" height="{h}" fill="#b46827"/>',
         txt(52, 55, 'How far does Ashley’s Blevins line go?', size=31, weight=700),
         txt(52, 85, 'The color and connectors show what has actually been checked.', size=17, fill='#52616a')]
    rows = [
        ('James Blevins (c. 1708)', 'Earliest person in linked tree; no overseas birthplace', 'TREE', '#9b7955'),
        ('James Blevins (c. 1740)', 'Parentage disputed by Blevins researcher', 'TREE', '#9b7955'),
        ('Joseph Sr. (c. 1770) → Daniel (c. 1802)', 'Two proposed parent-child links; originals needed', 'TREE', '#9b7955'),
        ('Shubiel Blevins (1844–1913?)', '1860 household lead; Civil War roster and grave', 'MIXED', '#547487'),
        ('William Elkanah (1876–1929)', 'Death certificate names Shubiel + Ada Thompson', 'RECORD', '#127f82'),
        ('William Howard (c. 1908–1991?)', '1920 Howard + William E. household; relationship open', 'LEAD', '#547487'),
        ('Gladys Louise Blevins (1938–2008)', '1940 census: William Howard + Mary Hines', 'RECORD', '#127f82'),
        ('Alice Smith → Ashley Weatherford', '1986 marriage return + family account', 'MIXED', '#547487'),
    ]
    top, step, box_h = 116, 98, 74
    for i, (name, note, status, color) in enumerate(rows):
        y = top + i * step
        if i:
            line_color = '#127f82' if i in (4, 6, 7) else '#9b7955'
            dash = '' if i in (4, 6, 7) else ' stroke-dasharray="7 7"'
            b.append(f'<line x1="101" y1="{y-step+box_h}" x2="101" y2="{y}" stroke="{line_color}" stroke-width="3"{dash}/>')
        b.extend([f'<rect x="52" y="{y}" width="1016" height="{box_h}" rx="12" fill="#fff" stroke="#d8dedc"/>',
                  f'<rect x="52" y="{y}" width="8" height="{box_h}" rx="4" fill="{color}"/>',
                  txt(78, y+29, name, size=21, weight=700),
                  txt(78, y+55, note, size=16, fill='#52616a'),
                  f'<rect x="901" y="{y+17}" width="140" height="34" rx="17" fill="{color}"/>',
                  txt(971, y+40, status, size=13, fill='#fff', weight=700, extra='text-anchor="middle"')])
    b.extend(['<rect x="52" y="911" width="1016" height="1" fill="#d8dedc"/>',
              txt(52, 891, 'Open: William Howard’s birth/1910 record; Shubiel’s roster page; Joseph and both James links.', size=15, fill='#52616a')])
    save('blevins-deep-lineage.svg', ''.join(b), w, h,
         'Ashley Weatherford’s Blevins evidence ladder',
         'Eight layers from James Blevins circa 1708 to Ashley. Dashed connectors indicate proposed or ambiguous links. William Elkanah’s 1929 death record directly names Shubiel and Ada. The 1920 census suggests, but does not prove, William Howard as William Elkanah’s son. The oldest colonial links are tree hypotheses.')


if __name__ == '__main__':
    lineage()
    property_assessments()
    kramer_work()
    bosch_connection()
    weatherford_smith_generations()
    smith_blevins_lineage()
    weatherford_deep_lineage()
    miller_raber_family()
    blevins_deep_lineage()
