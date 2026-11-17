# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/battle_cache/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR
from skeletons.gui.battle_session import IBattleClientCache as IBattleClientCache
_CACHE_MAX_LENGTH = 4096
_RECORD_HEADER_FORMAT = 'HH'
_RECORD_HEADER_SIZE: Any

class BattleClientCache(IBattleClientCache):
    __chunks: Any
    __records: Any
    def __init__(self):
        ...
    def getRecord(self, recordClass):
        ...
    def clear(self):
        ...
    def save(self):
        ...
    def load(self):
        ...
    @classmethod
    def _packRecord(cls, record):
        ...
    @classmethod
    def _unpackRecordHeader(cls, offset, buf):
        ...
    @classmethod
    def _unpackRecord(cls, record, chunk):
        ...
