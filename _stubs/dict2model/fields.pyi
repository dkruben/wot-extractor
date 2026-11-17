# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dict2model/fields.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import Math as Math
import typing as typing
from datetime import datetime as datetime
from future.utils import viewitems as viewitems
from dict2model import utils as utils
from dict2model import validate as validate
from dict2model.exceptions import ValidationError as ValidationError, ValidationErrorMessage as ValidationErrorMessage, AccessToFieldDeniedError as AccessToFieldDeniedError
from soft_exception import SoftException as SoftException
from dict2model.types import ValidatorsType as ValidatorsType, TFilterParams as TFilterParams
from dict2model.schemas import Schema as Schema, SchemaModelType as SchemaModelType

class AccessDeniedField(object):
    __slots__: tuple
    __nonzero__: Any
    def __bool__(self):
        ...
    def __setattr__(self, *args):
        ...
    def __getattribute__(self, *args):
        ...
    def __eq__(self, *args):
        ...
    def __ne__(self, *args):
        ...
    def __lt__(self, *args):
        ...
    def __le__(self, *args):
        ...
    def __gt__(self, *args):
        ...
    def __ge__(self, *args):
        ...
    def __hash__(self):
        ...
    def __repr__(self):
        ...

class Field(object):
    __slots__: tuple
    required: Any
    default: Any
    filterParams: Any
    _serializedValidators: Any
    _deserializedValidators: Any
    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...
    def serialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def deserialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _serialize(self, incoming, **kwargs):
        ...
    def _deserialize(self, incoming, **kwargs):
        ...

class Boolean(Field):
    _trueValues: set
    _falseValues: set
    __slots__: tuple
    def _serialize(self, incoming, **kwargs):
        ...
    def _deserialize(self, incoming, **kwargs):
        ...
    def _convert(self, incoming):
        ...

class String(Field):
    __slots__: tuple
    def _serialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        ...
    @staticmethod
    def _convert(incoming, skipValidation=False):
        ...

class Number(Field):
    numberType: Any
    __slots__: tuple
    _serializeAsString: Any
    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None, serializeAsString=False):
        ...
    def serialize(self, incoming, **kwargs):
        ...
    def _serialize(self, incoming, **kwargs):
        ...
    def _deserialize(self, incoming, **kwargs):
        ...
    def _convert(self, incoming):
        ...
    @staticmethod
    def _toString(value):
        ...

class Integer(Number):
    numberType: Any
    __slots__: tuple

class Float(Number):
    numberType: Any
    __slots__: tuple

class DateTime(Field):
    __slots__: tuple
    _localtime: Any
    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None, localtime=False):
        ...
    def _serialize(self, incoming, **kwargs):
        ...
    def _deserialize(self, incoming, **kwargs):
        ...

class Url(String):
    __slots__: tuple
    _relative: Any
    _serializedValidators: Any
    _deserializedValidators: Any
    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None, relative=False):
        ...

class NonEmptyString(String):
    __slots__: tuple
    _serializedValidators: Any
    _deserializedValidators: Any
    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...

class StrictEnum(Field):
    __slots__: tuple
    _enumClass: Any
    def __init__(self, enumClass, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...
    def _serialize(self, incoming, **kwargs):
        ...
    def _deserialize(self, incoming, **kwargs):
        ...
    def _convert(self, incoming):
        ...

class IntEnum(StrictEnum):
    __slots__: tuple
    def _convert(self, incoming):
        ...

class StrEnum(StrictEnum):
    __slots__: tuple
    def _convert(self, incoming):
        ...

class Nested(Field):
    __slots__: tuple
    _schema: Any
    def __init__(self, schema, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...
    def _serialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        ...

class List(Field):
    __slots__: tuple
    _fieldOrSchema: Any
    def __init__(self, fieldOrSchema, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...
    def _serialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _convert(self, incoming, skipValidation, converter, **kwargs):
        ...

class UniCapList(List):
    __slots__: tuple
    def _convert(self, incoming, skipValidation, converter, **kwargs):
        ...

class Dict(Field):
    __slots__: tuple
    _keyFieldOrSchema: Any
    _valueFieldOrSchema: Any
    def __init__(self, keyFieldOrSchema, valueFieldOrSchema, required=True, default=..., filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...
    def _serialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _convert(self, incoming, skipValidation, keyConverter, valueConverter, **kwargs):
        ...

class HexColorCode(String):
    COLOR_CODE_RE = '^#[A-Fa-f0-9]{6}$'
    __slots__: tuple
    _serializedValidators: Any
    _deserializedValidators: Any
    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...

class ListFromString(Field):
    __slots__: tuple
    _delimiter: Any
    _listOfFields: Any
    _stringField: Any
    def __init__(self, field, delimiter=None, required=True, default=..., filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...
    def _serialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _deserialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _splitString(self, string):
        ...

class Vector2(ListFromString):
    __slots__: tuple
    _vectorClass = Math.Vector2
    _zeroVector: tuple
    _deserializedValidators: Any
    def __init__(self, required=True, default=None, filterParams=None, serializedValidators=None, deserializedValidators=None):
        ...
    def deserialize(self, incoming, skipValidation=False, **kwargs):
        ...
    def _serialize(self, incoming, skipValidation=False, **kwargs):
        ...

class Vector3(Vector2):
    __slots__: tuple
    _vectorClass = Math.Vector3
    _zeroVector: tuple

class Vector4(Vector2):
    __slots__: tuple
    _vectorClass = Math.Vector4
    _zeroVector: tuple
