# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/frameworks/wulf/view/view_event.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing

class Position2D(object):
    __slots__: tuple
    __positionX: Any
    __positionY: Any
    def __init__(self, x=0, y=0):
        ...
    @property
    def positionX(self):
        ...
    @property
    def positionY(self):
        ...

class BoundingBox(Position2D):
    __slots__: tuple
    __width: Any
    __height: Any
    def __init__(self, x=0, y=0, width=0, height=0):
        ...
    @property
    def width(self):
        ...
    @property
    def height(self):
        ...

class ViewEvent(object):
    __slots__: tuple
    __core: Any
    def __init__(self, core):
        ...
    def __repr__(self):
        ...
    @property
    def eventType(self):
        ...
    @property
    def decoratorID(self):
        ...
    @property
    def contentID(self):
        ...
    @property
    def isOn(self):
        ...
    @property
    def mouse(self):
        ...
    @property
    def bbox(self):
        ...
    @property
    def direction(self):
        ...
    def hasArgument(self, name):
        ...
    def getArgument(self, name, default=None):
        ...
    @property
    def targetViewID(self):
        ...
