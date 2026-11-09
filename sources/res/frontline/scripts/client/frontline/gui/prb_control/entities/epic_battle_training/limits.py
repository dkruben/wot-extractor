# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic_battle_training/limits.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/prb_control/entities/epic_battle_training/limits.py
from __future__ import absolute_import
from future.utils import viewvalues
from CurrentVehicle import g_currentVehicle
from constants import PREBATTLE_ACCOUNT_STATE, PREBATTLE_TYPE
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import isVehLevelUnlockableInBattle
from gui.prb_control.entities.base.limits import AbstractTeamIsValid, LimitsCollection, VehicleIsValid, TeamNoPlayersInBattle, TeamIsValid
from gui.prb_control.settings import PREBATTLE_RESTRICTION
from skeletons.gui.shared import IItemsCache
from helpers import dependency
from items import vehicles

class ObserverInTeamIsValid(AbstractTeamIsValid):
    itemsCache = dependency.descriptor(IItemsCache)

    def check(self, rosters, team, teamLimits):
        accountsInfo = self._getAccountsInfo(rosters, team)
        if len(accountsInfo) < teamLimits['minCount']:
            return (False, 'limit/minCount')
        if self.__isAllObservers(accountsInfo):
            return (False, 'observers')
        return (
         True, '')

    @classmethod
    def __isAllObservers(cls, accountsInfo):
        if not accountsInfo:
            return False
        for accInfo in viewvalues(accountsInfo):
            if not accInfo['state'] & PREBATTLE_ACCOUNT_STATE.READY:
                continue
            if 'vehTypeCompDescr' not in accInfo or 'vehLevel' not in accInfo:
                vehDescr = vehicles.VehicleDescr(compactDescr=accInfo['vehCompDescr'])
                vehTypeCompDescr = vehDescr.type.compactDescr
            else:
                vehTypeCompDescr = accInfo['vehTypeCompDescr']
            if not cls.itemsCache.items.getItemByCD(vehTypeCompDescr).isObserver:
                return False

        return True


class EpicVehicleIsValid(VehicleIsValid):

    def check(self, teamLimits):
        isValid, restriction = super(EpicVehicleIsValid, self).check(teamLimits)
        if restriction == PREBATTLE_RESTRICTION.VEHICLE_EPIC_ONLY:
            return (True, '')
        vehicle = g_currentVehicle.item
        if vehicle and isVehLevelUnlockableInBattle(vehicle.level):
            return (False, PREBATTLE_RESTRICTION.VEHICLE_WILL_BE_UNLOCKED)
        return (isValid, restriction)


class EpicBattleTrainingLimits(LimitsCollection):

    def __init__(self, entity):
        super(EpicBattleTrainingLimits, self).__init__(entity, (
         EpicVehicleIsValid(),), (
         TeamNoPlayersInBattle(PREBATTLE_TYPE.EPIC_TRAINING),
         TeamIsValid(),
         ObserverInTeamIsValid()))
