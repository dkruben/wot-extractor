# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/prebattle_timer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from comp7_core_constants import ArenaPrebattlePhase as ArenaPrebattlePhase
from comp7_core.gui.Scaleform.daapi.view.meta.Comp7PrebattleTimerMeta import Comp7PrebattleTimerMeta as Comp7PrebattleTimerMeta
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from constants import ARENA_PERIOD as ARENA_PERIOD, VEHICLE_SELECTION_BLOCK_DELAY as VEHICLE_SELECTION_BLOCK_DELAY
from gui.Scaleform.genConsts.PREBATTLE_TIMER import PREBATTLE_TIMER as PREBATTLE_TIMER
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency, i18n as i18n
from math_common import round_py2_style_int as round_py2_style_int
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class Comp7PrebattleTimer(Comp7PrebattleTimerMeta):
    __sessionProvider: Any
    __RES_ROOT = R.strings.comp7_core.prebattleTimer
    __isSelectionConfirmed: Any
    __winConditionStr: Any
    __isPrebattleInputStateLocked: Any
    __isUIUpdateNeeded: Any
    __lastProcessedState: Any
    def __init__(self):
        ...
    def updateBattleCtx(self, battleCtx):
        ...
    def setCountdown(self, state, timeLeft):
        ...
    def onReadyBtnClick(self):
        ...
    def hideCountdown(self, state, speed):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _isDisplayWinCondition(self):
        ...
    def _getMessage(self):
        ...
    def __updateUIIfNeeded(self):
        ...
    def __invalidateLastProcessedState(self):
        ...
    def __updateHint(self):
        ...
    def __updateButton(self):
        ...
    def __getInfoVO(self):
        ...
    def __onPrebattleInputStateLocked(self, _):
        ...
    def __updateMessageAndWinDescription(self):
        ...
    def __isSelectionPossible(self):
        ...
    def __setIsSelectionConfirmed(self, value):
        ...
    def __setIsPrebattleInputStateLocked(self, value):
        ...
    def __getVehicleBanCtrl(self):
        ...
    def __isVehicleBanEnabled(self):
        ...
    def __getBanPhaseData(self, countdownTimeLeft=None):
        ...
    def __updateBanPhaseUI(self):
        ...
