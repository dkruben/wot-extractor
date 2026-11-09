# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/model_managers/balance_model_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import constants as constants
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.gen.view_models.views.common_balance_content_model import CommonBalanceContentModel as CommonBalanceContentModel
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from frameworks.wulf import NumberFormatType as NumberFormatType
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.gen.view_models.ui_kit.currency_item_model import CurrencyItemModel as CurrencyItemModel
from gui.impl.gen.view_models.views.value_price import ValuePrice as ValuePrice
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class CurrencyStatus(CONST_CONTAINER):
    IN_PROGRESS = 0
    NOT_AVAILABLE = 1
    AVAILABLE = 2

class BalanceModelManager(object):
    __itemsCache: Any
    __wallet: Any
    __gui: Any
    __slots__: tuple
    __CURRENCY_FORMATTER: dict
    __SPECIAL_TOOLTIPS: dict
    __currencyIndexes: Any
    __viewModel: Any
    __stats: Any
    __isGoldAutoPurchaseEnabled: Any
    def __init__(self, viewModel, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def start(self, currencies):
        ...
    def stop(self):
        ...
    def __addCurrency(self, currency, value):
        ...
    def __getCurrencyFormat(self, currency, value):
        ...
    def __onFreeXpUpdated(self, value):
        ...
    def __onMoneyUpdated(self, _):
        ...
    def __onCurrencyUpdated(self, currency, value):
        ...
    def __onWalletChanged(self, status):
        ...
