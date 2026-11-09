# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/prebattle/prebattle_hints_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
from constants import ARENA_PERIOD as ARENA_PERIOD
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer, ViewStatus as ViewStatus
from gui import InputHandler as InputHandler
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.prebattle.prebattle_hints_view_model import PrebattleHintsViewModel as PrebattleHintsViewModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.prebattle_hints.controller import IPrebattleHintsController as IPrebattleHintsController
from hints_common.prebattle.schemas import configSchema as configSchema
from hints_common.prebattle.schemas import HintModel as HintModel

class PrebattleHintsView(ViewImpl, BattleGUIKeyHandler, IArenaLoadController):
    __slots__: tuple
    _LAYOUT_ID: Any
    _VIEW_MODEL_CLASS = PrebattleHintsViewModel
    _TRY_CLOSE_WINDOW_PERIOD = 0.1
    _sessionProvider: Any
    _connectionMgr: Any
    _hintsController: Any
    _appLoader: Any
    _settingsCore: Any
    _hintModel: Any
    def __init__(self, hintModel):
        ...
    @classmethod
    def needToShow(cls):
        ...
    @staticmethod
    def _isTimeToCloseWindow(sessionProvider):
        ...
    def handleEscKey(self, isDown):
        ...
    @property
    def viewModel(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _onHandleKeyDown(self, event):
        ...
    def _tryToCloseWindow(self):
        ...
    def _tryToCloseNextTime(self):
        ...
    def _onDisconnected(self):
        ...
    def _successClose(self):
        ...
    @property
    def _battleApp(self):
        ...

class PrebattleHintsWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, hintModel, hintsViewClass=None, parent=None):
        ...
