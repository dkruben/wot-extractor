# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/missions_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import namedtuple as namedtuple
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import Windowing as Windowing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import MISSIONS_PAGE as MISSIONS_PAGE
from adisp import adisp_async as adispasync, adisp_process as adisp_process
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES as BUTTON_LINKAGES
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.event_boards.event_helpers import checkEventExist as checkEventExist
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import HIDE_DONE as HIDE_DONE, HIDE_UNAVAILABLE as HIDE_UNAVAILABLE
from gui.Scaleform.daapi.view.lobby.missions.regular.sound_constants import TASKS_SOUND_SPACE as TASKS_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.user_missions import missions_group_packers as missions_group_packers
from gui.Scaleform.daapi.view.meta.MissionsListViewBaseMeta import MissionsListViewBaseMeta as MissionsListViewBaseMeta
from gui.Scaleform.daapi.view.meta.MissionsPageMeta import MissionsPageMeta as MissionsPageMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import ListDAAPIDataProvider as ListDAAPIDataProvider
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.marathon.marathon_event_controller import getMarathons as getMarathons
from gui.server_events import caches as caches, settings as settings
from gui.server_events.events_dispatcher import hideMissionDetails as hideMissionDetails, showMissionDetails as showMissionDetails
from gui.server_events.events_helpers import isBattleMattersQuestID as isBattleMattersQuestID
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.events import MissionsEvent as MissionsEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.sounds.ambients import BattleMattersSoundEnv as BattleMattersSoundEnv, LobbySubViewEnv as LobbySubViewEnv, MarathonPageSoundEnv as MarathonPageSoundEnv, MissionsCategoriesSoundEnv as MissionsCategoriesSoundEnv, MissionsEventsSoundEnv as MissionsEventsSoundEnv, MissionsPremiumSoundEnv as MissionsPremiumSoundEnv
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from items import getTypeOfCompactDescr as getTypeOfCompactDescr
from skeletons.gui.app_loader import GuiGlobalSpaceID as GuiGlobalSpaceID, IAppLoader as IAppLoader
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IHangarSpaceSwitchController as IHangarSpaceSwitchController, ILimitedUIController as ILimitedUIController, ILiveOpsWebEventsController as ILiveOpsWebEventsController, IMapboxController as IMapboxController, IMarathonEventsController as IMarathonEventsController, IRankedBattlesController as IRankedBattlesController, IWinbackController as IWinbackController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from wg_async import wg_async as wg_async, wg_await as wg_await
from typing import List as List, Union as Union
from gui.server_events.event_items import DailyEpicTokenQuest as DailyEpicTokenQuest, DailyQuest as DailyQuest, PremiumQuest as PremiumQuest
TabData: Any
TABS_DATA_ORDERED: list
MARATHONS_START_TAB_INDEX = 1
NON_FLASH_TABS: tuple
TABS_WITHOUT_COMMON_MUSIC: tuple

class MissionsPage(LobbySubView, MissionsPageMeta):
    _COMMON_SOUND_SPACE = TASKS_SOUND_SPACE
    __sound_env__ = LobbySubViewEnv
    __VOICED_TABS: dict
    eventsCache: Any
    lobbyContext: Any
    eventsController: Any
    marathonsCtrl: Any
    __liveOpsWebEventsController: Any
    __mapboxCtrl: Any
    __battleMattersController: Any
    __limitedUIController: Any
    __winbackController: Any
    __filterData: Any
    _eventID: Any
    _groupID: Any
    __marathonPrefix: Any
    __needToScroll: Any
    _showMissionDetails: Any
    __builders: Any
    __currentTabAlias: Any
    __subTab: Any
    __ctx: Any
    __soundSpace: Any
    def __init__(self, ctx):
        ...
    def onTabSelected(self, alias, prefix):
        ...
    def getCurrentTabAlias(self):
        ...
    def getFilterData(self):
        ...
    def onClose(self):
        ...
    def resetFilters(self):
        ...
    @property
    def currentTab(self):
        ...
    def getDynamicSoundEnv(self):
        ...
    def _populate(self):
        ...
    def _invalidate(self, ctx=None):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _initialize(self, ctx=None):
        ...
    def __onPrimeTimeStatusUpdated(self, *_):
        ...
    def __eventStatusUpdated(self, resetCurrentTab=True):
        ...
    def __fireTabChangedEvent(self):
        ...
    def __handleMissionsPageClose(self, _):
        ...
    def __showMarathonReward(self, isAccessible, prefix):
        ...
    def __onMarathonVehicleReceived(self, prefix):
        ...
    def __onWindowAccessibilityChanged(self, isAccessible):
        ...
    def __pageInvalidate(self, _):
        ...
    def __scrollToGroup(self):
        ...
    def __onPageUpdate(self, *args):
        ...
    def __onEventsVisited(self, counters=None):
        ...
    def __updateFilterLabel(self):
        ...
    def __onFilterChanged(self, event):
        ...
    def __onFilterClosed(self, event):
        ...
    def __updateLiveOpsWebEventsTab(self, *_):
        ...
    def __changeSoundSpace(self):
        ...
    def __updateHeader(self, updateTabsDataProvider=True):
        ...
    def __getHeaderTabData(self, tabData):
        ...
    def __battleMattersTabIsEnabled(self):
        ...
    @staticmethod
    def __getSuitableEvents(tab):
        ...
    def __elenHasDisplayableEvents(self):
        ...
    def __filterApplied(self):
        ...
    def __tryOpenMissionDetails(self):
        ...
    def __showFilter(self):
        ...

