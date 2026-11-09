# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/battle_royale_appearance_cache_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/battle_royale_appearance_cache_ctrl.py
from __future__ import absolute_import
import BigWorld
from gui.battle_control.controllers.appearance_cache_ctrls import getWholeVehModels
from gui.battle_control.controllers.appearance_cache_ctrls.default_appearance_cache_ctrl import DefaultAppearanceCacheController
from items.vehicles import VehicleDescriptor

class BattleRoyaleAppearanceCacheController(DefaultAppearanceCacheController):
    FORCED_CACHED_VEHICLES = ('germany:G24_VK3002DB_SH', 'france:F43_AMC_35_SH', 'china:Ch24_Type64_SH')
    EQUIPMENT_VEHICLES = ('germany:G00_Bomber_SH', 'china:Ch00_ClingeBot_SH')

    def arenaLoadCompleted(self):
        super(BattleRoyaleAppearanceCacheController, self).arenaLoadCompleted()
        self._precacheExtraResources()

    def _precacheExtraResources(self):
        isMinSettings = not BigWorld.canToDowngradePreset()
        cachedDescs = set()
        if isMinSettings:
            playerVehicleDescr = BigWorld.player().vehicleTypeDescriptor
            cachedDescs.add(playerVehicleDescr.name)
            self._appearanceCache.loadResources(playerVehicleDescr.makeCompactDescr(), getWholeVehModels(playerVehicleDescr))
            for vehicleTypeName in BattleRoyaleAppearanceCacheController.EQUIPMENT_VEHICLES:
                descr = VehicleDescriptor(typeName=vehicleTypeName)
                self._appearanceCache.loadResources(descr.makeCompactDescr(), getWholeVehModels(descr))

        for veh in self._arena.vehicles.values():
            vDesc = veh['vehicleType']
            isNotForced = vDesc.name not in BattleRoyaleAppearanceCacheController.FORCED_CACHED_VEHICLES
            if vDesc.name in cachedDescs or isNotForced and isMinSettings:
                continue
            cachedDescs.add(vDesc.name)
            self._appearanceCache.loadResources(vDesc.makeCompactDescr(), getWholeVehModels(vDesc))
