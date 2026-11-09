# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serializable_types/customizations/paint.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from typing import Dict as Dict
from items.components.c11n_constants import ApplyArea as ApplyArea
from py2to3.patched_future import with_metaclass as with_metaclass
from serialization.field import intField as intField, applyAreaEnumField as applyAreaEnumField
from serialization.serializable_component import SerializableComponent as SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass
from ..types import C11nSerializationTypes as C11nSerializationTypes
__all__: tuple

# base nao representavel no stub: with_metaclass(...)
class PaintComponent:
    customType = C11nSerializationTypes.PAINT
    fields: Any
    __slots__: tuple
    id: Any
    appliedTo: Any
    def __init__(self, id=0, appliedTo=...):
        ...
    def toDict(self):
        ...
