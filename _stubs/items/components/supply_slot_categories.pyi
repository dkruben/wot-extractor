# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/supply_slot_categories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import Set as Set, Any as Any, Optional as Optional, List as List, Dict as Dict, Tuple as Tuple
from ResMgr import DataSection as DataSection
from debug_utils import LOG_CODEPOINT_WARNING as LOG_CODEPOINT_WARNING
from items import _xml as _xml
from soft_exception import SoftException as SoftException

class SlotCategories(object):
    FIREPOWER = 'firepower'
    SURVIVABILITY = 'survivability'
    MOBILITY = 'mobility'
    STEALTH = 'stealth'
    TACTICS = 'tactics'
    FIRESUPPORT = 'firesupport'
    RECONNAISSANCE = 'reconnaissance'
    UNIVERSAL = 'universal'
    ORDER: tuple
    ALL: _Any

class CategoriesHolder(object):
    __slots__: tuple
    categories: _Any
    def __init__(self):
        ...
    def checkIntersection(self, other):
        ...

class SupplySlotFactorLevels(object):
    REGULAR = 0
    IMPROVED = 1
    ALL: tuple

class SupplySlotFilter(object):
    @staticmethod
    def defineActiveValuesLevel(slotCategories, supplyCategories):
        ...

class AttrsOperation(object):
    MUL = 'mul'
    ADD = 'add'
    ALL: tuple
    _DEFAULT_VALUES: dict
    _OPERATIONS: dict
    @staticmethod
    def updateDictWithAttribute(attrsDict, attrName, opType, value):
        ...

class LevelsFactor(object):
    __slots__: tuple
    values: _Any
    opType: _Any
    def __init__(self, values, opType=None):
        ...
    def __str__(self):
        ...
    def getActiveValue(self, level):
        ...
    def applyLevelToAttrsDict(self, level, attrsDict, attrName):
        ...
    @staticmethod
    def readLevelsFactor(xmlCtx, factorSection):
        ...
    @staticmethod
    def readTypelessLevelsFactor(xmlCtx, factorSection, factorName):
        ...
    @staticmethod
    def _readFactorValues(xmlCtx, section, sectionName):
        ...
