# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/GlobalMapBase.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
from future.moves import pickle as pickle
from future.utils import viewitems as viewitems
from past.builtins import xrange as xrange
from ops_pack import OpsUnpacker as OpsUnpacker, packPascalString as packPascalString, unpackPascalString as unpackPascalString, initOpsFormatDef as initOpsFormatDef
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
OK = GM_ERROR.OK
GM_ERROR_NAMES: dict

class GM_ERROR:
    WAIT_OK = -1
    OK = 0
    METHOD_COOLDOWN = 1
    BAD_METHOD = 2
    NO_CLAN = 3
    BATTLE_NOT_FOUND = 4
    UNIT_NOT_READY = 5

class GM_CLIENT_METHOD:
    SUBSCRIBE = 1
    UNSUBSCRIBE = 2
    JOIN_BATTLE = 3
    SET_DEV_MODE = 4
    KEEP_ALIVE = 5

class GM_OP:
    UNPACK_BATTLE = 1
    FINISH_BATTLE = 2
    REMOVE_BATTLE = 3
    UNPACK_BATTLE_UNIT = 4
    REMOVE_BATTLE_UNIT = 5
    ON_CLAN_RESTORED = 6

class GlobalMapBase(OpsUnpacker):
    _opsFormatDefs: Any
    FORMAT_HEADER = '<ii'
    SIZE_HEADER: Any
    FORMAT_ADD_BATTLE_HEADER = '<qHii?'
    SIZE_ADD_BATTLE_HEADER: Any
    FORMAT_ADD_BATTLE_UNIT_HEADER = '<qh'
    SIZE_ADD_BATTLE_UNIT_HEADER: Any
    battles: Any
    battleUnits: Any
    _dirty: Any
    _packed: Any
    def __init__(self):
        ...
    def _empty(self):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def _persist(self):
        ...
    def pack(self, isForced=False):
        ...
    def unpack(self, packedData):
        ...
    def serialize(self):
        ...
    def deserialize(self, pdata):
        ...
    def _addBattle(self, battleID, peripheryID, createTime, startTime, localizedData):
        ...
    def _unpackBattle(self, packedData):
        ...
    def _finishBattle(self, battleID):
        ...
    def _removeBattle(self, battleID):
        ...
    def _addBattleUnit(self, battleID, strUnitUpdate):
        ...
    def _unpackBattleUnit(self, packedData):
        ...
    def _removeBattleUnit(self, battleID):
        ...
