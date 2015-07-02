##Description

[![Build Status](https://travis-ci.org/GeographicaGS/daynight2geojson.svg?branch=master)](https://travis-ci.org/GeographicaGS/daynight2geojson)

Get day and night global geometry and dumps to a GeoJSON file.

Builded on top of Matplotlib Basemap Toolkit Library.
Geojson and Shapely libraries are used to deal with geometries.

Output Coordinate Reference System (CRS): EPSG 4326

More about it:

[Link to Geographica Blog] (http://www.blog-geographica.com/2015/03/15/mapping-the-worldwide-night-and-dump-it-to-geojson-2/)


##Requirements

- Geojson Python library (>= 1.0.9). https://github.com/frewsxcv/python-geojson
- Shapely Python library (>= 1.4). https://github.com/Toblerity/Shapely
- Matplotlib Basemap Toolkit Python library (>= 1.0.7). https://github.com/matplotlib/basemap

See requirements of above libraries (Numpy, Matplotlib, GEOS, etc.).

## Installing
You can install this package from PYPI:
https://pypi.python.org/pypi/daynight2geojson

```bash
$ pip install daynight2geojson
```

If you want to install from pip and you do not have installed Basemap:

```bash
$ pip install daynight2geojson --allow-external basemap --allow-unverified basemap
```

##Usage

Basic usage:

```python
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
- test/daynighttesting.py


##Examples:

[Open GeoJSON day_night 2015/01/15 12:00](https://github.com/GeographicaGS/daynight2geojson/blob/master/data/geojson/day_night_20150115_1200.geojson)
![day_night_20150115_1200](https://github.com/GeographicaGS/daynight2geojson/blob/master/data/img/day_night_20150115_1200.png)
![day_night_20150115_1200_globe](https://github.com/GeographicaGS/daynight2geojson/blob/master/data/img/day_night_20150115_1200_globe.png)

[Open GeoJSON day_night 2015/01/15 18:00](https://github.com/GeographicaGS/daynight2geojson/blob/master/data/geojson/day_night_20150115_1800.geojson)
![day_night_20150115_1800](https://github.com/GeographicaGS/daynight2geojson/blob/master/data/img/day_night_20150115_1800.png)
![day_night_20150115_1800_globe](https://github.com/GeographicaGS/daynight2geojson/blob/master/data/img/day_night_20150115_1800_globe.png)

[Open GeoJSON day_night UTC now](https://github.com/GeographicaGS/daynight2geojson/blob/master/data/geojson/day_night_2015_utc_now.geojson)
![day_night_2015_utc_now](https://github.com/GeographicaGS/daynight2geojson/blob/master/img/data/day_night_2015_utc_now.png)


##About author
Developed by Cayetano Benavent (2015).

GIS Analyst at Geographica.

http://www.geographica.gs/

##License
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
