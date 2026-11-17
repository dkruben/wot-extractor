# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/data_wrapper/clan_supply.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import NamedTuple as NamedTuple, Dict as Dict, Union as Union, TYPE_CHECKING as TYPE_CHECKING, List as List
from shared_utils import makeTupleByDict as makeTupleByDict, CONST_CONTAINER as CONST_CONTAINER
from typing import Optional as Optional
_logger: Any
PointSettings: Any
ProgressionSettings: Any
PointProgress: Any
ProgressionProgress: Any
FragsCondition: Any
FullDamageCondition: Any
ExpCondition: Any
WinCondition: Any
CONDITIONS_TYPE: Any
SimpleCondition: Any
_RULE_TYPE_TO_CLAZZ: dict
CommonCondition: Any
ConditionsInfo: Any
Quest: Any
QuestsInfo: Any

class DataNames(CONST_CONTAINER):
    PROGRESSION_SETTINGS = 'PROGRESSION_SETTINGS'
    PROGRESSION_PROGRESS = 'PROGRESSION_PROGRESS'
    QUESTS_INFO = 'QUESTS_INFO'
    QUESTS_INFO_POST = 'QUESTS_INFO_POST'

class PointStatus(CONST_CONTAINER):
    PURCHASED = 'PURCHASED'
    AVAILABLE = 'AVAILABLE'

class ConditionRuleType(CONST_CONTAINER):
    FULL_DAMAGE = 'FULL_DAMAGE'
    FRAGS = 'FRAGS'
    WIN = 'WIN'
    EXP = 'EXP'

class ConditionSquadState(CONST_CONTAINER):
    SOLO = 'solo'
    PLATOON = 'platoon'
    DETACHMENT = 'detachment'

class QuestStatus(CONST_CONTAINER):
    INCOMPLETE = 'INCOMPLETE'
    REWARD_AVAILABLE = 'REWARD_AVAILABLE'
    REWARD_PENDING = 'REWARD_PENDING'
    COMPLETE = 'COMPLETE'

def _makeSimpleCondition(conditionData):
    ...
def makeQuestInfo(incomeData):
    ...
