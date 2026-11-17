# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/battle_cache/cache_records.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
import weakref as weakref
from builtins import zip as zip
from collections import defaultdict as defaultdict
from future.utils import listvalues as listvalues
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.battle_control.battle_constants import CACHE_RECORDS_IDS as CACHE_RECORDS_IDS
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
_MODULE_LIST_SIZE_FORMAT = '<B'
_MODULE_LIST_FORMAT = '{}i'
_MODULE_LIST_RECORD_FORMAT: Any
_MODULE_LIST_SIZE_LEN: Any
_IGNORE_LIST_SIZE_FORMAT = '<B'
_IGNORE_LIST_FORMAT = '{}L'
_IGNORE_LIST_RECORD_FORMAT: Any
_IGNORE_LIST_SIZE_LEN: Any
_RELATIONS_SIZE_FORMAT = '<B'
_RELATIONS_KEYS_LIST_FORMAT = '{}L'
_RELATIONS_VALUES_LIST_FORMAT = '{}B'
_RELATIONS_SIZE_LEN: Any

class _Relations(CONST_CONTAINER):
    FRIEND = 1
    IGNORED = 2
    TMP_IGNORED = 4

class AbstractCacheRecord(object):
    sessionProvider: Any
    __cache: Any
    def __init__(self, cache):
        ...
    @classmethod
    def get(cls):
        ...
    @classmethod
    def getRecordID(cls):
        ...
    def unpack(self, record):
        ...
    def pack(self):
        ...
    def clear(self):
        ...
    def save(self):
        ...
    def load(self):
        ...

class TmpBRProgressionCacheRecord(AbstractCacheRecord):
    _modules: Any
    def __init__(self, cache):
        ...
    @classmethod
    def getRecordID(cls):
        ...
    def addModule(self, value):
        ...
    def getModules(self):
        ...
    def pack(self):
        ...
    def unpack(self, record):
        ...

class BRInitialModules(TmpBRProgressionCacheRecord):
    @classmethod
    def getRecordID(cls):
        ...

class RelationsCacheRecord(AbstractCacheRecord):
    __relations: Any
    def __init__(self, cache):
        ...
    @classmethod
    def getRecordID(cls):
        ...
    def unpack(self, record):
        ...
    def pack(self):
        ...
    def clear(self):
        ...
    def addFriend(self, vehicleID):
        ...
    def removeFriend(self, vehicleID):
        ...
    def isFriend(self, vehicleID):
        ...
    def addIgnored(self, vehicleID):
        ...
    def removeIgnored(self, vehicleID):
        ...
    def isIgnored(self, vehicleID):
        ...
    def addTmpIgnored(self, vehicleID):
        ...
    def removeTmpIgnored(self, vehicleID):
        ...
    def isTmpIgnored(self, vehicleID):
        ...
    def __addRelation(self, vehicleID, relationID):
        ...
    def __removeRelation(self, vehicleID, relationID):
        ...
    def __checkRelation(self, vehicleID, relationID):
        ...
