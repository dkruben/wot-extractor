# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/currency_tab_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen.view_models.views.lobby.exchange.currency_model import CurrencyType as CurrencyType, CurrencyModel as CurrencyModel
from gui.impl.gen.view_models.views.lobby.exchange.currency_tab_model import CurrencyTabModel as CurrencyTabModel
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_TYPE_TO_VALUE_PATH: dict
_CURRENCY_TOOLTIPS: dict

class CurrenciesTabView(SubModelPresenter):
    __slots__: tuple
    __wallet: Any
    __itemsCache: Any
    __tooltipData: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def __updateCurrencies(self):
        ...
    def __onBalanceUpdated(self, *args, **kwargs):
        ...
    def __onWalletChanged(self, _):
        ...
    def createToolTip(self, event):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getCurrencyValueFromType(currencyType, itemsCache=None):
    ...
