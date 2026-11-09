# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/PveMinimapController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/PveMinimapController.py
from __future__ import absolute_import
from constants import PVE_MINIMAP_DEFAULT_ZOOM, PVE_MINIMAP_DEFAULT_BORDERS
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from script_component.DynamicScriptComponent import DynamicScriptComponent

class PveMinimapController(DynamicScriptComponent):

    def set_minimapData(self, prev):
        if self.minimapData.zoomLevel != prev.zoomLevel:
            self._sendZoomUpdated()
        elif self.minimapData.minimapBorders != prev.minimapBorders:
            self._sendMinimapBorders()

    def _onAvatarReady(self):
        if self.minimapData.zoomLevel != PVE_MINIMAP_DEFAULT_ZOOM:
            self._sendZoomUpdated()
        elif self.minimapData.minimapBorders != PVE_MINIMAP_DEFAULT_BORDERS:
            self._sendMinimapBorders()

    def _sendZoomUpdated(self):
        g_eventBus.handleEvent(events.ScalableBattleMinimapEvent(events.ScalableBattleMinimapEvent.ZOOM_UPDATED, {'zoomLevel': (self.minimapData.zoomLevel)}), EVENT_BUS_SCOPE.BATTLE)

    def _sendMinimapBorders(self):
        g_eventBus.handleEvent(events.ScalableBattleMinimapEvent(events.ScalableBattleMinimapEvent.BORDERS_UPDATED, {'minimapBorders': (self.minimapData.minimapBorders)}), EVENT_BUS_SCOPE.BATTLE)
