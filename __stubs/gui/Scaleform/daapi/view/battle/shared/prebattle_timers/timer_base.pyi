# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/prebattle_timers/timer_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.daapi.view.meta.PrebattleTimerBaseMeta import PrebattleTimerBaseMeta as PrebattleTimerBaseMeta
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE, BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import i18n as i18n
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_TIMER_ANIMATION_SHIFT = 0.4
_STATE_TO_MESSAGE: dict

class PreBattleTimerBase(PrebattleTimerBaseMeta, IAbstractPeriodView, IArenaVehiclesController):
    sessionProvider: Any
    lobbyContext: Any
    _state: Any
    _battleTypeStr: Any
    __timeLeft: Any
    __callbackID: Any
    __arenaPeriod: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def updateBattleCtx(self, battleCtx):
        ...
    def setPeriod(self, period):
        ...
    def setCountdown(self, state, timeLeft):
        ...
    def hideCountdown(self, state, speed):
        ...
    def _onHideAll(self, speed):
        ...
    def _getMessage(self):
        ...
    def _isDisplayWinCondition(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onPrebattleHighlightsStart(self, _=None):
        ...
    def _onPrebattleHighlightsClose(self, _=None):
        ...
    def __setTimeShiftCallback(self):
        ...
    def __updateTimer(self):
        ...
    def _clearTimeShiftCallback(self):
        ...
