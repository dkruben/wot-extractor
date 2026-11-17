# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/popovers/filter_popover_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.filter_toggle_group_model import FilterToggleGroupModel as FilterToggleGroupModel
from gui.impl.gen.view_models.views.lobby.crew.popovers.filter_popover_view_model import FilterPopoverViewModel as FilterPopoverViewModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.crew.filter.state import FilterState as FilterState
from gui.impl.lobby.crew.tooltips.dismissed_toggle_tooltip import DismissedToggleTooltip as DismissedToggleTooltip
from gui.impl.pub import PopOverViewImpl as PopOverViewImpl
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.lobby.crew.filter import FilterGroupSettings as GroupSettings
from typing import Iterable as Iterable, Optional as Optional, Callable as Callable
FilterGroups: Any

class FilterPopoverView(PopOverViewImpl):
    __slots__: tuple
    itemsCache: Any
    __title: Any
    __groupSettings: Any
    __onStateUpdated: Any
    __state: Any
    __showResetBtn: Any
    __canResetCallback: Any
    onTooltipCreated: Any
    def __init__(self, title, groupSettings, onStateUpdated, state=None, showResetBtn=True, canResetCallback=None):
        ...
    @property
    def viewModel(self):
        ...
    def updateGroupSettings(self, groupSettings):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @args2params(...)
    def __onUpdateFilter(self, groupID, toggleID):
        ...
    def __onResetFilter(self):
        ...
    def __fillModel(self):
        ...
