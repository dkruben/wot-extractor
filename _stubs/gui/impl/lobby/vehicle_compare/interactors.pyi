# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/interactors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.lobby.tank_setup.interactors.base import InteractingItem as InteractingItem
from gui.impl.lobby.tank_setup.interactors.battle_booster import BaseBattleBoosterInteractor as BaseBattleBoosterInteractor
from gui.impl.lobby.tank_setup.interactors.consumable import BaseConsumableInteractor as BaseConsumableInteractor
from gui.impl.lobby.tank_setup.interactors.opt_device import BaseOptDeviceInteractor as BaseOptDeviceInteractor
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID as NONE_ID

class CompareInteractingItem(InteractingItem):
    __slots__: tuple
    onSelected: Any
    def __init__(self, item):
        ...
    def clear(self):
        ...

class CompareBattleBoosterInteractor(BaseBattleBoosterInteractor):
    def changeSlotItem(self, slotID, itemIntCD):
        ...
    def swapSlots(self, leftID, rightID):
        ...
    def revertSlot(self, slotID):
        ...

class CompareOptDeviceInteractor(BaseOptDeviceInteractor):
    def changeSlotItem(self, slotID, itemIntCD):
        ...
    def swapSlots(self, leftID, rightID):
        ...
    def revertSlot(self, slotID):
        ...

class CompareConsumableInteractor(BaseConsumableInteractor):
    def changeSlotItem(self, slotID, itemIntCD):
        ...
    def swapSlots(self, leftID, rightID):
        ...
    def revertSlot(self, slotID):
        ...

def _sendSwapSlotAction(interactor, leftID, rightID):
    ...
def _sendSelectSlotAction(interactor, slotID, itemIntCD):
    ...
