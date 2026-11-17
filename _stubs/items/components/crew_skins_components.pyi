# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/crew_skins_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import items as items
import nations as nations
from items.components.crew_skins_constants import CrewSkinType as CrewSkinType, TANKMAN_SEX as TANKMAN_SEX, CREW_SKIN_PROPERTIES_MASKS as CREW_SKIN_PROPERTIES_MASKS

class CrewSkin(object):
    itemType = CrewSkinType.CREW_SKIN
    __slots__: tuple
    id: Any
    priceGroup: Any
    tags: Any
    firstNameID: Any
    lastNameID: Any
    iconID: Any
    description: Any
    sex: Any
    nation: Any
    rarity: Any
    historical: Any
    soundSetID: Any
    priceGroupTags: Any
    realms: Any
    def __init__(self, ID, priceGroup, firstNameID, lastNameID, iconID, description, rarity, tags, historical, soundSetID, realms):
        ...
    @property
    def compactDescr(self):
        ...

class PriceGroup(object):
    itemType = CrewSkinType.ITEM_GROUP
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

class CrewSkinsCache(object):
    __slots__: tuple
    priceGroupTags: Any
    skins: Any
    priceGroups: Any
    priceGroupNames: Any
    itemToPriceGroup: Any
    def __init__(self):
        ...
    def validateCrewSkin(self, tmanDescr, itemId):
        ...
    @staticmethod
    def _validateItem(tmanDescr, item):
        ...
