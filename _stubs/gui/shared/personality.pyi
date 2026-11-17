# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/personality.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
from functools import partial as partial
import typing as typing
import weakref as weakref
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.account_validator import ValidationCodes as ValidationCodes, InventoryVehiclesValidator as InventoryVehiclesValidator, InventoryOutfitValidator as InventoryOutfitValidator, InventoryTankmenValidator as InventoryTankmenValidator
from adisp import adisp_process as adisp_process
import wg_async as future_async
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from gui import SystemMessages as SystemMessages, g_guiResetters as g_guiResetters
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.login.EULADispatcher import EULADispatcher as EULADispatcher
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.impl import backport as backport
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache as crewBooksViewedCache
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.items_parameters.params_cache import g_paramsCache as g_paramsCache
from gui.shared.utils import requesters as requesters
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper as UsersInfoHelper
from gui.wgnc import g_wgncProvider as g_wgncProvider
from helpers import isPlayerAccount as isPlayerAccount, time_utils as time_utils, dependency as dependency, uniprof as uniprof
from helpers.blueprint_generator import g_blueprintGenerator as g_blueprintGenerator
from helpers.statistics import HANGAR_LOADING_STATE as HANGAR_LOADING_STATE
from skeletons.account_helpers.settings_core import ISettingsCache as ISettingsCache, ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gameplay import IGameplayLogic as IGameplayLogic, PlayerEventID as PlayerEventID
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController
from skeletons.gui.game_control import IGameStateTracker as IGameStateTracker
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache, IBoostersStateProvider as IBoostersStateProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace, IRaresCache as IRaresCache
from skeletons.gui.sounds import ISoundsController as ISoundsController
from skeletons.gui.web import IWebController as IWebController
from skeletons.ui_logging import IUILoggingCore as IUILoggingCore
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from uilogging.mods_statistic.logger import ModsStatisticLogger as ModsStatisticLogger
from gui.goodies.booster_state_provider import BoosterStateProvider as BoosterStateProvider
from gui import mods as mods
_logger: Any
guiModsInit: Any
guiModsFini: Any
guiModsSendEvent: Any

class ServicesLocator(object):
    itemsCache: Any
    gameState: Any
    loginManager: Any
    eventsCache: Any
    soundCtrl: Any
    webCtrl: Any
    settingsCache: Any
    settingsCore: Any
    goodiesCache: Any
    boosterStateProvider: Any
    battleResults: Any
    lobbyContext: Any
    connectionMgr: Any
    statsCollector: Any
    eventsController: Any
    gameplay: Any
    hangarSpace: Any
    rareAchievesCache: Any
    appLoader: Any
    offersProvider: Any
    uiLoggingCore: Any
    @classmethod
    def clear(cls):
        ...
    @classmethod
    def onDisconnected(cls):
        ...

def onAccountShowGUI(ctx):
    ...
def onAccountBecomeNonPlayer():
    ...
def onServerReplayEntering():
    ...
def onServerReplayExiting():
    ...
# decorador original: @adisp_process
def onAvatarBecomePlayer():
    ...
def onAvatarBecomeNonPlayer():
    ...
def onAccountBecomePlayer():
    ...
# decorador original: @future_async.wg_async
def onClientUpdate(diff, updateOnlyLobbyCtx):
    ...
def onShopResyncStarted():
    ...
# decorador original: @future_async.wg_async
def onShopResync():
    ...
def onCenterIsLongDisconnected(isLongDisconnected):
    ...
def onIGRTypeChanged(roomType, xpFactor):
    ...
def onKickedFromServer(reason, kickReasonType, expiryTime):
    ...
def onScreenShotMade(path):
    ...
def init():
    ...
def fini():
    ...
def onConnected():
    ...
def onDisconnected():
    ...
def disableLobbyGUI():
    ...
def onRecreateDevice():
    ...
# decorador original: @future_async.wg_async
def __runComponentsSync(ctx, funcs):
    ...
# decorador original: @future_async.wg_async
def __runItemsCacheSync(_, callback=None):
    ...
# decorador original: @future_async.wg_async
def __runQuestSync(_, callback=None):
    ...
# decorador original: @adisp_process
def __runSettingsSync(_, callback=None):
    ...
# decorador original: @adisp_process
def __processEULA(_, callback=None):
    ...
# decorador original: @future_async.wg_async
def __processValidator(validator, callback):
    ...
def __validateInventoryVehicles(_, callback=None):
    ...
def __validateInventoryOutfit(_, callback=None):
    ...
def __validateInventoryTankmen(_, callback=None):
    ...
# decorador original: @future_async.wg_async
def __cacheVehicles(_, callback=None):
    ...
def __notifyOnSyncComplete(ctx, callback=None):
    ...
def __requestDossier(_, callback=None):
    ...
# decorador original: @future_async.wg_async
def __initializeHangarSpace(_, callback=None):
    ...
def __initializeHangar(ctx=None, callback=None):
    ...
# decorador original: @adisp_process
def __processWebCtrl(_, force=True, skipLogin=False, callback=None):
    ...
def __runUiLogging(_, ensureSession=False, callback=None):
    ...
# decorador original: @adisp_process
def __processElen(_, callback=None):
    ...
