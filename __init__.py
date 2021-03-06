# -*- coding: utf-8 -*-

mVersion = "0.0.4"

#******************************************************************************
#
# ZStats
# ---------------------------------------------------------
# Extended zonal statistics and report generation
#
# Copyright (C) 2011 Alexander Bruy (alexander.bruy@nextgis.org)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/copyleft/gpl.html>. You can also obtain it by writing
# to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston,
# MA 02111-1307, USA.
#
#******************************************************************************

def name():
  return "ZonalStats"

def description():
  return "Extended zonal statistics and report generation"

def category():
  return "Raster"

def version():
  return mVersion

def qgisMinimumVersion():
  return "1.7.2"

def authorName():
  return "Alexander Bruy (NextGIS)"

def icon():
  return "icons/zonalstats.png"

def classFactory( iface ):
  from zonalstats import ZonalStatsPlugin
  return ZonalStatsPlugin( iface )

