# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/crew_books_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import items as items
import nations as nations
from items.components.crew_books_constants import CrewBookCacheType as CrewBookCacheType, CREW_BOOK_RARITY as CREW_BOOK_RARITY

class CrewBook(object):
    itemType = CrewBookCacheType.CREW_BOOK
    __slots__: tuple
    id: Any
    priceGroup: Any
    tags: Any
    name: Any
    description: Any
    iconID: Any
    nation: Any
    type: Any
    priceGroupTags: Any
    def __init__(self, ID, priceGroup, name, description, iconID, type, tags):
        ...
    @property
    def itemTypeName(self):
        ...
    @property
    def compactDescr(self):
        ...
    @property
    def level(self):
        ...
    def getExtensionLessIcon(self):
        ...
    def getUserName(self):
        ...

class PriceGroup(object):
    itemType = CrewBookCacheType.ITEM_GROUP
    __slots__: tuple
    price: Any
    name: Any
    id: Any
    notInShop: Any
    tags: Any
    def __init__(self):
        ...
    @property
    def compactDescr(self):
        ...

class CrewBooksCache(object):
    __slots__: tuple
    priceGroupTags: Any
    books: Any
    rarityGroups: Any
    priceGroups: Any
    priceGroupNames: Any
    itemToPriceGroup: Any
    def __init__(self):
        ...
    def getCrewBookExp(self, id):
        ...
    def validateCrewBookNation(self, itemId, nationID):
        ...
    def validateBookPersonality(self, itemId, tmanInvID):
        ...
