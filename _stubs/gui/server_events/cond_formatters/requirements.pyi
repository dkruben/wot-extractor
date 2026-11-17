# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/cond_formatters/requirements.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import types as types
import nations as nations
from constants import EVENT_TYPE as EVENT_TYPE, IGR_TYPE as IGR_TYPE, IS_CHINA as IS_CHINA
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.cond_formatters import packText as packText, packTokenProgress as packTokenProgress, getSeparatorBlock as getSeparatorBlock
from gui.server_events.cond_formatters.formatters import ConditionsFormatter as ConditionsFormatter, ConditionFormatter as ConditionFormatter
from gui.server_events.conditions import GROUP_TYPE as GROUP_TYPE, AndGroup as AndGroup
from gui.server_events.formatters import TOKEN_SIZES as TOKEN_SIZES
from gui.shared.formatters import text_styles as text_styles, icons as icons
from helpers import int2roman as int2roman, dependency as dependency
from helpers.i18n import makeString as ms
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException

class RecursiveFormatter(ConditionsFormatter):
    __gatheringFormatters: Any
    def __init__(self, formatters=None, gatheringFormatters=None):
        ...
    def createGatheringFormatters(self):
        ...
    def _packCondition(self, *args, **kwargs):
        ...
    def _getFormattedField(self, *args, **kwargs):
        ...
    def _packConditions(self, *args, **kwargs):
        ...

class VehicleConditionAdapter(object):
    _condition: Any
    _suitableVehicles: Any
    def __init__(self, condition, suitableVehicles):
        ...
    def isAvailable(self):
        ...
    def getName(self):
        ...
    def getValue(self):
        ...

class VehicleGroupAdapter(VehicleConditionAdapter):
    def isEmpty(self):
        ...
    def getSortedItems(self):
        ...

class VehicleGroupOrAdapter(VehicleGroupAdapter):
    def isAvailable(self, *args, **kwargs):
        ...

class VehicleGroupAndAdapter(VehicleGroupAdapter):
    def isAvailable(self, *args, **kwargs):
        ...

class AccountRequirementsFormatter(ConditionsFormatter):
    def __init__(self, formatters=None):
        ...
    def format(self, conditions, event):
        ...
    @staticmethod
    def _processRequirements(requirements):
        ...
    def _getGroupFormatter(self, group):
        ...
    def _packCondition(self, *args, **kwargs):
        ...
    def _getFormattedField(self, *args, **kwargs):
        ...
    def _packConditions(self, *args, **kwargs):
        ...

class TQAccountRequirementsFormatter(AccountRequirementsFormatter):
    def __init__(self):
        ...
    def _getGroupFormatter(self, group):
        ...

class SingleGroupFormatter(ConditionsFormatter):
    def __init__(self):
        ...
    def conclusion(self, group, event, requirements, passed, total):
        ...
    def format(self, group, event):
        ...
    @staticmethod
    def _styler(isRequirementMet):
        ...
    def _packCondition(self, *args, **kwargs):
        ...
    def _getFormattedField(self, *args, **kwargs):
        ...
    def _packConditions(self, *args, **kwargs):
        ...

class RecursiveGroupFormatter(RecursiveFormatter):
    def __init__(self, formatters=None):
        ...
    def conclusion(self, group, event, requirements, passed, total):
        ...
    def format(self, group, event, isNested=False, topHasOrGroup=False):
        ...
    @classmethod
    def _processNonGroupConditions(cls, branch, isNested, isAvailable, separator, isInOrGroup):
        ...
    @staticmethod
    def _getIcon(isAvailable):
        ...
    @staticmethod
    def _styler(isRequirementMet):
        ...
    @staticmethod
    def _iconize(isAvailable, isNested, branch):
        ...

class TQRecursiveGroupFormatter(RecursiveGroupFormatter):
    def __init__(self):
        ...

class PremiumAccountFormatter(ConditionFormatter):
    @classmethod
    def format(cls, condition, event, styler):
        ...

class PremiumPlusAccountFormatter(ConditionFormatter):
    @classmethod
    def format(cls, condition, event, styler):
        ...

class WotPlusFormatter(ConditionFormatter):
    @classmethod
    def format(cls, condition, event, styler):
        ...

class InClanRequirementFormatter(ConditionFormatter):
    itemsCache: Any
    @classmethod
    def format(cls, condition, event, styler):
        ...

class IgrTypeRequirementFormatter(ConditionFormatter):
    @classmethod
    def format(cls, condition, event, styler):
        ...

class GlobalRatingRequirementFormatter(ConditionFormatter):
    @classmethod
    def format(cls, condition, event, styler):
        ...

class VehiclesRequirementFormatter(ConditionFormatter):
    @classmethod
    def format(cls, condition, event, styler):
        ...

class HasReceivedMultipliedXPFormatter(ConditionFormatter):
    itemsCache: Any
    @classmethod
    def format(cls, condition, event, styler):
        ...

class AccountDossierRequirementFormatter(ConditionFormatter):
    @classmethod
    def format(cls, condition, event, styler):
        ...
    @classmethod
    def _dossierBlock2BattleMode(cls, block):
        ...

class TokenGatheringRequirementFormatter(ConditionFormatter):
    eventsCache: Any
    _tokens: Any
    _isAvailable: Any
    def __init__(self):
        ...
    def format(self, styler):
        ...
    def gather(self, condition, event):
        ...
    def isAvailable(self):
        ...

def packTokens(tokens):
    ...
def relate(relation, value, label):
    ...
def prepareAccountConditionsGroup(conditions, event):
    ...
def _isVehicleConditionAvailable(condition, suitableVehicles):
    ...
def _getAdapter(condition, suitableVehicles):
    ...
