# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/LightingGenerationMode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
import math as math
import BigWorld as BigWorld
import GUI as GUI
import Keys as Keys
import Math as Math
import ResMgr as ResMgr
import WWISE as WWISE
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from helpers import game_mode_emulator as game_mode_emulator
g_lightGenModeEnabled = False
g_currentMoveRate = 0.5
g_gui = None
g_enableCameraInput = False
MOVE_SPEED_MAX = 200.0
MOVE_SPEED_POW = 2.0
MOVE_SPEED_ADJUST = 0.1
FOV_ADJUST: Any
FOV_MIN: Any
FOV_MAX: Any
SCRIPT_ARG_NAME = 'lightingGen'
MOUSE_TOGGLE_KEYS: list
PROFILE_CAMERA_TRANSFORMS_XML_NAME = 'scripts/profile_camera_transforms.xml'
g_cameraTransforms: list
g_curCameraTransform = 0

class CameraTransform:
    matrix: Any
    def __init__(self, matrix):
        ...
    def apply(self):
        ...

def _clampCameraTransformIdx(val):
    ...
def _loadCameraTransforms():
    ...
def _setCameraTransform(idx):
    ...
def enabled():
    ...
def onStartup():
    ...
def _clearGUI():
    ...
def _displayGUI(text):
    ...
def _close():
    ...
def _tick():
    ...
def _startLightingGeneration():
    ...
def _offlineLoadCheck():
    ...
def launch(spaceName):
    ...
def adjustSpeed(diff):
    ...
def adjustFOV(diff):
    ...
def handleKeyEvent(event):
    ...
def handleMouseEvent(event):
    ...
