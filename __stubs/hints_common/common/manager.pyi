# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/hints_common/common/manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
import importlib as importlib
import section2dict as section2dict
from extension_utils import ResMgr as ResMgr
from dict2model import exceptions as exceptions
from dict2model.models import Model as Model
from dict2model.schemas import Schema as Schema
_logger: Any
SCHEMA_NAME_DELIMITER = ':'
HINTS_TAG = 'hint'
SCHEMA_TAG = 'schema'

class BaseHintsModelsManager(object):
    __slots__: tuple
    _schemaTag: Any
    _importedSchemas: Any
    _defaultSchema: Any
    def __init__(self, xmlPath, defaultSchema, schemaTag=...):
        ...
    def _registerFromXml(self, xmlPath):
        ...
    def _register(self, schema, rawHintData):
        ...
    def _importSchema(self, location):
        ...
    def _addToStorage(self, schema, model):
        ...
    def _checkSchemaType(self, schema):
        ...
    def _validateRegistered(self):
        ...

def _readHintsXml(xmlPath):
    ...
