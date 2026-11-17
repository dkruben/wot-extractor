# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/sub_views/content/select_option_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event
from frameworks.wulf import ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.framework.entities import View as View
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.goodies.demount_kit import getDemountKitForOptDevice as getDemountKitForOptDevice
from gui.impl import backport as backport
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.dialogs.dialog_template_utils import getCurrencyTooltipAlias as getCurrencyTooltipAlias
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import TooltipType as TooltipType
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyType as CurrencyType, CurrencySize as CurrencySize
from gui.impl.gen.view_models.views.dialogs.sub_views.select_demount_kit_view_model import SelectDemountKitViewModel as SelectDemountKitViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.select_map_view_model import SelectMapViewModel as SelectMapViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.select_money_view_model import SelectMoneyViewModel as SelectMoneyViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel as SelectOptionBaseItemViewModel, ComponentType as ComponentType
from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_view_model import SelectOptionViewModel as SelectOptionViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from typing import List as List, Optional as Optional, Callable as Callable
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Money as Money
from gui.goodies.goodie_items import DemountKit as DemountKit

class SelectOptionBasePresenter(object):
    __slots__: tuple
    _VIEW_MODEL = SelectOptionBaseItemViewModel
    __viewModel: Any
    __isDisabled: Any
    tooltipFactory: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self):
        ...
    def dispose(self):
        ...

class SelectOptionContent(ViewImpl):
    __slots__: tuple
    __presenterList: Any
    onSelectionChanged: Any
    __selectedIndex: Any
    def __init__(self, layoutID=None):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def selectedIndex(self):
        ...
    @selectedIndex.setter
    def selectedIndex(self, value):
        ...
    def setMessage(self, value):
        ...
    def addOption(self, controller):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __itemClickHandler(self, args):
        ...

class MoneyOption(SelectOptionBasePresenter):
    __slots__: tuple
    _VIEW_MODEL = SelectMoneyViewModel
    _itemsCache: Any
    __price: Any
    tooltipFactory: Any
    def __init__(self, price):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self):
        ...
    def dispose(self):
        ...
    def _moneyChangeHandler(self, *_):
        ...
    def updatePrice(self, newPrice):
        ...
    @property
    def shortage(self):
        ...
    def _updateShortage(self):
        ...
    def _updateMoney(self):
        ...
    def _updateIcon(self):
        ...
    def _tooltipFactory(self):
        ...

class DemountKitOption(SelectOptionBasePresenter):
    __slots__: tuple
    _VIEW_MODEL = SelectDemountKitViewModel
    _itemsCache: Any
    __demountKit: Any
    tooltipFactory: Any
    def __init__(self, itemCD):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self):
        ...
    def dispose(self):
        ...
    def _goodiesChangeHandler(self, *_):
        ...
    def _tooltipFactory(self):
        ...

class MapOption(SelectOptionBasePresenter):
    _VIEW_MODEL = SelectMapViewModel
    def __init__(self, mapId):
        ...
    @property
    def viewModel(self):
        ...
    def _updateIcon(self, mapId):
        ...
    def _updateText(self, mapId):
        ...
