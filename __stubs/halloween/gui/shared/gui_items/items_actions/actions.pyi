# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/shared/gui_items/items_actions/actions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_async as adisp_async
import wg_async as future_async
from gui.shared.gui_items.items_actions.actions import BuyAndInstallConsumables as BuyAndInstallConsumables
from gui.shared.gui_items.items_actions.actions import _needExchangeForBuy as _needExchangeForBuy
from gui.shared.money import ZERO_MONEY as ZERO_MONEY
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from halloween.gui.shared.event_dispatcher import showHWTankSetupConfirmDialog as showHWTankSetupConfirmDialog
from gui.shared.utils import decorators as decorators
from gui.shared.gui_items.processors.vehicle import BuyAndInstallConsumablesProcessor as BuyAndInstallConsumablesProcessor
from gui.shared.gui_items.processors.messages.items_processor_messages import ItemBuyProcessorMessage as ItemBuyProcessorMessage
from gui.shared.money import Money as Money
from gui.shared.gui_items.processors import makeSuccess as makeSuccess
from gui.impl import backport as backport
from gui.impl.gen import R as R

class HWBuyAndInstallConsumables(BuyAndInstallConsumables):
    __slots__: tuple
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

class HWBuyAndInstallConsumablesProcessor(BuyAndInstallConsumablesProcessor):
    def _successHandler(self, code, ctx=None):
        ...

class HWItemBuyProcessorMessage(ItemBuyProcessorMessage):
    def _getMsgCtx(self):
        ...
