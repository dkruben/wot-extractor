# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/recruit_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.AccountSettings import AccountSettings as AccountSettings, RECRUITS_NOTIFICATIONS as RECRUITS_NOTIFICATIONS
from helpers.i18n import makeString as _ms
from constants import ENDLESS_TOKEN_TIME as ENDLESS_TOKEN_TIME
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items import Tankman as Tankman
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from helpers import dependency as dependency
from items import tankmen as tankmen, vehicles as vehicles
from items.components import skills_constants as skills_constants
from items.components.component_constants import EMPTY_STRING as EMPTY_STRING
from items.special_crew import CustomCrew as CustomCrew
from items.tankmen import TankmanDescr as TankmanDescr, MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from nations import NONE_INDEX as NONE_INDEX, INDICES as INDICES, NAMES as NationNames
from shared_utils import first as first, findFirst as findFirst
from skeletons.gui.server_events import IEventsCache as IEventsCache
from soft_exception import SoftException as SoftException
from .events_helpers import getTankmanRewardQuests as getTankmanRewardQuests
from typing import List as List, Union as Union
_NEW_SKILL = 'new_skill'
_BASE_NAME = 'base'
_TANKWOMAN_ROLE_LEVEL = 100
_TANKWOMAN_ICON = 'girl-empty.png'
_TANKMAN_NAME = 'tankman'
_TANKMAN_ICON = 'tankman.png'
_TANKWOMAN_LEARNT_SKILLS: list
_INCREASE_LIMIT_LOGIN = 5

class RecruitGroupID(object):
    WOMEN1 = 'women1'

class RecruitSourceID(object):
    TANKWOMAN = 'tankwoman'
    TWITCH_0 = 'twitch0'
    TWITCH_1 = 'twitch1'
    TWITCH_2 = 'twitch2'
    TWITCH_3 = 'twitch3'
    TWITCH_4 = 'twitch4'
    TWITCH_5 = 'twitch5'
    TWITCH_6 = 'twitch6'
    TWITCH_7 = 'twitch7'
    TWITCH_8 = 'twitch8'
    TWITCH_9 = 'twitch9'
    TWITCH_10 = 'twitch10'
    TWITCH_11 = 'twitch11'
    TWITCH_12 = 'twitch12'
    TWITCH_13 = 'twitch13'
    TWITCH_14 = 'twitch14'
    TWITCH_15 = 'twitch15'
    TWITCH_16 = 'twitch16'
    TWITCH_17 = 'twitch17'
    TWITCH_18 = 'twitch18'
    TWITCH_19 = 'twitch19'
    TWITCH_20 = 'twitch20'
    TWITCH_21 = 'twitch21'
    TWITCH_22 = 'twitch22'
    TWITCH_23 = 'twitch23'
    TWITCH_24 = 'twitch24'
    TWITCH_25 = 'twitch25'
    TWITCH_26 = 'twitch26'
    TWITCH_27 = 'twitch27'
    TWITCH_28 = 'twitch28'
    TWITCH_29 = 'twitch29'
    TWITCH_30 = 'twitch30'
    TWITCH_31 = 'twitch31'
    TWITCH_32 = 'twitch32'
    TWITCH_33 = 'twitch33'
    TWITCH_34 = 'twitch34'
    TWITCH_35 = 'twitch35'
    TWITCH_36 = 'twitch36'
    TWITCH_37 = 'twitch37'
    TWITCH_38 = 'twitch38'
    TWITCH_39 = 'twitch39'
    TWITCH_40 = 'twitch40'
    TWITCH_41 = 'twitch41'
    TWITCH_42 = 'twitch42'
    TWITCH_43 = 'twitch43'
    TWITCH_44 = 'twitch44'
    TWITCH_45 = 'twitch45'
    TWITCH_46 = 'twitch46'
    TWITCH_47 = 'twitch47'
    TWITCH_48 = 'twitch48'
    TWITCH_49 = 'twitch49'
    TWITCH_50 = 'twitch50'
    BUFFON = 'buffon'
    LOOTBOX = 'lootbox'
    COMMANDER_MARINA = 'commander_marina'
    COMMANDER_PATRICK = 'commander_patrick'
    TWITCH_GIRL = 'twitch_girl'
    TWITCH_GUY = 'twitch_guy'
    EVENTS: tuple

