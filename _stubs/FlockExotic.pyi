# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/FlockExotic.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import random as random
from functools import partial as partial
import BigWorld as BigWorld
import Math as Math
import AnimationSequence as AnimationSequence
import FlockManager as FlockManager
from Flock import FlockLike as FlockLike
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
_MATH_2PI: Any

class FlockExotic(BigWorld.Entity, FlockLike, CallbackDelayer):
    flightAngleMin: Any
    flightAngleMax: Any
    __isTriggered: Any
    __models: Any
    models: Any
    def __init__(self):
        ...
    def prerequisites(self):
        ...
    def __createMotor(self, positionStart, positionEnd, speed, flightTime):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def name(self):
        ...
    def __loadModels(self, prereqs):
        ...
    def __removeModels(self):
        ...
    def __removeModel(self, model):
        ...
    def __getRandomSpawnPos(self):
        ...
    def __getRandomTargetPos(self, startPos):
        ...
    def onTrigger(self):
        ...
