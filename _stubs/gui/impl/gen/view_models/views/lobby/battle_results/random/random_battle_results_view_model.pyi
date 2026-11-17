# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/random/random_battle_results_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, Map as Map, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import AdditionalBonusModel as AdditionalBonusModel
from gui.impl.gen.view_models.views.lobby.battle_results.base_capture_info_model import BaseCaptureInfoModel as BaseCaptureInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel as DetailedPersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.financial_report_model import FinancialReportModel as FinancialReportModel
from gui.impl.gen.view_models.views.lobby.battle_results.player_satisfaction_model import PlayerSatisfactionModel as PlayerSatisfactionModel
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel as PostbattleAchievementModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_battle_info_model import RandomBattleInfoModel as RandomBattleInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_team_stats_model import RandomTeamStatsModel as RandomTeamStatsModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel

class RandomBattleResultsViewModel(ViewModel):
    __slots__: tuple
    OVERVIEW = 'overview'
    TEAMS_STATISTICS = 'teamScore'
    PROGRESSION = 'missionProgress'
    FINANCIAL_REPORT = 'financialReport'
    onClose: Any
    onOpenMissions: Any
    def __init__(self, properties=10, commands=2):
        ...
    @property
    def battleInfo(self):
        ...
    @staticmethod
    def getBattleInfoType():
        ...
    @property
    def teamStats(self):
        ...
    @staticmethod
    def getTeamStatsType():
        ...
    @property
    def baseCaptureInfo(self):
        ...
    @staticmethod
    def getBaseCaptureInfoType():
        ...
    @property
    def financialReport(self):
        ...
    @staticmethod
    def getFinancialReportType():
        ...
    @property
    def additionalBonus(self):
        ...
    @staticmethod
    def getAdditionalBonusType():
        ...
    @property
    def playerSatisfaction(self):
        ...
    @staticmethod
    def getPlayerSatisfactionType():
        ...
    @property
    def router(self):
        ...
    @staticmethod
    def getRouterType():
        ...
    def getAchievements(self):
        ...
    def setAchievements(self, value):
        ...
    @staticmethod
    def getAchievementsType():
        ...
    def getDetailedPersonalEfficiency(self):
        ...
    def setDetailedPersonalEfficiency(self, value):
        ...
    @staticmethod
    def getDetailedPersonalEfficiencyType():
        ...
    def getPathToPlugins(self):
        ...
    def setPathToPlugins(self, value):
        ...
    @staticmethod
    def getPathToPluginsType():
        ...
    def _initialize(self):
        ...
