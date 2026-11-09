# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/pve_prebattle_timer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase as PreBattleTimerBase
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE
from helpers import dependency as dependency
from pve_battle_hud import WidgetType as WidgetType
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class PvePrebattleTimer(PreBattleTimerBase):
    _sessionProvider: Any
    _battleTypeStr: Any
    def updateBattleCtx(self, battleCtx):
        ...
    def setCountdown(self, state, timeLeft):
        ...
    def hideCountdown(self, state, speed):
        ...
    def _getMessage(self):
        ...
