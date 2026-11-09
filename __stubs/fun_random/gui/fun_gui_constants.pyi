# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/fun_gui_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants_utils import ConstInjector as ConstInjector
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.prb_control import settings as settings
from gui.shared.gui_items import Vehicle as Vehicle
from messenger import m_constants as m_constants
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
ATTR_NAME = 'FUN_RANDOM'
PRB_REQ_TYPE_ATTR_NAME = 'CHANGE_FUN_SUB_MODE'
_LUI_RULE_ENTRY_POINT = 'FunRandomEntryPoint'
_LUI_RULE_NOTIFICATIONS = 'FunRandomNotifications'
_LUI_RULES: list
ACCOUNT_SUBMODE_DEFAULT_SETTINGS: dict

class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    FUN_RANDOM = 268435456

class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type: Any
    FUN_RANDOM = 'fun_random'
    FUN_RANDOM_SQUAD = 'funRandomSquad'

class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type: Any
    FUN_RANDOM = 'funRandom'

class REQUEST_TYPE(settings.REQUEST_TYPE, ConstInjector):
    CHANGE_FUN_SUB_MODE = 47

class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    FUN_RANDOM_NOTIFICATIONS = 100
    FUN_RANDOM_PROGRESSION = 101

class VEHICLE_TAGS(Vehicle.VEHICLE_TAGS, ConstInjector):
    _const_type: Any
    FUN_RANDOM = 'fun_random'

class FunRandomTooltipConstants(CONST_CONTAINER):
    FUN_RANDOM_CALENDAR_DAY = 'funRandomCalendarDay'
    FUN_RANDOM_MODE_SELECTOR_CALENDAR_DAY = 'funRandomModeSelectorCalendarDay'
    FUN_RANDOM_REWARDS = 'funRandomRewards'
    LOBBY_TOOLTIPS_SET: tuple

class AccountSettingsConstants(CONST_CONTAINER):
    FUN_RANDOM_ACCOUNT_SETTINGS = 'funRandomAccountSettings'
    FUN_RANDOM_INFO_PAGE_SHOWN = 'funRandomInfoPageShown'
    FUN_RANDOM_SEEN_TRIGGERS_COMPLETION = 'funRandomSeenTriggersCompletion'

def initFunRandomLimitedUIIds():
    ...
