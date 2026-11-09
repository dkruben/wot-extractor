# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/challenges/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.resources import R as R
CONDITION_TEXT_RES = R.strings.challenges.condition
DEFAULT_CONDITION_TEXT_RES = R.strings.challenges.condition.unknown
DEFAULT_CONDITION_TITLE_TEXT_RES = R.strings.challenges.condition.unknown.title
ACHIEVEMENT_TEXT_RES = R.strings.achievements
CHALLENGES_BATTLE_RESULT_ICONS: dict

class TextResKey(str, Enum):
    EVENT_COUNT = 'eventCount'
    MIN_DISTANCE = 'minDistance'
    MAX_DISTANCE = 'maxDistance'
    TITLE = 'title'
    LIMITED_TIME = 'limittedTime'
    WHILE_ENEMY_INVISIBLE = 'whileEnemyInvisible'
    WHILE_INVISIBLE = 'whileInvisible'
    WHILE_FULL_HEALTH = 'whileFullHealth'
    RAMMING = 'ramming'
    TOTAL = 'total'
    WITHIN_VIEW_RANGE = 'withinViewRange'
    COMPARE_WITH_MAX_HEALTH = 'compareWithMaxHealth'
    CLASSES_DIVERSITY = 'classesDiversity'
    CLASSES = 'classes'

class TemplateParam(str, Enum):
    GOAL = 'goal'
    DISTANCE = 'distance'
    TIME_LIMIT = 'timeLimit'
    CLASS_COUNT = 'classCount'
    VEHICLE_CLASS = 'vehicleClass'

class ConditionIcon(str, Enum):
    DEFAULT = 'folder'
    COMPLEX = 'folder'
    DAMAGE_BLOCK = 'damage_block'
    TOP = 'top'
    KILL_VEHICLES = 'kill_vehicles'
    DISCOVER = 'discover'
    HURT_VEHICLES = 'hurt_vehicles'
    RAM = 'ram'
    HIT = 'hit'
    ACHIEVEMENT = 'achievement'
    MODULE_CRIT = 'module_crit'
