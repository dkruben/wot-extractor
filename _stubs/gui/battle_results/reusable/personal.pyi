# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/personal.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
from constants import PREMIUM_TYPE as PREMIUM_TYPE, PlayerSatisfactionRating as PlayerSatisfactionRating
from gui.battle_results.reusable import records as records, ReusableInfoFactory as ReusableInfoFactory
from gui.battle_results.reusable import shared as shared
from gui.battle_results.reusable import sort_keys as sort_keys
from gui.battle_results.reusable.economics_records import EconomicsRecordsChains as EconomicsRecordsChains
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.ranked_battles.ranked_models import PostBattleRankInfo as PostBattleRankInfo
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.battle_results.reusable.vehicles import VehiclesInfo as VehiclesInfo
from gui.shared.utils.requesters.StatsRequester import _ControllableXPData as _ControllableXPData
_LifeTimeInfo: Any

class SquadBonusInfo(object):
    itemsCache: Any
    eventsCache: Any
    __slots__: tuple
    __vehicles: Any
    __joinedOnArena: Any
    __size: Any
    def __init__(self, vehicles=None, joinedOnArena=None, size=0, **kwargs):
        ...
    def getVehiclesLevelsDistance(self):
        ...
    def getSquadFlags(self, vehicleID, intCD):
        ...

class PersonalAvatarInfo(object):
    __slots__: tuple
    __accountDBID: Any
    __clanDBID: Any
    __team: Any
    __isPrematureLeave: Any
    __eligibleForCrystalRewards: Any
    __playerSatisfactionRating: Any
    __commendationsReceived: Any
    __fairplayViolations: Any
    __squadBonusInfo: Any
    __winnerIfDraw: Any
    __extInfo: Any
    def __init__(self, bonusType, accountDBID=0, clanDBID=0, team=0, isPrematureLeave=False, fairplayViolations=None, squadBonusInfo=None, winnerIfDraw=0, eligibleForCrystalRewards=False, avatarPlayerSatisfactionRating=..., commendationsReceived=0, **kwargs):
        ...
    @property
    def accountDBID(self):
        ...
    @property
    def clanDBID(self):
        ...
    @property
    def team(self):
        ...
    @property
    def isPrematureLeave(self):
        ...
    @property
    def winnerIfDraw(self):
        ...
    @property
    def eligibleForCrystalRewards(self):
        ...
    @property
    def playerSatisfactionRating(self):
        ...
    @property
    def commendationsReceived(self):
        ...
    @property
    def extensionInfo(self):
        ...
    def getPersonalSquadFlags(self, vehicles):
        ...
    def hasPenalties(self):
        ...
    def getPenaltyDetails(self):
        ...

class PersonalInfo(shared.UnpackedInfo):
    __slots__: tuple
    itemsCache: Any
    __vehicles: Any
    __isObserver: Any
    __isTeamKiller: Any
    __premiumMask: Any
    __isWotPlus: Any
    __wotPlusTier: Any
    __isAddXPBonusApplied: Any
    _economicsRecords: Any
    __lifeTimeInfo: Any
    __questsProgress: Any
    __PM2Progress: Any
    __c11nProgress: Any
    __xpProgress: Any
    __rankInfo: Any
    __dogTags: Any
    __prestigeResults: Any
    __questTokensCount: Any
    __questTokensConvertion: Any
    __goldBankGain: Any
    __avatar: Any
    __progressiveReward: Any
    def __init__(self, bonusType, personal, bonusCapsOverrides=None):
        ...
    @property
    def avatar(self):
        ...
    @property
    def isObserver(self):
        ...
    @property
    def hasAnyPremium(self):
        ...
    @property
    def isPremium(self):
        ...
    @property
    def isPremiumPlus(self):
        ...
    @property
    def isPremiumVIP(self):
        ...
    @property
    def isWotPlus(self):
        ...
    @property
    def wotPlusTier(self):
        ...
    @property
    def isAddXPBonusApplied(self):
        ...
    @isAddXPBonusApplied.setter
    def isAddXPBonusApplied(self, state):
        ...
    @property
    def isTeamKiller(self):
        ...
    @property
    def xpProgress(self):
        ...
    def getVehicleCDsIterator(self, result):
        ...
    def getVehicleItemsIterator(self):
        ...
    def getAchievements(self, result):
        ...
    def getLifeTimeInfo(self):
        ...
    def getQuestsProgress(self):
        ...
    def getDogTagsProgress(self):
        ...
    def getGoldBankGain(self):
        ...
    def getPM2Progress(self):
        ...
    def getC11nProgress(self):
        ...
    def getQuestTokensCount(self):
        ...
    def getQuestTokensConvertion(self):
        ...
    def getRankInfo(self):
        ...
    def getProgressiveReward(self):
        ...
    def getPrestigeResults(self):
        ...
    def getBaseCreditsRecords(self):
        ...
    def getPremiumCreditsRecords(self):
        ...
    def getCreditsDiff(self):
        ...
    def getMoneyRecords(self):
        ...
    def getCrystalRecords(self):
        ...
    def getBaseXPRecords(self):
        ...
    def getPremiumXPRecords(self):
        ...
    def getPremiumXPAddRecords(self):
        ...
    def getXPRecords(self):
        ...
    def getXPDiff(self):
        ...
    def getTmenXPRecords(self):
        ...
    def getCrystalDetailsRecords(self):
        ...
    def updateXPEarnings(self, extraXPData):
        ...
    def __collectRequiredData(self, info):
        ...
