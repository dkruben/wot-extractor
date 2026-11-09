# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_results/composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui import SystemMessages as SystemMessages
from gui.battle_results.composer import IBattleResultStatsCtrl as IBattleResultStatsCtrl
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from last_stand.gui.battle_results import templates as templates
from last_stand.gui.shared import event_dispatcher as event_dispatcher

class LastStandBattleStatsComposer(IBattleResultStatsCtrl):
    _block: Any
    def __init__(self, _):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def clear(self):
        ...
    def setResults(self, results, reusable):
        ...
    def getVO(self):
        ...
    def popAnimation(self):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...

def showErrorMessage():
    ...
