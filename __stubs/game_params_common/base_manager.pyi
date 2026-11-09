# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/game_params_common/base_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import listvalues as listvalues
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from py2to3 import patched_typing as patched_typing
from soft_exception import SoftException as SoftException
from dict2model.schemas import SchemaModelType as SchemaModelType
_logger: Any
TSchemaInfo: Any

class SchemaInfo(object):
    __slots__: tuple
    schema: Any
    def __init__(self, schema):
        ...

# base nao representavel no stub: patched_typing.Generic[...]
class BaseSchemaManager:
    __slots__: tuple
    _schemas: Any
    _usedInReplaySchemaKeys: Any
    def __init__(self):
        ...
    def registerSchema(self, *args, **kwargs):
        ...
    def getModel(self, schema, **kwargs):
        ...
    def getSchemasInfo(self):
        ...
    def getSchemaInfo(self, schema):
        ...
    def getUsedInReplayKeys(self):
        ...
    def _addSchema(self, schemaInfo):
        ...
