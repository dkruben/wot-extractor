# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/newbie_hints/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from account_helpers.settings_core.options import AimSetting as AimSetting
from account_helpers.settings_core import settings_constants as settings_constants
FEATURE_NEWBIE_HINTS = 'newbie_hints'
FEATURE_NEWBIE_HINTS_SETTINGS = 'newbie_hints_settings'
TOOLTIP_MIN_VIEW_TIME = 2.0
SETTINGS_CHECKBOX_KEYS_MAPPING: dict
TOOLTIP_ID_MAPPING: dict
NEWBIE_HINTS_RETICLE_MAPPING: dict
NEWBIE_SETTINGS_RETICLE_PARAMS: list

class NewbieHintsLogActions(str, Enum):
    APPLY = 'apply'
    WATCHED = 'watched'
    CLICK = 'click'

class NewbieHintsLogViews(str, Enum):
    SETTINGS = 'settings'
    SETTINGS_ARCADE = 'settings_arcade'
    SETTINGS_SNIPER = 'settings_sniper'
    BATTLE = 'battle'

class SettingsNewbieTooltips(str, Enum):
    PREBATTLE_HINTS = '#tooltips:newbiePrebattleHints'
    INBATTLE_HINTS = '#tooltips:newbieBattleHints'
    INBATTLE_HINTS_RESET = 'restartNewbieBattleHints'

class CheckBoxState(str, Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'

class NewbieHintsLogItems(str, Enum):
    BTN_RESET_VIEWED_HINTS = 'inbattle_hints_reset_btn'
    CHECKBOX_PREBATTLE_HINTS = 'prebattle_hints_checkbox'
    CHECKBOX_INBATTLE_HINTS = 'inbattle_hints_checkbox'
    TOOLTIP_SETTINGS_PREBATTLE_HINTS = 'prebattle_hints_tooltip'
    TOOLTIP_SETTINGS_INBATTLE_HINTS = 'inbattle_hints_tooltip'
    TOOLTIP_SETTINGS_INBATTLE_HINTS_RESET = 'inbattle_reset_tooltip'
