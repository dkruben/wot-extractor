# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/battle/fort_rush_hud.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import weakref as weakref
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from typing import Optional as Optional, Sequence as Sequence, Tuple as Tuple, Callable as Callable, TYPE_CHECKING as TYPE_CHECKING
import GUI as GUI
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_view_model import FortRushHudViewModel as FortRushHudViewModel, AnnouncementTypeEnum as AnnouncementTypeEnum
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl, ViewImpl as ViewImpl
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from constants import ARENA_PERIOD as ARENA_PERIOD
from fort_rush.gui.impl.battle.capture_indicators_ctrl import CaptureIndicatorsCtrl as CaptureIndicatorsCtrl
from fort_rush.gui.impl.battle.team_score_sub_view import TeamScoreSubView as TeamScoreSubView
from skeletons.gui.app_loader import IAppLoader as IAppLoader, GuiGlobalSpaceID as GuiGlobalSpaceID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency, time_utils as time_utils
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
import Event as Event

class FortRushHudView(ViewImpl):
    LAYOUT_ID: Any
    _sessionProvider: Any
    _appLoader: Any
    __isBattleLoading: Any
    _callbackDelayer: Any
    markersCtrl: Any
    __captureIndicatorsCtrl: Any
    __teamScoreSubView: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __setup(self):
        ...
    def showHint(self, text, description, showCountdown, countdown):
        ...
    def hideHint(self):
        ...
    def _updateHint(self, text, description, countdown):
        ...
    def _startPeriodTimer(self):
        ...
    def _stopPeriodTimer(self):
        ...
    def _onSecond(self):
        ...
    def _getListeners(self):
        ...
    def _getEvents(self):
        ...
    def _onCameraChanged(self, controlModeName, vehicleID=None):
        ...
    def _onBattleLoading(self, event):
        ...
    def applyVisibility(self):
        ...
    def _updateHudVisibility(self, arenaPeriod):
        ...
    def _onRoundFinished(self, *args):
        ...
    def _onArenaPeriodChange(self, arenaPeriod, *args):
        ...
    def _setArenaPeriodTimer(self, arenaPeriod):
        ...
    def _finalize(self):
        ...

class FortRushHudWindow(WindowImpl):
    def __init__(self):
        ...
    def _onReady(self):
        ...
