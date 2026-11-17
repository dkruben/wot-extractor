# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/free_camera.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
import math as math
import logging as logging
from future.utils import lmap as lmap
import GUI as GUI
import BigWorld as BigWorld
import Settings as Settings
import ResMgr as ResMgr
import BattleReplay as BattleReplay
import constants as constants
import Math as Math
import math_utils as math_utils
import Keys as Keys
import CommandMapping as CommandMapping
from gui.shared.utils.key_mapping import getVirtualKey as getVirtualKey
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from Math import Vector3 as Vector3
from AvatarInputHandler.VideoCamera import VideoCamera as VideoCamera, _InertiaScalar as _InertiaScalar, KeySensor as KeySensor, _AlignerToLand as _AlignerToLand
from AvatarInputHandler.DynamicCameras import CameraWithSettings as CameraWithSettings
from AvatarInputHandler.cameras import readFloat as readFloat
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from account_helpers.settings_core.settings_constants import CONTROLS as CONTROLS
from debug_utils import LOG_WARNING as LOG_WARNING
from helpers import isPlayerAvatar as isPlayerAvatar
_logger: Any
_DEFAULT_SPEED_LEVEL_LIMITS: tuple

class FreeVideoCamera(VideoCamera, CameraWithSettings):
    camera: Any
    aimingSystem: Any
    _sensitivityLimit: Any
    __selectedTargetID: Any
    _collisionKeys: Any
    __maxPitch: Any
    __minPitch: Any
    __speedIfCollision: Any
    __skipFlags: Any
    __randomDir: Any
    __acObstacleForwardCheckDistance: Any
    __acCameraColliderRadius: Any
    __bounceMultiplier: Any
    __isCollisionBouncing: Any
    __collisionDetected: Any
    _isVerticalVelocitySeparated: Any
    _inertiaEnabled: Any
    _heightInertia: Any
    __heightAboveTerrain: Any
    _mouseSensitivity: Any
    _scrollSensitivity: Any
    _horzInvert: Any
    _vertInvert: Any
    _movementSensor: Any
    _verticalMovementSensor: Any
    _heightAboveGroundSensor: Any
    _rotationSensor: Any
    __collided: Any
    def __init__(self, configDataSec):
        ...
    def getAlignerToLandClass(self):
        ...
    def destroy(self):
        ...
    def enable(self, **args):
        ...
    def disable(self):
        ...
    def setHeight(self, height):
        ...
    def setMinMaxHeight(self, minHeight, maxHeight):
        ...
    def handleKeyEvent(self, key, isDown):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
    def reload(self):
        ...
    def writeUserPreferences(self):
        ...
    def _readConfigs(self, dataSec):
        ...
    def _readCfg(self, configDataSec):
        ...
    def _readBaseCfg(self, dataSec):
        ...
    def _readUserCfg(self):
        ...
    def _makeCfg(self):
        ...
    @staticmethod
    def _getConfigsKey():
        ...
    def _getMouseSensitivitySettingKey(self):
        ...
    def _applyMouseSensitivityFromAccount(self):
        ...
    def setUserConfigValue(self, name, value):
        ...
    def __updateProperties(self):
        ...
    def _readMovementSettings(self, configDataSec):
        ...
    def _readRotationSettings(self, configDataSec, rotationMappings):
        ...
    def _checkSpaceBounds(self, startPos, endPos):
        ...
    def _update(self):
        ...
    def _isKeyPressed(self, mapping, defaultKey):
        ...
    def _handleCollision(self, vel):
        ...
    def __readCollisionSettings(self, configDataSec):
        ...
    def __getSideCollisions(self, lookPoint, pos, rightVector, raycastSideOffset):
        ...
    def __initMovementSensors(self):
        ...
    def __handleAdvancedCollision(self, pos, lookDir, vel):
        ...
    def __raycastTo(self, end, skipFlags=0, ignoreDynamicId=0, ignorePart=-1):
        ...
    def __onMappingChanged(self, *args):
        ...

class _SensitivityLimit(object):
    guiSessionProvider: Any
    __movementSensor: Any
    __keyMappings: Any
    __sensitivityIndex: Any
    __speedSensitivity: Any
    def __init__(self, defaultSensitivity, movementSensor, keyMappings):
        ...
    def setSpeedSensitivity(self, index, sensitivity):
        ...
    def handleKeyEvent(self, key, isDown):
        ...
    def __applySpeedSensitivity(self):
        ...

class _SensitivityLimitKeySensor(KeySensor):
    __callback: Any
    keyMappings: Any
    def setCallback(self, callback):
        ...
    def evaluateSensitivityKeys(self, delta):
        ...
    def handleKeyEvent(self, key, isDown):
        ...
    def reloadKeySettings(self, newKeyMappings):
        ...

class _VariableHeightAlignerToLand(_AlignerToLand):
    _DEFAULT_MIN_HEIGHT_CAMERA = 10.0
    _DEFAULT_MAX_HEIGHT_CAMERA = 120.0
    _minHeight: Any
    _maxHeight: Any
    _distanceToCeilingAssets: Any
    _distanceToFloorAssets: Any
    _minHeightSafe: Any
    _maxHeightSafe: Any
    _avgLandHeight: Any
    avgLandHeightUpdateSpeed: Any
    __skipFlags: Any
    def __init__(self):
        ...
    def getAlignedPosition(self, position):
        ...
    def updateLandHeight(self, pos, deltaTime):
        ...
    def enableWithFixedHeight(self, currentPos, height, ignoreTerrain=False):
        ...
    def setCollisionSkipFlags(self, flags):
        ...
    def setMinMaxHeight(self, minHeight, maxHeight):
        ...
    def _getLandAt(self, position):
        ...
    def __isWaterCloser(self, position, waterDist, terrainCollision):
        ...

def getCameraAsSettingsHolder(settingsDataSec):
    ...
