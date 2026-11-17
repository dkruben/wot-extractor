# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/perks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ITEM_DEFS_PATH as ITEM_DEFS_PATH
from items.readers.perks_readers import readPerksCacheFromXML as readPerksCacheFromXML
from items.components.perks_components import PerksCashe as PerksCashe
_PERK_XML_PATH: Any
g_cache = None

class Cache(object):
    __slots__: tuple
    __perks: Any
    def __init__(self):
        ...
    def initPerks(self):
        ...
    @property
    def perks(self):
        ...

def init(preloadEverything):
    ...
