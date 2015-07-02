Description
-----------

.. image:: https://travis-ci.org/GeographicaGS/daynight2geojson.svg?branch=master
    :target: https://travis-ci.org/GeographicaGS/daynight2geojson

Get day and night global geometry and dumps to a GeoJSON file.

Builded on top of Matplotlib Basemap Toolkit Library. Geojson and
Shapely libraries are used to deal with geometries.

Output Coordinate Reference System (CRS): EPSG 4326


Requirements
------------

-  Geojson Python library (>= 1.0.9).
   https://github.com/frewsxcv/python-geojson
-  Shapely Python library (>= 1.4). https://github.com/Toblerity/Shapely
-  Matplotlib Basemap Toolkit Python library (>= 1.0.7).
   https://github.com/matplotlib/basemap

See requirements of above libraries (Numpy, Matplotlib, GEOS, etc.).

Installing
----------

If you want to install from pip and you do not have installed Basemap:

pip install daynight2geojson --allow-external basemap --allow-unverified basemap

Usage
-----

Basic usage:

.. code:: python

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

Test script: - test/daynighttesting.py


Examples:
---------

https://github.com/GeographicaGS/daynight2geojson

About author
------------

Developed by Cayetano Benavent (2015).

GIS Analyst at Geographica.

http://www.geographica.gs/

License
-------

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

.. |Build Status| image:: https://travis-ci.org/GeographicaGS/daynight2geojson.svg?branch=master
   :target: https://travis-ci.org/GeographicaGS/daynight2geojson
