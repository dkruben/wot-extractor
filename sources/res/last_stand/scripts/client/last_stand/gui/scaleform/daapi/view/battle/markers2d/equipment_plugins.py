# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/markers2d/equipment_plugins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/markers2d/equipment_plugins.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.markers2d.plugins import EquipmentsMarkerPlugin
from gui.Scaleform.daapi.view.battle.shared.markers2d import settings

class LSEquipmentsMarkerPlugin(EquipmentsMarkerPlugin):
    LS_EQUIPMENT_MARKER_LINKAGE = 'LSFortConsumablesMarkerUI'
    LS_MARKERS = ('LSEventDeathZoneUI', )

    def _getMarkerLinkage(self, item):
        if item.getMarker() in self.LS_MARKERS:
            return self.LS_EQUIPMENT_MARKER_LINKAGE
        return settings.MARKER_SYMBOL_NAME.EQUIPMENT_MARKER
