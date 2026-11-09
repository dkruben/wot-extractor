# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TriggersManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from future.utils import itervalues as itervalues, viewvalues as viewvalues, viewitems as viewitems
import BigWorld as BigWorld
import Math as Math
import PlayerEvents as PlayerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from helpers import isPlayerAvatar as isPlayerAvatar
g_manager = None

class TRIGGER_TYPE(object):
    AIM = 0
    AREA = 1
    AIM_AT_VEHICLE = 3
    AUTO_AIM_AT_VEHICLE = 4
    VEHICLE_DESTROYED = 5
    PLAYER_VEHICLE_ON_SOFT_TERRAIN = 6
    PLAYER_VEHICLE_TRACKS_DAMAGED = 7
    PLAYER_SHOT_MISSED = 8
    SNIPER_MODE = 12
    PLAYER_TANKMAN_SHOOTED = 13
    PLAYER_VEHICLE_IN_FIRE = 14
    PLAYER_VEHICLE_OBSERVED = 15
    PLAYER_RECEIVE_DAMAGE = 16
    PLAYER_DISCRETE_SHOOT = 17
    PLAYER_DETECT_ENEMY = 18
    VEHICLE_VISUAL_VISIBILITY_CHANGED = 19
    PLAYER_DEVICE_CRITICAL = 20
    PLAYER_MOVE = 21
    SHOW_TRACER = 22
    PLAYER_SHOT_HIT = 23
    STUN = 24
    SIXTH_SENSE = 25
    PLAYER_ENTER_SPG_STRATEGIC_MODE = 26
    PLAYER_ENTER_SPG_SNIPER_MODE = 27
    PLAYER_LEAVE_SPG_MODE = 28
    CTRL_MODE_CHANGE = 29
    PLAYER_USED_AOE_EQUIPMENT = 30
    PLAYER_CONTINUOUS_BURST_START = 31
    PLAYER_CONTINUOUS_BURST_STOP = 32
    CURRENT_VEHICLE_AREA = 33

class ITriggerListener(object):
    def onTriggerActivated(self, args):
        ...
    def onTriggerDeactivated(self, args):
        ...

class TriggersManager(object):
    UPDATE_PERIOD = 0.05
    isActive: Any
    __autoTriggers: Any
    __activeAutoTriggers: Any
    __pendingManualTriggers: Any
    __activeManualTriggers: Any
    __listeners: Any
    __nextTriggerId: Any
    __cbID: Any
    __isOnArena: Any
    __isEnabled: Any
    __shotPoints: Any
    __explodePoints: Any
    __previousCurrentVehicleID: Any
    def __init__(self):
        ...
    def isEnabled(self):
        ...
    def destroy(self):
        ...
    def enable(self, enable):
        ...
    def clearTriggers(self, keepTriggersFromMap):
        ...
    def addListener(self, listener):
        ...
    def delListener(self, listener):
        ...
    def addTrigger(self, tType, **params):
        ...
    def delTrigger(self, triggerID):
        ...
    def fireTrigger(self, tType, **kwargs):
        ...
    def fireTriggerInstantly(self, tType, **kwargs):
        ...
    def activateTrigger(self, triggerType, **kwargs):
        ...
    def deactivateTrigger(self, triggerType):
        ...
    def update(self):
        ...
    def getTriggerPosition(self, tType, name):
        ...
    def getDistanceToTrigger(self, tType, name):
        ...
    def isAutoTriggerActive(self, tType, name):
        ...
    def __onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        ...
    def __getAreaTriggerActivationStatus(self, vehicle, params, wasActive):
        ...
    def __getAimTriggerActivationStatus(self, vehicle, camera, params):
        ...

def init():
    ...
