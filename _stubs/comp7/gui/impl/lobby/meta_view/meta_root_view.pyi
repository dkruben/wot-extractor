# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/meta_root_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from shared_utils import findFirst as findFirst
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.game_control.comp7_shop_controller import ShopControllerStatus as ShopControllerStatus
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.root_view_model import RootViewModel as RootViewModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.tab_model import TabModel as TabModel
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as SeasonState
from comp7.gui.impl.gen.view_models.views.lobby.year_model import YearState as YearState
from comp7.gui.impl.lobby.comp7_helpers.comp7_lobby_sounds import getComp7MetaSoundSpace as getComp7MetaSoundSpace, playComp7MetaViewTabSound as playComp7MetaViewTabSound
from comp7.gui.impl.lobby.meta_view.pages.leaderboard_page import LeaderboardPage as LeaderboardPage
from comp7.gui.impl.lobby.meta_view.pages.progression_page import ProgressionPage as ProgressionPage
from comp7.gui.impl.lobby.meta_view.pages.rank_rewards_page import RankRewardsPage as RankRewardsPage
from comp7.gui.impl.lobby.meta_view.pages.shop_page import ShopPage as ShopPage
from comp7.gui.impl.lobby.meta_view.pages.weekly_quests_page import WeeklyQuestsPage as WeeklyQuestsPage
from comp7.gui.impl.lobby.meta_view.pages.yearly_rewards_page import YearlyRewardsPage as YearlyRewardsPage
from comp7.gui.impl.lobby.meta_view.pages.yearly_statistics_page import YearlyStatisticsPage as YearlyStatisticsPage
from comp7.gui.impl.lobby.meta_view.products_helper import hasUnseenProduct as hasUnseenProduct
from comp7.gui.selectable_reward.common import Comp7SelectableRewardManager as Comp7SelectableRewardManager
from comp7.gui.shared.event_dispatcher import showComp7AllRewardsSelectionWindow as showComp7AllRewardsSelectionWindow, showComp7MetaRootTab as showComp7MetaRootTab
from comp7.skeletons.gui.game_control import IComp7ShopController as IComp7ShopController
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver, visitor as visitor
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, ViewStatus as ViewStatus
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_tooltip import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from comp7.gui.impl.lobby.meta_view.pages import PageSubModelPresenter as PageSubModelPresenter
from comp7.gui.impl.lobby.hangar.meta_tab_state import IMetaTabState as IMetaTabState
from gui.offers import OffersDataProvider as OffersDataProvider
from gui.shared.events import NavigationEvent as NavigationEvent
from frameworks_common.state_machine import State as State
_logger: Any

class MetaRootView(ViewImpl, BaseStateObserver):
    __slots__: tuple
    __comp7Controller: Any
    __comp7ShopController: Any
    __guiLoader: Any
    __offersProvider: Any
    _COMMON_SOUND_SPACE: Any
    __pages: Any
    __tabId: Any
    __products: Any
    __onLoadingParams: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def tabId(self):
        ...
    def getPageById(self, tabId):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createContextMenu(self, event):
        ...
    def switchPage(self, tabId, **params):
        ...
    def updateTabNotifications(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def __currentPage(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onShopDataUpdated(self, status):
        ...
    def __onShopStateChanged(self):
        ...
    def __onScheduleUpdated(self):
        ...
    def __onStatusUpdated(self, _):
        ...
    def __onOfflineStatusUpdated(self):
        ...
    def __updateWeeklyQuestsClaimRewardsModel(self):
        ...
    def __initPages(self):
        ...
    def __clearPages(self):
        ...
    def __updateTabs(self):
        ...
    def __onClose(self):
        ...
    def __onViewStatusChanged(self, viewID, status):
        ...
    # decorador original: @args2params(...)
    def __onSideBarTabChanged(self, tabId):
        ...
