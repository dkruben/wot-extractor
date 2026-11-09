# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/ArenaInfoComp7Component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/ArenaInfoComp7Component.py
from __future__ import absolute_import
from future.utils import viewitems
from ArenaInfoComp7BaseComponent import ArenaInfoComp7BaseComponent
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID
from comp7.gui.battle_control.arena_info.arena_vos import Comp7Keys
from gui.battle_control import avatar_getter
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.battle_control.arena_info.settings import ARENA_LISTENER_SCOPE as _SCOPE
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class ArenaInfoComp7Component(ArenaInfoComp7BaseComponent, IArenaVehiclesController):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(ArenaInfoComp7Component, self).__init__()
        self.__invalidateRanks()
        self.__sessionProvider.addArenaCtrl(self)

    def getCtrlScope(self):
        return _SCOPE.VEHICLES

    def invalidateVehiclesInfo(self, arenaDP):
        self.__invalidateRanks()

    def onLeaveWorld(self):
        self.__sessionProvider.removeArenaCtrl(self)
        arena = avatar_getter.getArena()
        if arena is not None:
            arena.onNewVehicleListReceived -= self.__onNewVehicleListReceived
            arena.onVehicleAdded -= self.__onVehicleAdded
        super(ArenaInfoComp7Component, self).onLeaveWorld()
        return

    def set_ranks(self, prev):
        self.__invalidateRanks()

    def set_bannedVehicles(self, _):
        if self._isAvatarReady:
            self.__updateBannedVehicles()

    def set_vehicleBanList(self, _):
        if self._isAvatarReady:
            self.__updateVehicleBanList()

    def _onAvatarReady(self):
        self.__sessionProvider.removeArenaCtrl(self)
        arena = avatar_getter.getArena()
        if arena is not None:
            arena.onNewVehicleListReceived += self.__onNewVehicleListReceived
            arena.onVehicleAdded += self.__onVehicleAdded
        self.__invalidateRanks()
        self.__updateBannedVehicles()
        self.__updateVehicleBanList()
        return

    def __invalidateRanks(self):
        vInfos = self.__sessionProvider.getArenaDP().getVehiclesInfoIterator()
        ranks = {vInfo.vehicleID: self.ranks[vInfo.vehicleID] for vInfo in vInfos if vInfo.vehicleID in self.ranks}
        self.__updateGameModeStats(ranks)

    def __invalidateRank(self, vehicleID):
        if vehicleID in self.ranks:
            ranks = {vehicleID: (self.ranks[vehicleID])}
            self.__updateGameModeStats(ranks)

    def __onNewVehicleListReceived(self):
        self.__invalidateRanks()

    def __onVehicleAdded(self, vehicleID):
        if self._isAvatarReady:
            self.__invalidateRank(vehicleID)

    @staticmethod
    def __updateGameModeStats(ranks):
        arena = avatar_getter.getArena()
        if not arena:
            return
        stats = {}
        for vehID, rank in viewitems(ranks):
            stats[vehID] = {(Comp7Keys.RANK): (rank['divisionRank']), 
               (Comp7Keys.IS_QUAL_ACTIVE): (rank['isQualActive'])}

        if stats:
            arena.updateGameModeSpecificStats(isStatic=True, stats=stats)

    def __updateBannedVehicles(self):
        vehicleBanCtrl = self.__sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.COMP7_VEHICLE_BAN_CTRL)
        if vehicleBanCtrl is not None and self.bannedVehicles:
            vehicleBanCtrl.bannedVehicles = self.bannedVehicles
        return

    def __updateVehicleBanList(self):
        vehicleBanCtrl = self.__sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.COMP7_VEHICLE_BAN_CTRL)
        if vehicleBanCtrl is not None:
            vehicleBanCtrl.vehiclesListForBan = self.vehicleBanList
        return
