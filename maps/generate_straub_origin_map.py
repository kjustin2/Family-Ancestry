"""Map the conflicting country labels for Louisa Straub, without inventing a town."""

import html
import json
import urllib.request
from pathlib import Path

from generate_map import GEOJSON, paths


def main():
    request = urllib.request.Request(GEOJSON, headers={"User-Agent": "FamilyAncestryResearch/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        features = json.load(response)["features"]
    countries = {feature["properties"]["ADMIN"]: feature for feature in features}
    bounds = (-5.5, 42.0, 16.5, 55.5)
    box = (52, 112, 600, 392)

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="590" viewBox="0 0 1160 590" role="img" aria-labelledby="title desc">',
        '<title id="title">Louisa Straub: France and Germany in conflicting birth reports</title>',
        '<desc id="desc">A map colors France and Germany only at country scale. Louisa Hollinger’s original 1941 death certificate reports France for her and father Nicholas Straub, while the 1900, 1910, 1920 and 1930 census records report Germany for Louisa. No birth town or route is identified; her arrival-year reports disagree.</desc>',
        '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#173b4a}.title{font-size:29px;font-weight:700}.subtitle{font-size:16px;fill:#526a75}.country{font-size:20px;font-weight:700}.cardtitle{font-size:19px;font-weight:700}.body{font-size:16px}.note{font-size:14px;fill:#526a75}.land{fill:#e5e9e4;stroke:#abb8af;stroke-width:1}.france{fill:#66a7af;stroke:#347985;stroke-width:2}.germany{fill:#d8a160;stroke:#a9753e;stroke-width:2}</style>',
        '<rect width="1160" height="590" rx="18" fill="#f5f7f5"/>',
        '<text x="42" y="50" class="title">Louisa Straub: two country labels</text>',
        '<text x="42" y="77" class="subtitle">Country-scale evidence only · Her birth town and travel route have not been found</text>',
        '<rect x="28" y="100" width="640" height="438" rx="16" fill="#eaf1f1"/>',
    ]
    for country in ("Belgium", "Netherlands", "Luxembourg", "Switzerland", "Austria", "Italy", "Czechia", "Poland", "Spain", "United Kingdom"):
        if country in countries:
            parts.append(f'<path d="{html.escape(paths(countries[country], bounds, box))}" class="land"/>')
    for country, css in (("France", "france"), ("Germany", "germany")):
        parts.append(f'<path d="{html.escape(paths(countries[country], bounds, box))}" class="{css}"/>')
    parts += [
        '<text x="173" y="360" class="country" fill="#104c55">FRANCE</text>',
        '<text x="405" y="285" class="country" fill="#764817">GERMANY</text>',
        '<rect x="696" y="106" width="432" height="136" rx="14" fill="#e1f0f0"/>',
        '<text x="718" y="141" class="cardtitle">1941 death certificate</text>',
        '<text x="718" y="173" class="body">Louisa and father Nicholas: France</text>',
        '<text x="718" y="204" class="note">Original form; birthplace from informant</text>',
        '<rect x="696" y="256" width="432" height="136" rx="14" fill="#f4e9d9"/>',
        '<text x="718" y="291" class="cardtitle">1900–1930 censuses</text>',
        '<text x="718" y="323" class="body">Louisa: Germany</text>',
        '<text x="718" y="354" class="note">Four household reports, not a birth record</text>',
        '<rect x="696" y="406" width="432" height="130" rx="14" fill="#fff" stroke="#ced9d8"/>',
        '<text x="718" y="440" class="cardtitle">What we can conclude</text>',
        '<text x="718" y="471" class="body">Foreign birth is well supported.</text>',
        '<text x="718" y="500" class="note">Specific town and arrival date remain open.</text>',
        '<text x="32" y="570" class="note">Map outlines: Natural Earth 1:110m, public domain. Country borders are modern context, not Louisa’s 1877 boundaries.</text>',
        '</svg>',
    ]
    output = Path(__file__).with_name("straub-origin-evidence.svg")
    output.write_text("\n".join(parts), encoding="utf-8")
    print(output)
    try:
        import cairosvg
    except ImportError:
        print("Optional PNG preview skipped; install cairosvg to regenerate it.")
    else:
        preview = output.with_name("straub-origin-evidence-preview.png")
        cairosvg.svg2png(url=str(output), write_to=str(preview))
        print(preview)


if __name__ == "__main__":
    main()
