# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/common/fun_random_common/fun_battle_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from constants_utils import AbstractBattleMode as AbstractBattleMode
from fun_random_common.battle_results import fun_random as fun_random
from fun_random_common.fun_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, UNIT_MGR_FLAGS as UNIT_MGR_FLAGS, ROSTER_TYPE as ROSTER_TYPE, INVITATION_TYPE as INVITATION_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE

class FunRandomBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.FUN_RANDOM
    _QUEUE_TYPE = QUEUE_TYPE.FUN_RANDOM
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.FUN_RANDOM
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.FUN_RANDOM
    _INVITATION_TYPE = INVITATION_TYPE.FUN_RANDOM
    _UNIT_MGR_NAME = 'FunRandomUnitMgr'
    _UNIT_MGR_FLAGS = UNIT_MGR_FLAGS.FUN_RANDOM
    _ROSTER_TYPE = ROSTER_TYPE.FUN_RANDOM_ROSTER
    _BATTLE_RESULTS_CONFIG = fun_random
    _SM_TYPE_BATTLE_RESULT = 'funRandomBattleResults'
    _SM_TYPES: list
    @property
    def _rosterClass(self):
        ...
