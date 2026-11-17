# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/sub_views/common/single_price.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.dialogs.dialog_template_utils import toString as toString
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import TooltipType as TooltipType
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyType as CurrencyType, CurrencySize as CurrencySize
from gui.impl.gen.view_models.views.dialogs.sub_views.single_price_view_model import SinglePriceViewModel as SinglePriceViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional, Union as Union
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from frameworks.wulf import PyResAccessor as PyResAccessor
from gui.shared.money import Money as Money

class SinglePrice(ViewImpl):
    __slots__: tuple
    LAYOUT_DYN_ACCESSOR = R.views.dialogs.sub_views.common.SinglePrice
    _itemsCache: Any
    __text: Any
    __price: Any
    __size: Any
    __currencyTypeClass: Any
    __showDiscountValue: Any
    def __init__(self, text, price, size=..., layoutID=None, currencyTypeClass=..., showDiscountValue=True):
        ...
    @property
    def viewModel(self):
        ...
    def updatePrice(self, newPrice):
        ...
    def setSize(self, newSize):
        ...
    def setText(self, newText):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _moneyChangeHandler(self, *_):
        ...
    def __updateViewModel(self):
        ...

def _convertMoneyToTuple(money):
    ...
