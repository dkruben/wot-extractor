# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serialization/component_bin_deserializer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
from past.builtins import xrange as xrange
from typing import Dict as Dict, Type as Type
import varint as varint
from constants import IS_EDITOR as IS_EDITOR
from py2to3.moves.io import FastBytesIO as FastBytesIO
from serialization.definitions import FieldFlags as FieldFlags, FieldTypes as FieldTypes
from serialization.exceptions import SerializationException as SerializationException, FoundItemException as FoundItemException
from serialization.serializable_component import SerializableComponent as SerializableComponent
__all__: tuple

class ComponentBinDeserializer(object):
    __stream: Any
    customTypes: Any
    def __init__(self, customTypes):
        ...
    def decode(self, data):
        ...
    def hasItem(self, data, path, value):
        ...
    def __decodeCustomType(self, itemType, path=None, wanted=None):
        ...
    def __decodeArray(self, itemType, k, path, next, wanted):
        ...
    def __decodeString(self):
        ...
