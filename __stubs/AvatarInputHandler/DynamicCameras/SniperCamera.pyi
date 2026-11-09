# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/SniperCamera.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
from builtins import range as range
import BigWorld as BigWorld
import GUI as GUI
from Math import Vector2 as Vector2, Vector3 as Vector3, Matrix as Matrix
import BattleReplay as BattleReplay
import Settings as Settings
import constants as constants
import math_utils as math_utils
from AvatarInputHandler import AimingSystems as AimingSystems
from AvatarInputHandler import cameras as cameras, aih_global_binding as aih_global_binding
from BigWorld import SniperAimingSystem as SniperAimingSystem, SniperAimingSystemRemote as SniperAimingSystemRemote
from AvatarInputHandler.DynamicCameras import CameraDynamicConfig as CameraDynamicConfig, CameraWithSettings as CameraWithSettings, calcYawPitchDelta as calcYawPitchDelta
from AvatarInputHandler.DynamicCameras import createCrosshairMatrix as createCrosshairMatrix, createOscillatorFromSection as createOscillatorFromSection, AccelerationSmoother as AccelerationSmoother
from AvatarInputHandler.cameras import readFloat as readFloat, readVec3 as readVec3, ImpulseReason as ImpulseReason, FovExtended as FovExtended
from BattleReplay import CallbackDataNames as CallbackDataNames
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from account_helpers.settings_core.settings_constants import CONTROLS as CONTROLS
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_DEBUG as LOG_DEBUG
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_logger: Any

class SniperCamera(CameraWithSettings, CallbackDelayer):
    _DYNAMIC_ENABLED = True
    _SNIPER_ZOOM_LEVEL = -1
    _FILTER_LENGTH = 5
    _DEFAULT_MAX_ACCELERATION_DURATION = 1.5
    _MIN_REL_SPEED_ACC_SMOOTHING = 0.7
    _DEFAULT_FOV: Any
    _DEFAULT_CLIP_PLANE_SCALE: Any
    camera: Any
    aimingSystem: Any
    __aimOffset: Any
    __zoomFactor: Any
    __impulseOscillator: Any
    __movementOscillator: Any
    __noiseOscillator: Any
    __dynamicCfg: Any
    __accelerationSmoother: Any
    __onChangeControlMode: Any
    __aimingSystem: Any
    __cam: Any
    __prevTime: Any
    __curSense: Any
    __curScrollSense: Any
    __zoom: Any
    __crosshairMatrix: Any
    __waitVehicleCallbackId: Any
    __binoculars: Any
    __defaultAimOffset: Any
    __aimMarkerDistance: Any
    __autoUpdateDxDyDz: Any
    @staticmethod
    def enableDynamicCamera(enable):
        ...
    @staticmethod
    def isCameraDynamic():
        ...
    @staticmethod
    def setSniperZoomSettings(value):
        ...
    def __init__(self, dataSec, defaultOffset=None, binoculars=None):
        ...
    @staticmethod
    def _getConfigsKey():
        ...
    def _getMouseSensitivitySettingKey(self):
        ...
    def _handleSettingsChange(self, diff):
        ...
    def create(self, onChangeControlMode=None):
        ...
    def _aimingSystemClass(self):
        ...
    def destroy(self):
        ...
    def enable(self, targetPos, saveZoom):
        ...
    def disable(self):
        ...
    def update(self, dx, dy, dz, updatedByKeyboard=False):
        ...
    def onRecreateDevice(self):
        ...
    def applyImpulse(self, position, impulse, reason=...):
        ...
    def applyDistantImpulse(self, position, impulseValue, reason=...):
        ...
    def setMaxZoom(self):
        ...
    def __applyNoiseImpulse(self, noiseMagnitude):
        ...
    def __rotateAndZoom(self, dx, dy, dz):
        ...
    def __showVehicle(self, show):
        ...
    def __setupCamera(self, targetPos):
        ...
    def __waitVehicle(self):
        ...
    def __applySerializedZoom(self, zoomFactor):
        ...
    def __updateZoom(self):
        ...
    def __applyZoom(self, zoomFactor):
        ...
    def __updateCrosshairMatrix(self):
        ...
    def __getZooms(self):
        ...
    def __setupZoom(self, dz):
        ...
    def __cameraUpdate(self, allowModeChange=True):
        ...
    def __calcAimOffset(self, aimLocalTransform=None):
        ...
    def __calcCurOscillatorAcceleration(self, deltaTime):
        ...
    def __updateOscillators(self, deltaTime):
        ...
    def __isPositionUnderwater(self, position):
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
    def writeUserPreferences(self):
        ...
    def _updateSettingsFromServer(self):
        ...

def getCameraAsSettingsHolder(settingsDataSec):
    ...
