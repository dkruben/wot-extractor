# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/battle_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, ARENA_GUI_TYPE as ARENA_GUI_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from constants_utils import AbstractBattleMode as AbstractBattleMode
from story_mode_common.battle_results import story_mode as story_mode
from story_mode_common.story_mode_constants import SM_CONGRATULATIONS_MESSAGE as SM_CONGRATULATIONS_MESSAGE
from story_mode_common.configs.story_mode_settings import settingsSchema as settingsSchema

class StoryModeBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.STORY_MODE
    _QUEUE_TYPE = QUEUE_TYPE.STORY_MODE
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.STORY_MODE_REGULAR
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.STORY_MODE_REGULAR
    _BATTLE_MGR_NAME = 'StoryModeBattlesMgr'
    _GAME_PARAMS_KEY = settingsSchema.gpKey
    _BATTLE_RESULTS_CONFIG = story_mode
    _SM_TYPE_BATTLE_RESULT = 'storyModeBattleResults'
    _SM_TYPES: list
