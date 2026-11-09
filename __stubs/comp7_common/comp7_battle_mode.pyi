# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/common/comp7_common/comp7_battle_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7_common import comp7_constants as comp7_constants
from comp7_common.comp7_battle_results import comp7 as comp7
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, QUEUE_TYPE as QUEUE_TYPE
from constants_utils import AbstractBattleMode as AbstractBattleMode, addBattleResultsConfig as addBattleResultsConfig

class Comp7BattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = comp7_constants.PREBATTLE_TYPE.COMP7
    _QUEUE_TYPE = QUEUE_TYPE.COMP7
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.COMP7
    _ARENA_GUI_TYPE = comp7_constants.ARENA_GUI_TYPE.COMP7
    _INVITATION_TYPE = comp7_constants.INVITATION_TYPE.COMP7
    _UNIT_MGR_NAME = 'Comp7UnitMgr'
    _UNIT_MGR_FLAGS = comp7_constants.UNIT_MGR_FLAGS.COMP7
    _ROSTER_TYPE = comp7_constants.ROSTER_TYPE.COMP7_ROSTER
    _BATTLE_RESULTS_CONFIG = comp7
    _SEASON_TYPE_BY_NAME = 'comp7'
    _SEASON_TYPE = comp7_constants.GameSeasonType.COMP7
    _SEASON_MANAGER_TYPE: tuple
    _SM_TYPE_BATTLE_RESULT = 'comp7BattleResults'
    _SM_TYPES: list
    def registerAdditionalBattleResultSysMsgType(self):
        ...
    def registerAdditionalBattleResultsConfig(self):
        ...
    @property
    def _rosterClass(self):
        ...
