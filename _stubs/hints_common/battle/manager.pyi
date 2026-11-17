# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/hints_common/battle/manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import listvalues as listvalues
from dict2model import exceptions as exceptions
from hints_common.battle.schemas.base import HMCType as HMCType, CommonHintSchema as CommonHintSchema
from hints_common.common.manager import BaseHintsModelsManager as BaseHintsModelsManager
from py2to3 import patched_typing as patched_typing
_logger: Any
_g_manager = None
DEFAULT_XML = 'scripts/item_defs/hints/battle_hints.xml'

# base nao representavel no stub: patched_typing.Generic[...]
class CommonBattleHintsModelsManager(BaseHintsModelsManager):
    __slots__: tuple
    _hints: Any
    _hintsBySchemas: Any
    def __init__(self, schemaTag, defaultSchema):
        ...
    def get(self, uniqueName):
        ...
    def getAll(self):
        ...
    def getBySchema(self, schema):
        ...
    def _addToStorage(self, schema, model):
        ...
    def _checkSchemaType(self, schema):
        ...

def init(schemaTag, defaultSchema):
    ...
def get():
    ...
