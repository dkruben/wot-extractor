# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/map_zones/mixins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/map_zones/mixins.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class MapZonesListener(object):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def startListen(self):
        mapZones = self._sessionProvider.shared.mapZones
        if mapZones:
            mapZones.onMarkerToZoneAdded += self._onMarkerToZoneAdded
            mapZones.onMarkerFromZoneRemoved += self._onMarkerFromZoneRemoved
            mapZones.onMarkerProgressUpdated += self._onMarkerProgressUpdated
            mapZones.onZoneTransformed += self._onZoneTransformed
            mapZones.onTransformedZoneRemoved += self._onTransformedZoneRemoved

    def stopListen(self):
        mapZones = self._sessionProvider.shared.mapZones
        if mapZones:
            mapZones.onMarkerToZoneAdded -= self._onMarkerToZoneAdded
            mapZones.onMarkerFromZoneRemoved -= self._onMarkerFromZoneRemoved
            mapZones.onMarkerProgressUpdated -= self._onMarkerProgressUpdated
            mapZones.onZoneTransformed -= self._onZoneTransformed
            mapZones.onTransformedZoneRemoved -= self._onTransformedZoneRemoved

    def _onMarkerToZoneAdded(self, zoneMarker, matrix):
        pass

    def _onMarkerFromZoneRemoved(self, zoneMarker):
        pass

    def _onMarkerProgressUpdated(self, zoneMarker):
        pass

    def _onZoneTransformed(self, zone):
        pass

    def _onTransformedZoneRemoved(self, zone):
        pass
