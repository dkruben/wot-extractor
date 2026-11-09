# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/arcade_camera_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from collections import namedtuple as namedtuple
import math as math
import time as time
import math_utils as math_utils
from AvatarInputHandler.cameras import readFloat as readFloat, readVec2 as readVec2, readInt as readInt, readString as readString
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
LINEAR_EASING = math_utils.Easing.linearEasing
SQUARE_EASING = math_utils.Easing.squareEasing
EXPONENTIAL_EASING = math_utils.Easing.exponentialEasing
EASING_FUNCTION_MAP: dict
MinMax: Any
ZoomState: Any

class EScrollDir(Enum):
    IN = 0
    OUT = 1
    @staticmethod
    def convertDZ(dz):
        ...

class OverScrollProtector(object):
    __slots__: tuple
    __interval: Any
    __lastScrollTime: Any
    __eScrollDirection: Any
    def __init__(self):
        ...
    def start(self, interval, eScrollDirection):
        ...
    def updateOnScroll(self, eScrollDirection):
        ...
    def isProtecting(self):
        ...
    def reset(self):
        ...

class ZoomStateSwitcher(object):
    __slots__: tuple
    __settings: Any
    _NONE_INDEX = -1
    __zoomStates: Any
    __index: Any
    __currentZoomState: Any
    def __init__(self):
        ...
    def __iter__(self):
        ...
    def loadConfig(self, dataSection):
        ...
    def isEmpty(self):
        ...
    def reset(self):
        ...
    def switchToState(self, stateName):
        ...
    def getNextState(self):
        ...
    def getPrevState(self):
        ...
    def setCurrentState(self, zoomState):
        ...
    def getCurrentState(self):
        ...
    def __getState(self, func, startIndex):
        ...
    def __isIndexValid(self, index):
        ...
    def __isEnabledBySettings(self, index):
        ...

class CollideAnimatorEasing(object):
    __easing: Any
    def __init__(self):
        ...
    def start(self, distance, interval):
        ...
    def update(self, deltaTime):
        ...
    def stop(self):
        ...

def readAngle(dataSec, name, minVal, maxVal, defaultVal):
    ...
def readEasing(dataSec, name, minVal, maxVal, defaultVal):
    ...
def readZoomState(dataSec):
    ...