class _BaseRecruitInfo(object):
    __slots__: tuple
    _recruitID: Any
    _expiryTime: Any
    _nations: Any
    _freeSkills: Any
    _learntSkills: Any
    _freeXP: Any
    _roleLevel: Any
    _lastSkillLevel: Any
    _firstName: Any
    _lastName: Any
    _roles: Any
    _icon: Any
    _group: Any
    _sourceID: Any
    _isPremium: Any
    _isFemale: Any
    _hasNewSkill: Any
    _crewCustomName: Any
    def __init__(self, recruitID, expiryTime, nations, learntSkills, freeSkills, freeXP, roleLevel, lastSkillLevel, firstName, lastName, roles, icon, group, sourceID, isPremium, isFemale, hasNewSkill):
        ...
    def __cmp__(self, other):
        ...
    def getGroupName(self):
        ...
    def getRecruitID(self):
        ...
    def getEventName(self):
        ...
    def getLabel(self):
        ...
    def getDescription(self):
        ...
    def getFirstName(self):
        ...
    def getLastName(self):
        ...
    def getIsPremium(self):
        ...
    def getRoleLevel(self):
        ...
    def getFreeXP(self):
        ...
    def getEarnedSkills(self, multiplyNew=False):
        ...
    def getAllKnownSkills(self, multiplyNew=False):
        ...
    def getFreeSkills(self):
        ...
    def getLastSkillLevel(self):
        ...
    def getExpiryTime(self):
        ...
    def getExpiryTimeStamp(self):
        ...
    def getSmallIcon(self):
        ...
    def getDynIconName(self):
        ...
    def getBigIcon(self):
        ...
    def getBarracksIcon(self):
        ...
    def getRoles(self):
        ...
    @property
    def defaultRole(self):
        ...
    def getNations(self):
        ...
    def getFullUserName(self):
        ...
    def getRankID(self):
        ...
    def getSourceID(self):
        ...
    def getSpecialIcon(self):
        ...
    def isFemale(self):
        ...
    def getFakeTankman(self):
        ...
    def getFakeTankmanInVehicle(self, vehicle, role, dropIrrelevantSkills=False):
        ...
    def getNewSkillCount(self, onlyFull=False):
        ...
    def getCrewCustomName(self):
        ...
    def _getSkillsForDescr(self):
        ...
    def _getFreeSkillsForDescr(self):
        ...
    def _getCrewCustomName(self):
        ...
    def __makeFakeDescriptor(self):
        ...
    def _getDefaultNation(self):
        ...
    @property
    def defaultNation(self):
        ...
    def _getNationGroup(self, nationID):
        ...
    def getSpecialVoiceTag(self, specialSoundCtrl):
        ...

class _QuestRecruitInfo(_BaseRecruitInfo):
    __slots__: tuple
    __operationName: Any
    def __init__(self, questID, operationName):
        ...
    def getEventName(self):
        ...
    def getLabel(self):
        ...
    def getDescription(self):
        ...
    def getHowToGetInfo(self):
        ...
    def getNewSkillCount(self, onlyFull=False):
        ...
    def _getFreeSkillsForDescr(self):
        ...

class _TokenRecruitInfo(_BaseRecruitInfo):
    __slots__: tuple
    _isPremium: Any
    _group: Any
    __freeSkills: Any
    def __init__(self, tokenName, expiryTime, nations, isPremium, group, freeSkills, skills, freeXP, lastSkillLevel, roleLevel, sourceID, roles):
        ...
    def getEventName(self):
        ...
    def getLabel(self):
        ...
    def getDescription(self):
        ...
    def getHowToGetInfo(self):
        ...
    def getFullUserNameByNation(self, nationID=None):
        ...
    def getIconByNation(self, nationID):
        ...
    def _getSkillsForDescr(self):
        ...
    def _getFreeSkillsForDescr(self):
        ...
    def _getCrewCustomName(self):
        ...
    def __parseTankmanData(self, nationID):
        ...

def _getRecruitInfoFromQuest(questID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getRecruitInfoFromToken(tokenName, eventsCache=None):
    ...
def getRecruitInfo(recruitID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAllRecruitsInfo(sortByExpireTime=False, eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRecruitIDs(eventsCache=None):
    ...
def getSourceIdFromQuest(questID):
    ...
def getNewRecruitsCounter():
    ...
def getNewRecruits():
    ...
def setNewRecruitVisited(recruitID):
    ...
def removeRecruitForVisit(recruitID):
    ...
def updateNegative():
    ...
