# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/lobby_notifier.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from constants import ARENA_PERIOD as ARENA_PERIOD
_NOTIFICATION_TIME = 20.0

class LobbyNotifier(IAbstractPeriodView):
    __isNotified: Any
    def __init__(self):
        ...
    def setCountdown(self, state, timeLeft):
        ...
    def __doNotify(self):
        ...
