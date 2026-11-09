# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/collections_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from copy import deepcopy as deepcopy
from future.utils import viewitems as viewitems
import typing as typing
from typing import Optional as Optional
USABLE_COLLECTION_ENTITIES: set
UNUSABLE_COLLECTION_ENTITIES: set
COLLECTION_ITEM_TYPE_NAMES: Any
COLLECTIONS_PREFIX = 'cllc'
g_collectionsRelatedItems: Any

# base nao representavel no stub: namedtuple(...)
class CollectionItem:
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...

# base nao representavel no stub: namedtuple(...)
class Collection:
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...
    def replace(self, data):
        ...
    @classmethod
    def __packItemConfigs(cls, dataToUpdate):
        ...

# base nao representavel no stub: namedtuple(...)
class CollectionsConfig:
    def __new__(cls, **kwargs):
        ...
    def getCollection(self, collectionId):
        ...
    def replace(self, data):
        ...
    def getRawData(self):
        ...
    @classmethod
    def __packCollectionConfigs(cls, dataToUpdate):
        ...

class CollectionRelatedItems:
    __items: Any
    def __init__(self):
        ...
    def setData(self, data):
        ...
    @property
    def items(self):
        ...

def isCollectionsPrefix(itemName):
    ...
def makeCollectionItemEntitlementName(collectionId, itemId):
    ...
def makeCollectionRewardEntitlementName(collectionId, requiredCount):
    ...
