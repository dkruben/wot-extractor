# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/challenges_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from enum import Enum as Enum, unique as unique
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Dict as Dict, List as List, Optional as Optional, Set as Set
CHALLENGES_PDATA_KEY = 'challenges'
CHALLENGES_QUEST_PREFIX = 'challenge:'
CHALLENGES_FAIL_QUEST_POSTFIX = ':fail'
CHALLENGE_TOKEN_TYPE_TO_PREFIX: dict
CHALLENGE_MIN_VEHICLE_LEVEL = 6

class ChallengeTokenType(object):
    ACTIVE = 'active'
    ATTEMPT = 'attempt'
    QUEST = 'quest'
    WIN = 'win'
    ALL: tuple

class ChallengeTokenPrefixes(object):
    BASE = 'challenge:'
    ACTIVE: Any
    ATTEMPT: Any
    QUEST: Any
    WIN: Any

class _Enum(Enum):
    @classmethod
    def hasValue(cls, value):
        ...
    @classmethod
    def makeValue(cls, value):
        ...

# decorador original: @unique
class ChallengeTypes(_Enum):
    REGULAR = 'regular'
    SPECIAL = 'special'

# decorador original: @unique
class ChallengeDifficulties(_Enum):
    HARD = 1
    MEDIUM = 2
    EASY = 3

# decorador original: @unique
class ChallengeMainRewardTypes(_Enum):
    VEHICLE = 'vehicle'
    ATTACHMENTS_SET = 'attachments_set'
    STYLE_3D = 'style_3d'
    STYLE_2D = 'style_2d'
    CREW_MEMBER = 'crew_member'
    IMPROVED_EQUIPMENT = 'improved_equipment'
    GOLD = 'gold'
    CREDITS = 'credits'
    CRYSTAL = 'crystal'
    FREE_XP = 'freeXP'
    EQUIP_COIN = 'equipCoin'
    EMPTY = ''

class ChallengesConfig(object):
    _config: Any
    _challengesConfigs: Any
    _challenges: Any
    _enabledChallenges: Any
    _specialChallenges: Any
    def __init__(self, config):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def challengesIDs(self):
        ...
    @property
    def specialChallengesIDs(self):
        ...
    @property
    def enabledChallengesIDs(self):
        ...
    @property
    def challengesConfigs(self):
        ...
    def getChallengeConfig(self, challengeID):
        ...

class ChallengeConfig(object):
    _config: Any
    _type: Any
    _difficulty: Any
    _mainRewardType: Any
    _tokenIDs: Any
    def __init__(self, config):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def challengeID(self):
        ...
    @property
    def startTime(self):
        ...
    @property
    def finishTime(self):
        ...
    @property
    def challengeType(self):
        ...
    @property
    def difficulty(self):
        ...
    @property
    def mainRewardType(self):
        ...
    @property
    def priority(self):
        ...
    @property
    def allowedCompletions(self):
        ...
    @property
    def freeRestartsPerCompletion(self):
        ...
    @property
    def restartPrice(self):
        ...
    @property
    def attempts(self):
        ...
    @property
    def quests(self):
        ...
    @property
    def tokenIDs(self):
        ...
    def getTokenID(self, tokenType):
        ...
    def isAvailable(self, curTime=None):
        ...

def isChallengeToken(tokenID):
    ...
def isChallengeQuest(questID):
    ...
def isChallengeFailQuest(questID):
    ...
def makeChallengeFailQuestID(questID):
    ...
def makeChallengeTokenID(tokenType, challengeID):
    ...
