# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/PhysicsTurretShape.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import collections as collections
from builtins import open as open
from future.utils import listvalues as listvalues, viewvalues as viewvalues, viewitems as viewitems
from past.builtins import xrange as xrange
import Math as Math
from py2to3.compat.ioCompat import UnicodeFileAdapter as UnicodeFileAdapter
from py2to3.patched_future import with_metaclass as with_metaclass
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass
_DEBUG_WITH_SVG = False

# base nao representavel no stub: with_metaclass(...)
class PhysicsTurretShape:
    PARAMS_DESC: dict
    PARAM_NAME_BY_INDEX: Any
    __polys: Any
    __params: Any
    __box: Any
    __isDirty: Any
    __isSetParams: Any
    def __init__(self, bbMin=None, bbMax=None):
        ...
    def resetParams(self):
        ...
    def getIsDirty(self):
        ...
    def getIsSetParams(self):
        ...
    def setTurretBox(self, bbMin, bbMax):
        ...
    def setParam(self, name, value):
        ...
    def setParamByIndex(self, index, value):
        ...
    def setParams(self, params):
        ...
    def getParam(self, name):
        ...
    def getParamsValues(self):
        ...
    def getPolygons(self):
        ...
    def __recalcPolys(self):
        ...

class _Scene:
    name: Any
    items: Any
    height: Any
    width: Any
    svgname: Any
    def __init__(self, name='scene', height=400, width=400):
        ...
    def add(self, item):
        ...
    def strarray(self):
        ...
    def write_svg(self, filename=None):
        ...
    def display(self, prog='explorer'):
        ...

class _Line:
    start: Any
    end: Any
    def __init__(self, start, end):
        ...
    def strarray(self):
        ...

def _intersectPlaneSegment(planePt, planeN, seg1, seg2):
    ...
def createPhysicsTurretShape(bbMin, bbMax):
    ...
