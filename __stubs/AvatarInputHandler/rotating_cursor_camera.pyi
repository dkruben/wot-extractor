# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/rotating_cursor_camera.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import BigWorld as BigWorld
import math_utils as math_utils

class RotatingCoursorCamera(object):
    __camera: Any
    __minPitch: Any
    __maxPitch: Any
    __minDist: Any
    __maxDist: Any
    __sensitivity: Any
    __maxDistHalfLife: Any
    __pivotOffset: Any
    def __init__(self, cfg):
        ...
    @property
    def sourceMatrix(self):
        ...
    @property
    def pivotDistance(self):
        ...
    @property
    def aimingSystem(self):
        ...
    def setup(self, targetPosition, initialRotations, distanceToTarget):
        ...
    def move(self, rotations, distance):
        ...
    def destroy(self):
        ...
    def handleMouseEvent(self, dx, dy, dz):
        ...
    def clampDistance(self, value):
        ...
    def __createCamera(self):
        ...
