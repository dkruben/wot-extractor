# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dict2model/extensions/battle_type.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import ARENA_BONUS_TYPE_NAMES as ARENA_BONUS_TYPE_NAMES, ARENA_GAMEPLAY_NAMES as ARENA_GAMEPLAY_NAMES
from dict2model import models as models, validate as validate
from dict2model.fields import UniCapList as UniCapList, String as String
from dict2model.schemas import Schema as Schema
from dict2model.types import ValidatorsType as ValidatorsType
from dict2model.fields import Field as Field
_battleTypeSchema: Any
BattleTypesModelType: Any

class BattleTypeModel(models.Model):
    __slots__: tuple
    arenaBonusType: Any
    gameplayNames: Any
    def __init__(self, arenaBonusType, gameplayNames):
        ...
    def _reprArgs(self):
        ...

class BattleTypesModel(models.Model):
    __slots__: tuple
    battleTypes: Any
    _gameplayByBattleType: Any
    def __init__(self, battleTypes):
        ...
    def isSuitableForBattleType(self, arenaBonusType, gameplayName):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: Schema[...]
class BattleTypesSchema:
    def __init__(self, fields, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        ...
