# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/DebugDrawEntity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from future.utils import viewvalues as viewvalues
from past.builtins import xrange as xrange
import BigWorld as BigWorld
import GUI as GUI
from Math import Vector3 as Vector3, Matrix as Matrix
import math_utils as math_utils
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer

class DebugDrawEntity(BigWorld.Entity):
    BOX_MODEL = 'helpers/models/unit_cube.model'
    SPHERE_MODEL = 'helpers/models/unit_sphere.model'
    objectStates: Any
    reuseModels: Any
    reuse3DTexts: Any
    timer: Any
    def __init__(self):
        ...
    def set_drawObjects(self, prev):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def __update(self):
        ...
    def __createDirectedLine(self, pointA, pointB, width):
        ...
    def __createBox(self, position, rotation, size):
        ...
    def __createSphere(self, position, radius):
        ...
    def __getModel(self, modelName):
        ...
    def __create3DText(self, position, text, color, textSize):
        ...
