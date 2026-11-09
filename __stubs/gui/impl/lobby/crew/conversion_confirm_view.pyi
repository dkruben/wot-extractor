# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/conversion_confirm_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.conversion_confirm_view_model import ConversionConfirmViewModel as ConversionConfirmViewModel
from gui.impl.lobby.crew.base_crew_view import BaseCrewSubView as BaseCrewSubView
from gui.impl.lobby.crew.filter.data_providers import JunkTankmenDataProvider as JunkTankmenDataProvider
from gui.impl.lobby.crew.tooltips.conversion_tooltip import ConversionTooltip as ConversionTooltip
from gui.impl.pub import WindowImpl as WindowImpl
from gui.shared.event_dispatcher import showJunkTankmen as showJunkTankmen
from gui.shared.gui_items.items_actions import factory as factory
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from PlayerEvents import g_playerEvents as g_playerEvents

class ConversionConfirmView(BaseCrewSubView):
    itemsCache: Any
    __slots__: tuple
    __dataProvider: Any
    __tooltipData: Any
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onDisconnected(self):
        ...
    def _onCancel(self):
        ...
    def _onClose(self):
        ...
    def _onShowTankman(self):
        ...
    def _onConfirm(self):
        ...
    def __onUpdate(self):
        ...

class ConversionConfirmWindow(WindowImpl):
    def __init__(self):
        ...
