# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/stronghold/manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/stronghold/manager.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager
from gui.Scaleform.daapi.view.battle.stronghold.plugins import StrongholdVehicleMarkerPlugin

class StrongholdMarkersManager(MarkersManager):

    def _setupPlugins(self, arenaVisitor):
        setup = super(StrongholdMarkersManager, self)._setupPlugins(arenaVisitor)
        setup['vehicles'] = StrongholdVehicleMarkerPlugin
        return setup
