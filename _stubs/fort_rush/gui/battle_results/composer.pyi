# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_results/composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from soft_exception import SoftException as SoftException
from gui.battle_results.pbs_helpers.common import pushNoBattleResultsDataMessage as pushNoBattleResultsDataMessage
from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl as IBattleResultStatsCtrl, BattleResults as BattleResults
from fort_rush.gui.shared.event_dispatcher import showFortRushBattleResultView as showFortRushBattleResultView
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo

class FortRushBattleResultStatsCtrl(IBattleResultStatsCtrl):
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
    def setResults(self, results, reusable):
        ...
    def getResults(self):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
