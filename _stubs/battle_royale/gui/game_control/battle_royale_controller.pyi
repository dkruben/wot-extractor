# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/battle_royale_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import lzip as lzip, viewitems as viewitems
from itertools import groupby as groupby
import BigWorld as BigWorld
import BattleReplay as BattleReplay
import Event as Event
import season_common as season_common
from adisp import adisp_process as adisp_process
from shared_utils import first as first, makeTupleByDict as makeTupleByDict, nextTick as nextTick
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ROYALE_VEHICLE as ROYALE_VEHICLE, CURRENT_VEHICLE as CURRENT_VEHICLE, ROYALE_INTRO_VIDEO_SHOWN_FOR_SEASON as ROYALE_INTRO_VIDEO_SHOWN_FOR_SEASON
from battle_royale.gui.constants import AmmoTypes as AmmoTypes, BattleRoyalePerfProblems as BattleRoyalePerfProblems, BattleRoyaleSubMode as BattleRoyaleSubMode, BattleRoyaleModeState as BattleRoyaleModeState
from battle_royale.gui.constants import BR_COIN as BR_COIN
from battle_royale.gui.constants import STP_COIN as STP_COIN
from battle_royale.gui.constants import SUB_MODE_ID_KEY as SUB_MODE_ID_KEY
from battle_royale.gui.game_control.br_vo_controller import BRVoiceOverController as BRVoiceOverController
from battle_royale.gui.royale_models import BattleRoyaleSeason as BattleRoyaleSeason
from battle_royale.gui.shared.event_dispatcher import showInfoPage as showInfoPage
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from constants import QUEUE_TYPE as QUEUE_TYPE, Configs as Configs, PREBATTLE_TYPE as PREBATTLE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, BATTLE_ROYALE_SCENE as BATTLE_ROYALE_SCENE
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.ClientHangarSpace import SERVER_CMD_CHANGE_HANGAR as SERVER_CMD_CHANGE_HANGAR, SERVER_CMD_CHANGE_HANGAR_PREM as SERVER_CMD_CHANGE_HANGAR_PREM
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS
from gui.game_control.season_provider import SeasonProvider as SeasonProvider
from gui.impl.gen import R as R
from gui.periodic_battles.models import PeriodType as PeriodType
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction, LeavePrbAction as LeavePrbAction
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from gui.server_events.events_constants import BATTLE_ROYALE_GROUPS_ID as BATTLE_ROYALE_GROUPS_ID
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import getParentWindow as getParentWindow, showBrowserOverlayView as showBrowserOverlayView
from gui.shared.events import ProfilePageEvent as ProfilePageEvent, ProfileStatisticEvent as ProfileStatisticEvent, ProfileTechniqueEvent as ProfileTechniqueEvent
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS, VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES
from gui.shared.items_parameters.shell_params import ShellParams as ShellParams
from gui.shared.money import DynamicMoney as DynamicMoney
from gui.shared.utils import SelectorBattleTypesUtils as SelectorBattleTypesUtils
from gui.shared.utils.graphics import getGraphicsEngineValue as getGraphicsEngineValue
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier, PeriodicNotifier as PeriodicNotifier, TimerNotifier as TimerNotifier
from helpers import dependency as dependency, time_utils as time_utils
from helpers.server_settings import BattleRoyaleConfig as BattleRoyaleConfig
from helpers.statistics import HARDWARE_SCORE_PARAMS as HARDWARE_SCORE_PARAMS
from items import vehicles as vehicles
from items.battle_royale import isBattleRoyale as isBattleRoyale
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IEventsNotificationsController as IEventsNotificationsController, IHangarSpaceSwitchController as IHangarSpaceSwitchController, IBattleRoyaleController as IBattleRoyaleController, IBattleRoyaleTournamentController as IBattleRoyaleTournamentController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from stats_params import BATTLE_ROYALE_STATS_ENABLED as BATTLE_ROYALE_STATS_ENABLED
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill
_logger: Any
BattleRoyaleProgressionPoints: Any
PERFORMANCE_GROUP_LIMITS: dict
_PERIOD_INFO_TO_MOD_STATE: dict

class BATTLE_ROYALE_GAME_LIMIT_TYPE(object):
    SYSTEM_DATA = 0
    HARDWARE_PARAMS = 1

