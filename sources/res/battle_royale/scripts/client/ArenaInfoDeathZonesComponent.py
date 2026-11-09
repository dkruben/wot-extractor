# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/ArenaInfoDeathZonesComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/ArenaInfoDeathZonesComponent.py
from __future__ import absolute_import
from builtins import range
import CGF, Math
from death_zones_helpers import ZONE_STATE, DEATH_ZONE_IDS
from script_component.DynamicScriptComponent import DynamicScriptComponent

class ArenaInfoDeathZonesComponent(DynamicScriptComponent):

    def __init__(self):
        super(ArenaInfoDeathZonesComponent, self).__init__()
        prefab = 'content/CGFPrefabs/steel_hunter/death_zones_rules.prefab'
        CGF.loadAndCreatePrefab(prefab, self.entity.spaceID, Math.Vector3(0, 0, 0))
        self.visibilityMskZones = [0 for _ in enumerate(DEATH_ZONE_IDS)]
        self.updatedZones = []

    def _onAvatarReady(self):
        self.updatedZones = [idx for idx, value in enumerate(self.activeZones) if value != ZONE_STATE.SAVE]

    def setNested_activeZones(self, changePath, _):
        self.updatedZones.extend(range(changePath[0], changePath[0] + 1))

    def setSlice_activeZones(self, path, _):
        startIdx, stopIdx = path[-1]
        self.updatedZones.extend(range(startIdx, stopIdx))
