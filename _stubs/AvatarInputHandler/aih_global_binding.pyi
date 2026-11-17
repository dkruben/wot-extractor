# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/aih_global_binding.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
import Math as Math
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME, GUN_MARKER_FLAG as GUN_MARKER_FLAG, STRATEGIC_CAMERA as STRATEGIC_CAMERA, DEFAULT_GUN_MARKER_STATE as DEFAULT_GUN_MARKER_STATE
from soft_exception import SoftException as SoftException
_logger: Any
_FLOAT_EPSILON = 0.003
_DEFAULT_VALUES: dict

class BINDING_ID(object):
    CTRL_MODE_NAME = 1
    AIM_OFFSET = 2
    ZOOM_FACTOR = 3
    GUN_MARKERS_FLAGS = 4
    CLIENT_GUN_MARKER_STATE = 5
    SERVER_GUN_MARKER_STATE = 6
    DUAL_ACC_GUN_MARKER_STATE = 7
    CLIENT_GUN_MARKER_DATA_PROVIDER = 8
    CLIENT_SPG_GUN_MARKER_DATA_PROVIDER = 9
    SERVER_GUN_MARKER_DATA_PROVIDER = 10
    SERVER_SPG_GUN_MARKER_DATA_PROVIDER = 11
    DUAL_ACC_GUN_MARKER_DATA_PROVIDER = 12
    STRATEGIC_CAMERA = 13
    MULTI_GUN_COLLISIONS = 14
    SPG_SHOTS_INDICATOR_STATE = 15
    RANGE: tuple

class _Observable(object):
    value: Any
    __subscribers: Any
    def __init__(self, value):
        ...
    def clear(self):
        ...
    def subscribe(self, subscriber):
        ...
    def unsubscribe(self, subscriber):
        ...
    def change(self, other):
        ...
    def _isChanged(self, other):
        ...

class _ObservableVector2(_Observable):
    def __init__(self):
        ...
    def _isChanged(self, other):
        ...

class _GlobalDataDescriptor(object):
    __slots__: tuple
    __storage: dict
    __bindingID: Any
    __reader: Any
    __writer: Any
    def __init__(self, bindingID, reader=False, writer=False):
        ...
    def __set__(self, instance, value):
        ...
    def __get__(self, instance, _=None):
        ...
    @classmethod
    def clear(cls):
        ...
    @classmethod
    def subscribe(cls, bindingID, subscriber):
        ...
    @classmethod
    def unsubscribe(cls, bindingID, subscriber):
        ...

def bindRO(bindingID):
    ...
def bindRW(bindingID):
    ...
def subscribe(bindingID, observer):
    ...
def unsubscribe(bindingID, observer):
    ...
def clear():
    ...
