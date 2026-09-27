"""Draw same-year housing context without turning prices into family wealth."""

from pathlib import Path
from xml.sax.saxutils import escape


def label(x, y, value, *, size=16, color="#17343d", weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="{anchor}">{escape(value)}</text>')


def rect(x, y, width, height, color, radius=0):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{color}"/>'


def main():
    width, height = 1200, 770
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">1940 housing context for four family regions</title>',
        '<desc id="desc">Left: Duffy Weatherford’s 1000 dollar home estimate versus Virginia’s 2633 dollar median, and Ferdinand Kramer’s 2400 dollar estimate versus Pennsylvania’s 3205 dollar median. Right: 1940 median gross monthly rents were 45 dollars in DC, 27 in Pennsylvania, 19 in Virginia, and 15 in Tennessee. Family estimates and state medians are broad comparisons, not measures of wealth.</desc>',
        rect(0, 0, width, height, "#f7f5ee"),
        rect(0, 0, 13, height, "#a27432"),
        label(45, 58, "A 1940 housing snapshot", size=32, weight=700),
        label(45, 89, "Two original household entries beside Census Bureau state figures", size=18, color="#53686d"),
        rect(40, 118, 535, 535, "#ffffff", 16),
        rect(600, 118, 560, 535, "#ffffff", 16),
        label(64, 160, "Reported home value", size=23, weight=700),
        label(64, 188, "1940 dollars · family and state, side by side", size=15, color="#53686d"),
        label(624, 160, "Median gross monthly rent", size=23, weight=700),
        label(624, 188, "1940 dollars · statewide housing markets", size=15, color="#53686d"),
    ]

    # These are recorded family estimates and state medians, not like-for-like homes.
    home_groups = [
        ("Virginia", "Duffy Weatherford", 1000, 2633, 230),
        ("Pennsylvania", "Ferdinand Kramer", 2400, 3205, 424),
    ]
    x_bar, home_scale = 222, 300 / 3500
    for state, family, family_value, median, y in home_groups:
        parts += [
            label(64, y, state, size=18, weight=700),
            label(64, y + 39, family, size=15),
            rect(x_bar, y + 19, 300, 22, "#eef2f0", 7),
            rect(x_bar, y + 19, round(family_value * home_scale), 22, "#a27432", 7),
            label(550, y + 37, f"${family_value:,}", size=15, weight=700, anchor="end"),
            label(64, y + 83, "State median", size=15, color="#53686d"),
            rect(x_bar, y + 63, 300, 22, "#eef2f0", 7),
            rect(x_bar, y + 63, round(median * home_scale), 22, "#527788", 7),
            label(550, y + 81, f"${median:,}", size=15, weight=700, anchor="end"),
        ]

    rents = [("DC", 45), ("Pennsylvania", 27), ("Virginia", 19), ("Tennessee", 15)]
    rent_scale = 300 / 50
    for i, (place, value) in enumerate(rents):
        y = 241 + i * 86
        parts += [
            label(624, y, place, size=17, weight=700),
            rect(768, y - 19, 300, 25, "#eef2f0", 7),
            rect(768, y - 19, round(value * rent_scale), 25, "#527788", 7),
            label(1093, y, f"${value}", size=17, weight=700),
        ]

    parts += [
        label(64, 626, "Family values: original 1940 census entries", size=14, color="#6b7778"),
        label(624, 626, "Gross rent includes tenant-paid utilities and fuels", size=14, color="#6b7778"),
        label(45, 690, "State medians are broad context; house type, lot and neighborhood may differ.", size=17, weight=700),
        label(45, 719, "Values, rents and wages are different measures. None establishes equity, savings or inheritance.", size=15, color="#53686d"),
        label(45, 747, "Sources and definition notes: context/housing-and-work-1940.md", size=13, color="#617579"),
        "</svg>",
    ]
    Path(__file__).with_name("housing-context-1940.svg").write_text("".join(parts), encoding="utf-8")


if __name__ == "__main__":
    main()
