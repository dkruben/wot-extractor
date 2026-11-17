# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/hints_common/battle/schemas/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from dict2model import exceptions as exceptions, fields as fields, models as models, schemas as schemas, validate as validate
from dict2model.extensions.battle_type import BattleTypesModel as BattleTypesModel, BattleTypesSchema as BattleTypesSchema
from hints_common.battle.schemas.const import DEFAULT_PRIORITY as DEFAULT_PRIORITY, DEFAULT_COMPONENT as DEFAULT_COMPONENT, DEFAULT_SCOPE as DEFAULT_SCOPE, RESERVED_SCOPES as RESERVED_SCOPES, MAX_PRIORITY as MAX_PRIORITY
from py2to3 import patched_typing as patched_typing
from dict2model.extensions.battle_type import BattleTypeModel as BattleTypeModel
from dict2model.types import ValidatorsType as ValidatorsType
_logger: Any
HMCPropsType: Any
HMCContextType: Any
HMCType: Any
commonHintPropsSchema: Any
commonHintContextSchema: Any

class SchemaDependentModel(models.Model):
    __slots__: tuple
    def prepare(self, schema, **kwargs):
        ...
    def _prepare(self, schema, **kwargs):
        ...

class CommonHintPropsModel(BattleTypesModel):
    __slots__: tuple
    name: Any
    scope: Any
    component: Any
    unique: Any
    priority: Any
    skipOverlay: Any
    _uniqueName: Any
    def __init__(self, name, scope, component, unique, priority, skipOverlay, battleTypes):
        ...
    @property
    def uniqueName(self):
        ...
    def _reprArgs(self):
        ...

class CommonHintContextModel(SchemaDependentModel):
    __slots__: tuple
    _ctx: Any
    def __init__(self, *args, **kwargs):
        ...
    def create(self, data):
        ...
    def _prepare(self, schema, **kwargs):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: patched_typing.Generic[...]
class CommonHintModel(SchemaDependentModel):
    __slots__: tuple
    props: Any
    context: Any
    def __init__(self, props, context):
        ...
    @property
    def uniqueName(self):
        ...
    def validate(self, arenaBonusType, gameplayName, *args, **kwargs):
        ...
    def _prepare(self, schema, **kwargs):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: BattleTypesSchema[...]
class CommonHintPropsSchema:
    __slots__: tuple
    def __init__(self, modelClass=..., serializedValidators=None, deserializedValidators=None):
        ...

# base nao representavel no stub: schemas.Schema[...]
class CommonHintSchema:
    __slots__: tuple
    propsSchema: Any
    contextSchema: Any
    def __init__(self, modelClass=..., propsSchema=None, contextSchema=None, serializedValidators=None, deserializedValidators=None):
        ...

def validateCommonHintPropsModel(model):
    ...
