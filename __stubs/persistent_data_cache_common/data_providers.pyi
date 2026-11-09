# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/data_providers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from persistent_data_cache_common.common import getLogger as getLogger
from soft_exception import SoftException as SoftException
from persistent_data_cache_common.types import TData as TData, TDataFactory as TDataFactory
from persistent_data_cache_common.serializers import ISerializer as ISerializer

class PDProvider(object):
    __slots__: tuple
    _logger: Any
    _name: Any
    _factory: Any
    _serializer: Any
    _data: Any
    def __init__(self, name, factory, serializer):
        ...
    @property
    def name(self):
        ...
    def destroy(self):
        ...
    @property
    def isDataCreated(self):
        ...
    def getSerializerClass(self):
        ...
    def get(self):
        ...
    def create(self):
        ...
    def serialize(self, rawData):
        ...
    def deserialize(self, serializedData):
        ...
