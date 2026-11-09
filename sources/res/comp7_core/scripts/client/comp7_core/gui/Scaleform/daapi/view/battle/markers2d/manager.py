# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/markers2d/manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/markers2d/manager.py
from __future__ import absolute_import
from comp7_core.gui.Scaleform.daapi.view.battle.markers2d import plugins
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import MarkersManager
from gui.Scaleform.daapi.view.battle.shared.points_of_interest import markers2d as poi_plugins

class Comp7MarkersManager(MarkersManager):

    def _setupPlugins(self, arenaVisitor):
        setup = super(Comp7MarkersManager, self)._setupPlugins(arenaVisitor)
        setup['vehicles'] = plugins.Comp7VehicleMarkerPlugin
        setup['settings'] = plugins.Comp7SettingsPlugin
        setup['pointsOfInterest'] = poi_plugins.PointsOfInterestPlugin
        return setup
