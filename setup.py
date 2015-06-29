# -*- coding: utf-8 -*-

# This file is part of daynight2geojson.
# https://github.com/GeographicaGS/daynight2geojson

# Licensed under the GPLv2 license:
# https://www.gnu.org/licenses/gpl-2.0.txt
# Copyright (c) 2015, Cayetano Benavent <cayetanobv@gmail.com>

from setuptools import setup, find_packages


# Get the long description from README file.
# Before upload a new version run rstgenerator.sh
# to update Readme reStructuredText file from 
# original Readme markdown file.
with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='daynight2geojson',
    version='0.1',
    
    description='Get day and night global geometry and dumps to a GeoJSON file. Builded on top of Matplotlib Basemap Toolkit Library.',
    long_description=long_description,
    
    author='Cayetano Benavent',
    author_email='cayetano.benavent@geographica.gs',
    
    # The project's main homepage.
    url='https://github.com/GeographicaGS/daynight2geojson',
    
    # Licensed under the GPLv2 license:
    # https://www.gnu.org/licenses/gpl-2.0.txt
    license='GPLv2',
    
    # According to: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    
    keywords='night GIS matplotlib basemap geojson',
    
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'matplotlib',
        'basemap>=1.0.7,<2.0',
        'geojson>=1.0.9,<2.0',
        'shapely>=1.5.0,<2.0'
    ]

)
