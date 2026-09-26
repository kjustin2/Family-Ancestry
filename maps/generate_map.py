"""Generate a source-labelled family place map from public-domain Natural Earth geometry."""

import html
import json
import urllib.request
from pathlib import Path

GEOJSON = (
    "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/"
    "geojson/ne_110m_admin_0_countries.geojson"
)
OUT = Path(__file__).with_name("ancestral-places.svg")


def project(lon, lat, bounds, box):
    min_lon, min_lat, max_lon, max_lat = bounds
    x, y, width, height = box
    return (
        x + (lon - min_lon) / (max_lon - min_lon) * width,
        y + (max_lat - lat) / (max_lat - min_lat) * height,
    )


def paths(feature, bounds, box):
    geometry = feature["geometry"]
    polygons = geometry["coordinates"] if geometry["type"] == "MultiPolygon" else [geometry["coordinates"]]
    result = []
    for polygon in polygons:
        for ring in polygon:
            # Ignore Alaska, Hawaii, and other separated U.S. polygons in the lower-48 panel.
            visible = [(lon, lat) for lon, lat in ring if bounds[0] <= lon <= bounds[2] and bounds[1] <= lat <= bounds[3]]
            if len(visible) < 3:
                continue
            points = [project(lon, lat, bounds, box) for lon, lat in visible]
            result.append("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in points) + " Z")
    return " ".join(result)


def marker(lon, lat, bounds, box, label, note="", dx=12, dy=-8, color="#b24b35"):
    x, y = project(lon, lat, bounds, box)
    label = html.escape(label)
    note = html.escape(note)
    return (
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{color}" stroke="white" stroke-width="2"/>'
        f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" class="place">{label}</text>'
        + (f'<text x="{x + dx:.1f}" y="{y + dy + 16:.1f}" class="note">{note}</text>' if note else "")
    )


def main():
    request = urllib.request.Request(GEOJSON, headers={"User-Agent": "FamilyAncestryResearch/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        features = json.load(response)["features"]
    countries = {feature["properties"]["ADMIN"]: feature for feature in features}
    us_bounds, us_box = (-125, 24, -66, 50), (75, 125, 500, 290)
    de_bounds, de_box = (5.7, 47.2, 15.2, 55.1), (685, 125, 420, 290)
    pf_bounds, pf_box = (7.48, 49.12, 8.42, 49.56), (75, 505, 715, 285)
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="860" viewBox="0 0 1200 860" role="img" aria-labelledby="title desc">',
        '<title id="title">Family history place map: Pennsylvania, Virginia and the German Palatinate</title>',
        '<desc id="desc">General place markers, not personal addresses. The German connection to Magdalena Disque is proposed, while the older mill sites are documented independently.</desc>',
        '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#20354a}.title{font-size:29px;font-weight:700}.heading{font-size:19px;font-weight:700}.place{font-size:16px;font-weight:650}.note{font-size:12px;fill:#52677a}.fine{font-size:12px;fill:#52677a}.sea{fill:#edf4f6}.land{fill:#d9e3dc;stroke:#9eafa4;stroke-width:1.5}.panel{fill:#f8fbfb;stroke:#d5e2e4;stroke-width:1.5}.grid{stroke:#e4ebed;stroke-width:1}.number{font-size:13px;font-weight:700;fill:white}</style>',
        '<rect width="1200" height="860" fill="#f2f6f4"/>',
        '<text x="55" y="50" class="title">Where the known and proposed lines lived</text>',
        '<text x="55" y="76" class="note">Town and city centers only • Not a travel route, home address, or proof of a family link</text>',
        '<rect x="48" y="98" width="540" height="350" rx="18" class="panel"/>',
        '<rect x="613" y="98" width="540" height="350" rx="18" class="panel"/>',
        '<text x="70" y="124" class="heading">United States</text>',
        '<text x="635" y="124" class="heading">Germany</text>',
        f'<path d="{paths(countries["United States of America"], us_bounds[:4], us_box)}" class="land"/>',
        f'<path d="{paths(countries["Germany"], de_bounds[:4], de_box)}" class="land"/>',
        marker(-75.8813, 41.2459, us_bounds[:4], us_box, "Wilkes-Barre, PA", "Kramer directories; Disque lead", dx=-180, dy=-14),
        marker(-77.0469, 38.8048, us_bounds[:4], us_box, "Alexandria, VA", "Weatherford–Smith family report", dx=-180, dy=32, color="#346f9b"),
        marker(7.95, 49.25, de_bounds[:4], de_box, "The Palatinate", "Disqué–Schaaf mill region", dx=18, dy=0),
        '<rect x="48" y="470" width="1105" height="340" rx="18" class="panel"/>',
        '<text x="70" y="498" class="heading">Palatinate place detail (approximate town centers)</text>',
    ]
    for lon in (7.6, 7.8, 8.0, 8.2, 8.4):
        x, _ = project(lon, 49.3, pf_bounds[:4], pf_box)
        parts.append(f'<line x1="{x:.1f}" y1="520" x2="{x:.1f}" y2="785" class="grid"/>')
    for lat in (49.2, 49.3, 49.4, 49.5):
        _, y = project(7.8, lat, pf_bounds[:4], pf_box)
        parts.append(f'<line x1="75" y1="{y:.1f}" x2="790" y2="{y:.1f}" class="grid"/>')
    places = [
        ("1", "Geiselberger Mühle", 7.66, 49.33, "Schaaf mill, documented"),
        ("2", "Siebeldingen", 8.05, 49.21, "Disqué mill, documented"),
        ("3", "Rinnthal", 7.93, 49.22, "Sebastian's mill, documented"),
        ("4", "Wilgartswiesen", 7.88, 49.23, "Disqué mill, documented"),
        ("5", "Hinterweidenthal", 7.75, 49.20, "Disqué mill, documented"),
        ("6", "Knittelsheim", 8.25, 49.20, "Johann Ludwig's mill, documented"),
        ("7", "Hofstätten", 7.90, 49.24, "1844 migrant's recorded birthplace"),
        ("8", "Trippstadt", 7.82, 49.36, "Fröhlich birth; migration card"),
    ]
    for index, name, lon, lat, note in places:
        x, y = project(lon, lat, pf_bounds[:4], pf_box)
        parts += [
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="#b24b35" stroke="white" stroke-width="2"/>',
            f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" class="number">{index}</text>',
            f'<text x="820" y="{533 + (int(index)-1)*32}" class="place">{index}. {html.escape(name)}</text>',
            f'<text x="820" y="{549 + (int(index)-1)*32}" class="fine">{html.escape(note)}</text>',
        ]
    parts += [
        '<text x="55" y="834" class="fine">Outline: Natural Earth, public domain (1:110m). Coordinates are approximate centers; geometry simplified.</text>',
        '</svg>',
    ]
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(OUT)
    try:
        import cairosvg
    except ImportError:
        print("Optional PNG preview skipped; install cairosvg to regenerate it.")
    else:
        png = OUT.with_name("ancestral-places-preview.png")
        cairosvg.svg2png(url=str(OUT), write_to=str(png))
        print(png)


if __name__ == "__main__":
    main()
