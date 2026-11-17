# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/session_stats_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.shared.utils.requesters import IRandomAccountStats as IRandomAccountStats, IRandomVehStats as IRandomVehStats, ISessionStatsRequester as ISessionStatsRequester
ValueWithDelta: Any
RatioValue: Any
CreditsDetails: Any
CrystalDetails: Any
_ARENA_TYPE_TO_RETURN_CLASS_MAP: dict

class _StatKind(object):
    DAY_STAT = 'dayStat'
    VEHICLE_DAY_STAT = 'vehDayStat'

class BaseStats(object):
    data: Any
    def __init__(self, data):
        ...
    @property
    def battleCnt(self):
        ...
    @property
    def incomeCredits(self):
        ...
    @property
    def xp(self):
        ...
    @property
    def incomeCrystal(self):
        ...
    @property
    def freeXP(self):
        ...
    @property
    def averageXp(self):
        ...
    @property
    def ratioDamage(self):
        ...
    @property
    def helpDamage(self):
        ...
    @property
    def ratioKill(self):
        ...
    @property
    def averageDamage(self):
        ...
    @property
    def blockedDamage(self):
        ...
    @property
    def winRate(self):
        ...
    @property
    def wins(self):
        ...
    @property
    def averageFrags(self):
        ...
    @property
    def survivedRatio(self):
        ...
    @property
    def spotted(self):
        ...
    @property
    def netCredits(self):
        ...
    @property
    def netCrystal(self):
        ...

class BaseAccountStats(BaseStats):
    @property
    def creditsDetails(self):
        ...
    @property
    def crystalDetails(self):
        ...
    @property
    def averageVehicleLevel(self):
        ...
    @staticmethod
    def _sumRecords(data, *startWithStrings):
        ...

class BaseVehicleStats(BaseStats):
    ...

class RandomAccountStats(BaseAccountStats, IRandomAccountStats):
    @property
    def wtr(self):
        ...

class RandomVehStats(BaseVehicleStats, IRandomVehStats):
    @property
    def wtr(self):
        ...

class SessionStatsRequester(AbstractSyncDataRequester, ISessionStatsRequester):
    settingsCore: Any
    def getAccountStats(self, arenaType):
        ...
    def getVehiclesStats(self, arenaType, vehId):
        ...
    def getStatsVehList(self, arenaType):
        ...
    def getAccountWtr(self):
        ...
    def _requestCache(self, callback=None):
        ...
    def __getStats(self, arenaType, statsKind=..., isVehStats=False, vehicleId=None):
        ...
    @staticmethod
    def __getWtr(data, arenaType, statsKind, vehicleId=None):
        ...
