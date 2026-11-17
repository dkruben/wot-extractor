# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/interactors/base_equipment.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from wg_async import wg_await as wg_await, wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.impl.lobby.tank_setup.interactors.base import BaseInteractor as BaseInteractor
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID as NONE_ID
from gui.shared.event_dispatcher import showTankSetupExitConfirmDialog as showTankSetupExitConfirmDialog

class BaseEquipmentInteractor(BaseInteractor):
    __slots__: tuple
    _installedIndices: Any
    _playerLayout: Any
    def setItem(self, item):
        ...
    @property
    def affectsTTC(self):
        ...
    def getPlayerLayout(self):
        ...
    def changeSlotItem(self, slotID, itemIntCD):
        ...
    def swapSlots(self, leftID, rightID, actionType=...):
        ...
    def revertSlot(self, slotID):
        ...
    def buyMore(self, itemCD):
        ...
    # decorador original: @wg_async
    def showExitConfirmDialog(self):
        ...
    def _resetInstalledIndices(self):
        ...
    def _resetPlayerLayout(self):
        ...
