# -*- coding: utf-8 -*-

"""
/***************************************************************************
 YardingDistance
                                 A QGIS plugin
 This plugin calucurates the "Yarding Distance" (average of distance from Polygon to Point).
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-05-20
        copyright            : (C) 2024 by Sanda takeru / HOKKAIDO Regional Forest Office
        email                : takeru_sanda999@maff.go.jp
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Sanda takeru / HOKKAIDO Regional Forest Office'
__date__ = '2024-05-20'
__copyright__ = '(C) 2024 by Sanda takeru / HOKKAIDO Regional Forest Office'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from pathlib import Path

from PyQt5.QtGui import QIcon
from qgis.core import QgsProcessingProvider
from .yarding_distance_algorithm import YardingDistanceAlgorithm


class YardingDistanceProvider(QgsProcessingProvider):

    def __init__(self):
        """
        Default constructor.
        """
        QgsProcessingProvider.__init__(self)

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        self.addAlgorithm(YardingDistanceAlgorithm())
        # add additional algorithms here
        # self.addAlgorithm(MyOtherAlgorithm())

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'Yarding Distance'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('Yarding Distance')

    def icon(self):
        path = (Path(__file__).parent / "icon.png").resolve()
        return QIcon(str(path))

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()
