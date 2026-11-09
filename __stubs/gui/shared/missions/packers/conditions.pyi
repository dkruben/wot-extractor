# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/missions/packers/conditions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES as MISSIONS_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.conditions.condition_group_model import ConditionGroupModel as ConditionGroupModel
from gui.impl.gen.view_models.common.missions.conditions.preformatted_condition_model import PreformattedConditionModel as PreformattedConditionModel
from gui.server_events import formatters as formatters
from gui.server_events.cond_formatters import FORMATTER_IDS as FORMATTER_IDS
from gui.server_events.cond_formatters import FormattableField as FormattableField
from gui.server_events.cond_formatters import prebattle as prebattle, postbattle as postbattle, vehicle as vehicle
from gui.server_events.cond_formatters.bonus import BattlesCountFormatter as BattlesCountFormatter
from gui.server_events.cond_formatters.bonus import MissionsBonusConditionsFormatter as MissionsBonusConditionsFormatter
from gui.server_events.cond_formatters.challenges.postbattle import ChallengePostBattleConditionsFormatter as ChallengePostBattleConditionsFormatter
from gui.server_events.formatters import PreFormattedCondition as PreFormattedCondition
from gui.shared.formatters.plain_text import PlainTextFormatter as PlainTextFormatter
from personal_missions_constants import CONDITION_ICON as CONDITION_ICON
from soft_exception import SoftException as SoftException
from typing import Optional as Optional, Union as Union
from gui.server_events.conditions import _Condition as _Condition
from gui.server_events.conditions import _ConditionsGroup as _ConditionsGroup
from gui.server_events.event_items import ServerEventAbstract as ServerEventAbstract
from gui.server_events.event_items import Quest as Quest
_logger: Any
CONDITION_GROUP_AND = 'and'
CONDITION_GROUP_OR = 'or'
CONDITION_GROUP_NOP = 'nop'
CONDITION_GROUP_NOT = 'not'
CONDITION_DEFAULT_NAME = 'play'
CONDITION_GROUP_TYPE_LIST: tuple
CONDITION_SPECIFIC_TYPE_LIST: tuple
CONDITION_TYPE_LIST: Any

class PreFormattedConditionModelPacker(object):
    @staticmethod
    def pack(preFormattedConditionTuple, conditionType):
        ...

class UIConditionPacker(object):
    def _packConditions(self, conditions, event):
        ...
    def _convertConditionIntoPreFormattedCondition(self, ctx):
        ...
    def pack(self, event, model):
        ...
    def _pack(self, event, model):
        ...
    def _traversConditionItemsList(self, ctx):
        ...
    def _traversConditionGroup(self, ctx, operation):
        ...
    def _traversCondition(self, ctx):
        ...
    def _travers(self, ctx):
        ...

class BonusConditionPacker(UIConditionPacker):
    isPostBattleConditionPresent: Any
    def __init__(self):
        ...
    def _convertConditionIntoPreFormattedCondition(self, ctx):
        ...
    def packWithPostBattleCondCheck(self, event, model, isPostBattleConditionPresent):
        ...
    def _pack(self, event, model):
        ...

class PostBattleConditionPacker(UIConditionPacker):
    postBattleCondFormatter: Any
    def __init__(self):
        ...
    def _convertConditionIntoPreFormattedCondition(self, ctx):
        ...
    def _pack(self, event, model):
        ...
    @classmethod
    def packDefaultCondition(cls, event, model):
        ...
    @staticmethod
    def getPlayBattleCondition(event, packer=...):
        ...

class ChallengePostBattleConditionPacker(PostBattleConditionPacker):
    postBattleCondFormatter: Any
    def __init__(self):
        ...

def getDefaultBonusCondPacker():
    ...
def getDefaultPreBattleCondFormatter():
    ...
def getDefaultPostBattleCondFormatter():
    ...
def getDefaultVehicleCondFormatter():
    ...
def getDefaultMissionsBonusConditionsFormatter():
    ...
def getDefaultBattlesCountFormatter(hasPostBattleConditions):
    ...
def getDefaultPreformattedConditionModel():
    ...
def getDefaultPlainTextFormatter():
    ...
def getDefaultConditionGroupModel():
    ...
def getDefaultPreFormattedConditionModelPacker():
    ...
