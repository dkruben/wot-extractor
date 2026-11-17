# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/comp7_light_battle_results_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, Map as Map, ViewModel as ViewModel
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_battle_info_model import Comp7LightBattleInfoModel as Comp7LightBattleInfoModel
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_team_stats_model import Comp7LightTeamStatsModel as Comp7LightTeamStatsModel
from comp7_light.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel as ScheduleInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import AdditionalBonusModel as AdditionalBonusModel
from gui.impl.gen.view_models.views.lobby.battle_results.base_capture_info_model import BaseCaptureInfoModel as BaseCaptureInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel as DetailedPersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.financial_report_model import FinancialReportModel as FinancialReportModel
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel as PostbattleAchievementModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel

class WarningType(Enum):
    NONE = 'none'
    LEAVE = 'leave'

class Comp7LightBattleResultsViewModel(ViewModel):
    __slots__: tuple
    OVERVIEW = 'overview'
    TEAMS_STATISTICS = 'teamScore'
    PROGRESSION = 'missionProgress'
    FINANCIAL_REPORT = 'financialReport'
    onClose: Any
    onOpenMissions: Any
    def __init__(self, properties=11, commands=2):
        ...
    @property
    def scheduleInfo(self):
        ...
    @staticmethod
    def getScheduleInfoType():
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
    def router(self):
        ...
    @staticmethod
    def getRouterType():
        ...
    def getWarningType(self):
        ...
    def setWarningType(self, value):
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
