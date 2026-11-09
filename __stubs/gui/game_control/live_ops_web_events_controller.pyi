# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/live_ops_web_events_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from enum import Enum as Enum
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.server_events import caches as caches
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from skeletons.gui.game_control import ILiveOpsWebEventsController as ILiveOpsWebEventsController
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from Event import Event as Event, EventManager as EventManager
from constants import Configs as Configs
from account_helpers.AccountSettings import AccountSettings as AccountSettings, LIVE_OPS_WEB_EVENTS_COUNTERS as LIVE_OPS_WEB_EVENTS_COUNTERS, LIVE_OPS_WEB_EVENTS_UI_FLAGS as LIVE_OPS_WEB_EVENTS_UI_FLAGS
_LOW_QUALITY_PRESETS: tuple

class EventState(Enum):
    UNDEFINED = 'undefined'
    PRE_EVENT = 'preEvent'
    EVENT_ACTIVE = 'eventActive'
    POST_EVENT = 'postEvent'

class LiveOpsWebEventsController(Notifiable, ILiveOpsWebEventsController):
    __lobbyContext: Any
    __em: Any
    onSettingsChanged: Any
    onEventStateChanged: Any
    __previousEventState: Any
    __currentEventState: Any
    __isHighQualityPreset: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onDisconnected(self):
        ...
    def fini(self):
        ...
    @property
    def eventConfig(self):
        ...
    @property
    def eventUniqueName(self):
        ...
    def isEnabled(self):
        ...
    @property
    def eventUrl(self):
        ...
    @property
    def preEventStart(self):
        ...
    @property
    def eventStart(self):
        ...
    @property
    def postEventEnd(self):
        ...
    @property
    def eventEnd(self):
        ...
    @property
    def eventState(self):
        ...
    @property
    def previousEventState(self):
        ...
    @property
    def isEntryPointSmall(self):
        ...
    @property
    def isHighQualityPreset(self):
        ...
    def canShowHangarEntryPoint(self):
        ...
    def canShowEventsTab(self):
        ...
    def getEventTabVisited(self):
        ...
    def markEventTabVisited(self):
        ...
    def getIsFirstEventEntry(self):
        ...
    def markEventEntered(self):
        ...
    def __clear(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __updateSavedTab(self):
        ...
    def __getEventState(self):
        ...
    def __getTimerDelta(self):
        ...
    @staticmethod
    def __getTimeNow():
        ...
    def __timerUpdate(self):
        ...
    def __resetTimer(self):
        ...
