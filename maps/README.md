# Place map

## Story diagrams

- [Kramer lineage](kramer-lineage.svg) gives each of the three Ferdinand generations a stable label; the 1900 and 1930 census links are solid, while the 1913-to-Fred identity match is dashed.
- [Kramer work](kramer-work.svg) places documented occupations, Emil's named employer and Army enlistment in order without presenting one household's wages as a long-term wealth trend.
- [Bosch connection](bosch-1920-connection.svg) explains why both 1920 census sheets must be read together to identify Rose's parents.
- [Colette assessments](colette-assessments.svg) charts selected **nominal county property estimates** over time; it does not estimate anyone's net worth.
- [Weatherford–Smith generations](weatherford-smith-generations.svg) shows where the two known lines meet and the size of each named sibling group; the [generation guide](../branches/weatherford-smith-generations.md) lists every name and date status.
- [Smith–Blevins evidence map](smith-blevins-lineage.svg) separates Gladys's documented parent link from James's candidate parents and the older Tancy tree lead; the [Smith page](../branches/smith.md) explains each source.
- [Deeper Blevins evidence ladder](blevins-deep-lineage.svg) ([PNG preview](blevins-deep-lineage-preview.png)) follows the linked member tree into the 1700s while marking the record-backed, ambiguous and tree-only links; the [Blevins guide](../branches/blevins-deep-lineage.md) explains the Civil War and immigration evidence.
- [Deeper Weatherford line](weatherford-deep-lineage.svg) ([PNG preview](weatherford-deep-lineage-preview.png)) connects Ashley to George and Ella Weatherford and John Neathery and Annie Phelps, using original certificates and censuses; the [Weatherford page](../branches/weatherford.md) explains the evidence and older name conflict.
- [Miller–Raber family](miller-raber-family.svg) ([PNG preview](miller-raber-family-preview.png)) shows Melissa's two Berwick branches, which links come from family accounts, and where the Fairchild name remains unresolved.

Run `python maps/generate_story_charts.py` to regenerate these standalone SVGs. The labels and underlying records are explained in the adjacent family pages.

## Geographic map

[Sutera in Italy and Sicily](cordaro-sutera-places.svg) ([PNG preview](cordaro-sutera-places-preview.png)) marks the town named on the family-held passport. Palermo and Caltanissetta city orient the reader; neither is a documented family stop. The portrait location and any Atlantic route remain unknown. Regenerate it with `python maps/generate_sutera_map.py` (Natural Earth 1:50m outline; approximate OpenStreetMap place centers), then see the [Cordaro evidence](../branches/cordaro-passport-lead.md).

[Open the generated SVG map](ancestral-places.svg) or [PNG preview](ancestral-places-preview.png). It locates regions and town centers, not homes. **Berwick and Wilkes-Barre share a northeast Pennsylvania marker at the nationwide scale**, while the Palatinate inset uses approximate coordinates so nearby mill villages remain legible. The German locations are independently recorded mill places; the proposed link from their families to Magdalena Disque in Wilkes-Barre is still under investigation.

The map was made with [generate_map.py](generate_map.py) from [Natural Earth 1:110m country outlines](https://www.naturalearthdata.com/about/terms-of-use/) (public domain) and approximate town-center coordinates. Run `python maps/generate_map.py` to regenerate the SVG; this requires a network connection for the outline GeoJSON. The optional Python `cairosvg` package also regenerates the PNG preview. No map tile or geocoding service is needed to view either map.

For street-level historic maps, use [Alexandria's historic-map collection](https://alexandriava.gov/historic-alexandria/basic-page/historic-alexandria-maps) and [Luzerne County's map and directory resources](https://luzerne.pagenweb.org/). Current streets and buildings must not be assumed identical to those in an ancestor's time.
