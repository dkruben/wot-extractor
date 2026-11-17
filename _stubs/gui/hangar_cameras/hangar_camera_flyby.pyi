# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_cameras/hangar_camera_flyby.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import CGF as CGF
import Math as Math
import math_utils as math_utils
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer, TimeDeltaMeter as TimeDeltaMeter
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
_logger: Any
_MAX_DT = 0.05

# decorador original: @registerComponent
class FlyByComponent(object):
    editorTitle = 'Camera Flyby'
    category = 'Camera'
    domain = CGF.Domain.ClientEditor
    pitch: Any
    distance: Any
    duration: Any

class HangarCameraFlyby(object):
    __slots__: tuple
    __hangarSpace: Any
    __callbackDelayer: Any
    __timeDeltaMeter: Any
    __camera: Any
    __callback: Any
    __isActive: Any
    __timeFromStart: Any
    __yawEasing: Any
    __pitchEasing: Any
    __distEasing: Any
    def __init__(self, camera):
        ...
    @property
    def isActive(self):
        ...
    def fini(self):
        ...
    def activate(self, callback=None):
        ...
    def deactivate(self):
        ...
    def __update(self):
        ...
    def __findFlybyComponent(self):
        ...

class _FlybyEasing(object):
    _start: Any
    _end: Any
    _duration: Any
    def __init__(self, start, goal, duration):
        ...
    def update(self, time):
        ...

class _PitchDistEasing(_FlybyEasing):
    def update(self, time):
        ...

class _YawEasing(_FlybyEasing):
    def update(self, time):
        ...
