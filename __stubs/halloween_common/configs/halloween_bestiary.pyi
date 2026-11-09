# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/configs/halloween_bestiary.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from game_params_common.base_manager import GameParamsSchema as GameParamsSchema
from dict2model import models as models, fields as fields, schemas as schemas
from halloween_common.halloween_constants import HALLOWEEN_BESTIARY_PARAMS_KEY as HALLOWEEN_BESTIARY_PARAMS_KEY
shopSchema: Any
soundsSchema: Any
enemySchema: Any
enemiesSchema: Any
bestiarySchema: Any

class SoundsModel(models.Model):
    __slots__: tuple
    select: Any
    def __init__(self, select):
        ...

class ShopModel(models.Model):
    __slots__: tuple
    vehicle: Any
    bundles: Any
    def __init__(self, vehicle, bundles):
        ...

class EnemyModel(models.Model):
    __slots__: tuple
    name: Any
    unlockedByToken: Any
    style: Any
    ability: Any
    shop: Any
    needShowInHangar: Any
    sounds: Any
    def __init__(self, name, unlockedByToken, style, ability, shop, needShowInHangar, sounds):
        ...

class EnemiesModel(models.Model):
    __slots__: tuple
    enemy: Any
    def __init__(self, enemy):
        ...

class BestiaryModel(models.Model):
    __slots__: tuple
    enemies: Any
    def __init__(self, enemies):
        ...
