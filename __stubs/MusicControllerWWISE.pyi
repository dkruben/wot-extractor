# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/MusicControllerWWISE.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import ResMgr as ResMgr
import WWISE as WWISE
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from helpers import isPlayerAvatar as isPlayerAvatar
from items import _xml as _xml
from helpers import dependency as dependency
from skeletons.gui.game_control import ISpecialSoundCtrl as ISpecialSoundCtrl
MUSIC_EVENT_NONE = 0
MUSIC_EVENT_LOBBY = 2
MUSIC_EVENT_COMBAT = 3
MUSIC_EVENT_COMBAT_LOADING = 4
MUSIC_EVENT_COMBAT_VICTORY = 5
MUSIC_EVENT_COMBAT_LOSE = 6
MUSIC_EVENT_COMBAT_DRAW = 7
_BATTLE_RESULT_MUSIC_EVENTS: tuple
AMBIENT_EVENT_NONE = 1000
AMBIENT_EVENT_LOBBY = 1001
AMBIENT_EVENT_SHOP = 1002
AMBIENT_EVENT_STATISTICS = 1003
AMBIENT_EVENT_COMBAT = 1004
AMBIENT_EVENT_LOBBY_FORT = 1005
AMBIENT_EVENT_LOBBY_FORT_FINANCIAL_DEPT = 1006
AMBIENT_EVENT_LOBBY_FORT_TANKODROME = 1007
AMBIENT_EVENT_LOBBY_FORT_TRAINING_DEPT = 1008
AMBIENT_EVENT_LOBBY_FORT_MILITARY_ACADEMY = 1009
AMBIENT_EVENT_LOBBY_FORT_TRANSPORT_DEPT = 1010
AMBIENT_EVENT_LOBBY_FORT_INTENDANT_SERVICE = 1011
AMBIENT_EVENT_LOBBY_FORT_TROPHY_BRIGADE = 1012
AMBIENT_EVENT_LOBBY_FORT_OFFICE = 1013
AMBIENT_EVENT_LOBBY_FORT_MILITARY_SHOP = 1014
FORT_MAPPING: dict
_ARENA_EVENTS: tuple
_CMD_SERVER_CHANGE_HANGAR_AMBIENT = 'cmd_change_hangar_ambient'
_CMD_SERVER_CHANGE_HANGAR_MUSIC = 'cmd_change_hangar_music'
_ON_VEHICLE_KILLED_EVENT = 'music_stinger'
_SERVER_OVERRIDDEN = 0
_CLIENT_OVERRIDDEN = 1
_ARENA_PERIOD_STATE_NAME = 'STATE_arenastate'
_ARENA_PERIOD_STATE: dict
_ON_BECOME_PLAYER_STATES: tuple
g_musicController = None

class MusicController(object):
    __specialSounds: Any
    __lastBattleResultEvents: dict
    __overriddenEvents: Any
    __music: Any
    __ambient: Any
    __sndEventMusic: Any
    __soundEvents: Any
    _skipArenaChanges: Any
    __vehicleKilled: Any
    __isOnArena: Any
    __isPremiumAccount: Any
    __muted: Any
    __event: Any
    __eventID: Any
    class MusicEvent(object):
        __muted: Any
        __event: Any
        __eventID: Any
        def __init__(self, event=None):
            ...
        def replace(self, event, eventId, unlink=True):
            ...
        def mute(self, isMute):
            ...
        def param(self, paramName):
            ...
        def getEventId(self):
            ...
        def isPlaying(self):
            ...
        def destroy(self, force=False):
            ...
    def __init__(self):
        ...
    def init(self, path=None):
        ...
    def destroy(self):
        ...
    def __del__(self):
        ...
    def play(self, eventId, params=None, checkIsPlaying=False):
        ...
    def stopMusic(self):
        ...
    def stopAmbient(self, force=False):
        ...
    def stop(self):
        ...
    def stopEvent(self, eventId):
        ...
    def muteMusic(self, isMute):
        ...
    def setEventParam(self, paramName, paramValue):
        ...
    def onBecomePlayer(self):
        ...
    def onEnterArena(self):
        ...
    def onLeaveArena(self):
        ...
    def setAccountPremiumState(self, isPremium, restart=False):
        ...
    def __getEvent(self, eventId):
        ...
    def __onArenaStateChanged(self, *args):
        ...
    def __onArenaVehicleKilled(self, *args):
        ...
    def __getArenaSoundEvent(self, eventId):
        ...
    def __loadConfig(self):
        ...
    def __overrideEvents(self, eventNames):
        ...
    def _getSoundEventById(self, soundEventID):
        ...
    def isPlaying(self, soundEventID):
        ...
    def isCompleted(self, soundEventID):
        ...
    def reloadSounds(self):
        ...
    def __onEventNotificationsChanged(self, notificationsDiff):
        ...
    def changeHangarSound(self, notificationsDiff):
        ...
    def __loadCustomSounds(self, xmlName):
        ...
    def __updateOverridden(self, eventID, typeId, value):
        ...
    def unloadCustomSounds(self):
        ...
    def unloadServerSounds(self, isDisconnect=False):
        ...
    def __eraseOverridden(self, index):
        ...
    @property
    def skipArenaChanges(self):
        ...
    @skipArenaChanges.setter
    def skipArenaChanges(self, skipArenaChanges):
        ...

def create():
    ...
def init(arenaName):
    ...
def destroy():
    ...
def onBecomePlayer():
    ...
def onLeaveArena():
    ...
def onEnterArena():
    ...
def unloadCustomSounds():
    ...
def play(eventId=None):
    ...
