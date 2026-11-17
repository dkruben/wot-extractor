# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/vehicles_selection_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import logging as logging
import weakref as weakref
import BigWorld as BigWorld
import Math as Math
import math_utils as math_utils
from AvatarInputHandler import cameras as cameras, keys_handlers as keys_handlers
from AvatarInputHandler.control_modes import IControlMode as IControlMode
from AvatarInputHandler.rotating_cursor_camera import RotatingCoursorCamera as RotatingCoursorCamera
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import ARENA_PERIOD as ARENA_PERIOD, VEHICLE_SELECTION_BLOCK_DELAY as VEHICLE_SELECTION_BLOCK_DELAY
from gui.battle_control import avatar_getter as avatar_getter
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes
_logger: Any

class _CameraManager(object):
    CAMERA_TRANSITION_DURATION = 2
    __CAMERA_PITCH: Any
    __MIN_CAMERA_DISTANCE = 10
    __CAM_CHANGING_SETTINGS: set
    __sessionProvider: Any
    __settingsCore: Any
    __initialCamSetup: Any
    __camera: Any
    __cameraMover: Any
    __pendingVehicles: Any
    def __init__(self, cfg):
        ...
    @property
    def camera(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def reset(self):
        ...
    def moveCameraToDefault(self):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __locateCameraOnAllVehicles(self):
        ...
    def __setCamera(self):
        ...
    def __onVehicleEnteredWorld(self, vehicle):
        ...

class _CameraMover(CallbackDelayer):
    __TICK_DELAY = 0.01
    __camera: Any
    __startParams: Any
    __finalParams: Any
    __totalChanges: Any
    __startTime: Any
    __endTime: Any
    def __init__(self, camera):
        ...
    def startMovementTo(self, finalYaw, finalPitch, pivotDistance, transtitionTime):
        ...
    def stop(self):
        ...
    def __tick(self):
        ...
    def __getYawTotalChange(self, startYaw, finalYaw):
        ...
    def __getNewValueForParameter(self, paramName, timePassed, totalTime):
        ...

class VehiclesSelectionControlMode(IControlMode):
    __dynamicObjectsCache: Any
    __guiSessionProvider: Any
    __aih: Any
    __camManager: Any
    __arenaPeriod: Any
    __ownVehicleEffectGO: Any
    __lockedState: Any
    __lockStartTime: Any
    __callbackDelayer: Any
    def __init__(self, config, avatarInputHandler):
        ...
    @property
    def camera(self):
        ...
    def destroy(self):
        ...
    def enable(self, **args):
        ...
    def disable(self):
        ...
    def alwaysReceiveKeyEvents(self, isDown=True):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
    def onRecreateDevice(self):
        ...
    def moveCameraToDefault(self):
        ...
    def __onLockedState(self):
        ...
    def __onArenaPeriodChanged(self, period, periodEndTime, *_):
        ...
    def __updateArenaPeriod(self, period, periodEndTime):
        ...
