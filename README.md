##Description

Get day and night global geometry and dumps to a GeoJSON file.

Builded on top of Matplotlib Basemap Toolkit Library. 
Geojson and Shapely libraries are used to deal with geometries.

Output projection: Equirectangular (Cylindrical Equidistant)

Output ellipsoid: WGS84


##Requirements

- Geojson Python library. https://github.com/frewsxcv/python-geojson
- Shapely Python library. https://github.com/Toblerity/Shapely
- Matplotlib Basemap Toolkit Python library. https://github.com/matplotlib/basemap

See requirements of above libraries (Numpy, Matplotlib, GEOS, etc.).


##Usage

Basic usage:

```
from datetime import datetime
from daynight2geojson import DayNight2Geojson

# Filepath to output GeoJSON
filepath = '/tmp/day_night.geojson'

# input_date = None is for UTC now date
# For others input date: datetime object must be passed
#       datetime(year, month, day, hour, minute)
input_date = datetime(2015, 1, 15, 00, 00)

dn = DayNight2Geojson(filepath, input_date=input_date)
dn.getDayNight()
```

Test script:
- lib/bootstrap.py


##Examples:

[Open GeoJSON day_night 2015/01/15 12:00](https://github.com/cayetanobv/daynight2geojson/blob/master/geojson/day_night_20150115_1200.geojson)
![day_night_20150115_1200](https://github.com/cayetanobv/daynight2geojson/blob/master/img/day_night_20150115_1200.png)
![day_night_20150115_1200_globe](https://github.com/cayetanobv/daynight2geojson/blob/master/img/day_night_20150115_1200_globe.png)

[Open GeoJSON day_night 2015/01/15 18:00](https://github.com/cayetanobv/daynight2geojson/blob/master/geojson/day_night_20150115_1800.geojson)
![day_night_20150115_1800](https://github.com/cayetanobv/daynight2geojson/blob/master/img/day_night_20150115_1800.png)
![day_night_20150115_1800_globe](https://github.com/cayetanobv/daynight2geojson/blob/master/img/day_night_20150115_1800_globe.png)

[Open GeoJSON day_night UTC now](https://github.com/cayetanobv/daynight2geojson/blob/master/geojson/day_night_2015_utc_now.geojson)
![day_night_2015_utc_now](https://github.com/cayetanobv/daynight2geojson/blob/master/img/day_night_2015_utc_now.png)


##About author
Developed by Cayetano Benavent (2015).
GIS Analyst at Geographica.

http://www.geographica.gs/

##License
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

