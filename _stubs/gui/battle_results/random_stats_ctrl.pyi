# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/random_stats_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.battle_control.battle_constants import WinStatus as WinStatus
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from soft_exception import SoftException as SoftException
from gui.battle_results.pbs_helpers.common import pushNoBattleResultsDataMessage as pushNoBattleResultsDataMessage
from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl as IBattleResultStatsCtrl, BattleResults as BattleResults
from gui.shared.event_dispatcher import showBattleResultsWindow as showBattleResultsWindow
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo

class RandomBattleResultStatsCtrl(IBattleResultStatsCtrl):
    __sessionProvider: Any
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
    def __setBattleContext(self):
        ...
    @classmethod
    def representativeArenaBonusType(cls):
        ...
