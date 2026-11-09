# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/shared/gui_items/items_actions/actions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from adisp import adisp_async as adisp_async
import wg_async as future_async
from gui.shared.gui_items.items_actions.actions import BuyAndInstallConsumables as BuyAndInstallConsumables
from gui.shared.gui_items.items_actions.actions import _needExchangeForBuy as _needExchangeForBuy
from gui.shared.money import ZERO_MONEY as ZERO_MONEY
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from last_stand.gui.shared.event_dispatcher import showTankSetupConfirmDialog as showTankSetupConfirmDialog
from gui.shared.utils import decorators as decorators
from gui.shared.gui_items.processors.vehicle import BuyAndInstallConsumablesProcessor as BuyAndInstallConsumablesProcessor
from gui.shared.money import Money as Money
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.processors.messages.items_processor_messages import ItemBuyProcessorMessage as ItemBuyProcessorMessage
from gui.shared.gui_items.processors import plugins as proc_plugs, makeSuccess as makeSuccess
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO as ITEM_PRICE_ZERO
from LSAccountEquipmentController import getLSConsumables as getLSConsumables

class LSItemBuyProcessorMessage(ItemBuyProcessorMessage):
    def _getMsgCtx(self):
        ...

class LSConsumablesInstallValidator(proc_plugs.ConsumablesInstallValidator):
    def _getLayout(self):
        ...
    def _getInstalled(self):
        ...

class LSBuyAndInstallConsumablesProcessor(BuyAndInstallConsumablesProcessor):
    def _successHandler(self, code, ctx=None):
        ...
    def _setupPlugins(self):
        ...
    def _request(self, callback):
        ...
    def __getLayoutRaw(self):
        ...

class LSBuyAndInstallConsumables(BuyAndInstallConsumables):
    __slots__: tuple
    _changedItems: Any
    __confirmOnlyExchange: Any
    def __init__(self, vehicle, confirmOnlyExchange=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @future_async.wg_async
    def _confirm(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def _action(self, callback):
        ...

def getConsumablesPrice(consumables):
    ...
