# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/exchange_with_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.buy_and_exchange_bottom_content_type import BuyAndExchangeBottomContentType as BuyAndExchangeBottomContentType
from gui.impl.gen.view_models.views.lobby.exchange.exchange_with_items_model import ExchangeWithItemsModel as ExchangeWithItemsModel
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.impl.lobby.dialogs.buy_and_exchange import BuyAndExchange as BuyAndExchange
from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeContentResult as ExchangeContentResult
from gui.impl.lobby.dialogs.contents.multiple_items_content import MultipleItemsContent as MultipleItemsContent
from gui.impl.lobby.dialogs.contents.multiple_items_content_to_upgrade import MultipleItemsContentToUpgrade as MultipleItemsContentToUpgrade
from gui.shared.money import ZERO_MONEY as ZERO_MONEY
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
_logger: Any

class ExchangeWithItems(BuyAndExchange):
    __slots__: tuple
    __items: Any
    __totalPrice: Any
    _mainContent: Any
    def __init__(self, settings, items, price):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _exchangeComplete(self, result):
        ...
    def _stateToContent(self):
        ...
    @classmethod
    def _getContentClass(cls):
        ...

class ExchangeToBuyItems(ExchangeWithItems):
    __slots__: tuple
    def __init__(self, itemsCountMap):
        ...

class ExchangeToUpgradeDevice(ExchangeWithItems):
    __slots__: tuple
    def __init__(self, device):
        ...
    @classmethod
    def _getContentClass(cls):
        ...
