# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015.
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 


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
