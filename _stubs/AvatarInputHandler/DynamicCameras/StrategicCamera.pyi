# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/StrategicCamera.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import Math as Math
from Math import Vector2 as Vector2, Vector3 as Vector3
import BattleReplay as BattleReplay
import Settings as Settings
import constants as constants
import math_utils as math_utils
from AvatarInputHandler import cameras as cameras, aih_global_binding as aih_global_binding
from BigWorld import StrategicAimingSystem as StrategicAimingSystem, StrategicAimingSystemRemote as StrategicAimingSystemRemote
from AvatarInputHandler.DynamicCameras import createOscillatorFromSection as createOscillatorFromSection, CameraDynamicConfig as CameraDynamicConfig, CameraWithSettings as CameraWithSettings, SPGScrollSmoother as SPGScrollSmoother
from AvatarInputHandler.DynamicCameras.camera_switcher import CameraSwitcher as CameraSwitcher, SwitchTypes as SwitchTypes, CameraSwitcherCollection as CameraSwitcherCollection, SwitchToPlaces as SwitchToPlaces, TRANSITION_DIST_HYSTERESIS as TRANSITION_DIST_HYSTERESIS
from AvatarInputHandler.cameras import getWorldRayAndPoint as getWorldRayAndPoint, readFloat as readFloat, readVec2 as readVec2, ImpulseReason as ImpulseReason, FovExtended as FovExtended
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from account_helpers.settings_core import settings_constants as settings_constants
from account_helpers.settings_core.settings_constants import CONTROLS as CONTROLS
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from debug_utils import LOG_WARNING as LOG_WARNING
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from math_common import decimal_round as decimal_round
_DistRangeSetting: Any
_CAM_YAW_ROUND = 4

class StrategicCamera(CameraWithSettings, CallbackDelayer):
    _DYNAMIC_ENABLED = True
    ABSOLUTE_VERTICAL_FOV: Any
    _SMOOTHING_PIVOT_DELTA_FACTOR = 6.0
    camera: Any
    aimingSystem: Any
    __aimOffset: Any
    isAimOffsetEnabled: Any
    __positionOscillator: Any
    __positionNoiseOscillator: Any
    __activeDistRangeSettings: Any
    __dynamicCfg: Any
    __cameraYaw: Any
    __cameraTiltTan: Any
    __switchers: Any
    __cam: Any
    __curSense: Any
    __onChangeControlMode: Any
    __aimingSystem: Any
    __prevTime: Any
    __autoUpdatePosition: Any
    __dxdydz: Any
    __needReset: Any
    __smoothingPivotDelta: Any
    __transitionEnabled: Any
    __camDist: Any
    __scrollSmoother: Any
    __saveDist: Any
    @staticmethod
    def enableDynamicCamera(enable):
        ...
    @staticmethod
    def isCameraDynamic():
        ...
    def __init__(self, dataSec):
        ...
    def getCurSense(self):
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
    def setMaxDist(self):
        ...
    def getDistRatio(self):
        ...
    def getCurrentCamDist(self):
        ...
    def getCamDistRange(self):
        ...
    def getCamTransitionDist(self):
        ...
    def update(self, dx, dy, dz, rotateMode=True, zoomMode=True, updatedByKeyboard=False):
        ...
    def moveToPosition(self, pos):
        ...
    def calcVisibleAreaRatio(self):
        ...
    def applyImpulse(self, position, impulse, reason=...):
        ...
    def applyDistantImpulse(self, position, impulseValue, reason=...):
        ...
    def __applyNoiseImpulse(self, noiseMagnitude):
        ...
    def writeUserPreferences(self):
        ...
    def __cameraUpdate(self):
        ...
    def _handleSettingsChange(self, diff):
        ...
    def _updateSettingsFromServer(self):
        ...
    def __calcSmoothingPivotDelta(self, deltaTime):
        ...
    def __calcAimOffset(self):
        ...
    def __updateOscillator(self, deltaTime):
        ...
    def __updateCameraYaw(self):
        ...
    def __getPivotPosition(self, pivotHeight):
        ...
    def __getTransitionCamDist(self):
        ...
    def reload(self):
        ...
    def _readConfigs(self, dataSec):
        ...
    def _readBaseCfg(self, dataSec):
        ...
    def _readUserCfg(self):
        ...
    def _makeCfg(self):
        ...
    def __readDynamicDistRangeData(self, dataSec):
        ...
    def __getActiveDistRangeForArena(self):
        ...
    def __getDistRange(self):
        ...
    def __getCameraAcceleration(self):
        ...
    def __getCameraScrollMultiplier(self):
        ...
    def __enableSwitchers(self, updateTransitionEnabled=True):
        ...

def getCameraAsSettingsHolder(settingsDataSec):
    ...
