# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/hints_common/prebattle/schemas.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from constants import ARENA_BONUS_TYPE_IDS as ARENA_BONUS_TYPE_IDS
from dict2model import models as models, validate as validate
from dict2model.fields import Boolean as Boolean, Integer as Integer, List as List, String as String
from dict2model.schemas import Schema as Schema
from soft_exception import SoftException as SoftException
from dict2model.types import ValidatorsType as ValidatorsType
from dict2model.fields import Field as Field
_BHMType: Any
hintSchema: Any
configSchema: Any

class BaseHintModel(models.Model):
    __slots__: tuple
    _VIEW_CLASS_DELIMITER = ':'
    hintType: Any
    viewClass: Any
    def __init__(self, hintType, viewClass):
        ...
    def isEnabledFor(self, arenaBonusType):
        ...
    def splitViewClass(self):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: Schema[...]
class BaseHintSchema:
    def __init__(self, fields, modelClass, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        ...
    def validateRegistered(self, hints):
        ...

class HintModel(BaseHintModel):
    __slots__: tuple
    arenaBonusTypes: Any
    def __init__(self, arenaBonusTypes, hintType, viewClass):
        ...
    def isEnabledFor(self, arenaBonusType):
        ...

# base nao representavel no stub: BaseHintSchema[...]
class HintSchema:
    def __init__(self):
        ...

class PrebattleHintsConfigModel(models.Model):
    __slots__: tuple
    enabled: Any
    battleTimerThreshold: Any
    def __init__(self, enabled, battleTimerThreshold):
        ...
    def _reprArgs(self):
        ...
