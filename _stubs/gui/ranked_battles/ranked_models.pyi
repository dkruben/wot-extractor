# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/ranked_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
import typing as typing
from collections import namedtuple as namedtuple
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.periodic_battles.models import AlertData as AlertData
from gui.ranked_battles.constants import RankTypes as RankTypes, ZERO_RANK_ID as ZERO_RANK_ID, ZERO_DIVISION_ID as ZERO_DIVISION_ID
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from season_common import GameSeason as GameSeason
from shared_utils import CONST_CONTAINER as CONST_CONTAINER, first as first
ShieldStatus: Any
RankData: Any
BattleRankInfo: Any

class RankState(CONST_CONTAINER):
    UNDEFINED = 2
    NOT_ACQUIRED = 2
    ACQUIRED = 4
    LOST = 8
    CURRENT = 16
    NEW_FOR_PLAYER = 32
    BONUS = 64

class RankStatus(CONST_CONTAINER):
    NOT_ACHIEVED = 'not_achieved'
    ACHIEVED = 'achieved'
    LOST = 'lost'

class RankChangeStates(CONST_CONTAINER):
    LEAGUE_EARNED = 'leagueEarned'
    DIVISION_EARNED = 'divisionEarned'
    QUAL_EARNED = 'qualificationEarned'
    QUAL_UNBURN_EARNED = 'qualificationUnburnEarned'
    RANK_EARNED = 'rankEarned'
    RANK_UNBURN_PROTECTED = 'rankUnburnProtected'
    RANK_SHIELD_PROTECTED = 'rankShieldProtected'
    RANK_LOST = 'rankLost'
    STEP_EARNED = 'stepEarned'
    BONUS_STEP_EARNED = 'bonusStepEarned'
    STEPS_EARNED = 'stepsEarned'
    BONUS_STEPS_EARNED = 'bonusStepsEarned'
    STEP_LOST = 'stepLost'
    NOTHING_CHANGED = 'nothingChanged'

# base nao representavel no stub: namedtuple(...)
class RankedCycle:
    def __cmp__(self, other):
        ...
    def getUserName(self):
        ...

class RankedSeason(GameSeason):
    __isSpecial: Any
    def __init__(self, cycleInfo, seasonData, isSpecial):
        ...
    def _buildCycle(self, idx, status, start, end, number, announceOnly):
        ...
    def getUserName(self):
        ...

class RankStep(object):
    _stepID: Any
    _state: Any
    def __init__(self, stepID, stepState):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def getID(self):
        ...
    def getState(self):
        ...
    def isAcquired(self):
        ...
    def isBonus(self):
        ...
    def isCurrent(self):
        ...
    def isLost(self):
        ...
    def isNewForPlayer(self):
        ...

class RankProgress(object):
    _steps: Any
    def __init__(self, steps):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def getSteps(self):
        ...
    def getAcquiredSteps(self):
        ...
    def getBonusSteps(self):
        ...

class Division(object):
    __slots__: tuple
    firstRank: Any
    lastRank: Any
    __divisionID: Any
    __currentRank: Any
    __isFinal: Any
    __rankIDs: Any
    __isQualification: Any
    __isPostQualification: Any
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __init__(self, divisionID, firstRank, lastRank, currentRank, isFinal):
        ...
    def getID(self):
        ...
    def getRanksIDs(self):
        ...
    def getRankUserName(self, rankID):
        ...
    def getRankUserId(self, rankID):
        ...
    def getUserID(self):
        ...
    def getUserName(self):
        ...
    def isCompleted(self):
        ...
    def isCurrent(self):
        ...
    def isQualification(self):
        ...
    def isPostQualification(self):
        ...
    def isFinal(self):
        ...
    def isUnlocked(self):
        ...

class Rank(object):
    _ICON_SIZES: dict
    __rankID: Any
    __state: Any
    __progress: Any
    __division: Any
    __quests: Any
    __shieldStatus: Any
    __isUnburnable: Any
    __type: Any
    def __init__(self, rankID, rankState, progress=None, division=None, quests=None, shield=None, isUnburnable=False):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def isAcquired(self):
        ...
    def isCurrent(self):
        ...
    def isFinal(self):
        ...
    def isFirstInDivision(self):
        ...
    def isInitial(self):
        ...
    def isInitialForNextDivision(self):
        ...
    def isLost(self):
        ...
    def isLastInDivision(self):
        ...
    def isNewForPlayer(self):
        ...
    def isQualification(self):
        ...
    def isRewardClaimed(self):
        ...
    def isUnburnable(self):
        ...
    def isVisualUnburnable(self):
        ...
    def getAchievedStepsCount(self):
        ...
    def getDivision(self):
        ...
    def getDivisionUserName(self):
        ...
    def getIcon(self, size):
        ...
    def getID(self):
        ...
    def getProgress(self):
        ...
    def getQuest(self):
        ...
    def getState(self):
        ...
    def getShieldStatus(self):
        ...
    def getStepsCountToAchieve(self):
        ...
    def getType(self):
        ...
    def getQuests(self):
        ...
    def getUserName(self):
        ...

# base nao representavel no stub: namedtuple(...)
class PostBattleRankInfo:
    __slots__: tuple
    @classmethod
    def fromDict(cls, dictWithInfo):
        ...
    @property
    def shieldHP(self):
        ...
    @property
    def shieldState(self):
        ...

# base nao representavel no stub: namedtuple(...)
class RankedDossier:
    @staticmethod
    def defaults():
        ...

class RankedAlertData(AlertData):
    _RES_ROOT = R.strings.ranked_battles.alertMessage
    _RES_REASON_ROOT = R.strings.ranked_battles.rankedBattlesUnreachableView
    @classmethod
    def _getTooltip(cls, _):
        ...
