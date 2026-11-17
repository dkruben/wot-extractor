# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/battle_results/composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.battle_results.templates import comp7_templates as comp7_templates
from comp7.gui.impl.lobby.battle_results.submodel_presenters.battle_info import isDeserter as isDeserter
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.battle_control.battle_constants import WinStatus as WinStatus
from gui.battle_results import templates as templates
from gui.battle_results.composer import StatsComposer as StatsComposer
from gui.battle_results.pbs_helpers.common import pushNoBattleResultsDataMessage as pushNoBattleResultsDataMessage
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.shared.event_dispatcher import showBattleResultsWindow as showBattleResultsWindow
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from frameworks.wulf import ViewModel as ViewModel
BattleResultsModelType: Any
TooltipModelType: Any

class Comp7StatsComposer(StatsComposer):
    __sessionProvider: Any
    _battleResults: Any
    def __init__(self, reusable):
        ...
    @staticmethod
    def _getBattlePassBlock():
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
    def setResults(self, results, reusable):
        ...
    def getResults(self):
        ...

class TournamentComp7StatsComposer(StatsComposer):
    __sessionProvider: Any
    _battleResults: Any
    def __init__(self, reusable):
        ...
    @staticmethod
    def _getBattlePassBlock():
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
    def setResults(self, results, reusable):
        ...
    def getResults(self):
        ...
    @classmethod
    def representativeArenaBonusType(cls):
        ...

class TrainingComp7StatsComposer(StatsComposer):
    __sessionProvider: Any
    _battleResults: Any
    def __init__(self, reusable):
        ...
    @staticmethod
    def _getBattlePassBlock():
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
    def setResults(self, results, reusable):
        ...
    def getResults(self):
        ...
    @classmethod
    def representativeArenaBonusType(cls):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _setBattleWinStatus(reusable, sessionProvider=None):
    ...
