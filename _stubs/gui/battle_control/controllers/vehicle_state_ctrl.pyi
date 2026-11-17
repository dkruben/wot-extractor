# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vehicle_state_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from functools import partial as partial
from future.utils import listvalues as listvalues
import BigWorld as BigWorld
import BattleReplay as BattleReplay
import Event as Event
import SoundGroups as SoundGroups
import nations as nations
from BattleReplay import CallbackDataNames as CallbackDataNames
from constants import UNKNOWN_VEHICLE_ID as UNKNOWN_VEHICLE_ID
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, VEHICLE_WAINING_INTERVAL as VEHICLE_WAINING_INTERVAL, VEHICLE_UPDATE_INTERVAL as VEHICLE_UPDATE_INTERVAL, BATTLE_CTRL_ID as BATTLE_CTRL_ID, DEVICE_STATE_NORMAL as DEVICE_STATE_NORMAL
from gui.shared.utils.TimeInterval import TimeInterval as TimeInterval
from shared_utils import first as first

class _StateHandler(object):
    __slots__: tuple
    __updater: Any
    def __init__(self, updater):
        ...
    def clear(self):
        ...
    def handleStateChange(self, state, value):
        ...
    def notifyStateChanged(self, state, value):
        ...
    def _invalidate(self, vehicle):
        ...
    def __call__(self, vehicle):
        ...

class _SpeedStateHandler(_StateHandler):
    __slots__: tuple
    __speed: Any
    __maxSpeed: Any
    __isOwnVehicle: Any
    def __init__(self, updater, isOwnVehicle):
        ...
    def clear(self):
        ...
    def _invalidate(self, vehicle):
        ...
    @staticmethod
    def _formatSpeed(speed):
        ...

class _HealthStateHandler(_StateHandler):
    __slots__: tuple
    __health: Any
    def __init__(self, updater):
        ...
    def clear(self):
        ...
    def _invalidate(self, vehicle):
        ...

class _VehicleUpdater(object):
    __isAlive: Any
    __handlers: Any
    __ctrl: Any
    __vehicleID: Any
    __updateTI: Any
    def __init__(self, vehCtrl, vehicleID):
        ...
    def handleStateChange(self, state, value):
        ...
    def switch(self, vehicleID):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def clear(self):
        ...
    def updateOnce(self):
        ...
    def notifyStateChanged(self, state, value):
        ...
    def _update(self):
        ...
    def _setUpHandlers(self):
        ...

class VehicleStateController(IBattleController):
    __eManager: Any
    onVehicleStateUpdated: Any
    onVehicleControlling: Any
    onPostMortemSwitched: Any
    onRespawnBaseMoving: Any
    onEquipmentComponentUpdated: Any
    __cachedStateValues: Any
    __cachedRepairingCallbackID: Any
    __waitingTI: Any
    __vehicleID: Any
    __updater: Any
    __isRqToSwitch: Any
    __isInPostmortem: Any
    __needInvalidate: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, *_):
        ...
    def stopControl(self):
        ...
    @property
    def isInPostmortem(self):
        ...
    def setPlayerVehicle(self, vehicleID):
        ...
    def getControllingVehicle(self):
        ...
    def getControllingVehicleID(self):
        ...
    def notifyStateChanged(self, stateID, value):
        ...
    def __cachedRepairingCallback(self, value):
        ...
    def getStateValue(self, stateID):
        ...
    def refreshVehicleStateValue(self, stateID):
        ...
    def invalidate(self, state, value, vehicleID=0):
        ...
    def switchToPostmortem(self, noRespawnPossible, respawnAvailable):
        ...
    def switchToOther(self, vehicleID, needInvalidate=False):
        ...
    def refreshObserverVehicleVisual(self):
        ...
    def movingToRespawn(self):
        ...
    def _waiting(self):
        ...
    def _setup(self, vehicle):
        ...

class VehicleStateReplayRecorder(VehicleStateController):
    def invalidate(self, state, value, vehicleID=0):
        ...

class VehicleStateReplayPlayer(VehicleStateController):
    def startControl(self):
        ...
    def stopControl(self):
        ...

def createCtrl(setup):
    ...
