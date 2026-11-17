# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dog_tags_common/player_dog_tag.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.config.common import ComponentViewType as ComponentViewType
from soft_exception import SoftException as SoftException
from typing import Dict as Dict

class DogTagComponent(object):
    _componentDefinition: Any
    _value: Any
    _grade: Any
    def __init__(self, compId, value, grade):
        ...
    @property
    def compId(self):
        ...
    @property
    def value(self):
        ...
    @property
    def grade(self):
        ...
    @property
    def componentDefinition(self):
        ...

class PlayerDogTag(object):
    __str__: Any
    __hash__ = None
    _components: Any
    def __init__(self, comps):
        ...
    def getComponentByType(self, viewType):
        ...
    def getComponentIter(self):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __repr__(self):
        ...
    @staticmethod
    def fromDict(dtDict):
        ...
    def toDict(self):
        ...

class DisplayableDogTag(object):
    __str__: Any
    _nickName: Any
    _clanTag: Any
    _playerDT: Any
    def __init__(self, playerDT, nickName='', clanTag=''):
        ...
    def getNickName(self):
        ...
    def getClanTag(self):
        ...
    def getComponentByType(self, viewType):
        ...
    def __repr__(self):
        ...
    @staticmethod
    def fromDict(dtDict):
        ...
