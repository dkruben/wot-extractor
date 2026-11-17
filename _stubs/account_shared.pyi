# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/account_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import collections as collections
import re as re
import time as time
from functools import total_ordering as total_ordering
from constants import FairplayViolationType as FairplayViolationType
from items import vehicles as vehicles, ITEM_TYPES as ITEM_TYPES
from fairplay_violation_types import getViolationsByMask as getViolationsByMask, FairplayViolations as FairplayViolations
from items.components.c11n_constants import CustomizationType as CustomizationType
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
from typing import Union as Union, Tuple as Tuple
from soft_exception import SoftException as SoftException
_VERSION_REGEXP: Any

class AmmoIterator(object):
    next: Any
    __ammo: Any
    __idx: Any
    def __init__(self, ammo):
        ...
    def __iter__(self):
        ...
    def __next__(self):
        ...

class LayoutIterator(object):
    next: Any
    __layout: Any
    __idx: Any
    def __init__(self, layout):
        ...
    def __iter__(self):
        ...
    def __next__(self):
        ...

# decorador original: @total_ordering
class NotificationItem(object):
    item: Any
    asString: Any
    def __init__(self, item):
        ...
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...
    def __compare(self, other):
        ...

def getAmmoDiff(ammo1, ammo2):
    ...
def getEquipmentsDiff(eqs1, eqs2):
    ...
def currentWeekPlayDaysCount(curTime, newDayStart, newWeekStart):
    ...
def getFairPlayViolationName(violationsMask):
    ...
def getCustomizationItem(custType, custID):
    ...
def validateCustomizationItem(custData):
    ...
def parseVersion(version):
    ...
def isValidClientVersion(clientVersion, serverVersion):
    ...
def getClientMainVersion():
    ...
def readClientServerVersion():
    ...
