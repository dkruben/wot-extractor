# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/potapov_quests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
import time as time
import typing as typing
from future.utils import viewitems as viewitems
from past.builtins import intern as intern, xrange as xrange
from enum import Enum as Enum
import ResMgr as ResMgr
import nations as nations
import quest_xml_source as quest_xml_source
from items import ItemsPrices as ItemsPrices, _xml as _xml, vehicles as vehicles
from items.vehicles import VEHICLE_CLASS_TAGS as VEHICLE_CLASS_TAGS
from constants import COMMON_ROLE as COMMON_ROLE, COMMON_ROLE_TO_ROLE_TYPE as COMMON_ROLE_TO_ROLE_TYPE, EVENT_TYPE as EVENT_TYPE, IS_CLIENT as IS_CLIENT, IS_WEB as IS_WEB, ITEM_DEFS_PATH as ITEM_DEFS_PATH, PERSONAL_MISSION_2_FINAL_PAWN_COST as PERSONAL_MISSION_2_FINAL_PAWN_COST, PERSONAL_MISSION_2_FREE_TOKEN_NAME as PERSONAL_MISSION_2_FREE_TOKEN_NAME, PERSONAL_MISSION_FINAL_PAWN_COST as PERSONAL_MISSION_FINAL_PAWN_COST, PERSONAL_MISSION_FREE_TOKEN_NAME as PERSONAL_MISSION_FREE_TOKEN_NAME, HAS_PM1_COMPLETED_TOKEN as HAS_PM1_COMPLETED_TOKEN, HAS_PM2_COMPLETED_TOKEN as HAS_PM2_COMPLETED_TOKEN, HAS_PM3_COMPLETED_TOKEN as HAS_PM3_COMPLETED_TOKEN, HAS_PM4_COMPLETED_TOKEN as HAS_PM4_COMPLETED_TOKEN
from nations import ALLIANCES_TAGS as ALLIANCES_TAGS
from personal_missions_constants import VEHICLE_RESTRICTION_MAX_LEVEL as VEHICLE_RESTRICTION_MAX_LEVEL, VEHICLE_RESTRICTION_MIN_LEVEL as VEHICLE_RESTRICTION_MIN_LEVEL
from soft_exception import SoftException as SoftException
from debug_utils import LOG_ERROR as LOG_ERROR
from helpers import i18n as i18n
from web_stubs import i18n as i18n
from typing import FrozenSet as FrozenSet, Optional as Optional
from items.vehicles import VehicleType as VehicleType
POTAPOV_QUEST_XML_PATH: Any
_FALLOUT_BATTLE_TAGS: Any
_ALLOWED_TAG_NAMES: Any
g_cache = None
g_tileCache = None
g_seasonCache = None
PM_BRANCH_TO_FREE_TOKEN_NAME: dict
PM_BRANCH_TO_FINAL_PAWN_COST: dict
MAP_BRANCH_NAME_TO_COMPLETED_TOKEN: dict
POTAPOV_QUEST_COMPLETED_TOKENS: Any
PQ_REWARD_BY_DEMAND: dict
_MAP_BRANCH_TO_CLASSIFIER: dict

class PQ_BRANCH:
    REGULAR = 0
    PERSONAL_MISSION_2 = 2
    PERSONAL_MISSION_3 = 4
    PERSONAL_MISSION_4 = 8
    ALL: tuple
    PM1_NAME = 'regular'
    PM2_NAME = 'pm2'
    PM3_NAME = 'pm3'
    PM4_NAME = 'pm4'
    NAME_TO_TYPE: dict
    ALL_NAMES: Any
    PM_CAMPAIGNS_IDS: dict
    BRANCH_TO_OPERATION_IDS: dict
    OPERATION_ID_TO_BRANCH: dict
    TYPE_TO_NAME: dict
    MUTUAL_EXCLUSION_BRANCHES: dict
    WITH_AWARD_LIST_BRANCHES: Any
    WITHOUT_AWARD_LIST_BRANCHES: Any
    class QUEST_GROUPS(Enum):
        GROUP_1 = 1
        GROUP_2 = 2
        GROUP_3 = 3
    @classmethod
    def convertBranchNameToSeasonID(cls, branchName):
        ...
    @classmethod
    def convertNameToType(cls, branches):
        ...

class PQ_SWITCHES:
    IS_PM_BATTLE_PROGRESS_ENABLED = 'isPMBattleProgressEnabled'
    IS_REGULAR_QUEST_ENABLED = 'isRegularQuestEnabled'
    IS_PM2_QUEST_ENABLED = 'isPM2QuestEnabled'
    IS_PM3_QUEST_ENABLED = 'isPM3QuestEnabled'
    IS_PM4_QUEST_ENABLED = 'isPM4QuestEnabled'
    ALL: tuple
    DISABLED_PM_OPERATIONS = 'disabledPMOperations'
    DISABLED_PM_MISSIONS = 'disabledPersonalMissions'
    WITHOUT_AWARD_LIST_SWITCHERS: Any
    MAP_BRANCH_NAME_TO_SWITCH_NAME: dict

