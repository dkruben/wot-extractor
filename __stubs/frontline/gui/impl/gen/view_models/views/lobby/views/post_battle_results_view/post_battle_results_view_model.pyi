# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/post_battle_results_view/post_battle_results_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.achievement_model import AchievementModel as AchievementModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_financial_report_model import BattleFinancialReportModel as BattleFinancialReportModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_info_model import BattleInfoModel as BattleInfoModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_team_stats_model import BattleTeamStatsModel as BattleTeamStatsModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel as DetailedPersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel

class PostBattleResultsViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=6, commands=1):
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
    def financialReport(self):
        ...
    @staticmethod
    def getFinancialReportType():
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
    def _initialize(self):
        ...
