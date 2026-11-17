# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.battle_results import templates as templates
from gui.battle_results.components import base as base
from gui.battle_results.random_stats_ctrl import RandomBattleResultStatsCtrl as RandomBattleResultStatsCtrl
from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl as IBattleResultStatsCtrl
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.event_dispatcher import showLegacyBattleResultsWindow as showLegacyBattleResultsWindow
from gui.shared.system_factory import registerBattleResultStatsCtrl as registerBattleResultStatsCtrl
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController
from frameworks.wulf import ViewModel as ViewModel
BattleResultsModelType: Any
TooltipModelType: Any

class StatsComposer(IBattleResultStatsCtrl):
    __slots__: tuple
    _block: Any
    def __init__(self, reusable, common, personal, teams, text):
        ...
    def clear(self):
        ...
    def setResults(self, results, reusable):
        ...
    def getVO(self):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
    def _registerTabs(self, reusable):
        ...
    @staticmethod
    def _getBattlePassBlock():
        ...

class RegularStatsComposer(StatsComposer):
    def __init__(self, reusable):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...

class EpicStatsComposer(StatsComposer):
    def __init__(self, reusable):
        ...
    def _registerTabs(self, reusable):
        ...

class CyberSportStatsComposer(StatsComposer):
    def __init__(self, reusable):
        ...

class StrongholdBattleStatsComposer(StatsComposer):
    def __init__(self, reusable):
        ...

class StrongholdSortieBattleStatsComposer(StatsComposer):
    def __init__(self, reusable):
        ...

class RankedBattlesStatsComposer(StatsComposer):
    __resultsTeamsBlock: Any
    def __init__(self, reusable):
        ...
    def clear(self):
        ...
    def setResults(self, results, reusable):
        ...
    def getResultsTeamsVO(self):
        ...

class MapsTrainingStatsComposer(IBattleResultStatsCtrl):
    _fromNotifications: Any
    mapsTrainingController: Any
    _block: Any
    def __init__(self, _):
        ...
    def clear(self):
        ...
    def setResults(self, results, reusable):
        ...
    def getVO(self):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
