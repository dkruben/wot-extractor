# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/arena_sync_object.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems
from debug_utils import LOG_ERROR as LOG_ERROR
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts

class AttributeDict(dict):
    def __getattr__(self, item):
        ...

class ArenaSyncObject(object):
    EVENT_TYPE_DELIMITER = '.'
    __cache: Any
    __callbacks: Any
    def __init__(self):
        ...
    def __getattr__(self, item):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    def addCallback(self, syncEntryID, callback):
        ...
    def removeCallback(self, syncEntryID, callback):
        ...
    def getData(self, key):
        ...
    def __processChangeList(self, changeList):
        ...
    def __processDiffPath(self, diffpath, changeList):
        ...
