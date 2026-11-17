# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_table_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl import backport as backport
from helpers import dependency as dependency
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from helpers.i18n import makeString as _ms
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_maintenance import EventBoardsMaintenance as EventBoardsMaintenance
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_award_group import EventBoardsAwardGroup as EventBoardsAwardGroup
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_pagination import EventBoardsPagination as EventBoardsPagination
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_vos import makeTableViewHeaderVO as makeTableViewHeaderVO, makeEventBoardsTableDataVO as makeEventBoardsTableDataVO, makeEventBoardsTableViewStatusVO as makeEventBoardsTableViewStatusVO, makeTableHeaderVO as makeTableHeaderVO, makeTableViewBackgroundVO as makeTableViewBackgroundVO, makeCantJoinReasonTextVO as makeCantJoinReasonTextVO, makeAwardGroupDataTooltipVO as makeAwardGroupDataTooltipVO, makeParameterTooltipVO as makeParameterTooltipVO
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import getStatusTitleStyle as getStatusTitleStyle, getStatusCountStyle as getStatusCountStyle, formatUpdateTime as formatUpdateTime, formatErrorTextWithIcon as formatErrorTextWithIcon, getFullName as getFullName
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES as EVENTBOARDS_ALIASES
from gui.Scaleform.daapi.view.meta.EventBoardsTableViewMeta import EventBoardsTableViewMeta as EventBoardsTableViewMeta
from gui.event_boards.event_boards_items import EVENT_STATE as _es, EventSettings as EventSettings, LeaderBoard as LeaderBoard, PLAYER_STATE_REASON as _psr
MyInfo: Any
LeaderboardData: Any

class EventBoardsTableView(LobbySubView, EventBoardsTableViewMeta):
    eventsController: Any
    itemsCache: Any
    MIN_CATEGORY = 1
    MAX_CATEGORY = 5
    TOP_POSITION_RANK = -1
    MY_RANK = -2
    MAX_AWARD_GROUPS = 4
    __pagination: Any
    __awardGroup: Any
    __maintenance: Any
    __eventID: Any
    __leaderboardID: Any
    __maintenanceVisible: Any
    __eventData: Any
    __myInfo: Any
    __leaderboard: Any
    __leaderboardData: Any
    __rewardCategories: Any
    __stripes: Any
    __playerState: Any
    __top: Any
    __playerData: Any
    __method: Any
    def __init__(self, ctx):
        ...
    def getEventID(self):
        ...
    def changeLeaderboard(self, leaderboardID):
        ...
    def closeView(self):
        ...
    @property
    def eventData(self):
        ...
    @property
    def leaderboardID(self):
        ...
    def onStepPage(self, direction):
        ...
    def onShowRewardCategory(self, categoryID):
        ...
    def onRefresh(self):
        ...
    def setMyPlace(self):
        ...
    def showNextAward(self, visible):
        ...
    def playerClick(self, playerID):
        ...
    # decorador original: @adisp_process
    def participateStatusClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __cleanUp(self):
        ...
    def __setMaintenance(self, visible):
        ...
    def __setWaiting(self, visible):
        ...
    def __updateStatus(self):
        ...
    def __calculateRewardCategories(self, rewardGroups, leaderboardViewSize):
        ...
    def __updateRewardCategoriesPlayers(self, rewardCategories, rewards, excelItems):
        ...
    def __setPlayerData(self):
        ...
    def __fetchEventData(self):
        ...
    # decorador original: @adisp_process
    def __fetchLeaderboardPageData(self, page, rank):
        ...
    # decorador original: @adisp_process
    def __fetchMyLeaderboardInfo(self, onSuccess):
        ...
    def __moveToMyPlace(self):
        ...
    def __onViewLoaded(self, view, *args, **kwargs):
        ...
    def __updateHeader(self):
        ...
    def __updatePage(self):
        ...
    def __scrollToRank(self, rank):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def __getMyPosition(self, connectionMgr=None):
        ...
    def __getPositionByRank(self, rank):
        ...
    def __getCategoryByRank(self, rank):
        ...
