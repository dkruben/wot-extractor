# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/coordinate_system.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Math import Vector2 as Vector2, Vector3 as Vector3
ASSERT_EPS = 0.001

class CoordinateSystem2D(object):
    _origin: Any
    _direction1: Any
    _direction2: Any
    def __init__(self, origin, direction1, direction2=None):
        ...
    def transform(self, point):
        ...
    def invTransform(self, transformedPoint):
        ...
    def translateByTransformedVector(self, point, transformedVector):
        ...

class AXIS_ALIGNED_DIRECTION:
    PLUS_Z = 0
    MINUS_Z = 1
    PLUS_X = 2
    MINUS_X = 3
    RANGE: tuple
    FROM_NAME: dict
    TO_COORDINATES: dict
    OPPOSITE: dict
    @staticmethod
    def toVector(direction):
        ...
    @staticmethod
    def getBoundingBoxSegmentByDirection(bounds, dir):
        ...
    @staticmethod
    def getBoundingBoxSegmentByDirection3D(bounds, dir):
        ...
    @staticmethod
    def __getBoundingBoxSegmentByDirectionInternal(bounds, direction):
        ...

def getSomeOrthogonalVector2(vector):
    ...
def getBoundsFromHullPoints(hullPoints):
    ...
