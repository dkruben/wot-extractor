# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serialization/component_bin_serializer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import iteritems as iteritems
import varint as varint
from constants import IS_EDITOR as IS_EDITOR
from serialization.definitions import FieldFlags as FieldFlags, FieldTypes as FieldTypes
from serialization.exceptions import SerializationException as SerializationException
__all__: tuple

class ComponentBinSerializer(object):
    def __init__(self):
        ...
    def serialize(self, target):
        ...
    def __serializeCustomType(self, obj):
        ...
    def __serializeArray(self, value, itemType):
        ...
    def __serializeString(self, value):
        ...
    def __serialize(self, value, itemType):
        ...
