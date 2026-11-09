# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInBattleVehicleSwitch.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInBattleVehicleSwitch.py
from __future__ import absolute_import
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from helpers import dependency
from script_component.ScriptComponent import ScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class AvatarInBattleVehicleSwitch(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def set_vehicleSpawnList(self, _):
        if self._isAvatarReady:
            self.__updateAllVehsList()

    def set_spawnInfoForVehicle(self, _):
        if self._isAvatarReady:
            self.__updateCurrentVehicle()

    def confirmSelection(self):
        self.cell.confirmVehicleSelection()

    def chooseVehicle(self, newCD):
        self.cell.chooseVehicle(newCD)

    def switchSetup(self, vehTypeCD, groupId, layoutIdx):
        if groupId in self.spawnInfoForVehicle['vehDisabledSetupSwitches']:
            return
        self.cell.switchSetup(vehTypeCD, groupId, layoutIdx)

    def _onAvatarReady(self):
        self.__updateAllVehsList()
        if self.spawnInfoForVehicle:
            self.__updateCurrentVehicle()

    def __updateAllVehsList(self):
        self.__sessionProvider.dynamic.prebattleSetup.setAvailableVehicles(self.vehicleSpawnList)

    def __updateCurrentVehicle(self):
        self.__sessionProvider.dynamic.prebattleSetup.updateVehicleInfo(self.spawnInfoForVehicle)
