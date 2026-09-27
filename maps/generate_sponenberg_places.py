"""Generate an orientation map for the two Sponenberg research trails.

Modern map boundaries and place centers locate regions, not ancestral properties
or a documented travel route.
"""

from generate_geography_atlas import (
    ADMIN1_US_URL,
    COLORS,
    canvas,
    card,
    draw_features,
    dot,
    footer,
    load_geojson,
    save,
)


def main():
    states = load_geojson(ADMIN1_US_URL, "ne-admin1.geojson")
    pennsylvania = [
        feature for feature in states
        if feature["properties"].get("admin") == "United States of America"
        and feature["properties"].get("name") == "Pennsylvania"
    ]
    if not pennsylvania:
        raise RuntimeError("Natural Earth Pennsylvania outline missing")

    fig, ax = canvas(
        "Where the Sponenberg records lead in Pennsylvania",
        "Two Berwick-area trails; place markers do not prove their older family connection.",
        (-80.8, 39.5, -74.5, 42.5),
        figsize=(13.2, 7.6),
    )
    draw_features(ax, pennsylvania, fill="#e6ede6", edge="#8ba8a0", width=1.2)

    # OSM relation centers via Nominatim, checked 27 September 2026.
    # Harrisburg only orients Dauphin County; the 1915 text gives no town there.
    places = [
        (40.2663107, -76.8861122, 1, "#8e739b"),  # Harrisburg, relation 188218
        (41.2798029, -76.7130116, 4, "#5b79a4"),  # Picture Rocks, 188750
        (41.4086874, -75.6621294, 5, "#5b79a4"),  # Scranton, 187541
    ]
    for latitude, longitude, number, color in places:
        dot(ax, latitude, longitude, number, color, size=350)
    # Briarcreek and Berwick overlap at state scale; one symbol avoids a false
    # impression that the township and borough are far apart.
    ax.scatter([-76.2612], [41.0767], s=820, color=COLORS["miller"],
               edgecolors="white", linewidths=1.8, zorder=6)
    ax.text(-76.2612, 41.0767, "2/3", ha="center", va="center", color="white",
            weight="bold", fontsize=10, zorder=7)

    fig.text(0.71, 0.81, "PLACE KEY", fontsize=10, weight="bold", color="#587080")
    card(fig, 0.745, 1, "Dauphin County", "Immigrant grandfather in Philip's 1915 story", "#8e739b")
    fig.text(0.755, 0.706, "Harrisburg marker is county orientation only", fontsize=8.7, color="#587080")
    card(fig, 0.64, 2, "Briarcreek Township", "Daniel/John household; George/Philip farm", COLORS["miller"])
    card(fig, 0.545, 3, "Berwick", "Edward's store job and 1907 home", COLORS["miller"])
    card(fig, 0.45, 4, "Picture Rocks", "Philip's sons' jewelry/furniture work", "#5b79a4")
    card(fig, 0.355, 5, "Scranton", "Philip's son William's coal-company job", "#5b79a4")
    fig.text(0.71, 0.23, "No arrow is drawn: the exact German origin,\narrival date and connection to Daniel\nare still unknown.", fontsize=10.2, weight="bold", color="#8b5544")
    footer(fig, "Modern town/area markers, not homes or a voyage. Work locations come from the 1915 biographies and 1901 directory.")
    save(fig, "sponenberg-pennsylvania-places")


if __name__ == "__main__":
    main()
