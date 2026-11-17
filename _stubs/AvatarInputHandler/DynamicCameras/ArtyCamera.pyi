# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/ArtyCamera.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from math import pi as pi, copysign as copysign, atan2 as atan2, sqrt as sqrt
import BigWorld as BigWorld
from Math import slerp as slerp, Vector2 as Vector2, Vector3 as Vector3, Matrix as Matrix, MatrixProduct as MatrixProduct
import BattleReplay as BattleReplay
import Settings as Settings
import math_utils as math_utils
from AvatarInputHandler import aih_global_binding as aih_global_binding, cameras as cameras
from BigWorld import ArtyAimingSystem as ArtyAimingSystem, ArtyAimingSystemRemote as ArtyAimingSystemRemote
from AvatarInputHandler.DynamicCameras import createOscillatorFromSection as createOscillatorFromSection, CameraDynamicConfig as CameraDynamicConfig, CameraWithSettings as CameraWithSettings, SPGScrollSmoother as SPGScrollSmoother
from AvatarInputHandler.DynamicCameras.camera_switcher import CameraSwitcher as CameraSwitcher, SwitchTypes as SwitchTypes, CameraSwitcherCollection as CameraSwitcherCollection, SwitchToPlaces as SwitchToPlaces, TRANSITION_DIST_HYSTERESIS as TRANSITION_DIST_HYSTERESIS
from AvatarInputHandler.cameras import readFloat as readFloat, readVec2 as readVec2, ImpulseReason as ImpulseReason
from ProjectileMover import collideDynamicAndStatic as collideDynamicAndStatic
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from account_helpers.settings_core.settings_constants import CONTROLS as CONTROLS, GAME as GAME, SPGAim as SPGAim
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from debug_utils import LOG_WARNING as LOG_WARNING
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_SEARCH_COLLISION_DEPTH = 1
_OFFSET_FROM_NEAR_PLANE = 0.01

class Hysteresis(object):
    threshold: Any
    _state: Any
    __threshold: Any
    def __init__(self, state, threshold):
        ...
    def _dist(self, _):
        ...
    def update(self, state):
        ...
    def check(self, state):
        ...

class PositionHysteresis(Hysteresis):
    def __init__(self, threshold):
        ...
    def _dist(self, state):
        ...

class TimeHysteresis(Hysteresis):
    def __init__(self, threshold):
        ...
    def _dist(self, state):
        ...

class ArtyCamera(CameraWithSettings, CallbackDelayer):
    _DYNAMIC_ENABLED = True
    camera: Any
    aimingSystem: Any
    __aimOffset: Any
    isAimOffsetEnabled: Any
    __positionOscillator: Any
    __positionNoiseOscillator: Any
    __switchers: Any
    __dynamicCfg: Any
    __cam: Any
    __curSense: Any
    __onChangeControlMode: Any
    __camDist: Any
    __desiredCamDist: Any
    __aimingSystem: Any
    __prevTime: Any
    __prevAimPoint: Any
    __dxdydz: Any
    __autoUpdatePosition: Any
    __needReset: Any
    __sourceMatrix: Any
    __targetMatrix: Any
    __rotation: Any
    __positionHysteresis: Any
    __timeHysteresis: Any
    __transitionEnabled: Any
    __scrollSmoother: Any
    __collisionDist: Any
    __camViewPoint: Any
    @staticmethod
    def enableDynamicCamera(enable):
        ...
    @staticmethod
    def isCameraDynamic():
        ...
    def __init__(self, dataSec):
        ...
    @staticmethod
    def _getConfigsKey():
        ...
    def _getMouseSensitivitySettingKey(self):
        ...
    def create(self, onChangeControlMode=None):
        ...
    def destroy(self):
        ...
    def enable(self, targetPos, saveDist, switchToPos=None, switchToPlace=None):
        ...
    def disable(self):
        ...
    def teleport(self, pos):
        ...
    def getDistRatio(self):
        ...
    def getCurrentCamDist(self):
        ...
    def getCamDistRange(self):
        ...
    def getCamTransitionDist(self):
        ...
    def update(self, dx, dy, dz, updatedByKeyboard=False):
        ...
    def applyImpulse(self, position, impulse, reason=...):
        ...
    def applyDistantImpulse(self, position, impulseValue, reason=...):
        ...
    def writeUserPreferences(self):
        ...
    def __applyNoiseImpulse(self, noiseMagnitude):
        ...
    def __calculateAimOffset(self, aimWorldPos):
        ...
    def __handleMovement(self):
        ...
    def __getCameraDirection(self):
        ...
    def __getDesiredCameraDistance(self):
        ...
    def __updateTrajectoryDrawer(self):
        ...
    def __updateTime(self):
        ...
    def __choosePitchLevel(self, aimPoint):
        ...
    def __getCollisionTestOrigin(self, aimPoint, direction):
        ...
    def __resolveCollisions(self, aimPoint, distance, direction):
        ...
    def __calculateIdealState(self, deltaTime):
        ...
    def __interpolateStates(self, deltaTime, rotation, desiredDistance, collisionDist):
        ...
    def __cameraUpdate(self):
        ...
    def __updateOscillator(self, deltaTime):
        ...
    def __switchersDistRange(self):
        ...
    def _readConfigs(self, dataSec):
        ...
    def _readBaseCfg(self, dataSec):
        ...
    def _readUserCfg(self):
        ...
    def _makeCfg(self):
        ...
    def _handleSettingsChange(self, diff):
        ...
    def _updateSettingsFromServer(self):
        ...
    def __enableSwitchers(self, updateTransitionEnabled=True):
        ...

def getCameraAsSettingsHolder(settingsDataSec):
    ...
