# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/minimap_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import math as math
import string as string
from past.utils import old_div as old_div
import BigWorld as BigWorld
import Math as Math
import math_utils as math_utils
from constants import AOI as AOI
AOI_TO_FAR_TIME = 5.0
MINIMAP_SIZE: tuple
EPIC_MINIMAP_HIT_AREA = 210
_METERS_TO_KILOMETERS = 0.001
_MAX_SIZE_INDEX = 5

def isVehicleInAOI(matrix, estimateRadius):
    ...
def getPositionByLocal(localX, localY, bottomLeft, upperRight):
    ...
def makePositionMatrix(position):
    ...
def makeScaleMatrix(scale):
    ...
def makePositionAndScaleMatrix(position, scale):
    ...
def makePointInBBoxMatrix(position, bottomLeft, upperRight):
    ...
def makePointMatrixByLocal(localX, localY, bottomLeft, upperRight):
    ...
def metersToMinimapPixels(minSize, maxSize):
    ...
def getCellIdFromPosition(desiredShotPoint, boundingBox, dimensions):
    ...
def getPositionByCellIndex(cellIndex, bottomLeft, upperRight, dimensions):
    ...
def getCellName(cellId, dimensions):
    ...
def getMinimapBasePingScale(minimapSizeIndex, minScale, maxScale):
    ...
