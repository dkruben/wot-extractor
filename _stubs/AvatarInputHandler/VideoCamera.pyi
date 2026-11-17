# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/VideoCamera.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import time as time
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import GUI as GUI
import Keys as Keys
import Math as Math
import math_utils as math_utils
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from AvatarInputHandler import AimingSystems as AimingSystems
from AvatarInputHandler.cameras import ICamera as ICamera
from DetachedTurret import DetachedTurret as DetachedTurret
from Math import Vector3 as Vector3, Matrix as Matrix
from ProjectileMover import collideDynamicAndStatic as collideDynamicAndStatic
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from helpers import dependency as dependency
from helpers import isPlayerAvatar as isPlayerAvatar
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer, TimeDeltaMeter as TimeDeltaMeter
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class KeySensor(object):
    keyMappings: Any
    sensitivity: Any
    defaultSensitivity: Any
    _sensitivityKeys: Any
    currentVelocity: Any
    _currentKeys: Any
    def __init__(self, keyMappings, sensitivity, sensitivityIncDecKeys=None, sensitivityAcceleration=None):
        ...
    def addVelocity(self, velocity):
        ...
    def reset(self, defaultVelocity):
        ...
    def resetKeys(self):
        ...
    def handleKeyEvent(self, key, isDown):
        ...
    def evaluateSensitivityKeys(self, delta):
        ...
    def update(self, delta):
        ...

class _Inertia(object):
    frictionCoeff: Any
    def __init__(self, frictionCoeff):
        ...
    def integrate(self, thrust, velocity, delta):
        ...

class _InertiaScalar(object):
    frictionCoeff: Any
    def __init__(self, frictionCoeff):
        ...
    def integrate(self, thrustToAdd, currentVelocity, delta):
        ...

class _AlignerToLand(object):
    MIN_HEIGHT = 0.5
    desiredHeightShift: Any
    enabled: Any
    ignoreTerrain: Any
    __desiredHeightShift: Any
    __ignoreTerrain: Any
    __upPointDistance: Any
    __downPointDistance: Any
    def __init__(self):
        ...
    def updateLandHeight(self, pos, deltaTime):
        ...
    def enable(self, position, aboveSeaLevel=False):
        ...
    def enableWithFixedHeight(self, currentPos, height, ignoreTerrain=False):
        ...
    def setupLandFindingConfig(self, upPointDistance, downPointDistance):
        ...
    def disable(self):
        ...
    def _getLandAt(self, position):
        ...
    def getAlignedPosition(self, position):
        ...

class _VehicleBounder(object):
    SELECT_CHASSIS = 0
    SELECT_TURRET = 1
    SELECT_GUN = 2
    SELECT_LOOK_AT = 3
    __MAX_SELECT = 4
    SELECT_DETACHED_TURRET = 4
    isBound: Any
    lookAtPosition: Any
    matrix: Any
    __boundLocalPos: Any
    __vehicle: Any
    __lookAtProvider: Any
    __placement: Any
    def __getLookAtPosition(self):
        ...
    def __init__(self):
        ...
    def bind(self, vehicle, bindWorldPos=None):
        ...
    def selectPlacement(self, placement):
        ...
    def selectNextPlacement(self):
        ...
    def checkTurretDetachment(self, worldPos):
        ...

class _VehiclePicker(object):
    def pick(self):
        ...

class VideoCamera(ICamera, CallbackDelayer, TimeDeltaMeter):
    guiSessionProvider: Any
    _cam: Any
    __cameraTransition: Any
    _ypr: Any
    _position: Any
    __defaultFov: Any
    __velocity: Any
    __isVerticalVelocitySeparated: Any
    __yprVelocity: Any
    __zoomVelocity: Any
    __heightAboveGroundVelocity: Any
    _inertiaEnabled: Any
    _movementInertia: Any
    _rotationInertia: Any
    _heightInertia: Any
    _movementSensor: Any
    _verticalMovementSensor: Any
    _rotationSensor: Any
    _zoomSensor: Any
    _targetRadiusSensor: Any
    _heightAboveGroundSensor: Any
    _mouseSensitivity: Any
    _scrollSensitivity: Any
    _horzInvert: Any
    _vertInvert: Any
    __rotateAroundPointEnabled: Any
    __rotationRadius: Any
    _alignerToLand: Any
    __predefinedVelocities: Any
    __predefinedVerticalVelocities: Any
    _keySwitches: Any
    __isModeOverride: Any
    __basisMProv: Any
    __entityPicker: Any
    def __init__(self, configDataSec):
        ...
    @property
    def position(self):
        ...
    def getAlignerToLandClass(self):
        ...
    def getReasonsAffectCameraDirectly(self):
        ...
    def applyImpulse(self, position, impulse, reason=1):
        ...
    def create(self):
        ...
    def destroy(self):
        ...
    def enable(self, **args):
        ...
    def disable(self):
        ...
    def handleKeyEvent(self, key, isDown):
        ...
    def _handleKeySwitches(self, key, isDown):
        ...
    def _handleMoveAndSensitivityKeys(self, key, isDown):
        ...
    def resetMovement(self):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
    def __calcCurrentDeltaAdjusted(self):
        ...
    def __getMovementDirections(self):
        ...
    def _alignHeightUpdate(self, currentPosition, shift):
        ...
    def _update(self):
        ...
    def _setupCameraViewProvider(self, yprRotation, position):
        ...
    def _handleCollision(self, vel):
        ...
    def __simpleMovement(self, delta):
        ...
    def __inertialMovement(self, delta):
        ...
    def __getAlignedToPointPosition(self, rotationMat):
        ...
    def _readCfg(self, configDataSec):
        ...
    def _readMovementSettings(self, configDataSec):
        ...
    def _readRotationSettings(self, configDataSec, rotationMappings):
        ...
    def _readZoomSettings(self, configDataSec, zoomMappings):
        ...
    def __getLookAtYPR(self, lookAtPosition):
        ...
    def __toggleView(self):
        ...
    def __clampYPR(self, ypr):
        ...
    def __clampPR(self, ypr):
        ...
    def __calcFov(self):
        ...
    def __updateSenses(self, delta):
        ...
    def __resetSenses(self):
        ...
    def _checkSpaceBounds(self, startPos, endPos):
        ...
    def __processBindToVehicleKey(self):
        ...
    def __switchBind(self):
        ...
    def setViewMatrix(self, matrix):
        ...
    def getBasisMProv(self):
        ...
    def getCameraTransition(self):
        ...