class MissionViewBase(MissionsListViewBaseMeta):
    _filterData: Any
    _builder: Any
    _questsDP: Any
    __updateDataCallback: Any
    _totalQuestsCount: Any
    _filteredQuestsCount: Any
    _eventID: Any
    def __init__(self):
        ...
    def setBuilder(self, builder, filterData, eventID):
        ...
    def getTotalQuestsCount(self):
        ...
    def getCurrentQuestsCount(self):
        ...
    def getSuitableEvents(self):
        ...
    def setActive(self, isActive):
        ...
    def markVisited(self):
        ...
    def _onEventsUpdate(self, *args):
        ...
    def setFilters(self, filterData):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    @staticmethod
    def _getBackground():
        ...
    def _onDataChangedNotify(self):
        ...
    def __notifyDataChanged(self):
        ...

class MissionView(MissionViewBase):
    __sound_env__ = LobbySubViewEnv
    eventsCache: Any
    __battleMattersController: Any
    gameSession: Any
    __rankedController: Any
    __spaceSwitchController: Any
    __viewQuests: Any
    _totalQuestsCount: Any
    _filteredQuestsCount: Any
    _filterData: Any
    def __init__(self):
        ...
    def openMissionDetailsView(self, eventID, blockID):
        ...
    def setFilters(self, filterData):
        ...
    def dummyClicked(self, clickType):
        ...
    def markVisited(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _filterMissions(self):
        ...
    def _appendBlockDataToResult(self, result, data):
        ...
    def _getQuestTotalCountFromBlockData(self, data):
        ...
    def _getQuestFilteredCountFromBlockData(self, data):
        ...
    @staticmethod
    def _getDummy():
        ...
    # decorador original: @wg_async
    def _onEventsUpdate(self, *args):
        ...
    def _onBattleMattersStateChanged(self, *args):
        ...
    def __onUnlocksUpdate(self, unlocks):
        ...
    def __updateEvents(self):
        ...
    def __filter(self, event):
        ...
    def _getViewQuestFilter(self):
        ...
    def __onPremiumTypeChanged(self, newAcctType):
        ...

class ElenMissionView(MissionViewBase):
    eventsController: Any
    _totalQuestsCount: Any
    _filteredQuestsCount: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def onInventoryUpdate(self, _):
        ...
    # decorador original: @checkEventExist
    def openMissionDetailsView(self, eventID, blockID):
        ...
    # decorador original: @adisp_process
    def _onEventsUpdate(self, *args):
        ...
    # decorador original: @adispasync
    # decorador original: @adisp_process
    def _onEventsUpdateAsync(self, callback, *args):
        ...
    def _setMaintenance(self, visible):
        ...
    def __updateEvents(self, eventsData, playerData, myEventsTop):
        ...

class _GroupedQuestsProvider(ListDAAPIDataProvider):
    __list: Any
    def __init__(self):
        ...
    @property
    def collection(self):
        ...
    def fini(self):
        ...
    def buildList(self, dpList):
        ...
    def emptyItem(self):
        ...
    def getItemIndexHandler(self, fieldName, value):
        ...
    def clear(self):
        ...

def setHideDoneFilter():
    ...
