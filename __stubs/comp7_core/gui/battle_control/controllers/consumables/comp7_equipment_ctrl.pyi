# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_control/controllers/consumables/comp7_equipment_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import CGF as CGF
import Event as Event
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.consumables import equipment_ctrl as equipment_ctrl
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from items import vehicles as vehicles
from points_of_interest.managers import PoiStateUpdateSystem as PoiStateUpdateSystem
from points_of_interest_shared import PoiEquipmentNamesByPoiType as PoiEquipmentNamesByPoiType
from comp7_core.gui.battle_control.controllers.consumables.comp7_equipment_items import EQUIPMENT_TAG_TO_ITEM as EQUIPMENT_TAG_TO_ITEM, REPLAY_EQUIPMENT_TAG_TO_ITEM as REPLAY_EQUIPMENT_TAG_TO_ITEM
from helpers.fixed_dict import RoleEquipmentState as RoleEquipmentState
from PoiComponent import PoiComponent as PoiComponent

class Comp7EquipmentController(equipment_ctrl.EquipmentsController):
    onRoleEquipmentStateChanged: Any
    onRoleEquipmentCounterChanged: Any
    __roleEquipmentState: Any
    __roleEquipmentCounter: Any
    __roleEquipmentPreviousState: Any
    def __init__(self, setup):
        ...
    @classmethod
    def createItem(cls, descriptor, quantity, stage, timeRemaining, totalTime):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def clear(self, leave=True):
        ...
    def getRoleEquipmentState(self):
        ...
    def getRoleEquipmentCounter(self):
        ...
    def getRoleEquipmentPreviousState(self):
        ...
    def __onPoiAdded(self, event):
        ...
    def __rediscoverPoi(self):
        ...
    def __rediscoverRoleSkill(self):
        ...
    def __addPoiByType(self, poiType):
        ...
    def __onRoleEquipmentStateChanged(self, event):
        ...
    def __onRoleEquipmentCounterChanged(self, event):
        ...
    @staticmethod
    def __getPoiEquipment(poiType):
        ...

class Comp7ReplayEquipmentController(equipment_ctrl.EquipmentsReplayPlayer, Comp7EquipmentController):
    @classmethod
    def createItem(cls, descriptor, quantity, stage, timeRemaining, totalTime):
        ...
