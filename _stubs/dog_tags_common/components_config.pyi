# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dog_tags_common/components_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
from collections import defaultdict as defaultdict
import typing as typing
from enum import Enum as Enum
from future.utils import iterkeys as iterkeys, iteritems as iteritems, viewkeys as viewkeys, viewitems as viewitems, viewvalues as viewvalues
from cache import cached_property as cached_property
from dog_tags_common.config.common import ComponentPurpose as ComponentPurpose
from dog_tags_common.config.dog_tag_parser import readDogTags as readDogTags
from soft_exception import SoftException as SoftException
from typing import List as List, Optional as Optional
from dog_tags_common.config.dog_tag_framework import ComponentDefinition as ComponentDefinition, StartingComponents as StartingComponents
componentConfigAdapter: Any

class SourceData(Enum):
    ALL = 0
    DEPRECATED_ONLY = 1
    NON_DEPRECATED_ONLY = 2

class DictIterator(object):
    _dicts: Any
    def __init__(self, *dicts):
        ...
    def __repr__(self):
        ...
    def __iter__(self):
        ...
    def __getitem__(self, item):
        ...
    def iteritems(self):
        ...
    def itervalues(self):
        ...
    def iterkeys(self):
        ...
    def items(self):
        ...
    def keys(self):
        ...
    def values(self):
        ...
    def get(self, item, default=None):
        ...
    # decorador original: @cached_property
    def _dict(self):
        ...

class _ComponentConfigAdapter(object):
    _startingDogTag: Any
    _components: Any
    _components_d: Any
    _defaults: Any
    _defaults_d: Any
    _types: Any
    _types_d: Any
    _defaultAnimatedDogTag: Any
    def __init__(self):
        ...
    def _createAllCache(self, components):
        ...
    def _createIsDefaultCache(self, components):
        ...
    def _createGroupByTypeCache(self, components):
        ...
    def _createDefaultAnimatedDogTag(self, components):
        ...
    def getDefaultDogTag(self):
        ...
    def getDefaultAnimatedDogTag(self):
        ...
    def getComponentById(self, id_val, sourceData=...):
        ...
    def getAllComponents(self, sourceData=...):
        ...
    def exists(self, compId):
        ...
    def getDefaultComponents(self, sourceData=...):
        ...
    def getComponentsByPurpose(self, purpose, sourceData=...):
        ...
