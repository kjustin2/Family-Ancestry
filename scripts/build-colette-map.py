"""Build a small present-day neighborhood map from Fairfax County road data."""

import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "maps" / "colette-neighborhood.svg"
ENDPOINT = (
    "https://services1.arcgis.com/ioennV6PpG5Xodq0/arcgis/rest/"
    "services/OpenData_A1/FeatureServer/0/query"
)
WEST, SOUTH, EAST, NORTH = -77.168, 38.751, -77.153, 38.759
HOME_LON, HOME_LAT = -77.160869452122, 38.755193052501
GLADYS_LON, GLADYS_LAT = -77.162536619636, 38.754417595085
FLORENCE_LON, FLORENCE_LAT = -77.160738206784, 38.754186693613
MAP_X, MAP_Y, MAP_W, MAP_H = 44, 98, 888, 610


def point(lon, lat):
    return (
        MAP_X + (lon - WEST) / (EAST - WEST) * MAP_W,
        MAP_Y + (NORTH - lat) / (NORTH - SOUTH) * MAP_H,
    )


def parts(geometry):
    if geometry["type"] == "LineString":
        return [geometry["coordinates"]]
    if geometry["type"] == "MultiLineString":
        return geometry["coordinates"]
    return []


params = urlencode(
    {
        "where": "1=1",
        "geometry": f"{WEST},{SOUTH},{EAST},{NORTH}",
        "geometryType": "esriGeometryEnvelope",
        "inSR": "4326",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "FULLNAME,DRAW_SYMBOL",
        "outSR": "4326",
        "returnGeometry": "true",
        "f": "geojson",
    }
)
with urlopen(f"{ENDPOINT}?{params}", timeout=30) as response:
    features = json.load(response)["features"]

roads = []
for feature in features:
    name = feature["properties"].get("FULLNAME") or ""
    for coords in parts(feature["geometry"]):
        if len(coords) < 2:
            continue
        xy = [point(lon, lat) for lon, lat in coords]
        path = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in xy)
        major = name in {"BEULAH ST", "KINGSTOWNE VILLAGE PKWY"}
        roads.append((path, major))

svg = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760" role="img" aria-labelledby="title desc">',
    '<title id="title">Colette Drive family neighborhood in Franconia, Fairfax County</title>',
    '<desc id="desc">Present-day Fairfax County streets and approximate Census geocoder locations for John and Alice Weatherford at 6307 Colette Drive, Gladys Smith at 6330 Miller Drive, and Florence Weatherford at 6312 Miller Drive. Family relationships and residences are family-supplied; county parcel records independently connect the names to the addresses.</desc>',
    '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#233a49}.title{font-size:29px;font-weight:700}.sub{font-size:15px;fill:#526b73}.roadlabel{font-size:16px;font-weight:700;fill:#3f5861}.label{font-size:18px;font-weight:700}.body{font-size:15px}.small{font-size:13px;fill:#526b73}</style>',
    '<rect width="1200" height="760" fill="#f7faf7"/>',
    '<text x="44" y="48" class="title">Three family homes in one neighborhood</text>',
    '<text x="44" y="72" class="sub">Alexandria mailing address · Franconia, Fairfax County · current street layout</text>',
    f'<rect x="{MAP_X}" y="{MAP_Y}" width="{MAP_W}" height="{MAP_H}" rx="16" fill="#e5eee5" stroke="#c4d5ca"/>',
    f'<clipPath id="mapclip"><rect x="{MAP_X}" y="{MAP_Y}" width="{MAP_W}" height="{MAP_H}" rx="16"/></clipPath>',
    '<g clip-path="url(#mapclip)">',
]
for path, major in roads:
    svg.append(
        f'<path d="{path}" fill="none" stroke="{"#cfb987" if major else "#fffdf7"}" '
        f'stroke-width="{8 if major else 5}" stroke-linecap="round" stroke-linejoin="round"/>'
    )
for label, x, y in (
    ("Beulah Street", 215, 285),
    ("Colette Drive", 352, 345),
    ("Kingstowne Village Parkway", 675, 625),
):
    svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" class="roadlabel">{escape(label)}</text>')