class BattleRoyaleController(Notifiable, SeasonProvider, IBattleRoyaleController, IPrbListener):
    __lobbyContext: Any
    __eventsCache: Any
    __itemsCache: Any
    __hangarsSpace: Any
    __spaceSwitchController: Any
    __notificationsCtrl: Any
    __sessionProvider: Any
    __battleRoyaleTournamentController: Any
    __brProgression: Any
    TOKEN_QUEST_ID = 'token:br:title:'
    MAX_STORED_ARENAS_RESULTS = 20
    __em: Any
    onUpdated: Any
    onPrimeTimeStatusUpdated: Any
    onWidgetUpdate: Any
    onBalanceUpdated: Any
    onSubModeUpdated: Any
    onStatusTick: Any
    onTournamentBannerStateChanged: Any
    onEntryPointUpdated: Any
    __balance: Any
    __clientValuesInited: Any
    __clientShields: Any
    __performanceGroup: Any
    __serverSettings: Any
    __battleRoyaleSettings: Any
    __equipmentCount: Any
    __isBRLogicEnabled: Any
    __voControl: Any
    __defaultHangars: Any
    __isNeedToUpdateHeroTank: Any
    __profStatSelectBattlesTypeInited: Any
    __profTechSelectBattlesTypeInited: Any
    __callbackID: Any
    __isTournamentBannerEnabled: Any
    __currentSubModeID: Any
    __divisions: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    def getBRCoinBalance(self):
        ...
    def getSTPCoinBalance(self):
        ...
    def hasDailyBonus(self, vehicle):
        ...
    def getStpCoinsPerPlace(self, place):
        ...
    def __initBalanceCurrencies(self):
        ...
    def __updateBalanceCurrencies(self):
        ...
    def __updateDynamicCurrencies(self, currencies):
        ...
    def __onEventNotification(self, added, removed=...):
        ...
    def onDisconnected(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def getCurrentSubModeID(self):
        ...
    def setCurrentSubModeID(self, subModeID, updateNeeded=True):
        ...
    def selectSubModeBattle(self, selectedSubModeID, **kwargs):
        ...
    def getModeSettings(self):
        ...
    def isEnabled(self):
        ...
    def isStPatrick(self):
        ...
    def getEndTime(self):
        ...
    def getStartTime(self):
        ...
    def getTimeLeftTillCycleEnd(self):
        ...
    def getPerformanceGroup(self):
        ...
    def getVehicleShells(self, vehicleName):
        ...
    def getVehicleEquipment(self, vehicleName):
        ...
    @staticmethod
    def getBrCommanderSkills():
        ...
    def isActive(self):
        ...
    def isBattleRoyaleMode(self):
        ...
    def getModeState(self):
        ...
    def __isBattleRoyaleMode(self, state):
        ...
    def __isBattleRoyaleTournamentMode(self, state):
        ...
    def isBattlePassAvailable(self, bonusType):
        ...
    def isInBattleRoyaleSquad(self):
        ...
    def isInRandomSquadSubMode(self):
        ...
    def selectRoyaleBattle(self):
        ...
    def openInfoPageWindow(self, isModeSelector=False):
        ...
    def setDefaultHangarEntryPoint(self):
        ...
    def isGeneralHangarEntryPoint(self):
        ...
    def selectRandomBattle(self):
        ...
    def getPlayerLevelInfo(self):
        ...
    def getStats(self):
        ...
    @staticmethod
    # decorador original: @dependency.replace_none_kwargs(...)
    def showIntroWindow(ctx=None, parent=None, guiLoader=None):
        ...
    def getQuests(self):
        ...
    def isDailyQuestsRefreshAvailable(self):
        ...
    def showIntroVideo(self, alias, force=False):
        ...
    def getProgressionPointsTableData(self):
        ...
    def getTournamentBannerData(self):
        ...
    @property
    def isTournamentBannerEnabled(self):
        ...
    def __getIntroVideoURL(self):
        ...
    def __progressionPointsConfig(self):
        ...
    def __getProgressionPointsPerPlace(self, gameMode=...):
        ...
    def __selectRoyaleBattle(self, extData=None, **kwargs):
        ...
    def __selectBattleRoyaleTournament(self):
        ...
    def __serverSettingsChangeBrowserHandler(self, browser, diff):
        ...
    def _createSeason(self, cycleInfo, seasonData):
        ...
    def __eventAvailabilityUpdate(self, *_):
        ...
    def __onCheckSceneChange(self):
        ...
    def __enableRoyaleMode(self):
        ...
    def __disableRoyaleMode(self):
        ...
    # decorador original: @adisp_process
    def __doSelectBattleRoyaleTournamentPrb(self, dispatcher):
        ...
    # decorador original: @adisp_process
    def __doSelectBattleRoyalePrb(self, dispatcher, isSquad=False, extData=None, accountsToInvite=None, **kwargs):
        ...
    # decorador original: @adisp_process
    def __doSelectRandomPrb(self, dispatcher):
        ...
    # decorador original: @adisp_process
    def fightClick(self):
        ...
    # decorador original: @adisp_process
    def _doLeaveBattleRoyalePrb(self, dispatcher):
        ...
    def __getBattleRoyaleSettings(self):
        ...
    def __getCachedSettings(self):
        ...
    def __timerUpdate(self):
        ...
    def __timerTick(self):
        ...
    def __timerNotifier(self):
        ...
    def __resetTimer(self):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __updateRoyaleSettings(self, diff):
        ...
    def __onChangeProfileAlias(self, event):
        ...
    def __onProfileStatisticSelectBattlesType(self, event):
        ...
    def __onProfileStatisticDispose(self, event):
        ...
    def __onProfileTechniqueSelectBattlesType(self, event):
        ...
    def __onProfileTechniqueDispose(self, event):
        ...
    # decorador original: @adisp_process
    def __onSelectVehicleInHangar(self, event):
        ...
    def __clear(self):
        ...
    def __clearClientValues(self):
        ...
    def __updateRoyale(self, _):
        ...
    def __analyzeClientSystem(self):
        ...
    def __updateEquipmentCount(self):
        ...
    def __onVehicleChanged(self):
        ...
    def __tokenIsValid(self, quest):
        ...
    def __updateTournamentBannerState(self):
        ...
    def __getTournamentBannerAvailability(self):
        ...
    def __getTournamentBannerTimerDelta(self):
        ...
