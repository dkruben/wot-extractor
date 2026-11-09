# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/mapbox_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import random as random
from collections import namedtuple as namedtuple
from functools import partial as partial
import typing as typing
from future.utils import iteritems as iteritems
from account_helpers.AccountSettings import AccountSettings as AccountSettings, MAPBOX_PROGRESSION as MAPBOX_PROGRESSION
from wg_async import wg_async as wg_async, wg_await as wg_await, await_callback as await_callback, BrokenPromiseError as BrokenPromiseError
import adisp as adisp
import BigWorld as BigWorld
from BWUtil import AsyncReturn as AsyncReturn
from constants import QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE, Configs as Configs
import Event as Event
from frameworks.wulf import WindowLayer as WindowLayer
from gui.game_control.season_provider import SeasonProvider as SeasonProvider
from gui.mapbox import mapbox_helpers as mapbox_helpers
from gui.mapbox.mapbox_helpers import formatMapboxBonuses as formatMapboxBonuses, convertTimeFromISO as convertTimeFromISO
from gui.mapbox.mapbox_survey_manager import MapboxSurveyManager as MapboxSurveyManager
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.server_events import caches as caches
from gui.shared.event_dispatcher import showMapboxIntro as showMapboxIntro, showMapboxSurvey as showMapboxSurvey, showBrowserOverlayView as showBrowserOverlayView, showMapboxPrimeTimeWindow as showMapboxPrimeTimeWindow
from gui.shared.utils import SelectorBattleTypesUtils as SelectorBattleTypesUtils
from gui.shared.utils.SelectorBattleTypesUtils import setBattleTypeAsUnknown as setBattleTypeAsUnknown
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier, TimerNotifier as TimerNotifier
from gui.wgcg.mapbox.contexts import MapboxProgressionCtx as MapboxProgressionCtx, MapboxCompleteSurveyCtx as MapboxCompleteSurveyCtx
from helpers import dependency as dependency, server_settings as server_settings, time_utils as time_utils
from skeletons.gui.game_control import IMapboxController as IMapboxController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.web import IWebController as IWebController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
_logger: Any
ProgressionData: Any
MapData: Any
RewardData: Any
_LAST_PERIOD = 0
_RESTART_PROGRESSION_DELAY = 30

class MapboxController(Notifiable, SeasonProvider, IMapboxController, IGlobalListener):
    __lobbyContext: Any
    __systemMessages: Any
    __webCtrl: Any
    onPrimeTimeStatusUpdated: Any
    onUpdated: Any
    onMapboxSurveyShown: Any
    onMapboxSurveyCompleted: Any
    __callbackID: Any
    __progressionDataProvider: Any
    __settingsManager: Any
    __surveyManager: Any
    __isSyncing: Any
    def __init__(self):
        ...
    @property
    def surveyManager(self):
        ...
    def addProgressionListener(self, listener):
        ...
    def removeProgressionListener(self, listener):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onLobbyInited(self, event):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onDisconnected(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def isActive(self):
        ...
    def isAvailable(self):
        ...
    def isEnabled(self):
        ...
    def isMapboxMode(self):
        ...
    def isMapboxPrbActive(self):
        ...
    def isMapVisited(self, mapName):
        ...
    def getAlertBlock(self):
        ...
    def getModeSettings(self):
        ...
    def getProgressionData(self):
        ...
    def getProgressionRestartTime(self):
        ...
    def getUnseenItemsCount(self):
        ...
    # decorador original: @wg_async
    def forceUpdateProgressData(self):
        ...
    # decorador original: @adisp.adisp_process
    def handleSurveyCompleted(self, surveyData):
        ...
    # decorador original: @adisp.adisp_process
    def selectMapboxBattle(self):
        ...
    def showMapboxInfoPage(self):
        ...
    def showSurvey(self, mapName):
        ...
    def addVisitedMap(self, mapName):
        ...
    def setPrevBattlesPlayed(self, numBattles):
        ...
    def getPrevBattlesPlayed(self):
        ...
    def storeCycle(self):
        ...
    def getEventEndTimestamp(self):
        ...
    def __onUnitJoined(self, *args):
        ...
    def __modeEntered(self):
        ...
    def __selectRandomBattle(self):
        ...
    def __stopSubsystems(self):
        ...
    # decorador original: @adisp.adisp_process
    def __doSelectRandomPrb(self, dispatcher):
        ...
    def __timerUpdate(self):
        ...
    def __updateSavedTab(self):
        ...
    def __eventAvailabilityUpdate(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
    def __updateMode(self):
        ...

class MapboxProgressionDataProvider(Notifiable):
    __webCtrl: Any
    __lobbyContext: Any
    __mapboxCtrl: Any
    __eventsCache: Any
    __slots__: tuple
    __progressionData: Any
    __isSyncing: Any
    __isShuttingDown: Any
    __isStarted: Any
    __restartNotifier: Any
    __randomRestartProgressionDelay: Any
    onProgressionDataUpdated: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def getProgressionData(self):
        ...
    def getProgressionRestartTime(self):
        ...
    def getTimer(self):
        ...
    def getRestartTimer(self):
        ...
    # decorador original: @wg_async
    def forceUpdateProgressData(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
    def __timerUpdate(self):
        ...
    def __onSyncCompleted(self):
        ...
    # decorador original: @adisp.adisp_process
    def __request(self, callback):
        ...
    def __getProgressionRestartTimeWithRandomDelay(self):
        ...

class MapboxSettingsManager(object):
    __slots__: tuple
    __settings: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def clearSettings(self):
        ...
    def isMapVisited(self, mapName):
        ...
    def addVisitedMap(self, mapName):
        ...
    def setPrevBattlesPlayed(self, numBattles):
        ...
    def getPrevBattlesPlayed(self):
        ...
    def storeCycle(self, isActive, cycleId):
        ...
