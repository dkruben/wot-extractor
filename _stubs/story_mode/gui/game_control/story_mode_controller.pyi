# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/game_control/story_mode_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from logging import getLogger as getLogger
import AccountCommands as AccountCommands
import BigWorld as BigWorld
import Event as Event
import WWISE as WWISE
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSyncData as AccountSyncData
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from adisp import adisp_process as adisp_process
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, QUEUE_TYPE as QUEUE_TYPE
from frameworks.wulf import WindowLayer as WindowLayer
from gui import app_loader as app_loader
from gui.Scaleform.framework.view_overrider import OverrideData as OverrideData
from gui.battle_results import RequestResultsContext as RequestResultsContext
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.impl.gen import R as R
from gui.prb_control import prbEntityProperty as prbEntityProperty, prbDispatcherProperty as prbDispatcherProperty
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar, isPlayerAccount as isPlayerAccount
from helpers.server_settings import ServerSettings as ServerSettings
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.web import IWebController as IWebController
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from skeletons.ui_logging import IUILoggingCore as IUILoggingCore
from skeletons.gui.shared import IItemsCache as IItemsCache
from story_mode.account_settings import isNewbieAdvertisingScreenSeen as isNewbieAdvertisingScreenSeen, getMissionNewSeenId as getMissionNewSeenId, setMissionNewSeenId as setMissionNewSeenId
from story_mode.gui.battle_control.arena_info.player_format import StoryModeNameFormatter as StoryModeNameFormatter
from story_mode.gui.fade_in_out import UseStoryModeFading as UseStoryModeFading
from story_mode.gui.shared.event_dispatcher import showNewbieAdvertisingWindow as showNewbieAdvertisingWindow
from story_mode.gui.story_mode_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, VIEW_ALIAS as VIEW_ALIAS, INFO_PAGE_STORY_MODE as INFO_PAGE_STORY_MODE, INFO_PAGE_STORY_MODE_EVENT as INFO_PAGE_STORY_MODE_EVENT
from story_mode.gui.sound_constants import SOUND_REMAPPING as SOUND_REMAPPING, GAMEMODE_GROUP as GAMEMODE_GROUP, GAMEMODE_DEFAULT as GAMEMODE_DEFAULT
from story_mode.configs.sm_client_settings import getClientSettings as getClientSettings
from story_mode.gui.game_control.sounds_controller import SoundsController as SoundsController
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode_common.configs.story_mode_missions import missionsSchema as missionsSchema, MissionsModel as MissionsModel, MissionModel as MissionModel
from story_mode_common.configs.story_mode_settings import settingsSchema as settingsSchema, SettingsModel as SettingsModel
from story_mode_common.helpers import isMissionCompleted as isMissionCompleted, isTaskCompleted as isTaskCompleted, isMissionDisabledByABGroup as isMissionDisabledByABGroup
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME, SM_CONGRATULATIONS_MESSAGE as SM_CONGRATULATIONS_MESSAGE, STORY_MODE_BONUS_TYPES as STORY_MODE_BONUS_TYPES, MissionId as MissionId, STORY_MODE_PDATA_KEY as STORY_MODE_PDATA_KEY, PROGRESS_PDATA_KEY as PROGRESS_PDATA_KEY, MissionType as MissionType, STORY_MODE_AB_FEATURE as STORY_MODE_AB_FEATURE, EventMissionSelector as EventMissionSelector
from uilogging.performance.battle.loggers import BattleMetricsLogger as BattleMetricsLogger
from messenger.proto.bw.wrappers import ServiceChannelMessage as ServiceChannelMessage
from gui.Scaleform.battle_entry import BattleEntry as BattleEntry
from story_mode.configs.sm_client_settings import ClientSettingsModel as ClientSettingsModel
_logger: Any

class StoryModeOverrideData(OverrideData):
    _storyModeCtrl: Any
    def checkCondition(self, *args, **kwargs):
        ...

