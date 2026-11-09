# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/OfflineMode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import logging as logging
import sys as sys
import BigWorld as BigWorld
import GUI as GUI
import Keys as Keys
import Math as Math
import ResMgr as ResMgr
import WWISE as WWISE
from helpers import game_mode_emulator as game_mode_emulator
_logger: Any
g_offlineModeEnabled = False
g_offlineModeSpaceLoaded = False
g_currentMoveRate = 0.5
g_gui = None
MOVE_SPEED_MAX = 200.0
MOVE_SPEED_POW = 2.0
MOVE_SPEED_ADJUST = 0.1
FOV_ADJUST: Any
FOV_MIN: Any
FOV_MAX: Any
MOUSE_TOGGLE_KEYS: list
SPACE_LOAD_EPS = 0.0001
CAMERAS_XML_NAME: Any
g_cameraTransforms: list
g_curCameraTransform = 0
INSTRUCTIONS: str

class CameraTransform(object):
    matrix: Any
    def __init__(self, matrix):
        ...
    def apply(self):
        ...

def _clampCameraTransformIdx(val):
    ...
def _loadCameraTransforms():
    ...
def _saveCameraTransforms():
    ...
def _addCameraTransform():
    ...
def _setCameraTransform(idx):
    ...
def enabled():
    ...
def isSpaceLoaded():
    ...
def onStartup():
    ...
def _clearGUI():
    ...
def _displayGUI(spaceName):
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
