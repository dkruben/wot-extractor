# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/configs/halloween_loot.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from game_params_common.base_manager import GameParamsSchema as GameParamsSchema
from dict2model import models as models, fields as fields, schemas as schemas
from halloween_common.halloween_constants import HALLOWEEN_LOOT_PARAMS_KEY as HALLOWEEN_LOOT_PARAMS_KEY
lootSchema: Any
lootConfigSchema: Any

class LootModel(models.Model):
    __slots__: tuple
    lootId: Any
    bonus: Any
    def __init__(self, lootId, bonus):
        ...

class LootConfigModel(models.Model):
    __slots__: tuple
    loot: Any
    def __init__(self, loot):
        ...
    def getBonus(self, lootId):
        ...
    def getBonusItemsAmount(self, lootId):
        ...

def _getBonusReaders(*args, **kwargs):
    ...
