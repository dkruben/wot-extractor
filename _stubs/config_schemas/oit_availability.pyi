# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/config_schemas/oit_availability.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from dict2model import fields as fields, models as models
oitAvailabilitySchema: Any

class OitAvailabilityModel(models.Model):
    __slots__: tuple
    min: Any
    low: Any
    medium: Any
    high: Any
    ultra: Any
    def __init__(self, min, low, medium, high, ultra):
        ...
