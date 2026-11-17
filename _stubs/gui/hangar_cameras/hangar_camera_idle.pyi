# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_cameras/hangar_camera_idle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import BigWorld as BigWorld
import Math as Math
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer, TimeDeltaMeter as TimeDeltaMeter
import math_utils as math_utils
from account_helpers.settings_core.settings_constants import GAME as GAME
import gui.hangar_cam_settings as settings
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from .hangar_camera_settings_listener import HangarCameraSettingsListener as HangarCameraSettingsListener

class HangarCameraIdle(HangarCameraSettingsListener, CallbackDelayer, TimeDeltaMeter):
    TIME_OUT = 0.8
    MAX_DT = 0.05
    __camera: Any
    __easingInTime: Any
    __pitchParams: Any
    __distParams: Any
    __yawPeriod: Any
    __yawSpeed: Any
    __currentIdleTime: Any
    __camPeriod: Any
    __isForcedDisabled: Any
    __disabledCount: Any
    __isActive: Any
    __isInitialized: Any
    minValue: Any
    maxValue: Any
    period: Any
    startTime: Any
    startValue: Any
    speed: Any
    class IdleParams(object):
        minValue: Any
        maxValue: Any
        period: Any
        startTime: Any
        startValue: Any
        speed: Any
        def __init__(self):
            ...
    def __init__(self, camera):
        ...
    def destroy(self):
        ...
    def initialize(self, easingInTime, pitchParams, distParams, yawPeriod):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def isActive(self):
        ...
    def setStartDelay(self, delay):
        ...
    def _onHangarCamPeriodChanged(self):
        ...
    def __onCameraForceDisable(self, event):
        ...
    def __getHangarCamPeriodSetting(self):
        ...
    def __startCameraIdle(self):
        ...
    def __updateIdleMovement(self):
        ...
    def __updateValue(self, params):
        ...
    def __sinValue(self, params):
        ...
    def __setCameraParams(self, yaw, pitch, dist):
        ...
    def __updateEasingOut(self):
        ...
    def __easeOutValue(self, startSpeed, prevValue, dt):
        ...
    def __setStartParams(self, params):
        ...
    def __stopCameraIdle(self):
        ...
