# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/battle_control/controllers/equipment_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import math as math
from DynComponentsGroup import DynComponentsGroup as DynComponentsGroup
from HWBuffDrainLifeComponent import HWBuffDrainLifeComponent as HWBuffDrainLifeComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.shared.system_factory import registerEquipmentItem as registerEquipmentItem
from gui.battle_control import avatar_getter as avatar_getter, vehicle_getter as vehicle_getter
from gui.battle_control.controllers.consumables.equipment_ctrl import _ActivationError as _ActivationError, DynComponentsGroupItem as DynComponentsGroupItem, DynComponentsGroupReplayItem as DynComponentsGroupReplayItem
from gui.battle_control.battle_constants import DEVICE_STATE_DESTROYED as DEVICE_STATE_DESTROYED
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from halloween_common.halloween_constants import HWVehicleModifiers as HWVehicleModifiers

class HWEquipmentItem(DynComponentsGroupItem):
    def canActivate(self, entityName=None, avatar=None):
        ...
    def getUsageCost(self):
        ...
    def getDurationSeconds(self):
        ...
    def getCooldownSeconds(self):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def variant(self):
        ...
    def _getUsageCost(self):
        ...
    def _getDurationSeconds(self):
        ...
    def _getCooldownSeconds(self):
        ...
    def _applyModifiers(self, key, value):
        ...

class HWEquipmentReplayItemBase(DynComponentsGroupReplayItem):
    def getUsageCost(self):
        ...
    def getDurationSeconds(self):
        ...
    def getCooldownSeconds(self):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def variant(self):
        ...
    def _getUsageCost(self):
        ...
    def _getDurationSeconds(self):
        ...
    def _getCooldownSeconds(self):
        ...
    def _applyModifiers(self, key, value):
        ...

class HWEquipmentReplayItem(HWEquipmentReplayItemBase):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _HpRepairAndCrewHeal(HWEquipmentItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _AbilityWithDuration(HWEquipmentItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _NitroEquipmentItem(_AbilityWithDuration):
    def inCriticalCondition(self, avatar=None):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...

class _NitroEquipmentReplayItem(HWEquipmentReplayItemBase):
    def inCriticalCondition(self, avatar=None):
        ...

class _FastReload(_AbilityWithDuration):
    INSTANT_RELOAD = 'instantReload'
    DEVICES: tuple
    ERROR_NAME = 'hw_ability_gun_destroyed'
    guiSessionProvider: Any
    def getEntitiesIterator(self, avatar=None):
        ...
    def canActivate(self, entityName=None, avatar=None):
        ...
    def _canActivateFast(self, entityName=None, avatar=None):
        ...
    def _canActivateInstant(self, entityName=None, avatar=None):
        ...

class _HWInvisibility(HWEquipmentItem):
    def canActivate(self, entityName=None, avatar=None):
        ...

class _HWInstantShot(HWEquipmentItem):
    def activate(self, entityName=None, avatar=None):
        ...

def registerHWEquipmentsItems():
    ...
