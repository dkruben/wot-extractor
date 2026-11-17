# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/hints_common/prebattle/newbie/schemas.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from operator import attrgetter as attrgetter
import typing as typing
from dict2model.exceptions import ValidationErrorMessage as ValidationErrorMessage, ValidationError as ValidationError
from hints_common.prebattle.newbie.consts import BATTLES_TYPES as BATTLES_TYPES, HINT_TYPE_PREFIX as HINT_TYPE_PREFIX
from hints_common.prebattle.schemas import BaseHintModel as BaseHintModel, BaseHintSchema as BaseHintSchema
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from dict2model import models as models, fields as fields, validate as validate
hintSchema: Any
configSchema: Any

class NewbieHintModel(BaseHintModel):
    __slots__: tuple
    displayOrder: Any
    def __init__(self, hintType, viewClass, displayOrder):
        ...
    def isEnabledFor(self, arenaBonusType):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: BaseHintSchema[...]
class NewbieHintSchema:
    __slots__: tuple
    hints: Any
    def __init__(self):
        ...
    def validateRegistered(self, hints):
        ...

class NewbiePrebattleHintsConfigModel(models.Model):
    __slots__: tuple
    enabled: Any
    hintDisplayCount: Any
    def __init__(self, enabled, hintDisplayCount):
        ...
    def _reprArgs(self):
        ...
