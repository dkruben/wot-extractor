# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/Flock.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import random as random
from past.builtins import xrange as xrange
import math_utils as math_utils
import BigWorld as BigWorld
import Math as Math
import ResMgr as ResMgr
import SoundGroups as SoundGroups
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
from Math import Vector3 as Vector3
import AnimationSequence as AnimationSequence
ENVIRONMENT_EFFECTS_CONFIG_FILE = 'scripts/environment_effects.xml'

class DebugGizmo(object):
    model: Any
    motor: Any
    def __init__(self, modelName='helpers/models/position_gizmo.model'):
        ...
    def __del__(self):
        ...
    def visible(self, show):
        ...
    def attachTo(self, model):
        ...
    def attachToMatrix(self, matrix):
        ...
    def attachToPosition(self, pos):
        ...
    def setMatrix(self, matrix):
        ...

class DebugLine(object):
    thickness: Any
    __thickness: Any
    model: Any
    motor: Any
    start: Any
    end: Any
    def _setThickness(self, value):
        ...
    def __init__(self, start, end):
        ...
    def __del__(self):
        ...
    def set(self, start, end):
        ...

class DebugPolyLine(object):
    lines: Any
    def __init__(self):
        ...
    def set(self, points):
        ...

class FlockLike(object):
    __SoundNames = None
    MAX_DIST_SQ = 10000
    __sound: Any
    _animators: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _getModelsToLoad(self):
        ...
    def _loadModels(self, prereqs, spaceID):
        ...
    def _addSound(self, model, soundName=''):
        ...
    def _delSound(self):
        ...

class Flock(BigWorld.Entity, FlockLike):
    STRATEGY_USUAL_FLY = 0
    STRATEGY_FLY_AROUND_CW = 1
    STRATEGY_FLY_AROUND_CCW = 2
    HEIGHT_CHANGE_DECISION_COUNT = 3
    HEIGHT_CHANGE_SPEED_MULTIPLIER = 1.1
    HEIGHT_DISPERSION_CORRIDOR = 0.05
    CIRCLE_FLIGHT_ABOVE = 0.5
    CIRCLE_FLIGHT_PROBABILITY = 0.25
    __SoundNames = None
    __decisionCallbackId: Any
    __decisionCount: Any
    __decisionStrategy: Any
    filter: Any
    middlePosition: Any
    minHeight: Any
    maxHeight: Any
    _animators: Any
    models: Any
    deadZoneRadius: Any
    def __init__(self):
        ...
    def prerequisites(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def set_state(self, oldState):
        ...
    def boidsLanded(self):
        ...
    def name(self):
        ...
    def __setupFlyAroundCenter(self):
        ...
    def __doUsualFly(self):
        ...
    def __doAroundCenterFly(self):
        ...
    def __makeDecision(self):
        ...

def _addModelToScene(model):
    ...
def _delModelFromScene(model):
    ...
