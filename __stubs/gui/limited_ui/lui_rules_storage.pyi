# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/limited_ui/lui_rules_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from enumerations import Enumeration as Enumeration, EnumItem as EnumItem
from future.utils import listitems as listitems
import typing as typing
import BigWorld as BigWorld
from account_helpers import AccountSettings as AccountSettings
from expressions import parseExpression as parseExpression
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from typing import Optional as Optional, Dict as Dict, Set as Set, List as List, Tuple as Tuple, Iterable as Iterable
_logger: Any
LUI_RULES: Any
_POSTPONED_RULES_DELAY = 5.0
_SERVER_SETTINGS_BLOCK_BITS = 32

class LuiRuleTypes(CONST_CONTAINER):
    PERMANENT = 'permanent'
    COMMON = 'common'
    VERSIONED = 'versioned'
    NOVICE: tuple

# base nao representavel no stub: namedtuple(...)
class _LimitedUIRule:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...

class _LimitedUIRules(object):
    __settingsCore: Any
    __isInited: Any
    __rules: Any
    __postponedRulesCallbackID: Any
    __postponedCompletedRules: Any
    def __init__(self, rules):
        ...
    def getRule(self, ruleID):
        ...
    def getRulesIDs(self):
        ...
    def getRulesIDsByTypes(self, ruleTypes):
        ...
    def hasRule(self, ruleID):
        ...
    def hasRules(self):
        ...
    def hasRulesByTypes(self, ruleTypes):
        ...
    def getTokens(self, ruleID):
        ...
    def getSysMessage(self, ruleID):
        ...
    def clear(self):
        ...
    def isCompleted(self, ruleID):
        ...
    def completeRule(self, ruleID):
        ...
    def completeRules(self, ruleIDs):
        ...
    def storePostponedRules(self):
        ...
    def clearPostponedRulesCallback(self):
        ...
    def updateRules(self, rules):
        ...
    def __storePostponedRulesByDelay(self):
        ...
    @staticmethod
    def __isClientRuleCompleted(ruleID):
        ...
    def __isServerRuleCompleted(self, rule):
        ...
    def __clearStoredVersionedRules(self):
        ...
    @staticmethod
    def __getServerRuleStorageInfo(rule):
        ...
    def __hasPostponedRules(self):
        ...

class RulesStorageMaker(object):
    @classmethod
    def makeStorage(cls, rawRulesData=None):
        ...
    @classmethod
    def updateStorage(cls, storage, rawRulesData):
        ...
    @classmethod
    def __makeRules(cls, rawRulesData):
        ...
    @classmethod
    def __makeRulesData(cls, ruleType, rules, idGen):
        ...
    @staticmethod
    def __makeRuleData(idGen, expressionStr, message, ruleType):
        ...
    @classmethod
    def __normalizeRuleItem(cls, data, rulesIDs, item):
        ...
