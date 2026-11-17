# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from logging import getLogger as getLogger
import BigWorld as BigWorld
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from avatar_components.avatar_chat_key_handling import AvatarChatKeyHandling as AvatarChatKeyHandling
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage as ClassicPage
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer as StartCountdownSoundPlayer
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gameplay import PlayerEventID as PlayerEventID
from story_mode.gui.scaleform.daapi.view.battle.page_base import StoryModeBattlePageBase as StoryModeBattlePageBase, STORY_MODE_EXTERNAL_COMPONENTS as STORY_MODE_EXTERNAL_COMPONENTS
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME
_logger: Any
ONBOARDING_CONFIG: Any

class DynamicAliases(CONST_CONTAINER):
    PREBATTLE_TIMER_SOUND_PLAYER = 'prebattleTimerSoundPlayer'

class OnboardingBattlePage(StoryModeBattlePageBase, ClassicPage):
    storyModeCtrl: Any
    _visibleComponents: Any
    _blToggling: Any
    def __init__(self, components=..., external=..., fullStatsAlias=None, **kwargs):
        ...
    def reload(self):
        ...
    def _populate(self):
        ...
    def _onBattleLoadingStart(self):
        ...
    def _onKillCamSimulationFinish(self):
        ...
    def _changeCtrlMode(self, ctrlMode):
        ...
    def _setComponentsVisibility(self, visible=None, hidden=None):
        ...
