# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/pet_system_common/PetPromoConfig.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from pet_system_common.pet_constants import PetPromoConsts as PetPromoConsts
from typing import List as List, Dict as Dict, Iterable as Iterable
INVALID_PET_NAME_ID = -1

class PromoSource(object):
    QUEST_PROGRESSION = 'quest_progression'
    SHOP = 'shop'
    ALL: tuple

class PetPromoConfig(object):
    _config: Any
    def __init__(self, config):
        ...
    def getPets(self):
        ...
    def isEnabled(self):
        ...
    def getUrl(self, petID):
        ...
    def getSources(self, petID):
        ...
    def getShopUrl(self, petID):
        ...
    def getAvailablePets(self, unlockedPetsIDs):
        ...
