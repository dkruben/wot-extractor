# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/hangar_camera_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import logging as logging
from functools import partial as partial
import typing as typing
from collections import namedtuple as namedtuple
import math_utils as math_utils
import Event as Event
import BigWorld as BigWorld
import Math as Math
import CGF as CGF
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from shared_utils import first as first
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.hangar_cameras.hangar_camera_flyby import FlyByComponent as FlyByComponent
from gui.shared import g_eventBus as g_eventBus
from helpers import dependency as dependency
from math_common import isAlmostEqual as isAlmostEqual
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from vehicle_systems.components.vehicle_to_camera_alignment_components import VehicleToCameraAlignmentComponent as VehicleToCameraAlignmentComponent
from CameraComponents import CameraComponent as CameraComponent, ActiveCameraComponent as ActiveCameraComponent, CameraFlightComponent as CameraFlightComponent, OrbitComponent as OrbitComponent, DofComponent as DofComponent, IdleComponent as IdleComponent, ParallaxComponent as ParallaxComponent, FovComponent as FovComponent, ShiftComponent as ShiftComponent
from constants import IS_CLIENT as IS_CLIENT
from AvatarInputHandler.cameras import FovExtended as FovExtended
from gui.hangar_cameras.hangar_camera_yaw_filter import HangarCameraYawFilter as HangarCameraYawFilter
from gui.hangar_cameras.hangar_camera_parallax import HangarCameraParallax as HangarCameraParallax
from gui.hangar_cameras.hangar_camera_idle import HangarCameraIdle as HangarCameraIdle
from gui.hangar_cameras.hangar_camera_flyby import HangarCameraFlyby as HangarCameraFlyby
from typing import Optional as Optional
_EASE_SQUARE_OUT = 2
_DURATION_ = 2.0
_DEFAULT_MOTION_BLUR_ = 0.12
_DOF_START_PROGRESS_ = 0.5
_logger: Any
DOFParams: Any
TANK_CAMERA_NAMES: tuple

class CameraMode(object):
    DEFAULT = 'Tank'
    PLATOON = 'Platoon'
    ALL: tuple

class _MouseMoveParams(object):
    __slots__: tuple
    rotationSensitivity: Any
    zoomSensitivity: Any
    yawConstraints: Any
    pitchConstraints: Any
    distConstraints: Any
    distLength: Any
    shiftPivotDistances: Any
    shiftPivotLows: Any
    def __init__(self, rotationSensitivity=0.005, zoomSensitivity=0.003, yawConstraints=..., pitchConstraints=..., distConstraints=...):
        ...
    def updateLength(self):
        ...
    def setPivotShifts(self, shiftPivotLows, shiftPivotDistances):
        ...

class _FlightParams(object):
    __slots__: tuple
    duration: Any
    easing: Any
    motionBlur: Any
    route: Any
    def __init__(self, duration=..., easing=..., motionBlur=..., route=None):
        ...

class _DOFParams(object):
    __slots__: tuple
    active: Any
    nearStart: Any
    nearDist: Any
    farStart: Any
    farDist: Any
    def __init__(self, active=False, nearStart=0.0, nearDist=0.0, farStart=0.0, farDist=0.0):
        ...

class HangarCameraSystem(CGF.System):
    _settingsCore: Any
    _hangarSpace: Any
    CameraActivated: Any
    OrbitActivated: Any
    ActiveCameraIterate: Any
    CameraIterate: Any
    OrbitIterate: Any
    ActiveCameraAccess: Any
    VehicleToCameraAlignmentAccess: Any
    TransformAccess: Any
    OrbitAccess: Any
    CameraAccess: Any
    FovAccess: Any
    DofAccess: Any
    IdleAccess: Any
    ParallaxAccess: Any
    CameraFlightAccess: Any
    ShiftAccess: Any
    FlyByAccess: Any
    Reactions: Any
    __cam: Any
    __flightCam: Any
    __customizationHelper: Any
    __yawCameraFilter: Any
    __cameraIdle: Any
    __cameraParallax: Any
    __cameraFlyby: Any
    __mouseMoveParams: Any
    __flightParams: Any
    __vehicleToCameraCompIsActive: Any
    __minDist: Any
    __prevHorizontalFov: Any
    __currentHorizontalFov: Any
    __customFov: Any
    __prevDOFParams: Any
    __currentDOFParams: Any
    __rotationEnabled: Any
    __zoomEnabled: Any
    __cameraMode: Any
    __cameraName: Any
    __orbitCameraMap: Any
    __isActive: Any
    __flybyCallback: Any
    onCameraSwitched: Any
    onNewCameraAdded: Any
    def update(self):
        ...
    def __init__(self):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def onCameraAdded(self, cameraComponent):
        ...
    def onOrbitCameraActivated(self, cameraComponent):
        ...
    def isCameraAdded(self, cameraName):
        ...
    def isCameraSwitching(self):
        ...
    def getCurrentCameraName(self):
        ...
    def switchToTank(self, instantly=True, resetTransform=True):
        ...
    def cameraExists(self, cameraName):
        ...
    def findCameraGameObjectByName(self, name):
        ...
    def getCameraFlyBy(self):
        ...
    def activateCamera(self, name):
        ...
    def switchByCameraName(self, name, instantly=True, resetTransform=True, forceUpdate=True):
        ...
    def __switchByCameraName(self, name, instantly=True, resetTransform=True, forceUpdate=True):
        ...
    def resetCameraTarget(self, duration=0, resetRotation=True, resetDistance=True):
        ...
    def enableMovementByMouse(self, enableRotation=True, enableZoom=True):
        ...
    def enablePlatoonMode(self, enable=True):
        ...
    def setDOFParams(self, enabled, dofParams=None):
        ...
    def setMinDist(self, value):
        ...
    def moveCamera(self, targetPos=None, yaw=None, pitch=None, distance=None, duration=0, distConstraints=None):
        ...
    def activateCameraFlyby(self, callback=None):
        ...
    def deactivateCameraFlyby(self):
        ...
    def __onFlybyFinished(self):
        ...
    def __startFlight(self, prevMatrix, targetMatrix):
        ...
    def __handleLobbyViewMouseEvent(self, event):
        ...
    def __calculateDynamicFov(self):
        ...
    def __normaliseAngle(self, angle):
        ...
    def __setupCamera(self, gameObject, resetTransform=True, forceUpdate=True):
        ...
    def __setCameraShift(self, shiftComponent):
        ...
    def __setupFlightParams(self, gameObject, prevCameraName):
        ...
    def __onSetFovSetting(self):
        ...
    def __deactivateCameraComponents(self):
        ...
    def __activateDOF(self):
        ...
    def __onCameraSwitched(self):
        ...
    def tick(self):
        ...
    def __interpolateFOV(self, progress):
        ...
    def __interpolateDOF(self, progress):
        ...
