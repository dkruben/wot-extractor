# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serialization/definitions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import enum as enum
from constants import IS_EDITOR as IS_EDITOR
__all__: tuple
FieldType: Any

class FieldTypes(object):
    VARINT = 2
    TAGS = 4
    OPTIONS_ENUM = 8
    FLOAT = 16
    APPLY_AREA_ENUM = 32
    TYPED_ARRAY = 64
    CUSTOM_TYPE_OFFSET = 128
    STRING = 512

# decorador original: @enum.unique
class FieldFlags(enum.IntEnum):
    NONE = 0
    DEPRECATED = 1
    WEAK_EQUAL_IGNORED = 2
    NON_XML = 4
    NON_BIN = 8
    NON_SERIALIZABLE: Any
    SAVE_AS_STRING = 16
    SAVE_AS_EDITOR_ONLY = 32
