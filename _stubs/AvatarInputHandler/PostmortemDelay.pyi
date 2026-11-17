# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/PostmortemDelay.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import BigWorld as BigWorld
import Math as Math
import math_utils as math_utils
from AvatarInputHandler.DynamicCameras.ArcadeCamera import ArcadeCamera as ArcadeCamera
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_DEBUG as LOG_DEBUG

class PostmortemDelay(object):
    FADE_DELAY_TIME = 2.0
    KILLER_VISION_TIME = 5.0
    KILLER_VEHICLE_CAMERA_DISTANCE = 15.0
    KILLER_VEHICLE_CAMERA_PIVOT_SETTINGS: tuple
    KILLER_VEHICLE_PITCH_OFFSET = -0.3
    __killerVehicleID: Any
    __bActive: Any
    __mouseInputEnabled: Any
    __bChoiceWindowActive: Any
    __bFadeScreenActive: Any
    __bKillerVisionActive: Any
    __savedPivotSettings: Any
    __savedCameraDistance: Any
    __savedYawPitch: Any
    __arcadeCamera: Any
    __onKillerVisionStart: Any
    __onStop: Any
    __cbIDWait: Any
    __enableKillerVision: Any
    def __init__(self, arcadeCamera, onKillerVisionStart, onStop, enableKillerVision=True):
        ...
    def destroy(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
    def __fadeScreen(self, bFade=True):
        ...
    def __showChoiceWindow(self, bShow=True):
        ...
    def __moveCameraTo(self, vehicleID, sourceVehicleID=None):
        ...
    def __setCameraSettings(self, targetMP=None, pivotSettings=None, cameraDistance=None, yawPitch=None):
        ...
    def __tryStartKillerVision(self):
        ...
    def __startKillerVision(self):
        ...
    def __onKillerVisionFinished(self):
        ...
    def __onContinueBattle(self):
        ...
    def __onVehicleLeaveWorld(self, vehicle):
        ...
    def __onRoundFinished(self, period, *args):
        ...
    def __cancelWait(self):
        ...
