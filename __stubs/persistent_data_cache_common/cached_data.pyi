# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/cached_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import OrderedDict as OrderedDict
from future.utils import iteritems as iteritems, listitems as listitems
import wg_pickle as wg_pickle
from persistent_data_cache_common.common import getLogger as getLogger, MeasureExecutionTime as MeasureExecutionTime
from persistent_data_cache_common.types import TData as TData, TPDCVersion as TPDCVersion
from persistent_data_cache_common.serializers import ISerializer as ISerializer
from persistent_data_cache_common.data_providers import PDProvider as PDProvider

class LoadedData(object):
    __slots__: tuple
    _logger: Any
    _version: Any
    _data: Any
    def __init__(self, version, data):
        ...
    @property
    def version(self):
        ...
    def deserialize(self, onDataDeserialized=None):
        ...

class CreatedData(object):
    __slots__: tuple
    _logger: Any
    _version: Any
    _data: Any
    def __init__(self, version):
        ...
    def isEmpty(self):
        ...
    def add(self, provider, data):
        ...
    def toDict(self):
        ...

def dumps(cachedData):
    ...
def loads(string):
    ...
