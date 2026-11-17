# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/fun_stats_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fun_random.gui.battle_results.pbs_helpers import getEventID as getEventID
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.shared.event_dispatcher import showFunRandomBattleResults as showFunRandomBattleResults
from gui.battle_results.pbs_helpers.common import pushNoBattleResultsDataMessage as pushNoBattleResultsDataMessage
from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl as IBattleResultStatsCtrl, BattleResults as BattleResults
from soft_exception import SoftException as SoftException
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo

class FunBattleResultStatsCtrl(IBattleResultStatsCtrl, FunSubModesWatcher):
    _battleResults: Any
    def __init__(self, _):
        ...
    @property
    def ctrlImplType(self):
        ...
    def clear(self):
        ...
    def getVO(self):
        ...
    def getResults(self):
        ...
    def setResults(self, results, reusable):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
