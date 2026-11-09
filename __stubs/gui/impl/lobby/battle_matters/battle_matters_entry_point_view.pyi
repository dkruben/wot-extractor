# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_entry_point_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_entry_point_view_model import BattleMattersEntryPointViewModel as BattleMattersEntryPointViewModel, State as State
from gui.impl.gen import R as R
from gui.impl.lobby.battle_matters.tooltips.battle_matters_entry_tooltip_view import BattleMattersEntryTooltipView as BattleMattersEntryTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.events_dispatcher import showBattleMatters as showBattleMatters
from helpers import dependency as dependency
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from frameworks.wulf import ViewEvent as ViewEvent, View as View
from typing import Sequence as Sequence, Tuple as Tuple, Callable as Callable, Optional as Optional
from Event import Event as Event

class BattleMattersEntryPointView(ViewImpl):
    __slots__: tuple
    __battleMattersController: Any
    __eventsCache: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self):
        ...
    def _getEvents(self):
        ...
    def __update(self, *_):
        ...
    @staticmethod
    def __onClick():
        ...
