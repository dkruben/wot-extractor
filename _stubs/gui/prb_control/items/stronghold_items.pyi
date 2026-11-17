# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/items/stronghold_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import logging as logging
import itertools as itertools
import typing as typing
from UnitBase import UNIT_ROLE as UNIT_ROLE
from debug_utils import LOG_ERROR as LOG_ERROR
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE, ONE_HOUR as ONE_HOUR
_logger: Any
BATTLE_TYPE_SORTIE = 'SORTIE'
INSPIRATION = 'INSPIRATION'
ARTILLERY_STRIKE = 'ARTILLERY_STRIKE'
REQUISITION = 'REQUISITION'
HIGH_CAPACITY_TRANSPORT = 'HIGH_CAPACITY_TRANSPORT'
SUPPORT_TYPE = 'SUPPORT'
BOOST_TYPE = 'BOOST'
REQUISITION_TYPE = 'REQUISITION'
HEAVYTRUCKS_TYPE = 'HEAVYTRUCKS'
ARTILLERY_COMMANDER = 'artillery_commander'
INSPIRE_COMMANDER = 'inspiring_commander'
RESERVE_STRONGHOLD_ORDER: tuple
RESERVE_SORTIE_ORDER: tuple
SUPPORT_ORDER: tuple
RESERVE_ITEMS: dict
UNIT_ROLE_BY_RESERVE_TYPE: dict
_OldStrongholdDataScheme: tuple
_OldStrongholdDataProxyScheme: dict
_StrongholdDataScheme: tuple
StrongholdUnitStats: Any

class StrongholdSettings(object):
    __data: Any
    __rawData: Any
    __setDataMapping: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def forceCleanData(self):
        ...
    def updateData(self, rawData):
        ...
    def getData(self):
        ...
    def getHeader(self):
        ...
    def getTimer(self):
        ...
    def getState(self):
        ...
    def getReserve(self):
        ...
    def isValid(self):
        ...
    def isStrongholdUnitFreezed(self):
        ...
    def isFirstBattle(self):
        ...
    def isSortie(self):
        ...
    def isPlayersMatchingAvailable(self):
        ...
    def getSlotsInPlayersMatching(self):
        ...
    def getReserveOrder(self):
        ...
    def clearSelectedReserves(self):
        ...
    def __validateData(self, rawData):
        ...
    def __makeDiff(self, newRawData):
        ...
    def __setData(self, newRawData, diff):
        ...
    def __setHeader(self):
        ...
    def __setTimer(self):
        ...
    def __setState(self):
        ...
    def __setReadyButtonEnabled(self):
        ...
    def __setReserve(self):
        ...
    def __strongholdDataProxy(self, rawData):
        ...

