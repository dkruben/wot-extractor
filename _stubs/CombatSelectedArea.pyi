# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/CombatSelectedArea.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
import math_utils as math_utils
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
OVER_TERRAIN_HEIGHT = 0.5
MARKER_HEIGHT = 5.0
DEFAULT_RADIUS_MODEL = 'content/Interface/CheckPoint/CheckPoint.visual'
DEFAULT_ROTATE_MODEL = 'content/Interface/TargetPoint/rectangle2_1.visual'
COLOR_WHITE = 4294967295

class CombatSelectedArea(object):
    position: Any
    area: Any
    __terrainSelectedArea: Any
    __pixelQuad: Any
    __terrainRotatedArea: Any
    __fakeModel: Any
    __overTerrainHeight: Any
    __matrix: Any
    __rotateModelNode: Any
    __color: Any
    __size: Any
    __enableConstrainToArenaBounds: Any
    __area: Any
    __nextPosition: Any
    __speed: Any
    __time: Any
    def __init__(self, enableConstrainToArenaBounds=False):
        ...
    def updateSize(self, size):
        ...
    def setup(self, position, direction, size, visualPath, color, marker):
        ...
    def addLine(self, position, color, width, height):
        ...
    def setSelectingDirection(self, value=False):
        ...
    def setConstrainToArenaBounds(self, enable):
        ...
    def setOverTerrainOffset(self, offset):
        ...
    def relocate(self, position, direction):
        ...
    def setGUIVisible(self, isVisible):
        ...
    def setNextPosition(self, nextPosition, direction):
        ...
    def update(self, deltaTime):
        ...
    def setupDefault(self, position, direction, size, marker):
        ...
    def destroy(self):
        ...
    def pointInside(self, point):
        ...
    def pointInsideCircle(self, point, radius):
        ...
    def setColor(self, color=None):
        ...
    def enableAccurateCollision(self, isEnabled):
        ...
    def enableWaterCollision(self, isEnabled):
        ...
    def setMaxHeight(self, height):
        ...
