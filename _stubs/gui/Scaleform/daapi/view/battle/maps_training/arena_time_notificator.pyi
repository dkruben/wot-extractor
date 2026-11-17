# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/arena_time_notificator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_TIME_TO_NOTIFY_BATTLE_END = 120

class MapsTrainingArenaTimeNotificator(IAbstractPeriodView):
    sessionProvider: Any
    __prevLength: Any
    __period: Any
    __lastNotifiedTime: Any
    def __init__(self):
        ...
    def setTotalTime(self, totalTime):
        ...
