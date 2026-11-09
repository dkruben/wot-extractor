# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/shared/prebattle_timer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.battle.shared.battle_timers import PreBattleTimer as PreBattleTimer
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import i18n as i18n

class FortrushPrebattleTimer(PreBattleTimer):
    _STATE_TO_MESSAGE: dict
    def _getMessage(self):
        ...
    def setCountdown(self, state, timeLeft):
        ...
