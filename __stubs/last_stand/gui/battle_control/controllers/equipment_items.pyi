# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/equipment_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import time as time
from math import ceil as ceil
from math_common import decimal_round as decimal_round
from future.utils import viewitems as viewitems
from DynComponentsGroup import DynComponentsGroup as DynComponentsGroup
from helpers import dependency as dependency
from last_stand_common.last_stand_constants import BOOSTER_FACTOR_NAMES as BOOSTER_FACTOR_NAMES
from last_stand_common.ls_utils.boosters import getVehicleBoosterFactorsComponent as getVehicleBoosterFactorsComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control import avatar_getter as avatar_getter, vehicle_getter as vehicle_getter
from gui.battle_control.controllers.consumables.equipment_ctrl import _ActivationError as _ActivationError, DynComponentsGroupItem as DynComponentsGroupItem, DynComponentsGroupReplayItem as DynComponentsGroupReplayItem
from gui.battle_control.battle_constants import DEVICE_STATE_DESTROYED as DEVICE_STATE_DESTROYED
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, EQUIPMENT_STAGES as EQUIPMENT_STAGES
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys

class LSSituationalEquipmentItem(DynComponentsGroupItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class LSEquipmentItemBase(DynComponentsGroupItem):
    def inCriticalCondition(self, avatar=None):
        ...

class LSEquipmentItem(LSEquipmentItemBase):
    def canActivate(self, entityName=None, avatar=None):
        ...
    def _getUsageCost(self, vehicle):
        ...
    def _getDurationSeconds(self):
        ...

class LSEquipmentReplayItem(LSEquipmentItemBase, DynComponentsGroupReplayItem):
    _stage: Any
    def __init__(self, descriptor, quantity, stage, timeRemaining, totalTime, tags=None):
        ...
    def update(self, quantity, stage, timeRemaining, totalTime):
        ...
    def getCooldownPercents(self):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...
    def _getUsageCost(self, vehicle):
        ...
    def _getDurationSeconds(self):
        ...

class _HpRepairAndCrewHeal(LSEquipmentItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _AbilityWithDuration(LSEquipmentItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class LSDamageShield(_AbilityWithDuration):
    _BLOCKED_COMPONENT: tuple
    def canActivate(self, entityName=None, avatar=None):
        ...

class _NitroEquipmentItemBase(LSEquipmentItemBase, DynComponentsGroupItem):
    def inCriticalCondition(self, avatar=None):
        ...

class _NitroEquipmentItem(_NitroEquipmentItemBase, _AbilityWithDuration):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _NitroEquipmentReplayItem(_NitroEquipmentItemBase, LSEquipmentReplayItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _FastReload(_AbilityWithDuration):
    INSTANT_RELOAD = 'LS_instantReload'
    DEVICES: tuple
    ERROR_NAME = 'LS_gunDestroyed'
    guiSessionProvider: Any
    def getEntitiesIterator(self, avatar=None):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...
    def _canActivateFast(self, entityName=None, avatar=None):
        ...
    def _canActivateInstant(self, entityName=None, avatar=None):
        ...

class _LSInstantShot(LSEquipmentItem):
    _COOLDOWN: Any
    _lastTimeActive: Any
    def __init__(self, *args, **kwargs):
        ...
    def activate(self, entityName=None, avatar=None):
        ...
    def isInCooldown(self, now):
        ...
