# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/prebattle_highlights/prebattle_highlights_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.impl.battle.prebattle_highlights.presenters.prebattle_highlights_presenter import PrebattleHighlightsPresenter as PrebattleHighlightsPresenter
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.prebattle.prebattle_hints_view_model import PrebattleHintsViewModel as PrebattleHintsViewModel
from gui.impl.gen.view_models.views.battle.prebattle_highlights.prebattle_highlights_view_model import PrebattleHighlightsViewModel as PrebattleHighlightsViewModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class PrebattleHighlightsView(ViewImpl, BattleGUIKeyHandler):
    _LAYOUT_ID: Any
    _VIEW_MODEL_CLASS = PrebattleHighlightsViewModel
    __sessionProvider: Any
    __appLoader: Any
    __presenter: Any
    __pbhCtrl: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def handleEscKey(self, isDown):
        ...
    @property
    def _battleApp(self):
        ...
    def __isIngameMenuShown(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onDisconnected(self):
        ...
    def __onVehiclesDataReady(self):
        ...
    def __onPrebattleHighlightsStart(self, _):
        ...

class PrebattleHighlightsWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
    def _onReady(self):
        ...
