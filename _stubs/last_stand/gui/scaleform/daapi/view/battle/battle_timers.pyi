# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/battle_timers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.battle.shared import battle_timers as battle_timers
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE
from gui.impl import backport as backport
from gui.impl.gen import R as R
_HIDE_ALL_DELAY = 1.0

class PreBattleTimer(battle_timers.PreBattleTimer):
    _hideAllCB: Any
    _arenaBonusType: Any
    def __init__(self):
        ...
    def _dispose(self):
        ...
    def updateBattleCtx(self, battleCtx):
        ...
    def _getMessage(self):
        ...
    def _getWinConditionText(self, battleCtx):
        ...
    def _getWinMessage(self):
        ...
    def _onHideAll(self, speed):
        ...
    def _doHideAll(self):
        ...
    def _clearHideAllCB(self):
        ...
