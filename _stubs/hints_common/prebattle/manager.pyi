# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/hints_common/prebattle/manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
from dict2model import exceptions as exceptions
from hints_common.common.manager import BaseHintsModelsManager as BaseHintsModelsManager
from hints_common.prebattle.schemas import hintSchema as hintSchema, BaseHintSchema as BaseHintSchema
from hints_common.prebattle.schemas import BaseHintModel as BaseHintModel
_logger: Any
_g_manager = None
_HINTS_XML = 'scripts/item_defs/hints/prebattle_hints.xml'

class PrebattleHintsModelsManager(BaseHintsModelsManager):
    _hints: Any
    def __init__(self):
        ...
    def iterHints(self):
        ...
    def _checkSchemaType(self, schema):
        ...
    def _addToStorage(self, schema, model):
        ...
    def _validateRegistered(self):
        ...

def init():
    ...
def getInstance():
    ...
