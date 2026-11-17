# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/helpers/server_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from builtins import str as str
from future.utils import iteritems as iteritems
from typing import Tuple as Tuple, List as List
from shared_utils import makeTupleByDict as makeTupleByDict
_logger: Any

# base nao representavel no stub: namedtuple(...)
class RewardConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...
    @classmethod
    def __packResourceConfigs(cls, data):
        ...

# base nao representavel no stub: namedtuple(...)
class _ResourceConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...

# base nao representavel no stub: namedtuple(...)
class ResourceWellConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...
    def replace(self, data):
        ...
    def getRewardConfig(self, rewardID):
        ...
    def getParentRewardID(self, rewardID):
        ...
    def getSortedRewardsByOrder(self):
        ...
    @classmethod
    def __packRewardsConfigs(cls, data):
        ...
