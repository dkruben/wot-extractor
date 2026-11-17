# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/post_progression_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Dict as Dict, Set as Set, List as List, Callable as Callable, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING
from copy import copy as copy
from itertools import chain as chain
from future.utils import viewitems as viewitems
from items.components.post_progression_components import ProgressionTree as ProgressionTree
from items.vehicles import VehicleDescriptor as VehicleDescriptor
SERVER_SETTINGS_KEY = 'vehicle_post_progression_config'
EXT_DATA_SLOT_KEY = 'customRoleSlotTypeId'
EXT_DATA_PROGRESSION_KEY = 'vehPostProgression'
SETUPS_FEATURES: tuple
ROLESLOT_FEATURE = 'roleSlot'
FEATURES_NAMES: Any
POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES: tuple
POST_PROGRESSION_BUY_MODIFICATIONS_PRICES: tuple
CUSTOM_ROLE_SLOT_CHANGE_PRICE = 'customRoleSlotChangeCost'
POST_PROGRESSION_UNLOCK_AND_BUY_MODIFICATIONS_PRICES: Any
POST_PROGRESSION_ALL_PRICES: Any
ALLOWED_CURRENCIES_FOR_TREE_STEP: set
ALLOWED_CURRENCIES_FOR_BUY_MODIFICATION_STEP: set
ALLOWED_CURRENCIES_FOR_CUSTOM_ROLE_SLOT_CHANGE: set
ALLOWED_ACTIONS_CATEGORIES: set
ID_THRESHOLD = 16384
VEH_SKILL_TREE_ID_OFFSET = 10000
TANK_SETUP_GROUPS: dict
MAX_LAYOUTS_NUMBER_ON_VEHICLE: dict
GROUP_ID_BY_LAYOUT: dict
FEATURE_BY_GROUP_ID: dict
GROUP_ID_BY_FEATURE: dict
DEFAULT_LAYOUT_CAPACITY = 1
SWITCH_LAYOUT_CAPACITY = 2
POST_PROGRESSION_UNLOCKS_IDX = 0
POST_PROGRESSION_PAIRS_IDX = 1
POST_PROGRESSION_FEATURES_IDX = 2
POST_PROGRESSION_DISABLED_SWITCHES_IDX = 3

class ACTION_TYPES:
    MODIFICATION = 1
    PAIR_MODIFICATION = 2
    FEATURE = 3
    BIT_PACK = 4

class PAIR_TYPES:
    NOT_SET = 0
    FIRST = 1
    SECOND = 2

class TankSetupLayouts(object):
    OPTIONAL_DEVICES = 'devicesLayout'
    EQUIPMENT = 'eqsLayout'
    SHELLS = 'shellsLayout'
    BATTLE_BOOSTERS = 'boostersLayout'

class TankSetups(object):
    OPTIONAL_DEVICES = 'devicesSetups'
    EQUIPMENT = 'eqsSetups'
    SHELLS = 'shellsSetups'
    BATTLE_BOOSTERS = 'boostersSetups'

class TankSetupGroupsId(object):
    EQUIPMENT_AND_SHELLS = 1
    OPTIONAL_DEVICES_AND_BOOSTERS = 2

class VehicleState(object):
    __slots__: tuple
    __hash__ = None
    _unlocks: Any
    _pairs: Any
    _features: Any
    _disabledSwitches: Any
    def __init__(self, data=None):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __or__(self, other):
        ...
    @property
    def unlocks(self):
        ...
    @property
    def pairs(self):
        ...
    @property
    def features(self):
        ...
    @property
    def disabledSwitches(self):
        ...
    def addDisabledSwitch(self, groupID):
        ...
    def removeDisabledSwitch(self, groupID):
        ...
    def isSwitchDisabled(self, groupID):
        ...
    def isUnlocked(self, stepID):
        ...
    def addUnlock(self, stepID):
        ...
    def removeUnlock(self, stepID):
        ...
    def setPair(self, stepID, pairTypeID):
        ...
    def getPair(self, stepID):
        ...
    def removePair(self, stepID):
        ...
    def hasFeature(self, featureID):
        ...
    def addFeature(self, featureID):
        ...
    def removeFeature(self, featureID):
        ...
    def clean(self, removeUnlocks=True, removePairs=True, removeFeatures=True, removeDisabledSwitches=True):
        ...
    def isEmpty(self):
        ...
    def isResearchedTree(self, tree):
        ...
    def toActionCDs(self, tree):
        ...
    def toBattleActionCDsPack(self, tree):
        ...
    def toRawData(self):
        ...
    def toggleSwitchLayout(self, groupID):
        ...
    @staticmethod
    def getDefaultState():
        ...
    @staticmethod
    def __getDefaultUnlocksState():
        ...
    @staticmethod
    def __getDefaultPairsState():
        ...
    @staticmethod
    def __getDefaultFeaturesState():
        ...
    @staticmethod
    def __getDefaultDisabledSwitchesState():
        ...

class VehiclesPostProgression(object):
    __slots__: tuple
    ROOT_KEY = 'postProgression'
    __data: Any
    __dataW: Any
    def __init__(self, data, syncData=None):
        ...
    @property
    def _storage(self):
        ...
    @property
    def _storageW(self):
        ...
    def getVehicleState(self, vehTypeCD):
        ...
    def getVehicleFeaturesList(self, vehTypeCD):
        ...
    def setVehicleState(self, vehTypeCD, vehicleState):
        ...
    def removeVehicleState(self, vehTypeCD):
        ...
    def clean(self):
        ...
    @staticmethod
    def getDefaultStorage():
        ...

def extractSelectedSetup(setups, setupsIndexes):
    ...
def getSelectedVehicleAmmo(setup):
    ...
def getSetupInAmmoFormatForEquipment(setup):
    ...
def makeActionCompDescr(actionType, itemId, subId=0):
    ...
def makeDefaultSetupsIndexes():
    ...
def makeDefaultSetupsInVehicle():
    ...
def parseActionCompDescr(compDescr):
    ...
def unpackVehSetupsIndexes(vehSetupsIndexes):
    ...
def packVehSetupsIndexes(vehSetupsIndexes):
    ...
def getLayoutCapacity(invData, layout, vehDescr):
    ...
def packPostProgression(unlocks, pairs, tree):
    ...
def combinePackedCDs(actionCDs):
    ...
def unpackActiveModifications(actionCDs, vppCache, treeID):
    ...
def unpackActionCDs(actionCDs, vppCache, treeID):
    ...