class PQ_STATE:
    NONE = 0
    UNLOCKED = 1
    NEED_GET_MAIN_REWARD = 2
    MAIN_REWARD_GOTTEN = 3
    NEED_GET_ADD_REWARD = 4
    NEED_GET_ALL_REWARDS = 5
    ALL_REWARDS_GOTTEN = 6
    NEXT_STATE: dict
    NEED_GET_REWARD: tuple
    COMPLETED: tuple

class PQ_FLAG:
    NONE = 0
    PAUSE = 1

class SeasonCache:
    __seasonsInfo: Any
    def __init__(self):
        ...
    def getSeasonInfo(self, seasonID):
        ...
    def __readSeasons(self):
        ...

class TileCache(object):
    __tilesInfo: Any
    def __init__(self):
        ...
    def getTileInfo(self, tileID):
        ...
    def __iter__(self):
        ...
    def __readTiles(self):
        ...

class PQCache(object):
    __potapovQuestIDToQuestType: Any
    __questUniqueIDToPotapovQuestID: Any
    __tileIDchainIDToPotapovQuestID: Any
    __tileIDchainIDToFinalPotapovQuestID: Any
    __tileIDchainIDToInitialPotapovQuestID: Any
    def __init__(self, auxData=None):
        ...
    def questByPotapovQuestID(self, potapovQuestID):
        ...
    def hasPotapovQuest(self, potapovQuestID):
        ...
    def getPotapovQuests(self):
        ...
    def questByUniqueQuestID(self, uniqueQuestID):
        ...
    def isPotapovQuest(self, uniqueQuestID):
        ...
    def questListByTileIDChainID(self, tileID, chainID):
        ...
    def finalPotapovQuestIDByTileIDChainID(self, tileID, chainID):
        ...
    def initialPotapovQuestIDByTileIDChainID(self, tileID, chainID):
        ...
    def getPotapovQuestIDByUniqueID(self, uniqueQuestID):
        ...
    def branchByPotapovQuestID(self, potapovQuestID):
        ...
    def getPotapovQuestNameByQuestID(self, questID):
        ...
    def getPotapovQuestIDByName(self, questName):
        ...
    def __iter__(self):
        ...
    def __readQuestList(self, auxData=None):
        ...

class IClassifier(object):
    def __init__(self, questTags):
        ...
    @property
    def classificationAttr(self):
        ...
    def matchVehicle(self, vehicleType):
        ...

class ClassifierByClass(IClassifier):
    vehClass: Any
    def __init__(self, questTags):
        ...
    @property
    def classificationAttr(self):
        ...
    def matchVehicle(self, vehicleType):
        ...

class ClassifierByAlliance(IClassifier):
    alliance: Any
    def __init__(self, questTags):
        ...
    @property
    def classificationAttr(self):
        ...
    def matchVehicle(self, vehicleType):
        ...

class ClassifierByRole(IClassifier):
    commonRole: Any
    roles: Any
    def __init__(self, questTags):
        ...
    @property
    def classificationAttr(self):
        ...
    def matchVehicle(self, vehicleType):
        ...

class PQType(object):
    __slots__: tuple
    id: Any
    tags: Any
    isInitial: Any
    isFinal: Any
    minLevel: Any
    maxLevel: Any
    rewardByDemand: Any
    branch: Any
    branchName: Any
    tileID: Any
    chainID: Any
    internalID: Any
    requiredUnlocks: Any
    generalQuestID: Any
    mainQuestID: Any
    mainAwardListQuestID: Any
    addQuestID: Any
    addAwardListQuestID: Any
    classifier: Any
    isBranchWithAwardListQuests: Any
    isBranchWithoutAwardListQuests: Any
    mainQuestInfo: Any
    mainAwardListQuestInfo: Any
    addQuestInfo: Any
    addAwardListQuestInfo: Any
    userString: Any
    shortUserString: Any
    description: Any
    advice: Any
    def __init__(self, basicInfo):
        ...
    def getMajorTag(self):
        ...
    def maySelectQuest(self, unlockedQuests):
        ...
    def areRequiredQuestsUnlockedOrSelectable(self, unlockedQuests):
        ...
    def tryUnlockNextTile(self, potapovQuestsProgress):
        ...

class PQStorage(object):
    __compDescr: Any
    __quests: Any
    def __init__(self, compDescr=None, storage=None):
        ...
    def keys(self):
        ...
    def completedPQIDs(self):
        ...
    def unlockedPQIDs(self):
        ...
    def __getitem__(self, id):
        ...
    def __setitem__(self, id, value):
        ...
    def __contains__(self, id):
        ...
    def get(self, key, default=...):
        ...
    def pop(self, id):
        ...
    def makeCompDescr(self):
        ...
    def iteritems(self):
        ...
    def items(self):
        ...

def isPotapovQuestBranchEnabled(gameParams, branchName):
    ...
def isPotapovQuestTileEnabled(gameParams, pqType):
    ...
def isPotapovQuestEnabled(gameParams, questID):
    ...
def isPotapovQuestBranchTileAndMissionEnabled(gameParams, pqType):
    ...
def init():
    ...
def _readTags(xmlCtx, section, subsectionName):
    ...
def isWithoutAwardListBranchQuest(questName):
    ...
def getQuestBranchByQuestName(questName):
    ...
