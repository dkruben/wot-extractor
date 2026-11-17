# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/type.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from inspect import getmembers as getmembers
from enumerations import Enumeration as Enumeration
from enum import IntEnum as IntEnum
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from typing import Any as Any, List as List
from visual_script.misc import EDITOR_TYPE as EDITOR_TYPE, ASPECT as ASPECT
from py2to3.patched_future import with_metaclass as with_metaclass
__all__: tuple

class VScriptType(object):
    @classmethod
    def slotType(cls):
        ...
    @classmethod
    def vs_pyType(cls):
        ...
    @classmethod
    def vs_name(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...
    @classmethod
    def vs_editor(cls):
        ...
    @classmethod
    def vs_equals(cls, a, b):
        ...
    @classmethod
    def vs_toString(cls, value):
        ...
    @classmethod
    def vs_fromString(cls, str_):
        ...
    @classmethod
    def vs_connectionColor(cls):
        ...
    @classmethod
    def vs_iconConnected(cls):
        ...
    @classmethod
    def vs_iconDisconnected(cls):
        ...

class VScriptEnum(object):
    @classmethod
    def slotType(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...
    @classmethod
    def _vs_collectEnumEntries(cls):
        ...
    @classmethod
    def vs_name(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class VScriptStructField(object):
    name: _Any
    type: _Any
    def __init__(self, displayName, fieldType):
        ...
    def __get__(self, instance, owner):
        ...
    def __set__(self, instance, value):
        ...

class AllowVScriptStruct(type):
    def __new__(cls, name, bases, members):
        ...

# base nao representavel no stub: with_metaclass(...)
class VScriptStruct:
    def __new__(cls, *args, **kwargs):
        ...
    @classmethod
    def slotType(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...
    @classmethod
    def vs_module(cls):
        ...
    @classmethod
    def vs_name(cls):
        ...
