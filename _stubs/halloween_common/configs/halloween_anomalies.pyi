# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/configs/halloween_anomalies.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from game_params_common.base_manager import GameParamsSchema as GameParamsSchema
from dict2model import models as models, fields as fields, schemas as schemas, exceptions as exceptions
from halloween_common.halloween_constants import HALLOWEEN_ANOMALIES_PARAMS_KEY as HALLOWEEN_ANOMALIES_PARAMS_KEY, AnomalyType as AnomalyType, ALL_LOOT_ANOMALY_TYPES as ALL_LOOT_ANOMALY_TYPES
from game_params_common.scope import GameParamsScopeFlags as GameParamsScopeFlags
componentSchema: Any
componentsSchema: Any
anomalySchema: Any
anomaliesSchema: Any
recipeSchema: Any
recipesSchema: Any
_INGREDIENT_TYPES: tuple
_KNOWN_TYPES: Any
anomaliesConfigSchema: Any

class AnomalyModel(models.Model):
    __slots__: tuple
    id: Any
    type: Any
    weight: Any
    components: Any
    def __init__(self, id, type, weight, components):
        ...

class RecipeModel(models.Model):
    __slots__: tuple
    id: Any
    ingredients: Any
    weightInc: Any
    def __init__(self, id, ingredients, weightInc):
        ...

class ComponentModel(models.Model):
    __slots__: tuple
    id: Any
    amount: Any
    spec: Any
    def __init__(self, id, amount, spec):
        ...

class AnomaliesModel(models.Model):
    __slots__: tuple
    anomaly: Any
    def __init__(self, anomaly):
        ...

class RecipesModel(models.Model):
    __slots__: tuple
    recipe: Any
    def __init__(self, recipe):
        ...

class ComponentsModel(models.Model):
    __slots__: tuple
    component: Any
    def __init__(self, component):
        ...

class AnomaliesConfigModel(models.Model):
    __slots__: tuple
    reduceFactor: Any
    anomalies: Any
    recipes: Any
    def __init__(self, reduceFactor, anomalies, recipes):
        ...

def _validateAnomaliesConfig(config):
    ...