class StrongholdData(object):
    __header: Any
    __timer: Any
    __state: Any
    __reserve: Any
    __ready_button_enabled: Any
    __max_legionaries_count: Any
    __max_players_count: Any
    __min_players_count: Any
    __max_level: Any
    __min_level: Any
    __type: Any
    __direction: Any
    __battle_duration: Any
    __battle_idx: Any
    __battle_series_duration: Any
    __industrial_resource_multiplier: Any
    __battle_series_status: Any
    __current_battle: Any
    __clan: Any
    __enemy_clan: Any
    __sorties_before_start_lag: Any
    __fort_battles_before_start_lag: Any
    __sorties_before_end_lag: Any
    __time_to_ready: Any
    __matchmaker_next_tick: Any
    __battles_start_time: Any
    __battles_end_time: Any
    __public: Any
    __is_players_matching_available: Any
    __slots_locked_by_filter: Any
    __permissions: Any
    __selected_reserves: Any
    __available_reserves: Any
    __requisition_bonus_percent: Any
    __index: Any
    __clan_owner_id: Any
    __map_id: Any
    __geometry_id: Any
    __gameplay_id: Any
    __first_resp_clan_id: Any
    __battle_reward: Any
    __attacker: Any
    __id: Any
    __tag: Any
    __name: Any
    __color: Any
    __status_ready: Any
    __level: Any
    __bonus_percent: Any
    __description: Any
    __title: Any
    __production_elapsed: Any
    __intCD: Any
    class StrongholdDataHeader(object):
        __max_legionaries_count: Any
        __max_players_count: Any
        __min_players_count: Any
        __max_level: Any
        __min_level: Any
        __type: Any
        __direction: Any
        __battle_duration: Any
        __battle_idx: Any
        __battle_series_duration: Any
        __industrial_resource_multiplier: Any
        __battle_series_status: Any
        __current_battle: Any
        __clan: Any
        __enemy_clan: Any
        __index: Any
        __clan_owner_id: Any
        __map_id: Any
        __geometry_id: Any
        __gameplay_id: Any
        __first_resp_clan_id: Any
        __battle_reward: Any
        __attacker: Any
        __id: Any
        __tag: Any
        __name: Any
        __color: Any
        __status_ready: Any
        class StrongholdBattleSeriesItem(object):
            __index: Any
            __clan_owner_id: Any
            __map_id: Any
            __geometry_id: Any
            __gameplay_id: Any
            __first_resp_clan_id: Any
            __battle_reward: Any
            __current_battle: Any
            __attacker: Any
            def __init__(self, index, data):
                ...
            def getIndex(self):
                ...
            def getClanId(self):
                ...
            def getMapId(self):
                ...
            def getGeometryId(self):
                ...
            def getGameplayId(self):
                ...
            def getFirstClanId(self):
                ...
            def getBattleReward(self):
                ...
            def getCurrentBattle(self):
                ...
            def getAttacker(self):
                ...
        class StrongholdClanData(object):
            __id: Any
            __tag: Any
            __name: Any
            __color: Any
            __status_ready: Any
            def __init__(self, data):
                ...
            def getId(self):
                ...
            def getTag(self):
                ...
            def getName(self):
                ...
            def getColor(self):
                ...
            def getReadyStatus(self):
                ...
        def __init__(self):
            ...
        def setData(self, data):
            ...
        def getMaxLegionariesCount(self):
            ...
        def getMaxPlayersCount(self):
            ...
        def getMinPlayersCount(self):
            ...
        def getMaxLevel(self):
            ...
        def getMinLevel(self):
            ...
        def getType(self):
            ...
        def getDirection(self):
            ...
        def getBattleDuration(self):
            ...
        def getBattleIdx(self):
            ...
        def getBattleSeriesStatus(self):
            ...
        def getBattleSeriesDuration(self):
            ...
        def getIndustrialResourceMultiplier(self):
            ...
        def getCurrentBattle(self):
            ...
        def getClan(self):
            ...
        def getEnemyClan(self):
            ...
        def getBattleDurationMinutes(self):
            ...
        def getBattleSeriesDurationMinuts(self):
            ...
        def getBattleSeriesDurationHours(self):
            ...
        def isSortie(self):
            ...
    class StrongholdDataTimer(object):
        __sorties_before_start_lag: Any
        __fort_battles_before_start_lag: Any
        __sorties_before_end_lag: Any
        __time_to_ready: Any
        __matchmaker_next_tick: Any
        __battles_start_time: Any
        __battles_end_time: Any
        def __init__(self):
            ...
        def setData(self, data):
            ...
        def getSortiesBeforeStartLag(self):
            ...
        def getFortBattlesBeforeStartLag(self):
            ...
        def getSortiesBeforeEndLag(self):
            ...
        def getTimeToReady(self):
            ...
        def getMatchmakerNextTick(self):
            ...
        def getBattlesStartTime(self):
            ...
        def getBattlesEndTime(self):
            ...
    class StrongholdDataState(object):
        __public: Any
        __is_players_matching_available: Any
        __slots_locked_by_filter: Any
        def __init__(self):
            ...
        def setData(self, data):
            ...
        def getPublic(self):
            ...
        def isPlayersMatchingAvailable(self):
            ...
        def getSlotsLockedByFilter(self):
            ...
    class StrongholdDataReserve(object):
        __permissions: Any
        __selected_reserves: Any
        __available_reserves: Any
        __requisition_bonus_percent: Any
        __id: Any
        __type: Any
        __level: Any
        __bonus_percent: Any
        __description: Any
        __title: Any
        __production_elapsed: Any
        __intCD: Any
        class StrongholdReserveItem(object):
            __slots__: tuple
            __id: Any
            __type: Any
            __level: Any
            __bonus_percent: Any
            __description: Any
            __title: Any
            __production_elapsed: Any
            __intCD: Any
            def __init__(self, data):
                ...
            def getId(self):
                ...
            @property
            def intCD(self):
                ...
            def getType(self):
                ...
            def getGroupType(self):
                ...
            def getLevel(self):
                ...
            def getBonusPercent(self):
                ...
            def getDescription(self):
                ...
            def getTitle(self):
                ...
            def getProductionElapsed(self):
                ...
            def isUsingInBattle(self):
                ...
            def isRequisition(self):
                ...
            def __eq__(self, other):
                ...
            def __cmp__(self, other):
                ...
        def __init__(self):
            ...
        def setData(self, data):
            ...
        def getPermissions(self):
            ...
        def getSelectedReserves(self):
            ...
        def getAvailableReserves(self):
            ...
        def getRequisitionBonusPercent(self):
            ...
        def getReserveById(self, reserveId):
            ...
        def getUniqueReservesByGroupType(self, groupType):
            ...
        def getReserveCount(self, rType, level):
            ...
    def __init__(self):
        ...
    def getHeader(self):
        ...
    def setHeader(self, data):
        ...
    def getTimer(self):
        ...
    def setTimer(self, data):
        ...
    def getState(self):
        ...
    def setState(self, data):
        ...
    def getReadyButtonEnabled(self):
        ...
    def setReadyButtonEnabled(self, data):
        ...
    def getReserve(self):
        ...
    def setReserve(self, data):
        ...

def isEnemyBattleIndex(index):
    ...