hx, hy = point(HOME_LON, HOME_LAT)
gx, gy = point(GLADYS_LON, GLADYS_LAT)
fx, fy = point(FLORENCE_LON, FLORENCE_LAT)
svg += [
    f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="13" fill="#b04834" stroke="white" stroke-width="4"/>',
    f'<path d="M {hx + 12:.1f},{hy - 12:.1f} L {hx + 74:.1f},{hy - 58:.1f}" stroke="#b04834" stroke-width="2"/>',
    f'<rect x="{hx + 70:.1f}" y="{hy - 90:.1f}" width="191" height="52" rx="9" fill="white" stroke="#b04834"/>',
    f'<text x="{hx + 82:.1f}" y="{hy - 68:.1f}" class="body" font-weight="700">John &amp; Alice</text>',
    f'<text x="{hx + 82:.1f}" y="{hy - 50:.1f}" class="small">6307 Colette Drive</text>',
    f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="12" fill="#356e8a" stroke="white" stroke-width="4"/>',
    f'<path d="M {gx - 12:.1f},{gy + 10:.1f} L {gx - 63:.1f},{gy + 40:.1f}" stroke="#356e8a" stroke-width="2"/>',
    f'<rect x="{gx - 241:.1f}" y="{gy + 32:.1f}" width="181" height="52" rx="9" fill="white" stroke="#356e8a"/>',
    f'<text x="{gx - 229:.1f}" y="{gy + 54:.1f}" class="body" font-weight="700">Gladys Smith</text>',
    f'<text x="{gx - 229:.1f}" y="{gy + 72:.1f}" class="small">6330 Miller Drive</text>',
    f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="12" fill="#6e5690" stroke="white" stroke-width="4"/>',
    f'<path d="M {fx + 10:.1f},{fy + 10:.1f} L {fx + 52:.1f},{fy + 38:.1f}" stroke="#6e5690" stroke-width="2"/>',
    f'<rect x="{fx + 49:.1f}" y="{fy + 30:.1f}" width="198" height="52" rx="9" fill="white" stroke="#6e5690"/>',
    f'<text x="{fx + 61:.1f}" y="{fy + 52:.1f}" class="body" font-weight="700">Florence Weatherford</text>',
    f'<text x="{fx + 61:.1f}" y="{fy + 70:.1f}" class="small">6312 Miller Drive</text>',
    '</g>',
    '<rect x="954" y="98" width="202" height="610" rx="16" fill="white" stroke="#d2dfd5"/>',
    '<text x="976" y="132" class="label">Three parcels</text>',
    '<text x="976" y="165" class="body">John &amp; Alice</text>',
    '<text x="976" y="185" class="small">6307 Colette Drive</text>',
    '<text x="976" y="213" class="body">Gladys Smith</text>',
    '<text x="976" y="233" class="small">6330 Miller Drive</text>',
    '<text x="976" y="261" class="body">Florence</text>',
    '<text x="976" y="281" class="body">Weatherford</text>',
    '<text x="976" y="301" class="small">6312 Miller Drive</text>',
    '<line x1="976" y1="324" x2="1134" y2="324" stroke="#d2dfd5"/>',
    '<text x="976" y="355" class="label">Evidence</text>',
    '<text x="976" y="386" class="small">Family account gives</text>',
    '<text x="976" y="405" class="small">relationships and</text>',
    '<text x="976" y="424" class="small">residences. County</text>',
    '<text x="976" y="443" class="small">records confirm</text>',
    '<text x="976" y="462" class="small">names and parcels.</text>',
    '<line x1="976" y1="483" x2="1134" y2="483" stroke="#d2dfd5"/>',
    '<text x="976" y="516" class="label">Map note</text>',
    '<text x="976" y="548" class="small">Roads are current.</text>',
    '<text x="976" y="567" class="small">Pins are approximate</text>',
    '<text x="976" y="586" class="small">address locations.</text>',
    '<text x="44" y="738" class="small">Roads: Fairfax County GIS OpenData_A1. Address point: U.S. Census Geocoder. Generated 26 Sep 2026. North is up.</text>',
    '</svg>',
]
OUTPUT.write_text("\n".join(svg), encoding="utf-8")
print(f"Wrote {OUTPUT} from {len(features)} road features")
