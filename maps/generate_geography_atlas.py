"""Render three evidence-aware geographic maps from Natural Earth and OSM centers."""

import json
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

plt.rcParams["svg.fonttype"] = "none"

HERE = Path(__file__).parent
ROOT = HERE.parent
PLACES = json.loads((HERE / "place-centers.json").read_text(encoding="utf-8"))
ADMIN0_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
ADMIN1_US_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_1_states_provinces.geojson"
ADMIN1_DE_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_1_states_provinces.geojson"
INK = "#183849"
MUTED = "#587080"
SEA = "#eaf3f4"
LAND = "#eef0e8"
LINE = "#a8bcb8"
COLORS = {
    "kramer": "#247d78",
    "disque": "#bd813d",
    "cordaro": "#ba614e",
    "smith": "#8267a4",
    "weatherford": "#536fa9",
    "miller": "#769554",
    "mixed": "#2d536e",
}


def load_geojson(url, filename):
    cache = ROOT / "tmp" / filename
    cache.parent.mkdir(exist_ok=True)
    if not cache.exists():
        request = urllib.request.Request(url, headers={"User-Agent": "FamilyAncestryResearch/1.0"})
        with urllib.request.urlopen(request, timeout=40) as response:
            cache.write_bytes(response.read())
    return json.loads(cache.read_text(encoding="utf-8"))["features"]


def rings(feature):
    geometry = feature["geometry"]
    polygons = geometry["coordinates"] if geometry["type"] == "MultiPolygon" else [geometry["coordinates"]]
    for polygon in polygons:
        yield polygon[0]


def draw_features(ax, features, fill=LAND, edge=LINE, width=0.7, alpha=1):
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    # Keep map detail near screen resolution so generated SVGs remain reviewable.
    x_step = (x1 - x0) / 1200
    y_step = (y1 - y0) / 800
    for feature in features:
        for ring in rings(feature):
            if not any(x0 - 2 < lon < x1 + 2 and y0 - 2 < lat < y1 + 2 for lon, lat in ring):
                continue
            reduced = []
            for point in ring:
                if not reduced or abs(point[0] - reduced[-1][0]) > x_step or abs(point[1] - reduced[-1][1]) > y_step:
                    reduced.append(point)
            if len(reduced) < 3:
                continue
            ax.add_patch(Polygon(reduced, closed=True, facecolor=fill, edgecolor=edge,
                                 linewidth=width, alpha=alpha, zorder=1, clip_on=True))


def canvas(title, subtitle, bounds, figsize=(13.2, 7.6)):
    fig = plt.figure(figsize=figsize, facecolor="#f7f6f1")
    ax = fig.add_axes((0.045, 0.13, 0.63, 0.72), facecolor=SEA)
    ax.set_xlim(bounds[0], bounds[2])
    ax.set_ylim(bounds[1], bounds[3])
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_edgecolor("#bfd0cc")
        spine.set_linewidth(1.3)
    fig.text(0.045, 0.94, title, fontsize=22, weight="bold", color=INK)
    fig.text(0.045, 0.895, subtitle, fontsize=10.5, color=MUTED)
    return fig, ax


def dot(ax, lat, lon, number, color, size=340):
    ax.scatter([lon], [lat], s=size, color=color, edgecolors="white", linewidths=1.8, zorder=6)
    ax.text(lon, lat, str(number), ha="center", va="center", color="white", weight="bold", fontsize=11, zorder=7)


def place_dot(ax, key, number, color, size=340):
    p = PLACES[key]
    dot(ax, p["lat"], p["lon"], number, color, size)


def card(fig, y, number, title, note, color):
    fig.text(0.72, y, f"{number}", fontsize=11, weight="bold", color="white",
             bbox={"boxstyle": "round,pad=0.35", "facecolor": color, "edgecolor": "none"})
    fig.text(0.755, y + 0.006, title, fontsize=11.2, weight="bold", color=INK)
    fig.text(0.755, y - 0.022, note, fontsize=9.1, color=MUTED)


def footer(fig, line):
    fig.text(0.045, 0.072, line, fontsize=9.3, color=MUTED)
    fig.text(0.045, 0.041, "Modern outlines: Natural Earth (public domain). Approximate place centers: © OpenStreetMap contributors (ODbL).", fontsize=8.3, color=MUTED)


