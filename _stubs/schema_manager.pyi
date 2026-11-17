# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/schema_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from game_params_common.base_manager import BaseSchemaManager as BaseSchemaManager, SchemaInfo as SchemaInfo
from game_params_common.scope import clientFilter as clientFilter
from dict2model.schemas import SchemaModelType as SchemaModelType
from game_params_common.schema import GameParamsSchema as GameParamsSchema
_logger: Any
g_SchemaManager = None

class ClientSchemaInfo(SchemaInfo):
    __slots__: tuple
    skipValidation: Any
    def __init__(self, schema, skipValidation):
        ...

# base nao representavel no stub: BaseSchemaManager[...]
class SchemaManager:
    _models: Any
    def __init__(self):
        ...
    def registerSchema(self, schema, skipValidation=True):
        ...
    def set(self, serverSettings):
        ...
    def update(self, serverSettingsDiff):
        ...
    def getModel(self, schema, **kwargs):
        ...
    def updateSettings(self, serverSettings, diff):
        ...
    def clear(self):
        ...

def getSchemaManager():
    ...
