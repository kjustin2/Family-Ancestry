# Place map

## Story diagrams

- [Kramer lineage](kramer-lineage.svg) gives each of the three Ferdinand generations a stable label and marks unproved parent links with dashed lines.
- [Kramer work](kramer-work.svg) places documented occupations in order without presenting one household's wages as a long-term wealth trend.
- [Colette assessments](colette-assessments.svg) charts selected **nominal county property estimates** over time; it does not estimate anyone's net worth.
- [Weatherford–Smith generations](weatherford-smith-generations.svg) shows where the two known lines meet and the size of each named sibling group; the [generation guide](../branches/weatherford-smith-generations.md) lists every name and date status.

Run `python maps/generate_story_charts.py` to regenerate these standalone SVGs. The labels and underlying records are explained in the adjacent family pages.

## Geographic map

[Open the generated SVG map](ancestral-places.svg) or [PNG preview](ancestral-places-preview.png). It locates regions and town centers, not homes. The Palatinate inset uses approximate coordinates so nearby mill villages remain legible. The German locations are independently recorded mill places; the proposed link from their families to Magdalena Disque in Wilkes-Barre is still under investigation.

The map was made with [generate_map.py](generate_map.py) from [Natural Earth 1:110m country outlines](https://www.naturalearthdata.com/about/terms-of-use/) (public domain) and approximate town-center coordinates. Run `python maps/generate_map.py` to regenerate the SVG; this requires a network connection for the outline GeoJSON. The optional Python `cairosvg` package also regenerates the PNG preview. No map tile or geocoding service is needed to view either map.

For street-level historic maps, use [Alexandria's historic-map collection](https://alexandriava.gov/historic-alexandria/basic-page/historic-alexandria-maps) and [Luzerne County's map and directory resources](https://luzerne.pagenweb.org/). Current streets and buildings must not be assumed identical to those in an ancestor's time.
