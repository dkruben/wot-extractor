# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/battle_timers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import SoundGroups as SoundGroups
import CommandMapping as CommandMapping
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.Scaleform.daapi.view.meta.BattleTimerMeta import BattleTimerMeta as BattleTimerMeta
from gui.Scaleform.daapi.view.meta.PrebattleTimerMeta import PrebattleTimerMeta as PrebattleTimerMeta
from gui.Scaleform.genConsts.PREBATTLE_TIMER import PREBATTLE_TIMER as PREBATTLE_TIMER
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from helpers import dependency as dependency
from skeletons.gameplay import IGameplayLogic as IGameplayLogic, GameplayStateID as GameplayStateID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey
_BATTLE_END_TIME = 0
_logger: Any

class _WWISE_EVENTS(object):
    BATTLE_ENDING_SOON = 'time_buzzer_02'
    COUNTDOWN_TICKING = 'time_countdown'
    STOP_TICKING = 'time_countdown_stop'
    FLAG_APPEAR = 'pm_flag_appearance'
    FLAG_DISAPPEAR = 'pm_flag_disappearance'

class PreBattleTimer(PrebattleTimerMeta):
    __gameplayLogic: Any
    __isPMBattleProgressEnabled: Any
    __isRankedBattle: Any
    __sounds: Any
    __displayWinCondition: Any
    _battleTypeStr: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def onShowInfo(self):
        ...
    def onHideInfo(self):
        ...
    def updateBattleCtx(self, battleCtx):
        ...
    def _getWinConditionText(self, battleCtx):
        ...
    def _onPersonalQuestConditionsUpdate(self, *args):
        ...
    def __onMappingChanged(self, *args):
        ...
    def __callWWISE(self, wwiseEventName):
        ...
    def _dispose(self):
        ...
    def _onShowInfo(self, _=None, __=None):
        ...
    def _onPrebattleHighlightsStart(self, _=None):
        ...
    def __handleBattleLoading(self, event):
        ...

class BattleTimer(BattleTimerMeta, IAbstractPeriodView):
    sessionProvider: Any
    _isTicking: Any
    __state: Any
    __roundLength: Any
    __endingSoonTime: Any
    __isDeathScreenShown: Any
    __endWarningIsEnabled: Any
    __sounds: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    @property
    def arenaVisitor(self):
        ...
    def getRoundLength(self):
        ...
    def setTotalTime(self, totalTime):
        ...
    def setState(self, state):
        ...
    def hideTotalTime(self):
        ...
    def showTotalTime(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _sendTime(self, totalTime):
        ...
    def _callWWISE(self, wwiseEventName):
        ...
    def _setColor(self):
        ...
    def _startTicking(self):
        ...
    def __stopTicking(self):
        ...
    def __validateEndingSoonTime(self):
        ...
    def __checkEndWarningStatus(self):
        ...
    def __onShowDeathScreen(self):
        ...
    def __onVehicleLeaveWorld(self):
        ...
