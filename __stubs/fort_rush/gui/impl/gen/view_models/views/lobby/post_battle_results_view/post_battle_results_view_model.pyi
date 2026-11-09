# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/post_battle_results_view/post_battle_results_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.battle_info_model import BattleInfoModel as BattleInfoModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.battle_team_stats_model import BattleTeamStatsModel as BattleTeamStatsModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.detailed_personal_efficiency_item_model import DetailedPersonalEfficiencyItemModel as DetailedPersonalEfficiencyItemModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.fort_rush_reward_item_model import FortRushRewardItemModel as FortRushRewardItemModel
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
    def router(self):
        ...
    @staticmethod
    def getRouterType():
        ...
    def getIsLeaver(self):
        ...
    def setIsLeaver(self, value):
        ...
    def getDetailedPersonalEfficiency(self):
        ...
    def setDetailedPersonalEfficiency(self, value):
        ...
    @staticmethod
    def getDetailedPersonalEfficiencyType():
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def _initialize(self):
        ...
