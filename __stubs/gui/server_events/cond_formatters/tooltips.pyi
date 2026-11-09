# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_pass_common import BATTLE_PASS_RANDOM_QUEST_TOKEN_PREFIX as BATTLE_PASS_RANDOM_QUEST_TOKEN_PREFIX
from constants import EVENT_TYPE as EVENT_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.server_events.cond_formatters import packText as packText, getSeparator as getSeparator, requirements as requirements
from gui.server_events.cond_formatters.formatters import ConditionFormatter as ConditionFormatter, ConditionsFormatter as ConditionsFormatter
from gui.server_events.cond_formatters.requirements import prepareAccountConditionsGroup as prepareAccountConditionsGroup
from gui.server_events.conditions import GROUP_TYPE as GROUP_TYPE
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from soft_exception import SoftException as SoftException

class MissionsAccountRequirementsFormatter(ConditionsFormatter):
    def __init__(self):
        ...
    def format(self, conditions, event):
        ...
    @staticmethod
    def _processRequirements(rqs):
        ...
    def _format(self, group, event, isNested=False, topHasOrGroup=False):
        ...
    @classmethod
    def _processNonGroupConditions(cls, branch, isNested, separator, isInOrGroup, isNotLast):
        ...
    def _packCondition(self, *args, **kwargs):
        ...
    def _packConditions(self, *args, **kwargs):
        ...
    def _getFormattedField(self, *args, **kwargs):
        ...

class _TokenRequirementFormatter(ConditionFormatter):
    eventsCache: Any
    @classmethod
    def _getSpecialTokenText(cls, condition):
        ...
    @classmethod
    def format(cls, condition, event, styler=...):
        ...

def reqStyle(_):
    ...
def getSeparatorBlock(groupType=...):
    ...
