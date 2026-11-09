# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/IngameSoundNotifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from random import randrange as randrange
from functools import partial as partial
from future.utils import viewitems as viewitems
import Math as Math
import BigWorld as BigWorld
import ResMgr as ResMgr
import BattleReplay as BattleReplay
import Event as Event
import SoundGroups as SoundGroups
import VSE as VSE
import WWISE as WWISE
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from helpers import isPlayerAvatar as isPlayerAvatar
from account_helpers import AccountSettings as AccountSettings
from account_helpers.settings_core.settings_constants import SOUND as SOUND
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer, TimeDeltaMeter as TimeDeltaMeter
import importlib as importlib
_ENABLE_VO_LOGS = False
_SUBTITLE_PREFIX = '#'
_SUBTITLES_END_MARKER = '#end'

class IngameSoundNotifications(CallbackDelayer, TimeDeltaMeter):
    __EVENTS_PATH = 'gui/sound_notifications.xml'
    __CIRCUMSTANCES_PATH = 'gui/sound_circumstances.xml'
    __DEFAULT_LIFETIME = 3.0
    __TICK_DELAY = 0.5
    QueueItem: Any
    PlayingEvent: Any
    __isEnabled: Any
    __enabledSoundCategories: Any
    __remappedNotifications: Any
    __events: Any
    __eventsPriorities: Any
    __eventsCooldowns: Any
    __fxCooldowns: Any
    __circumstances: Any
    __circumstancesWeights: Any
    __circumstancesGroupsWeights: Any
    __playingEvents: Any
    __queues: Any
    _currentSubtitle: Any
    onPlayEvent: Any
    onAddEvent: Any
    onSubtitleShow: Any
    onSubtitleHide: Any
    __vseContextClass: Any
    _vsePlan: Any
    __soundNotificationsContext: Any
    __delayedCallbacks: Any
    def __init__(self, arenaType):
        ...
    def start(self):
        ...
    def __onTimeWarpStart(self):
        ...
    def __resetDelayedCallbacks(self):
        ...
    def destroy(self):
        ...
    def isPlaying(self, eventName):
        ...
    def setRemapping(self, remap):
        ...
    def play(self, vo, vehicleID=None, checkFn=None, position=None, boundVehicleID=None):
        ...
    @staticmethod
    def __importVSEContextClass(contextPath):
        ...
    def __playDelayed(self, eventName, vehicleID=None, checkFn=None, position=None, boundVehicleID=None, callbackIDHolder=None):
        ...
    def __playFX(self, eventName, vehicleID, position):
        ...
    def playNextQueueEvent(self, queueNum):
        ...
    def replayLastQueueEvent(self, queueNum):
        ...
    def getFirstQueueEvent(self, queueNum):
        ...
    def clear(self):
        ...
    def clearQueue(self, queueNum):
        ...
    def enableFX(self, isEnabled):
        ...
    def enableVoices(self, isEnabled, clearQueues=True):
        ...
    def isCategoryEnabled(self, category):
        ...
    def getEventInfo(self, eventName, parameter):
        ...
    def getPlayingEventData(self, queueNum, parameter):
        ...
    def getCircumstanceInfo(self, circIndex, parameter):
        ...
    def getCircumstanceIndex(self, circGroup, circName):
        ...
    def setEventCooldown(self, eventName, cooldown):
        ...
    def setEventPriority(self, eventName, priority, hold):
        ...
    def setCircumstanceWeight(self, circIndex, weight, hold):
        ...
    def setCircumstanceGroupWeight(self, groupName, weight, hold):
        ...
    def onNotificationBegins(self, eventName):
        ...
    def log(self, msg):
        ...
    def __checkPause(self):
        ...
    def __playFirstFromQueue(self, queueNum):
        ...
    def __readConfigs(self):
        ...
    def __tick(self):
        ...
    def __checkLifetime(self, queueItem):
        ...
    @staticmethod
    def __tickGroup(group, delta):
        ...
    def _showSubtitle(self, subtitle):
        ...
    def _hideSubtitle(self):
        ...
    def _soundMarkerHandler(self, marker):
        ...

class ComplexSoundNotifications(object):
    SPG_DISTANT_THREAT_SOUND = 'wpn_artillery_distant_threat'
    RTPC_EXT_SPG_SIGHT = 'RTPC_ext_artillery_sight'
    __activeSounds: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def notifyEnemySPGShotSound(self, distToTarget, shooterPosition):
        ...
    def __endSoundCallback(self, soundID):
        ...

def LOG_VO(msg, *kargs, **kwargs):
    ...
