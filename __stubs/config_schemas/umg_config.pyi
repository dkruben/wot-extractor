# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/config_schemas/umg_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from dict2model import fields as fields, models as models, schemas as schemas
slideSchema: Any
umgConfigSchema: Any

class ConfigModel(models.Model):
    __slots__: tuple
    enableAllDaily: Any
    enableAllWeekly: Any
    enableDailyWeeklyUI: Any
    enablePM3Banner: Any
    slides: Any
    def __init__(self, enableAllDaily, enableAllWeekly, enableDailyWeeklyUI, enablePM3Banner, slides):
        ...
    def _reprArgs(self):
        ...

class SlideModel(models.Model):
    __slots__: tuple
    name: Any
    priority: Any
    enabled: Any
    def __init__(self, name, priority, enabled):
        ...
    def _reprArgs(self):
        ...
