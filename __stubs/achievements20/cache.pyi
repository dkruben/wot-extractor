# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/achievements20/cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from functools import partial as partial
from time import time as time
from enum import Enum as Enum
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from past.builtins import xrange as xrange
from typing import TYPE_CHECKING as TYPE_CHECKING, Union as Union, Set as Set, List as List, Dict as Dict, Optional as Optional, Any as Any, Iterable as Iterable
from account_shared import getCustomizationItem as getCustomizationItem
from bonus_readers import readBonusSection as readBonusSection, getSupportedBonuses as getSupportedBonuses
from constants import IS_CLIENT as IS_CLIENT, IS_WEB as IS_WEB, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from dossiers2.custom.cache import getCache as getHelperCache
from dossiers2.custom.dependencies import VEHICLE_ACHIEVEMENTS_DEPENDENCIES as VEHICLE_ACHIEVEMENTS_DEPENDENCIES, CUSTOMIZATION_ACHIEVEMENTS_DEPENDENCIES as CUSTOMIZATION_ACHIEVEMENTS_DEPENDENCIES, VEHICLE_ACHIEVEMENTS_POP_UPS as VEHICLE_ACHIEVEMENTS_POP_UPS, CUSTOMIZATION_ACHIEVEMENTS_POP_UPS as CUSTOMIZATION_ACHIEVEMENTS_POP_UPS, _processAchievementDependency as _processAchievementDependency
from items import vehicles as vehicles, ITEM_TYPES as ITEM_TYPES, ITEM_TYPE_NAMES as ITEM_TYPE_NAMES, parseIntCompactDescr as parseIntCompactDescr
from items.components.c11n_constants import CustomizationType as CustomizationType
from nations import NAMES as NAMES, INDICES as INDICES
from realm_utils import ResMgr as rmgr
from soft_exception import SoftException as SoftException
from wotdecorators import singleton as singleton
from items.components.c11n_components import BaseCustomizationItem as BaseCustomizationItem
from dossiers2.common.DossierDescr import DossierDescr as DossierDescr
from items.vehicles import VehicleType as VehicleType
from ResMgr import DataSection as DataSection
DEPRECATED_BONUSES: set
ALLOWED_CUSTOMIZATION_TAGS: _Any
ITEM_CONDITION_KEYS: _Any
ITEM_FILTER_CONDITION_KEYS: _Any
VEHICLE_FILTER_CONDITION_KEYS: _Any
ALLOWED_ACHIEVEMENT_TYPES: _Any
ALLOWED_CONDITIONS_BY_ACHIEVEMENT_TYPE: dict
_VALID_PROGRESSIVE_TYPES: _Any
_VALID_UI_CONFIG_KEYS: _Any
_VALID_ICON_POSITIONS: _Any
_VALID_ICON_SIZE_MAPS: _Any
ROOT_ACHIEVEMENT_IDS: tuple
_CONFIG_FILE = 'scripts/item_defs/advanced_achievements/advanced_achievements.xml'
__stageAllValueGetterByCondition: dict
__conditionReaders: dict

class ProgressiveTypes(Enum):
    PROGRESSIVE = 'progressive'
    NOT_PROGRESSIVE = 'notProgressive'

class UIConfigFields(Enum):
    TYPE = 'type'
    BACKGROUND = 'background'
    STRING_KEY = 'stringKey'
    ICON_POSITION = 'iconPosition'
    ORDER = 'order'
    THEME = 'theme'
    ICON_SIZE_MAP = 'iconSizeMap'
    VEHICLE = 'vehicle'

class IconPositions(Enum):
    TOP = 'top'
    CENTER = 'center'
    BOTTOM = 'bottom'

class IconSizeMap(Enum):
    DEFAULT = ''
    PERSONAL_MISSIONS = 'personal_missions'

# decorador original: @singleton
class g_cache(object):
    _achievementsGettersByItemType: dict
    __data: _Any
    __totalVehicleAchievement: _Any
    def __init__(self):
        ...
    def init(self):
        ...
    def _getAchievementsByItem(self, itemTypeName, item):
        ...
    def _getAchievementsByVehicleFilter(self, itemTypeName, vehicleType):
        ...
    def _getAchievementsByCustomizationItemFilter(self, itemTypeName, item):
        ...
    def getAchievementsByItem(self, item, receivedItems):
        ...
    def getAchievementByID(self, achievementType, achievementID):
        ...
    def getTotalVehicleAchievement(self):
        ...
    def getScore(self, achievement, dossier, excludeList=None):
        ...
    def getAchievementsScore(self, accountDossierDescr):
        ...

class Achievement(object):
    __data: _Any
    def __init__(self, achievementData):
        ...
    def __getattr__(self, item):
        ...
    def __getitem__(self, item):
        ...
    def __contains__(self, item):
        ...
    def getActiveStage(self, currentValue, currentStage):
        ...
    def isAchievedByUnlock(self):
        ...
    def isAchievementCompleted(self, currentValue):
        ...
    @staticmethod
    def isAnyStageCompleted(currentStage):
        ...
    def getOwnScore(self, dossier):
        ...
    def getID(self):
        ...
    def getType(self):
        ...
    def getCurrentDataFromDossier(self, dossierDescr):
        ...
    def updateValueInDossier(self, dossierDescr, currentValue=None, currentStage=None, currentTimestamp=None):
        ...
    def initializeValueInDossier(self, dossierDescr, currentValue=None, currentStage=None):
        ...
    def getStageBonusByValue(self, currentStage):
        ...
    def getStagePointsByValue(self, currentStage):
        ...
    def getAllBonuses(self):
        ...
    def getStageValue(self, stage):
        ...

def getCache():
    ...
def _readConfig():
    ...
def __readUIConfig(section, achievementID):
    ...
def __readAchievements(achievementsType, achievementsSection):
    ...
def __stageAllValueGetterByVehicleFilter(filterData):
    ...
def __stageAllValueGetterByCustomizationItemFilter(filterData):
    ...
def __readStages(stagesSection, conditions):
    ...
def __readVehicleFilterConditions(filterSection):
    ...
def __readCustomizationItemConditions(customizationItemSection):
    ...
def __readCustomizationItemFilter(filterSection):
    ...
def __readConditions(conditionsSections):
    ...
def init():
    ...
