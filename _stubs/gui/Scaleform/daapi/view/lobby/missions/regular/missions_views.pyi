# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/missions_views.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from wg_async import wg_async as wg_async, wg_await as wg_await
from constants import PremiumConfigs as PremiumConfigs
from debug_utils import LOG_ERROR as LOG_ERROR
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES as BUTTON_LINKAGES
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_maintenance import EventBoardsMaintenance as EventBoardsMaintenance
from gui.Scaleform.daapi.view.lobby.event_boards.event_helpers import checkEventExist as checkEventExist
from gui.Scaleform.daapi.view.meta.CurrentVehicleMissionsViewMeta import CurrentVehicleMissionsViewMeta as CurrentVehicleMissionsViewMeta
from gui.Scaleform.daapi.view.meta.MissionsEventBoardsViewMeta import MissionsEventBoardsViewMeta as MissionsEventBoardsViewMeta
from gui.Scaleform.daapi.view.meta.MissionsGroupedViewMeta import MissionsGroupedViewMeta as MissionsGroupedViewMeta
from gui.Scaleform.daapi.view.meta.MissionsMarathonViewMeta import MissionsMarathonViewMeta as MissionsMarathonViewMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES as EVENTBOARDS_ALIASES
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.event_boards.settings import expandGroup as expandGroup, isGroupMinimized as isGroupMinimized
from gui.server_events import settings as settings, caches as caches
from gui.server_events.events_dispatcher import hideMissionDetails as hideMissionDetails
from gui.server_events.events_dispatcher import showMissionsCategories as showMissionsCategories
from gui.server_events.events_helpers import isMarathon as isMarathon, isDailyQuest as isDailyQuest, isPremium as isPremium
from gui.shared import actions as actions
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.events import LoadViewEvent as LoadViewEvent
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showTankPremiumAboutPage as showTankPremiumAboutPage, showHangar as showHangar
from gui.shared.formatters import text_styles as text_styles, icons as icons
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IReloginController as IReloginController, IMarathonEventsController as IMarathonEventsController, IBrowserController as IBrowserController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R

class _GroupedMissionsView(MissionsGroupedViewMeta):
    def clickActionBtn(self, actionID):
        ...
    def expand(self, gID, value):
        ...

class MissionsGroupedView(_GroupedMissionsView):
    def dummyClicked(self, clickType):
        ...
    @staticmethod
    def _getBackground():
        ...
    @staticmethod
    def _getDummy():
        ...
    def _getViewQuestFilter(self):
        ...

class MissionsMarathonView(MissionsMarathonViewMeta):
    _browserCtrl: Any
    _marathonsCtrl: Any
    eventsCache: Any
    __browserID: Any
    _marathonEvent: Any
    _width: Any
    _height: Any
    _builder: Any
    __loadBrowserCallbackID: Any
    __browserView: Any
    __viewActive: Any
    def __init__(self):
        ...
    def closeView(self):
        ...
    def getSuitableEvents(self):
        ...
    # decorador original: @adisp_process
    def reload(self):
        ...
    def setActive(self, isActive):
        ...
    def setBuilder(self, builder, filterData, eventID):
        ...
    def setMarathon(self, prefix):
        ...
    def viewSize(self, width, height):
        ...
    def markVisited(self):
        ...
    # decorador original: @adisp_process
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    # decorador original: @wg_async
    def _onEventsUpdate(self, *args):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __cancelLoadBrowserCallback(self):
        ...
    def __loadBrowser(self):
        ...
    def __updateEvents(self):
        ...
    def __updateBrowserProperties(self, *args):
        ...

class MissionsEventBoardsView(MissionsEventBoardsViewMeta):
    __eventsData: Any
    __tableView: Any
    __maintenance: Any
    def __init__(self):
        ...
    # decorador original: @checkEventExist
    def orderClick(self, eventID):
        ...
    # decorador original: @checkEventExist
    def techniqueClick(self, eventID):
        ...
    # decorador original: @checkEventExist
    def awardClick(self, eventID):
        ...
    # decorador original: @adisp_process
    def serverClick(self, eventID, server):
        ...
    # decorador original: @checkEventExist
    # decorador original: @adisp_process
    def registrationClick(self, eventID):
        ...
    # decorador original: @checkEventExist
    # decorador original: @adisp_process
    def participateClick(self, eventID):
        ...
    # decorador original: @checkEventExist
    def expand(self, gID, value):
        ...
    def onRefresh(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _invalidate(self, *args, **kwargs):
        ...
    @staticmethod
    def _getBackground():
        ...
    def _setMaintenance(self, visible):
        ...
    # decorador original: @checkEventExist
    def __onFilterApply(self, eventID, leaderboardsID):
        ...
    def __onViewLoaded(self, view, *args, **kwargs):
        ...
    # decorador original: @adisp_process
    def __tableViewDisposed(self, view):
        ...
    def __openDetailsContainer(self, viewAlias, ctx=None):
        ...

class MissionsCategoriesView(_GroupedMissionsView):
    _lobbyContext: Any
    __showDQInMissionsTab = False
    @classmethod
    def setShowDQInMissionsTab(cls, value):
        ...
    @staticmethod
    def getViewQuestFilter():
        ...
    @staticmethod
    def getViewQuestFilterIncludingDailyQuests():
        ...
    def onClickButtonDetails(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    @staticmethod
    def _getBackground():
        ...
    def _getViewQuestFilter(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...

class CurrentVehicleMissionsView(CurrentVehicleMissionsViewMeta):
    def setBuilder(self, builder, filterData, eventID):
        ...
    @staticmethod
    def _getBackground():
        ...
    def _dispose(self):
        ...
    def __onBlocksDataChanged(self):
        ...
