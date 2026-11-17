# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/contents/common_balance_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from itertools import chain as chain
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen.view_models.views.common_balance_content_model import CommonBalanceContentModel as CommonBalanceContentModel
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from frameworks.wulf import NumberFormatType as NumberFormatType, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.value_price import ValuePrice as ValuePrice
from gui.impl.lobby.dialogs.model_managers.balance_model_manager import BalanceModelManager as BalanceModelManager
from gui.impl.pub.view_impl import ViewImpl as ViewImpl
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class CurrencyStatus(CONST_CONTAINER):
    IN_PROGRESS = 0
    NOT_AVAILABLE = 1
    AVAILABLE = 2

class CommonBalanceContent(ViewImpl):
    __itemsCache: Any
    __wallet: Any
    __slots__: tuple
    __CURRENCY_FORMATTER: dict
    __SPECIAL_TOOLTIPS: dict
    __modelManager: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
