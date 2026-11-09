# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/configs/story_mode_battle_mgr_quotums.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from dict2model import models as models, fields as fields, validate as validate, schemas as schemas, exceptions as exceptions
from story_mode_common.story_mode_constants import PRIORITY as PRIORITY
quotumSchema: Any
quotumsSchema: Any

class QuotumsModel(models.Model):
    __slots__: tuple
    quotums: Any
    def __init__(self, quotums):
        ...

class QuotumModel(models.Model):
    __slots__: tuple
    priority: Any
    quotum: Any
    def __init__(self, priority, quotum):
        ...

def validatePriorityies(model):
    ...
