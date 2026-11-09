# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/filter/filter_panel_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer, ViewStatus as ViewStatus
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.filter_panel_widget_model import FilterPanelWidgetModel as FilterPanelWidgetModel, FilterPanelType as FilterPanelType
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.crew.filter.state import FilterState as FilterState
from gui.impl.lobby.crew.popovers.filter_popover_view import FilterPopoverView as FilterPopoverView
from gui.impl.pub import ViewImpl as ViewImpl, PopOverWindow as PopOverWindow
from gui.impl.lobby.crew.filter import FilterGroupSettings as GroupSettings
from typing import Iterable as Iterable, Callable as Callable, Dict as Dict, Union as Union
OnUpdateState: Any
FilterGroups: Any

class FilterPanelWidget(ViewImpl):
    LAYOUT_ID = R.views.lobby.crew.widgets.FilterPanelWidget
    __slots__: tuple
    __state: Any
    __isSearchEnabled: Any
    __showResetBtn: Any
    __mainFilterSettings: Any
    __popoverGroupSettings: Any
    __popoverTitle: Any
    __amountInfo: Any
    __title: Any
    __panelType: Any
    __popoverTooltipHeader: Any
    __popoverTooltipBody: Any
    __searchPlaceholder: Any
    __searchTooltipHeader: Any
    __searchTooltipBody: Any
    __hasDiscountAlert: Any
    __popoverView: Any
    onPopoverTooltipCreated: Any
    def __init__(self, mainFilterSettings, popoverGroupSettings, popoverTitle, state, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def resetState(self):
        ...
    def updateHasDiscountAlert(self, hasDiscountAlert):
        ...
    def updatePopoverGroupSettings(self, popoverGroupSettings):
        ...
    def updateAmountInfo(self, filteredAmount, totalAmount):
        ...
    def refreshAmountInfo(self):
        ...
    def applyStateToModel(self):
        ...
    def hasAppliedFilters(self):
        ...
    def updateFilterToggleCounter(self, filterId, count):
        ...
    def createPopOver(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onPopoverStatusChanged(self, status):
        ...
    # decorador original: @args2params(...)
    def __onSearch(self, value):
        ...
    # decorador original: @args2params(...)
    def __onUpdateFilter(self, groupID, toggleID):
        ...
    def __onResetFilter(self):
        ...
    def __onPopoverStateUpdated(self):
        ...
    def __fillModel(self, initial=False):
        ...
