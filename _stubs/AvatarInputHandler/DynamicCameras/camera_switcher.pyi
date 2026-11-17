# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/camera_switcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import typing as typing
from enum import Enum as Enum
import BigWorld as BigWorld
import math_utils as math_utils
TRANSITION_DIST_HYSTERESIS = 0.01

class SwitchTypes(Enum):
    FROM_MAX_DIST = 0
    FROM_MIN_DIST = 1
    FROM_TRANSITION_DIST_AS_MAX = 2
    FROM_TRANSITION_DIST_AS_MIN = 3

class SwitchToPlaces(Enum):
    TO_RELATIVE_POS = 0
    TO_TRANSITION_DIST = 1
    TO_NEAR_POS = 2

class CameraSwitcher(object):
    _TIMEOUT_TIME = 0.35
    _INTERVAL_TO_SWITCH = 0.2
    __slots__: tuple
    __switchType: Any
    __switchToName: Any
    __switchToPos: Any
    __lastDist: Any
    __hasTimeout: Any
    __timeoutCallback: Any
    __timeoutTime: Any
    __intervalToSwitch: Any
    __lastScrollTime: Any
    __switchToPlaceType: Any
    def __init__(self, switchType, switchToName, switchToPos, intervalToSwitch=..., timeoutTime=...):
        ...
    def clear(self):
        ...
    def getSwitchParams(self):
        ...
    def needToSwitch(self, zValue, dist, minValue, maxValue, transitionValue=None):
        ...
    def getDistLimitationForSwitch(self, minValue, maxValue, transitionValue):
        ...
    def __clearTimeout(self):
        ...
    def __setTimeout(self):
        ...
    def __switchFromDist(self, zValue, dist, value):
        ...

class CameraSwitcherCollection(object):
    __cameraSwitchers: Any
    __isEnabled: Any
    __switchParams: Any
    def __init__(self, cameraSwitchers, isEnabled=True):
        ...
    def clear(self):
        ...
    def setIsEnabled(self, isEnabled):
        ...
    def getSwitchParams(self):
        ...
    def isEnabled(self):
        ...
    def needToSwitch(self, zValue, dist, minValue, maxValue, transitionValue=None):
        ...
    def getDistLimitationForSwitch(self, minValue, maxValue, transitionValue):
        ...
