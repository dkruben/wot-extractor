# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/story_mode_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle.pve_base.page import PveBaseBattlePage as PveBaseBattlePage
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer as StartCountdownSoundPlayer
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from story_mode.gui.scaleform.genConsts.STORY_MODE_BATTLE_VIEW_ALIASES import STORY_MODE_BATTLE_VIEW_ALIASES as STORY_MODE_BATTLE_VIEW_ALIASES
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from story_mode.gui.scaleform.daapi.view.battle.page_base import STORY_MODE_EXTERNAL_COMPONENTS as STORY_MODE_EXTERNAL_COMPONENTS, StoryModeBattlePageBase as StoryModeBattlePageBase
STORY_MODE_CONFIG: Any

class DynamicAliases(CONST_CONTAINER):
    PREBATTLE_TIMER_SOUND_PLAYER = 'prebattleTimerSoundPlayer'

class StoryModeBattlePage(StoryModeBattlePageBase, PveBaseBattlePage):
    def __init__(self, **kwargs):
        ...
    def _filterExistingViewAliases(self, income):
        ...
