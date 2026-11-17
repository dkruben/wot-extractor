# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/unit_helpers/MsgProcessor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from ops_pack import OpsPacker as OpsPacker, OpsUnpacker as OpsUnpacker, initOpsFormatDef as initOpsFormatDef

class CBM_OP:
    SET_ROUND = 0
    SET_RESULTS = 2
    SET_ENEMY_READY = 3

class ClanBattleMgrMsgProcessor(OpsUnpacker):
    _opsFormatDefs: Any
    _unit: Any
    def __init__(self, unit):
        ...
    def _setRound(self, isBattleRound):
        ...
    def _setResults(self, result):
        ...
    def _setEnemyReady(self, enemyReady):
        ...

class ClanBattleMgrOpsPacker(OpsPacker, ClanBattleMgrMsgProcessor):
    ...
