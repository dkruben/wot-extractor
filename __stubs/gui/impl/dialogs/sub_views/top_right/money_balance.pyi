# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/sub_views/top_right/money_balance.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.dialogs.dialog_template_tooltip import DialogTemplateTooltip as DialogTemplateTooltip
from gui.impl.dialogs.dialog_template_utils import getCurrencyTooltipAlias as getCurrencyTooltipAlias
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyType as CurrencyType
from gui.impl.gen.view_models.views.dialogs.sub_views.money_balance_view_model import MoneyBalanceViewModel as MoneyBalanceViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.tooltip_window import SimpleTooltipContent as SimpleTooltipContent
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import View as View
NO_WGM_TOOLTIP_DATA: dict

class MoneyBalance(ViewImpl):
    __slots__: tuple
    _itemsCache: Any
    _wallet: Any
    _currenciesList: Any
    _stats: Any
    _tooltips: Any
    def __init__(self, layoutID=None, viewModel=None, currenciesList=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initTooltips(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _moneyChangeHandler(self, *_):
        ...
    def _updateModel(self, model):
        ...
    def __setStats(self, model):
        ...
    @staticmethod
    def __WGMAvailableTooltipFactory(currency):
        ...
    @staticmethod
    def __WGMNotAvailableTooltipFactory(currency):
        ...
