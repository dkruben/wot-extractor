# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/StrategicCamerasInterpolator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
import math_utils as math_utils
from Event import EventManager as EventManager, Event as Event
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_EASING_METHOD = math_utils.easeInOutQuad
_INTERPOLATION_TIME = 0.2

class StrategicCamerasInterpolator(CallbackDelayer):
    __totalInterpolationTime: Any
    __elapsedTime: Any
    __easingMethod: Any
    __prevTime: Any
    __initialState: Any
    __finalState: Any
    __initialFov: Any
    __finalFov: Any
    __cam: Any
    _eventManager: Any
    onInterpolationStart: Any
    onInterpolationStop: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def enable(self, initialState, finalState, initialFov, finalFov):
        ...
    def __setupCamera(self):
        ...
    def disable(self):
        ...
    def __cameraUpdate(self):
        ...
