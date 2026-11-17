# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/post_progression_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listvalues as listvalues, viewitems as viewitems
import ResMgr as ResMgr
import constants as constants
from constants import IS_CLIENT as IS_CLIENT, IS_WEB as IS_WEB, TTC_TOOLTIP_SECTIONS as TTC_TOOLTIP_SECTIONS
from items import _xml as _xml
from items.attributes_helpers import readModifiers as readModifiers
from items.artefacts_helpers import VehicleFilter as VehicleFilter, readKpi as readKpi
from typing import Dict as Dict, Optional as Optional, Tuple as Tuple, List as List, Union as Union, Set as Set
from post_progression_common import ACTION_TYPES as ACTION_TYPES, FEATURES_NAMES as FEATURES_NAMES, PAIR_TYPES as PAIR_TYPES, parseActionCompDescr as parseActionCompDescr, ID_THRESHOLD as ID_THRESHOLD, POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES as POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES, POST_PROGRESSION_BUY_MODIFICATIONS_PRICES as POST_PROGRESSION_BUY_MODIFICATIONS_PRICES, POST_PROGRESSION_UNLOCK_AND_BUY_MODIFICATIONS_PRICES as POST_PROGRESSION_UNLOCK_AND_BUY_MODIFICATIONS_PRICES, ALLOWED_CURRENCIES_FOR_TREE_STEP as ALLOWED_CURRENCIES_FOR_TREE_STEP, ALLOWED_CURRENCIES_FOR_BUY_MODIFICATION_STEP as ALLOWED_CURRENCIES_FOR_BUY_MODIFICATION_STEP, ALLOWED_ACTIONS_CATEGORIES as ALLOWED_ACTIONS_CATEGORIES, unpackActiveModifications as unpackActiveModifications
from soft_exception import SoftException as SoftException
_XML_NAMESPACE = 'xmlns:xmlref'

class SimpleItem(object):
    __slots__: tuple
    id: Any
    def __init__(self):
        ...
    def readFromXML(self, xmlCtx, section, *args):
        ...

class ActionItem(SimpleItem):
    __slots__: tuple
    name: Any
    imgName: Any
    locName: Any
    actionType: Any
    tooltipSection: Any
    categories: Any
    def __init__(self):
        ...
    def readFromXML(self, xmlCtx, section, *args):
        ...
    @staticmethod
    def _readCategories(xmlCtx, section):
        ...

class Modification(ActionItem):
    __slots__: tuple
    actionType: Any
    modifiers: Any
    categories: Any
    kpi: Any
    def __init__(self):
        ...
    def readFromXML(self, xmlCtx, section, *args):
        ...

class PairModification(ActionItem):
    __slots__: tuple
    actionType: Any
    first: Any
    second: Any
    def __init__(self):
        ...
    def readFromXML(self, xmlCtx, section, *args):
        ...
    @staticmethod
    def _readModificationID(xmlCtx, section, modificationIDs):
        ...

class ProgressionFeature(ActionItem):
    __slots__: tuple
    actionType: Any
    def __init__(self):
        ...
    def readFromXML(self, xmlCtx, section, *args):
        ...

class TreeStep(SimpleItem):
    __slots__: tuple
    priceTag: Any
    action: Any
    unlocks: Any
    requiredUnlocks: Any
    vehicleFilter: Any
    level: Any
    position: Any
    directions: Any
    type: Any
    unlockStrategy: Any
    def __init__(self):
        ...
    def readFromXML(self, xmlCtx, section, *args):
        ...
    def addRequiredUnlock(self, stepID):
        ...
    @staticmethod
    def _readAction(xmlCtx, section, actionResolvers):
        ...

class ProgressionTree(SimpleItem):
    __slots__: tuple
    steps: Any
    rootStep: Any
    ppBattleIndex: Any
    def __init__(self):
        ...
    def readFromXML(self, xmlCtx, section, *args):
        ...
    def _validateLevels(self, xmlCtx):
        ...

class PostProgressionCache(object):
    __slots__: tuple
    _features: Any
    _featureIDs: Any
    _modifications: Any
    _modificationIDs: Any
    _pairs: Any
    _pairIDs: Any
    _trees: Any
    _treeIDs: Any
    _prices: Any
    actionToStorage: Any
    def __init__(self, featuresXML, modificationsXML, pairsXML, treesXML, pricesXML):
        ...
    @property
    def features(self):
        ...
    @property
    def featureIDs(self):
        ...
    @property
    def modifications(self):
        ...
    @property
    def modificationIDs(self):
        ...
    @property
    def pairs(self):
        ...
    @property
    def pairIDs(self):
        ...
    @property
    def trees(self):
        ...
    @property
    def treeIDs(self):
        ...
    @property
    def prices(self):
        ...
    def getAction(self, actionType, actionID):
        ...
    def getChildActions(self, parent):
        ...
    def getModificationByName(self, name):
        ...
    def _readItems(self, xmlPath, classObj, *args):
        ...
    @staticmethod
    def _readPrices(xmlPath):
        ...

def getFeatures(actionCDs, vppCache):
    ...
def getActiveModifications(actionCDs, vppCache, postProgressionTree=0):
    ...
