# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/serializers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import wg_pickle as wg_pickle
from persistent_data_cache_common.types import TData as TData
defaultSerializer: Any

class ISerializer(object):
    __slots__: tuple
    def deserialize(self, serializedData):
        ...
    def serialize(self, rawData):
        ...
    def rollbackSideEffects(self):
        ...

class WGPickleSerializer(ISerializer):
    __slots__: tuple
    def deserialize(self, serializedData):
        ...
    def serialize(self, rawData):
        ...
    def rollbackSideEffects(self):
        ...
