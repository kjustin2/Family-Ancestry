# Place map

[Open the generated SVG map](ancestral-places.svg) or [PNG preview](ancestral-places-preview.png). It locates regions and town centers, not homes. The Palatinate inset uses approximate coordinates so nearby mill villages remain legible. The German locations are independently recorded mill places; the proposed link from their families to Magdalena Disque in Wilkes-Barre is still under investigation.

The map was made with [generate_map.py](generate_map.py) from [Natural Earth 1:110m country outlines](https://www.naturalearthdata.com/about/terms-of-use/) (public domain) and approximate town-center coordinates. Run `python maps/generate_map.py` to regenerate the SVG; this requires a network connection for the outline GeoJSON. The optional Python `cairosvg` package also regenerates the PNG preview. No map tile or geocoding service is needed to view either map.

For street-level historic maps, use [Alexandria's historic-map collection](https://alexandriava.gov/historic-alexandria/basic-page/historic-alexandria-maps) and [Luzerne County's map and directory resources](https://luzerne.pagenweb.org/). Current streets and buildings must not be assumed identical to those in an ancestor's time.
