# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/xml_config_specs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import json as json
from Math import Vector2 as Vector2, Vector3 as Vector3, Vector4 as Vector4
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Any as Any
from ResMgr import DataSection as DataSection

class IParam(object):
    def read(self, section, name=''):
        ...

class SimpleParam(IParam):
    _DEFAULT = None
    _SIMPLE_METHOD = None
    _name: _Any
    _default: _Any
    def __init__(self, default=None, name=None):
        ...
    @property
    def name(self):
        ...
    @property
    def default(self):
        ...
    def read(self, section, name=''):
        ...
    def _read(self, section, name):
        ...

class IntParam(SimpleParam):
    _DEFAULT = 0
    _SIMPLE_METHOD = 'readInt'

class BoolParam(SimpleParam):
    _DEFAULT = False
    _SIMPLE_METHOD = 'readBool'

class FloatParam(SimpleParam):
    _DEFAULT = 0.0
    _SIMPLE_METHOD = 'readFloat'

class StrParam(SimpleParam):
    _DEFAULT = ''
    _SIMPLE_METHOD = 'readString'

class Vector2Param(SimpleParam):
    _DEFAULT: _Any
    _SIMPLE_METHOD = 'readVector2'

class Vector3Param(SimpleParam):
    _DEFAULT: _Any
    _SIMPLE_METHOD = 'readVector3'

class Vector4Param(SimpleParam):
    _DEFAULT: _Any
    _SIMPLE_METHOD = 'readVector4'

class JsonParam(SimpleParam):
    def _read(self, section, name):
        ...

class ListParam(SimpleParam):
    _DEFAULT: list
    _itemName: _Any
    _valueParam: _Any
    def __init__(self, valueParam=..., itemName='item', name=None):
        ...
    def _read(self, section, name):
        ...

class DictParam(SimpleParam):
    _DEFAULT: dict
    _itemName: _Any
    _keyParam: _Any
    _valueParam: _Any
    def __init__(self, valueParam=..., keyParam=..., itemName='item', name=None):
        ...
    def _read(self, section, name):
        ...

class ObjParam(SimpleParam):
    _DEFAULT: _Any
    _specs: _Any
    class Obj(object):
        ...
    def __init__(self, name=None, **specs):
        ...
    def _read(self, section, name):
        ...

class EnumParam(StrParam):
    _enum: _Any
    _defaultValue: _Any
    def __init__(self, enum, default, name=None):
        ...
    def _read(self, section, name):
        ...
