# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/DebugManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING, Iterable as Iterable, Dict as Dict
from Math import Vector2 as Vector2, Vector3 as Vector3
DebugManagerImpl = None

class COLORS(object):
    GREEN = 1996554018
    DARK_GREEN = 2147516501
    DARK_BLUE = 4278190335
    WHITE = 4294967295
    BLUE = 3137404927
    RED = 4289864226
    ZERO = 0
    DEFAULT = BLUE

def _impl(f):
    ...
# decorador original: @_impl
def registerObject(groupID, name):
    ...
# decorador original: @_impl
def clearObject(groupID, name):
    ...
# decorador original: @_impl
def isGroupEnabled(groupID):
    ...
# decorador original: @_impl
def setGroupEnabled(groupID, isEnabled):
    ...
# decorador original: @_impl
def removeObject(groupID, name):
    ...
# decorador original: @_impl
def removeGroup(groupID):
    ...
# decorador original: @_impl
def showMessage(groupID, name, value):
    ...
# decorador original: @_impl
def showText3D(groupID, name, info, position=..., entityID=None):
    ...
# decorador original: @_impl
def showText2D(groupID, name, text, position, isPixels=False, color=...):
    ...
# decorador original: @_impl
def showPoint2D(groupID, name, positions, isPixels=False, color=...):
    ...
# decorador original: @_impl
def showLine2D(groupID, name, positions, isLabel=False, isPixels=False, color=...):
    ...
# decorador original: @_impl
def showCircle2D(groupID, name, center, radius, isPixels=False, color=...):
    ...
# decorador original: @_impl
def showRectangle2D(groupID, name, start, end, isPixels=False, color=...):
    ...
# decorador original: @_impl
def showLine3D(groupID, name, positions, entityID=None, isArrow=False, color=...):
    ...
# decorador original: @_impl
def showPoint3D(groupID, name, positions, entityID=None, color=...):
    ...
# decorador original: @_impl
def showBox3D(groupID, name, center, direction=..., size=..., entityID=None, color=...):
    ...
# decorador original: @_impl
def showCircle3D(groupID, name, center, radius, entityID=None, normal=..., color=..., segments=36):
    ...
# decorador original: @_impl
def showSphere(groupID, name, center, radius, entityID=None, color=...):
    ...
# decorador original: @_impl
def showCylinder(groupID, name, start, end, radius, entityID=None, color=...):
    ...
