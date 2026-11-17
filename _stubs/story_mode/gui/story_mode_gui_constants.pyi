# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/story_mode_gui_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants_utils import ConstInjector as ConstInjector
from gui.Scaleform.daapi.settings import views as views
from gui.prb_control import settings as settings
IS_ONBOARDING_SEAMLESS_MISSION_CHANGING_ON = True
IS_STORY_MODE_FADE_IN_OUT_ON = True
STORY_MODE_FADE_IN_DURATION = 0.4
STORY_MODE_FADE_OUT_DURATION = 0.4
BONUS_ORDER: list
INFO_PAGE_STORY_MODE = 'infoPageStoryMode'
INFO_PAGE_STORY_MODE_EVENT = 'infoPageStoryMode_event'
ABILITY_ON_COOLDOWN_ACTIVATION_ERROR_KEY = 'ability_on_cooldown'

class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type: Any
    STORY_MODE = 'story_mode'

class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    STORY_MODE = 2147483648

class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type: Any
    STORY_MODE = 'StoryMode'

class VIEW_ALIAS(views.VIEW_ALIAS, ConstInjector):
    _const_type: Any
    STORY_MODE_BATTLE_PAGE = 'StoryModeBattlePage'
    ONBOARDING_BATTLE_PAGE = 'OnboardingBattlePage'
    ONBOARDING_SETTINGS_WINDOW = 'onboardingSettingsWindow'
    STORY_MODE_INTRO_VIDEO_WINDOW = 'storyModeIntroVideoWindow'
    STORY_MODE_WEB_VIEW_TRANSPARENT = 'StoryModeWebViewTransparent'
    STORY_MODE_OUTRO_VIDEO_WINDOW = 'storyModeOutroVideoWindow'
    STORY_MODE_BATTLE_RESULTS = 'storyModeBattleResults'
