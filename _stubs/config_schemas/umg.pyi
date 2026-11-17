# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/config_schemas/umg.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from dict2model import fields as fields, models as models, schemas as schemas, validate as validate
import typing as typing
_weightSchema: Any
umgMissionsConfigSchema: Any
umgEventsConfigSchema: Any

class WeightModel(models.Model):
    __slots__: tuple
    name: Any
    weight: Any
    def __init__(self, name, weight):
        ...
    def _reprArgs(self):
        ...

class WeightsModel(models.Model):
    __slots__: tuple
    weights: Any
    _weightByName: Any
    def __init__(self, weights):
        ...
    def getWeightByName(self, name):
        ...
    def _reprArgs(self):
        ...
