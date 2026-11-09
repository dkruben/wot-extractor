# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/unit_helpers/MsgProcessor.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/unit_helpers/MsgProcessor.py
from __future__ import absolute_import
from debug_utils import LOG_DEBUG_DEV
from ops_pack import OpsPacker, OpsUnpacker, initOpsFormatDef

class CBM_OP:
    SET_ROUND = 0
    SET_RESULTS = 2
    SET_ENEMY_READY = 3


class ClanBattleMgrMsgProcessor(OpsUnpacker):
    _opsFormatDefs = initOpsFormatDef({(CBM_OP.SET_ROUND): ('B', '_setRound'), 
       (CBM_OP.SET_RESULTS): ('b', '_setResults'), 
       (CBM_OP.SET_ENEMY_READY): ('B', '_setEnemyReady')})

    def __init__(self, unit):
        self._unit = unit

    def _setRound(self, isBattleRound):
        LOG_DEBUG_DEV('ClanBattleMgrMsgProcessor._setRound: ', isBattleRound)
        extras = self._unit._extras
        extras['isBattleRound'] = int(isBattleRound)

    def _setResults(self, result):
        LOG_DEBUG_DEV('ClanBattleMgrMsgProcessor._setResults: res=', result)
        extras = self._unit._extras
        extras['battleResultList'].append(result)

    def _setEnemyReady(self, enemyReady):
        LOG_DEBUG_DEV('ClanBattleMgrMsgProcessor._setEnemyReady: enemyReady=', enemyReady)
        extras = self._unit._extras
        extras['isEnemyReadyForBattle'] = enemyReady


class ClanBattleMgrOpsPacker(OpsPacker, ClanBattleMgrMsgProcessor):
    pass
