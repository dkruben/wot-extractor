# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/battle_results/fun_battle_results_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel as UserNameModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_random_battle_info_model import FunRandomBattleInfoModel as FunRandomBattleInfoModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_random_progress_model import FunRandomProgressModel as FunRandomProgressModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_random_reward_item_model import FunRandomRewardItemModel as FunRandomRewardItemModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_team_stats_model import FunTeamStatsModel as FunTeamStatsModel
from gui.impl.gen.view_models.views.lobby.battle_results.personal_efficiency_model import PersonalEfficiencyModel as PersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.premium_plus_model import PremiumPlusModel as PremiumPlusModel
from gui.impl.gen.view_models.views.lobby.battle_results.user_status_model import UserStatusModel as UserStatusModel

class Tab(IntEnum):
    PERSONAL = 1
    TEAMSTATS = 2

class FunBattleResultsViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=8, commands=1):
        ...
    @property
    def userNames(self):
        ...
    @staticmethod
    def getUserNamesType():
        ...
    @property
    def userStatus(self):
        ...
    @staticmethod
    def getUserStatusType():
        ...
    @property
    def battleInfo(self):
        ...
    @staticmethod
    def getBattleInfoType():
        ...
    @property
    def premiumPlus(self):
        ...
    @staticmethod
    def getPremiumPlusType():
        ...
    @property
    def teamStats(self):
        ...
    @staticmethod
    def getTeamStatsType():
        ...
    @property
    def progress(self):
        ...
    @staticmethod
    def getProgressType():
        ...
    def getEfficiency(self):
        ...
    def setEfficiency(self, value):
        ...
    @staticmethod
    def getEfficiencyType():
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
