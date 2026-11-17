# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/event_boards/event_boards_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import datetime as datetime
import typing as typing
import math as math
from future.utils import viewvalues as viewvalues
from comp7.gui.shared.gui_items.dossier.stats import getComp7DossierStats as getComp7DossierStats
from comp7.gui.impl.lobby.comp7_helpers.comp7_shared import getRankEnumValue as getRankEnumValue, getPlayerDivisionByDvsnID as getPlayerDivisionByDvsnID
from gui.event_boards.event_boards_items import LeaderBoard as LeaderBoard, IPlayerProgression as IPlayerProgression, isDataSchemaValid as isDataSchemaValid
from helpers import time_utils as time_utils
from helpers.dependency import descriptor as descriptor
from helpers_common import reprSlots as reprSlots
from shared_utils import first as first
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank as Rank
from comp7_ranks_common import Comp7Division as Comp7Division
from comp7_ranks_common import Comp7RanksConfig as Comp7RanksConfig
from comp7.gui.shared.gui_items.dossier.stats import AccountComp7StatsBlock as AccountComp7StatsBlock
from comp7.gui.shared.gui_items.dossier.stats import Comp7StatsBlock as Comp7StatsBlock
from typing import Tuple as Tuple
from typing import List as List, Optional as Optional
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class BattleUnitTypeData(object):
    __slots__: tuple
    solo: Any
    platoon: Any
    superPlatoon: Any
    total: Any
    def __init__(self, rawBattleUnitData):
        ...

class DailyVehicleData(object):
    __slots__: tuple
    dayIndex: Any
    vehicleCD: Any
    prestigePoints: Any
    totalDeathsPerUnitType: Any
    totalAssistedPerUnitType: Any
    damageReceivedPerUnitType: Any
    battleCountWinPerUnitType: Any
    battleCountLossPerUnitType: Any
    battleCountDrawPerUnitType: Any
    totalDamagePerUnitType: Any
    firstBattleTimestampsPerUnitType: Any
    fragsPerUnitType: Any
    lastBattleTimestampsPerUnitType: Any
    battleLengthTotalSecondsPerUnitType: Any
    totalSuperPlatoonBattles: Any
    totalPlatoonBattles: Any
    totalSoloBattles: Any
    totalBattles: Any
    damageEfficiency: Any
    fragsEfficiency: Any
    winsEfficiency: Any
    avgDamage: Any
    avgDamageAssisted: Any
    avgPrestigePoints: Any
    def __init__(self, vehicleCD, rawDailyVehicleData, dayIndex):
        ...

class DailyData(object):
    _itemsCache: Any
    __slots__: tuple
    __repr__ = reprSlots
    dayIndex: Any
    lastRatingPoints: Any
    lastDivision: Any
    maxDamage: Any
    inactivityPenalty: Any
    maxDivisionIndex: Any
    maxRatingPoints: Any
    lastActivityPoints: Any
    maxPrestigePoints: Any
    dataPerVehicle: Any
    date: Any
    maxDamageVehicle: Any
    maxPrestigePointsVehicle: Any
    isQualification: Any
    diffRatingPoints: Any
    totalDamage: Any
    totalPrestigePoints: Any
    totalSuperPlatoonBattles: Any
    totalPlatoonBattles: Any
    totalSoloBattles: Any
    totalBattles: Any
    totalWinsCount: Any
    totalLossCount: Any
    totalDrawCount: Any
    dayRatingPlayerDivision: Any
    dayPlayerRank: Any
    maxPlayerRank: Any
    winsEfficiency: Any
    avgDmgDealt: Any
    avgPrestige: Any
    topVehiclesCDs: Any
    def __init__(self, dayIndex, rawDailyData, qualificationCompleteDate, previousDayRatingPoints):
        ...
    def __getSortedTopDailyVehiclesCDs(self):
        ...

class AggregatedDailyData(object):
    _comp7Ctrl: Any
    __slots__: tuple
    __allDaysData: Any
    maxRatingDay: Any
    maxRating: Any
    maxAchievedRank: Any
    def __init__(self, allDaysData):
        ...
    def __getMaxAchievedRank(self):
        ...
    def __getMaxDayAndRating(self):
        ...

class Comp7LeaderBoard(LeaderBoard):
    __CUSTOM_EXPECTED_FIELDS_META: list
    EXPECTED_FIELDS_META: Any
    __lastEliteUserPosition: Any
    __lastEliteUserRating: Any
    __lastMasterRankPositionThreshold: Any
    def __init__(self):
        ...
    def setData(self, rawData, leaderboardID, infoType, leaderboardType):
        ...
    def getRecordsCount(self):
        ...
    def getLastEliteUserPosition(self):
        ...
    def getLastEliteUserRating(self):
        ...

class Comp7PlayerProgression(IPlayerProgression):
    _comp7Ctrl: Any
    _itemsCache: Any
    _DAYS_FIELD = 'days'
    _META_FIELD = 'meta'
    _EXPECTED_ROOT_FIELDS: tuple
    _EXPECTED_DAY_FIELDS: tuple
    _EXPECTED_META_FIELDS: tuple
    _EXPECTED_VEHICLE_FIELDS: tuple
    eventID: Any
    __meta: Any
    __lastUpdate: Any
    season: Any
    __allDaysData: Any
    __aggregatedDailyData: Any
    __todayIndex: Any
    def __init__(self, rawData, eventID, leaderboardID):
        ...
    @property
    def todayIndex(self):
        ...
    @property
    def lastUpdateTime(self):
        ...
    @property
    def allDaysData(self):
        ...
    @property
    def aggregatedDailyData(self):
        ...
    def getVehicleSeasonStats(self, vehCD, seasonNumber=None):
        ...
    def getSeasonStats(self, seasonNumber=None):
        ...
    def getTop3SeasonVehicles(self):
        ...
    @classmethod
    def _isDataStructureValid(cls, data):
        ...
    def __getBusinessDate(self, dt, ranksConfig):
        ...
    def __isPrimeHourBefore(self, hour):
        ...

def _dateStrToDatetime(dateStr):
    ...
