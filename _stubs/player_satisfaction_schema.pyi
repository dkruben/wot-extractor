# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/player_satisfaction_schema.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from constants import Configs as Configs
from dict2model import fields as fields, models as models
from dict2model.schemas import Schema as Schema
_interfacesSchema: Any
playerSatisfactionSchema: Any

class _InterfacesModel(models.Model):
    __slots__: tuple
    postbattle: Any
    spectatorMode: Any
    def __init__(self, postbattle, spectatorMode):
        ...
    def _reprArgs(self):
        ...

class PlayerSatisfactionConfigModel(models.Model):
    __slots__: tuple
    enabled: Any
    enabledInterfaces: Any
    def __init__(self, enabled, enabledInterfaces):
        ...
    def _reprArgs(self):
        ...