def save(fig, name):
    svg = HERE / f"{name}.svg"
    fig.savefig(svg, facecolor=fig.get_facecolor())
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8")
    fig.savefig(HERE / f"{name}-preview.png", dpi=145, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(name)


def germany(states):
    fig, ax = canvas("Two German research regions", "Baden Kramer records and Palatinate mill records occupy separate places and lines.", (7.35, 47.6, 8.8, 49.55))
    subset = [f for f in states if f["properties"].get("admin") == "Germany" and f["properties"].get("name") in ("Rheinland-Pfalz", "Baden-Württemberg", "Baden-W�rttemberg", "Hessen", "Saarland")]
    draw_features(ax, subset, fill="#e4ebe4", edge="#90aba7", width=1.0)
    ax.text(8.48, 48.25, "BADEN-\nWÜRTTEMBERG", ha="center", color="#91a8a3", fontsize=12, weight="bold", zorder=2)
    ax.text(7.62, 49.08, "RHINELAND-\nPALATINATE", ha="center", color="#91a8a3", fontsize=12, weight="bold", zorder=2)
    for n, key, color in [(1, "unadingen", "kramer"), (2, "knittelsheim", "disque"), (3, "siebeldingen", "disque"), (4, "rinnthal", "disque"), (5, "trippstadt", "disque")]:
        place_dot(ax, key, n, COLORS[color], size=390 if n == 1 else 310)
    ax.text(8.42, 47.79, "Unadingen", ha="center", fontsize=10, weight="bold", color=COLORS["kramer"])
    fig.text(0.71, 0.81, "READ THE MARKERS", fontsize=10, weight="bold", color=MUTED)
    card(fig, 0.745, 1, "Unadingen", "1812–78 Kramer household records", COLORS["kramer"])
    card(fig, 0.66, 2, "Knittelsheim", "Documented Disqué mill succession", COLORS["disque"])
    card(fig, 0.575, 3, "Siebeldingen", "1684 Bernhard Disqué mill offer", COLORS["disque"])
    card(fig, 0.49, 4, "Rinnthal", "Sebastian Disqué mill account", COLORS["disque"])
    card(fig, 0.405, 5, "Trippstadt", "Fröhlich birthplace on migration card", COLORS["disque"])
    fig.text(0.71, 0.29, "Baden is a recorded birthplace for Rose\nBosch's parents; their town is unknown.", fontsize=9.6, color=INK)
    fig.text(0.71, 0.19, "No record yet connects the Unadingen\nMatthäus to Pennsylvania Matthew.", fontsize=9.6, weight="bold", color=COLORS["kramer"])
    footer(fig, "Town centers, not ancestral properties. Modern state boundaries are orientation, not a map of 1812 or 1840 borders.")
    save(fig, "germany-family-places")


def europe(countries):
    fig, ax = canvas("European places in the records", "Exact town, regional birthplace, and unknown origin are visually distinct.", (-13.5, 35, 19, 57))
    draw_features(ax, countries, fill=LAND, edge="#b8c8c2", width=0.58)
    ireland = [f for f in countries if f["properties"].get("ADMIN") == "Ireland"]
    draw_features(ax, ireland, fill="#d9cfdf", edge=COLORS["smith"], width=1.2)
    ax.text(2.1, 46.4, "FRANCE", fontsize=11, color="#9daaa5", weight="bold")
    ax.text(10.1, 51.1, "GERMANY", fontsize=11, color="#9daaa5", weight="bold")
    ax.text(10.0, 43.7, "ITALY", fontsize=11, color="#9daaa5", weight="bold")
    place_dot(ax, "trippstadt", 1, COLORS["disque"], 350)
    place_dot(ax, "unadingen", 2, COLORS["kramer"], 350)
    place_dot(ax, "sutera", 3, COLORS["cordaro"], 390)
    place_dot(ax, "sassoferrato", 4, COLORS["cordaro"], 390)
    fig.text(0.71, 0.81, "EUROPEAN LAYERS", fontsize=10, weight="bold", color=MUTED)
    card(fig, 0.77, 1, "Palatinate", "Disqué mill sites and 1864 migration lead", COLORS["disque"])
    card(fig, 0.68, 2, "Unadingen, Baden", "Bernhard–Maria Kramer household", COLORS["kramer"])
    card(fig, 0.59, 3, "Sutera / Milocca", "Cordaro–Magro records; Palermo port", COLORS["cordaro"])
    card(fig, 0.50, 4, "Sassoferrato, Marche", "Joseph Caucci's 1942 birthplace report", COLORS["cordaro"])
    fig.text(0.71, 0.385, "Ireland", fontsize=11.2, weight="bold", color=COLORS["smith"])
    fig.text(0.71, 0.36, "Mulhall/Corbett elders reported Irish birth.\nNo county or arrival voyage is known;\nAshley's Smith connection is probable.", fontsize=9.5, color=MUTED, va="top")
    fig.text(0.71, 0.22, "Bosch parents: Baden-born in U.S. census,\nwith no German town identified.", fontsize=9.5, color=INK, va="top")
    footer(fig, "Caucci and Cordaro are separate Italian origins. Their inspected passenger records do not document every individual's crossing.")
    save(fig, "europe-family-places")


def america(states):
    fig, ax = canvas("American family chapters", "Cluster markers make the regional pattern readable; branch pages preserve each town and date.", (-89, 33.8, -69.5, 43.5))
    subset = [f for f in states if f["properties"].get("admin") == "United States of America"]
    draw_features(ax, subset, fill=LAND, edge="#a7b9b1", width=0.68)
    clusters = [
        (1, -75.87, 41.27, "mixed"),
        (2, -76.50, 41.19, "miller"),
        (3, -80.00, 40.44, "cordaro"),
        (4, -74.01, 40.71, "cordaro"),
        (5, -77.10, 38.84, "smith"),
        (6, -79.27, 36.62, "weatherford"),
        (7, -82.25, 36.45, "smith"),
        (8, -87.58, 38.31, "weatherford"),
    ]
    for n, lon, lat, color in clusters:
        dot(ax, lat, lon, n, COLORS[color], 390)
    ax.text(-78.4, 42.3, "PENNSYLVANIA", fontsize=10, weight="bold", color="#a6b4ad")
    ax.text(-81.0, 37.9, "VIRGINIA", fontsize=10, weight="bold", color="#a6b4ad")
    fig.text(0.71, 0.81, "READ THE REGIONS", fontsize=10, weight="bold", color=MUTED)
    card(fig, 0.75, 1, "Wyoming Valley, PA", "Wilkes-Barre Kramer + West Wyoming Cordaro", COLORS["mixed"])
    card(fig, 0.666, 2, "Berwick / Muncy area", "Miller–Raber generations and later return", COLORS["miller"])
    card(fig, 0.582, 3, "Pittsburgh, PA", "Pietra's 1909 listed destination", COLORS["cordaro"])
    card(fig, 0.498, 4, "New York port", "Pietra's documented 1909 arrival", COLORS["cordaro"])
    card(fig, 0.414, 5, "DC / Fairfax, VA", "Smith–Mulhall and Weatherford chapters", COLORS["smith"])
    card(fig, 0.33, 6, "Danville / Halifax", "Weatherford; nearby Milton Phelps", COLORS["weatherford"])
    card(fig, 0.246, 7, "Bristol / Johnson City", "Blevins–Hines 1930s records", COLORS["smith"])
    card(fig, 0.162, 8, "Gibson County, IN", "Morrison–Bennett candidate branch", COLORS["weatherford"])
    footer(fig, "One dot can group nearby towns. It is not an address, a property, a travel path, or proof that every branch is connected.")
    save(fig, "america-family-places")


def main():
    countries = load_geojson(ADMIN0_URL, "ne-110m-countries.geojson")
    us_states = load_geojson(ADMIN1_US_URL, "ne-admin1.geojson")
    de_states = load_geojson(ADMIN1_DE_URL, "ne-admin1-10m.geojson")
    germany(de_states)
    europe(countries)
    america(us_states)


if __name__ == "__main__":
    main()