class StoryModeController(IStoryModeController, IGlobalListener):
    _lobbyContext: Any
    _sessionProvider: Any
    _appLoader: Any
    _battleResults: Any
    _itemsCache: Any
    _webController: Any
    _uiLoggerCore: Any
    _statsCollector: Any
    _settingsCore: Any
    __selectedMissionId: Any
    __selectRandomBattle: Any
    __isOnboarding: Any
    __needToShowAwardData: Any
    __syncData: Any
    __isQuittingBattle: Any
    __isNameFormatterSubstituted: Any
    __missionsProgressDiff: Any
    __soundController: Any
    _delayedBattleResultsID: Any
    __pendingLastArenaUniqueId: Any
    __isWaitingLobbyInit: Any
    _eventMissionSelectorMap: Any
    onSyncDataUpdated: Any
    onMissionsConfigUpdated: Any
    onSettingsUpdated: Any
    def __init__(self):
        ...
    @property
    def isOnboarding(self):
        ...
    @property
    def isQuittingBattle(self):
        ...
    @property
    def selectedMissionId(self):
        ...
    @property
    def isSelectedMissionOnboarding(self):
        ...
    @selectedMissionId.setter
    def selectedMissionId(self, value):
        ...
    @property
    def settings(self):
        ...
    @property
    def missions(self):
        ...
    @property
    def needToShowAward(self):
        ...
    @property
    def storyModeInfoPageKey(self):
        ...
    @property
    def newMissionIdForNewbies(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def isEventEntryPointVisible(self):
        ...
    def isShowActiveModeState(self):
        ...
    def isEnabled(self):
        ...
    def isInPrb(self):
        ...
    # decorador original: @adisp_process
    def switchPrb(self):
        ...
    def popMissionProgressDiff(self, missionId):
        ...
    def isMissionCompleted(self, missionId):
        ...
    def isEventMissionSuitable(self, mission):
        ...
    def isFirstTaskNotCompleted(self, mission):
        ...
    def isAnyTaskNotCompleted(self, mission):
        ...
    def isSelectedMissionLocked(self):
        ...
    def isMissionTaskCompleted(self, missionId, taskId):
        ...
    def filterMissions(self, missionType=None):
        ...
    def isNewbieGuidanceNeeded(self):
        ...
    def isNewNeededForNewbies(self):
        ...
    def setNewForNewbiesSeen(self):
        ...
    def isMissionLocked(self, mission):
        ...
    def getFirstMission(self):
        ...
    def getNextMission(self, missionId):
        ...
    def quitBattle(self):
        ...
    def goToQueue(self):
        ...
    def exitQueue(self):
        ...
    @staticmethod
    def goToBattle():
        ...
    def goToHangar(self, guiCtx=None):
        ...
    def onOutroVideoComplete(self, arenaUniqueID):
        ...
    def popWaitingToBeShownAwardData(self):
        ...
    def startMusic(self):
        ...
    def stopMusic(self, forceStop=False):
        ...
    def startBattleMusic(self):
        ...
    def stopBattleMusic(self):
        ...
    def onLobbyInited(self, *_):
        ...
    def onPrbEntitySwitching(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    # decorador original: @adisp_process
    def onKickedFromQueue(self, queueType, *args):
        ...
    def chooseSelectedMissionId(self, isEvent=False):
        ...
    @property
    def _serverSettings(self):
        ...
    @property
    def _clientSettings(self):
        ...
    # decorador original: @adisp_process
    def _selectRandomMode(self):
        ...
    def _isMissionDisabledByABGroup(self, mission):
        ...
    def __onSelectVehicleInHangar(self, event):
        ...
    def __clear(self):
        ...
    def __onAvatarBecomeNonPlayer(self):
        ...
    def __configModelUpdateHandler(self, gpKey):
        ...
    def __onPrbDispatcherCreated(self):
        ...
    def __onAccountComponentsSynced(self, ctx, result):
        ...
    def __showBattleResults(self, lastArenaUniqueId):
        ...
    def __onLobbyAppInitialized(self, event):
        ...
    # decorador original: @adisp_process
    def __requestBattleResults(self, lastArenaUniqueId):
        ...
    def __onEnterPrb(self):
        ...
    def __onExitPrb(self):
        ...
    def __handleChatMessage(self, _, message):
        ...
    def __onClientUpdated(self, diff, *_):
        ...
    def __closeExcessiveWindows(self):
        ...
    # decorador original: @UseStoryModeFading(...)
    def __unsuccessfulSwitchHandler(self, *_):
        ...
    @property
    def __progress(self):
        ...
    def __chooseSelectedMissionsIds(self, missionType=..., precondition=..., condition=...):
        ...
    def __chooseLastUnlockedMissionIds(self):
        ...
    def __chooseNewbieSelectedMissionIds(self):
        ...
    def __chooseEventSelectedMissionIds(self):
        ...
    def __getNotCompletedMissions(self):
        ...
    def __getMissionsByBattleCount(self):
        ...
    def __getMissionsWithUnlockMission(self):
        ...
    def __assignSelectedMission(self):
        ...

def eventEntryPointValidator():
    ...
def newbieEntryPointValidator():
    ...
