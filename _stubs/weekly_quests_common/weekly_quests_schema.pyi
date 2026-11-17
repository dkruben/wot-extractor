# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/weekly_quests_common/weekly_quests_schema.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from constants import Configs as Configs
from dict2model import fields as fields, models as models, validate as validate
weeklyQuestsSchema: Any

class WeeklyQuestsConfigModel(models.Model):
    __slots__: tuple
    enabled: Any
    rerollTimeout: Any
    def __init__(self, enabled, rerollTimeout):
        ...
    def _reprArgs(self):
        ...
