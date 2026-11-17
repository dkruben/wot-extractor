# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/arena_vscript_config/schemas.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import IS_CLIENT as IS_CLIENT
from dict2model import fields as fields, models as models, validate as validate
from dict2model.extensions.battle_type import BattleTypesModel as BattleTypesModel, BattleTypesSchema as BattleTypesSchema
from dict2model.schemas import Schema as Schema
from visual_script.misc import ASPECT as ASPECT
from dict2model.extensions.battle_type import BattleTypeModel as BattleTypeModel
_vscriptParamSchema: Any
_vscriptSchema: Any
_aspectVScriptSchema: Any
_arenaVScriptSchema: Any
configSchema: Any

class VScriptParamModel(models.Model):
    __slots__: tuple
    name: Any
    value: Any
    def __init__(self, name, value):
        ...
    def _reprArgs(self):
        ...

class VScriptModel(models.Model):
    __slots__: tuple
    name: Any
    planId: Any
    param: Any
    def __init__(self, name, planId, param):
        ...
    def _reprArgs(self):
        ...

class AspectVScriptsModel(models.Model):
    __slots__: tuple
    plan: Any
    def __init__(self, plan):
        ...
    def _reprArgs(self):
        ...

class ArenaVScriptsModel(BattleTypesModel):
    __slots__: tuple
    client: Any
    server: Any
    _plans: Any
    def __init__(self, client, server, battleTypes):
        ...
    def getPlansForLoader(self, aspect):
        ...
    def _preparePlansForLoader(self):
        ...
    def _reprArgs(self):
        ...

class ConfigModel(models.Model):
    __slots__: tuple
    visualScript: Any
    def __init__(self, visualScript):
        ...
    def getPlansForLoader(self, aspect, arenaBonusType, gameplayName):
        ...

def _getCurrentAspect():
    ...
def _validateAnyPlanGiven(model):
    ...
def _defaultAspectVScriptModel():
    ...
