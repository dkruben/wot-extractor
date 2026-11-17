# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/fun_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import unique as unique, Enum as Enum
from gui.periodic_battles.models import PeriodType as PeriodType
FEP_MODE_ITEMS_QUEST_ID = 'FEP_mode_items'
FEP_PROGRESSION_PREFIX = 'FEP_progression_'
FEP_PROGRESSION_TRIGGER_QUEST_ID: Any
FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID: Any
FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID: Any
FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID: Any
FEP_PROGRESSION_EXECUTOR_QUEST_ID: Any
FEP_PROGRESSION_UNLIMITED_EXECUTOR_QUEST_ID: Any
FEP_PROGRESSION_COUNTER_ID: Any
FEP_PROGRESSION_UNLIMITED_COUNTER_ID: Any
PROGRESSION_COUNTER_TEMPLATE: Any
PROGRESSION_UNLIMITED_COUNTER_TEMPLATE: Any
PROGRESSION_EXECUTOR_TEMPLATE: Any
PROGRESSION_TRIGGER_TEMPLATE: Any
PROGRESSION_UNLIMITED_EXECUTOR_TEMPLATE: Any
PROGRESSION_UNLIMITED_TRIGGER_TEMPLATE: Any
FEP_PROGRESSION_BASE_TEMPLATE = '{}_{}'
STATE_TO_SINGLE: dict

class FunSubModesState(object):
    UNDEFINED = 0
    BEFORE_SEASON = 1
    BETWEEN_SEASONS = 2
    AFTER_SEASON = 3
    AVAILABLE = 5
    FROZEN = 6
    SINGLE_FROZEN = 7
    NOT_AVAILABLE = 8
    NOT_AVAILABLE_END = 9
    BEFORE_STATES: set
    INNER_STATES: set
    HIDDEN_ENTRY_STATES: set
    HIDDEN_SELECTOR_STATES: set

class FunNotificationType(object):
    NEW_SUB_MODES = 'newSubModes'
    STOP_SUB_MODES = 'stopSubModes'
    STOP_ALL_SUB_MODES = 'stopAllSubModes'
    SWITCH_OFF_SUB_MODES = 'switchOffSubModes'
    SWITCH_ON_SUB_MODES = 'switchOnSubModes'
    NEW_PROGRESSION = 'newProgression'

class FunTimersShifts(object):
    PROGRESSION = 0.5
    NOTIFICATIONS = 1.0
    SUB_MODE = 0.5

# decorador original: @unique
class FunNotificationSubModeState(Enum):
    UNDEFINED = PeriodType.UNDEFINED
    BEFORE_SEASON = PeriodType.BEFORE_SEASON
    BETWEEN_SEASONS = PeriodType.BETWEEN_SEASONS
    AFTER_SEASON = PeriodType.AFTER_SEASON
    AVAILABLE = PeriodType.AVAILABLE
    FROZEN = PeriodType.FROZEN

# decorador original: @unique
class FunSubModeBroadcast(Enum):
    START_NOTIFICATION = 'startNotification'
    STOP_NOTIFICATION = 'stopNotification'

# decorador original: @unique
class FunCustomShellsSource(Enum):
    REGULAR = 'regular'
    CUSTOM = 'custom'
