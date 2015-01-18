##Description

Get day and night global geometry and dumps to a GeoJSON file.

Output projection: Equirectangular (Cylindrical Equidistant)

Examples:
https://github.com/cayetanobv/daynight2geojson/blob/master/geojson/day_night_20150115_1200.geojson
![day_night_20150115_1200](https://github.com/cayetanobv/daynight2geojson/blob/master/img/day_night_20150115_1200.png)

https://github.com/cayetanobv/daynight2geojson/blob/master/geojson/day_night_20150115_1800.geojson
![day_night_20150115_1800](https://github.com/cayetanobv/daynight2geojson/blob/master/img/day_night_20150115_1800.png)

https://github.com/cayetanobv/daynight2geojson/blob/master/geojson/day_night_2015_utc_now.geojson
![day_night_2015_utc_now](https://github.com/cayetanobv/daynight2geojson/blob/master/img/day_night_2015_utc_now.png)


##Requirements

- Geojson Python library. https://github.com/frewsxcv/python-geojson
- Shapely Python Library. https://github.com/Toblerity/Shapely
- Matplotlib Basemap Toolkit Python Library. https://github.com/matplotlib/basemap


##Usage

Basic usage:

```
from datetime import datetime
from daynight2geojson import DayNight2Geojson

filepath = '/tmp/day_night.geojson'
input_date = datetime(2015, 1, 15, 12, 00)

dn = DayNight2Geojson(filepath)
dn.getDayNight()
```

Test script:
- lib/bootstrap.py

