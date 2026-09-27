"""Map Sicilian Cordaro places, a documented departure port, and local context."""

import html
import json
import urllib.request
from pathlib import Path

GEOJSON = (
    "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/"
    "geojson/ne_50m_admin_0_countries.geojson"
)
OUT = Path(__file__).with_name("cordaro-sutera-places.svg")


def project(lon, lat, bounds, box):
    west, south, east, north = bounds
    x, y, width, height = box
    return x + (lon - west) / (east - west) * width, y + (north - lat) / (north - south) * height


def polygon_path(polygon, bounds, box):
    result = []
    for ring in polygon:
        coords = [project(lon, lat, bounds, box) for lon, lat in ring]
        result.append("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in coords) + " Z")
    return " ".join(result)


def pin(lon, lat, bounds, box, color, radius=7):
    x, y = project(lon, lat, bounds, box)
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{color}" stroke="#fff" stroke-width="3"/>'


def main():
    request = urllib.request.Request(GEOJSON, headers={"User-Agent": "FamilyAncestryResearch/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        features = json.load(response)["features"]
    italy = next(f for f in features if f["properties"]["ADMIN"] == "Italy")
    polygons = italy["geometry"]["coordinates"]
    sicily = polygons[4]  # Natural Earth 50m: Sicily is a separate Italian polygon.

    italy_bounds, italy_box = (6, 35.7, 19, 47.6), (90, 150, 440, 465)
    sicily_bounds, sicily_box = (12.2, 36.45, 15.85, 38.55), (635, 155, 485, 440)
    sutera = (13.7313165, 37.5252277)  # OpenStreetMap relation 39258, approximate center.
    milocca = (13.73644, 37.47152)  # OpenStreetMap node 67254012: present Milena center.
    caltanissetta = (14.0632840, 37.4902628)  # OpenStreetMap relation 39221.
    palermo = (13.3524434, 38.1112268)  # OpenStreetMap relation 39513.
    sx, sy = project(*sutera, sicily_bounds, sicily_box)
    mx, my = project(*milocca, sicily_bounds, sicily_box)
    cx, cy = project(*caltanissetta, sicily_bounds, sicily_box)

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800" role="img" aria-labelledby="title desc">',
        '<title id="title">Cordaro family places in Sicily and the local context for migration</title>',
        '<desc id="desc">Italy overview and Sicily close-up. Sutera is named in the family passport and Pietra Magro\'s 1909 passenger list; Antonio Cordaro\'s 1878 birth and 1899 marriage are in nearby Milocca, now Milena. The 1909 list documents Palermo as the departure port. A 1905 landslide and sulfur-mine losses preceded the departures, but no personal migration motive is recorded.</desc>',
        '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#20354a}.title{font-size:30px;font-weight:700}.head{font-size:19px;font-weight:700}.label{font-size:17px;font-weight:650}.small{font-size:13px;fill:#536a78}.sea{fill:#eaf4f6}.land{fill:#d9e6dc;stroke:#89a69b;stroke-width:2;stroke-linejoin:round}.sicily{fill:#e9be77;stroke:#b97634;stroke-width:2;stroke-linejoin:round}.line{stroke:#ad512c;stroke-width:2;fill:none}</style>',
        '<rect width="1200" height="800" fill="#f3f7f5"/>',
        '<text x="50" y="55" class="title">Sutera and Milocca: two names in the Cordaro records</text>',
        '<text x="50" y="82" class="small">Milocca was a Sutera hamlet in 1878; the 1899 wedding was there • Palermo was the documented 1909 departure port</text>',
        '<rect x="48" y="115" width="520" height="530" rx="18" fill="#fbfdfc" stroke="#d8e6e4" stroke-width="2"/>',
        '<rect x="600" y="115" width="552" height="530" rx="18" fill="#fbfdfc" stroke="#d8e6e4" stroke-width="2"/>',
        '<text x="70" y="145" class="head">Italy</text>',
        '<text x="625" y="145" class="head">Sicily</text>',
        '<rect x="76" y="155" width="460" height="460" rx="12" class="sea"/>',
        '<rect x="620" y="155" width="512" height="460" rx="12" class="sea"/>',
    ]
    for index, polygon in enumerate(polygons):
        cls = "sicily" if index == 4 else "land"
        parts.append(f'<path d="{html.escape(polygon_path(polygon, italy_bounds, italy_box))}" class="{cls}"/>')
    parts.append(pin(*sutera, italy_bounds, italy_box, "#a84324", 8))
    parts.append('<text x="315" y="591" class="label">Sicily</text>')
    parts.append(f'<path d="{html.escape(polygon_path(sicily, sicily_bounds, sicily_box))}" class="sicily"/>')
    parts.append(pin(*palermo, sicily_bounds, sicily_box, "#698a9b", 5))
    parts.append('<text x="681" y="216" class="small">Palermo • 1909 ship departure</text>')
    parts.append(pin(*caltanissetta, sicily_bounds, sicily_box, "#698a9b", 6))
    parts.append(f'<path d="M {cx:.1f},{cy:.1f} L 925,443" stroke="#698a9b" stroke-width="1.5" fill="none"/>')
    parts.append('<text x="932" y="450" class="small">Caltanissetta city</text>')
    parts.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="15" fill="none" stroke="#a84324" stroke-width="2"/>')
    parts.append(pin(*sutera, sicily_bounds, sicily_box, "#a84324", 8))
    parts.append(f'<path d="M {sx:.1f},{sy:.1f} L 785,336" class="line"/>')
    parts.append('<text x="684" y="323" class="label">Sutera</text>')
    parts.append('<text x="684" y="342" class="small">Passport + Pietra\'s last Italian home</text>')
    parts.append(pin(*milocca, sicily_bounds, sicily_box, "#3b7190", 7))
    parts.append(f'<path d="M {mx:.1f},{my:.1f} L 930,512" stroke="#3b7190" stroke-width="2" fill="none"/>')
    parts.append('<text x="932" y="519" class="label">Milocca / Milena</text>')
    parts.append('<text x="932" y="538" class="small">1878 birth + 1899 marriage</text>')
    parts.extend([
        '<rect x="48" y="660" width="1104" height="106" rx="14" fill="#e4ede8"/>',
        '<circle cx="72" cy="685" r="7" fill="#a84324"/><text x="90" y="690" class="small">Passport + 1909 manifest: Sutera</text>',
        '<circle cx="420" cy="685" r="7" fill="#3b7190"/><text x="437" y="690" class="small">Original acts: Milocca</text>',
        '<circle cx="696" cy="685" r="6" fill="#698a9b"/><text x="713" y="690" class="small">Palermo: 1909 port · Caltanissetta: orientation</text>',
        '<text x="72" y="721" class="small">1905 landslide and sulfur-mine losses near Sutera preceded the departures; no record states the Cordaros’ motive.</text>',
        '<text x="72" y="746" class="small">Antonio reported a 1906 crossing; Pietra and two daughters appear on a 1909 passenger list.</text>',
        '<text x="50" y="783" class="small">Outline: Natural Earth 1:50m (public domain). Approximate centers: © OpenStreetMap contributors (ODbL). Not a historical map.</text>',
        '</svg>',
    ])
    OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
