# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/root_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from frameworks.wulf import ViewModel as ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.claim_rewards_model import ClaimRewardsModel as ClaimRewardsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.leaderboard_model import LeaderboardModel as LeaderboardModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.progression_model import ProgressionModel as ProgressionModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.rank_rewards_model import RankRewardsModel as RankRewardsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.shop_model import ShopModel as ShopModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.weekly_quests_model import WeeklyQuestsModel as WeeklyQuestsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.yearly_rewards_model import YearlyRewardsModel as YearlyRewardsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.yearly_statistics_model import YearlyStatisticsModel as YearlyStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.sidebar_model import SidebarModel as SidebarModel
from comp7.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel as ScheduleInfoModel

class RootViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=11, commands=1):
        ...
    @property
    def sidebar(self):
        ...
    @staticmethod
    def getSidebarType():
        ...
    @property
    def scheduleInfo(self):
        ...
    @staticmethod
    def getScheduleInfoType():
        ...
    @property
    def progressionModel(self):
        ...
    @staticmethod
    def getProgressionModelType():
        ...
    @property
    def rankRewardsModel(self):
        ...
    @staticmethod
    def getRankRewardsModelType():
        ...
    @property
    def weeklyQuestsModel(self):
        ...
    @staticmethod
    def getWeeklyQuestsModelType():
        ...
    @property
    def leaderboardModel(self):
        ...
    @staticmethod
    def getLeaderboardModelType():
        ...
    @property
    def yearlyRewardsModel(self):
        ...
    @staticmethod
    def getYearlyRewardsModelType():
        ...
    @property
    def shopModel(self):
        ...
    @staticmethod
    def getShopModelType():
        ...
    @property
    def yearlyStatisticsModel(self):
        ...
    @staticmethod
    def getYearlyStatisticsModelType():
        ...
    @property
    def claimRewardsModel(self):
        ...
    @staticmethod
    def getClaimRewardsModelType():
        ...
    def getPageViewId(self):
        ...
    def setPageViewId(self, value):
        ...
    def _initialize(self):
        ...
