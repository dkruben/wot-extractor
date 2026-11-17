# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/dictionary_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from past.builtins import long as long
from future.moves import pickle as pickle
from Math import Vector2 as Vector2, Vector3 as Vector3, Vector4 as Vector4, Matrix as Matrix
from debug_utils import LOG_ERROR as LOG_ERROR
from py2to3.compat import base64compat as base64compat
from visual_script.block import Block as Block, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue, Meta as Meta
from visual_script.misc import ASPECT as ASPECT, errorVScript as errorVScript, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.type import VScriptType as VScriptType
ALLOWED_DATA_TYPES: dict

class DictionaryMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class Dictionary(VScriptType, dict):
    def __init__(self, storage=None):
        ...
    @classmethod
    def vs_toString(cls, value):
        ...
    @classmethod
    def vs_fromString(cls, str_):
        ...
    @classmethod
    def vs_aspects(cls):
        ...
    @classmethod
    def vs_connectionColor(cls):
        ...

class EmptyDictionary(Block, DictionaryMeta):
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _get(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class AddToDictionary(Block, DictionaryMeta):
    _valueType: Any
    _isArray: Any
    _in: Any
    _dict: Any
    _key: Any
    _value: Any
    _override: Any
    _out: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    def captionText(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class IsInDictionary(Block, DictionaryMeta):
    _valueType: Any
    _isArray: Any
    _dict: Any
    _key: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _checkKey(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    def captionText(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetFromDictionary(Block, DictionaryMeta):
    _valueType: Any
    _isArray: Any
    _dict: Any
    _key: Any
    _value: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getArrayValue(self):
        ...
    def _getValue(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    def captionText(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class RemoveFromDictionary(Block, DictionaryMeta):
    _valueType: Any
    _isArray: Any
    _in: Any
    _dict: Any
    _key: Any
    _out: Any
    _res: Any
    _value: Any
    def __init__(self, *args, **kwargs):
        ...
    def _executeArray(self):
        ...
    def _executeValue(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    def captionText(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetKeysFromDictionary(Block, DictionaryMeta):
    _dict: Any
    _keys: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getKeys(self):
        ...
    def captionText(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...
