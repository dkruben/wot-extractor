# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/ClientArena.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import zlib as zlib
import weakref as weakref
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from future.moves import pickle as pickle
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from typing import Dict as Dict
import ArenaType as ArenaType
import BigWorld as BigWorld
import Event as Event
import Math as Math
import arena_component_system.client_arena_component_assembler as assembler
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from battle_modifiers_common import BattleModifiers as BattleModifiers, EXT_DATA_MODIFIERS_KEY as EXT_DATA_MODIFIERS_KEY
from constants import ARENA_PERIOD as ARENA_PERIOD, ARENA_UPDATE as ARENA_UPDATE, ATTACK_REASON as ATTACK_REASON
from helpers.bots import preprocessBotName as preprocessBotName
from items import vehicles as vehicles
from PlayerEvents import g_playerEvents as g_playerEvents
from post_progression_common import EXT_DATA_PROGRESSION_KEY as EXT_DATA_PROGRESSION_KEY, EXT_DATA_SLOT_KEY as EXT_DATA_SLOT_KEY
from visual_script.misc import ASPECT as ASPECT
from visual_script.multi_plan_provider import makeMultiPlanProvider as makeMultiPlanProvider, CallableProviderType as CallableProviderType
from arena_vscript_config import config as arenaVScriptsConfig
from wg_async import wg_async as wg_async, wg_await as wg_await, AsyncEvent as AsyncEvent, AsyncScope as AsyncScope, BrokenPromiseError as BrokenPromiseError
_logger: Any
TeamBaseProvider: Any

class _ArenaVehiclesAwaiter(AsyncEvent):
    _ids: Any
    _arenaRef: Any
    def __init__(self, scope, arena, vehIDs):
        ...
    def destroy(self):
        ...
    def set(self):
        ...
    def _unsubscribe(self):
        ...
    def _onNewVehicleListReceived(self):
        ...
    def _onVehicleAdded(self, vehID):
        ...

class ClientArena(object):
    __onUpdate: dict
    DEFAULT_ARENA_WORLD_ID = -1
    VEHICLES_AWAIT_TIMEOUT = 5.0
    NONE_POSITION: tuple
    settings: Any
    vehicles: Any
    positions: Any
    statistics: Any
    period: Any
    periodEndTime: Any
    periodLength: Any
    periodAdditionalInfo: Any
    viewPoints: Any
    isFogOfWarEnabled: Any
    hasFogOfWarHiddenVehicles: Any
    hasObservers: Any
    teamBasesData: Any
    arenaInfo: Any
    arenaObserverInfo: Any
    teamInfo: Any
    __vehicles: Any
    __positions: Any
    __statistics: Any
    __teamBasesData: Any
    __periodInfo: Any
    __viewPoints: Any
    __isFogOfWarEnabled: Any
    __hasFogOfWarHiddenVehicles: Any
    __arenaInfo: Any
    __arenaObserverInfo: Any
    __teamInfo: Any
    __settings: Any
    __eventManager: Any
    onArenaSettingsReceived: Any
    onNewVehicleListReceived: Any
    onVehicleAdded: Any
    onVehicleUpdated: Any
    onPositionsUpdated: Any
    onPeriodChange: Any
    onNewStatisticsReceived: Any
    onVehicleStatisticsUpdate: Any
    onVehicleKilled: Any
    onVehicleHealthChanged: Any
    onVehicleShot: Any
    onVehicleHit: Any
    onVehicleRecovered: Any
    onAvatarReady: Any
    onTeamBasePointsUpdate: Any
    onTeamBasePointsUpdateAlt: Any
    onTeamBaseCaptured: Any
    onTeamKiller: Any
    onCombatEquipmentUsed: Any
    onInteractiveStats: Any
    onGameModeSpecificStats: Any
    onViewPoints: Any
    onFogOfWarEnabled: Any
    onFogOfWarHiddenVehiclesSet: Any
    onTeamHealthPercentUpdate: Any
    onChatCommandTargetUpdate: Any
    onChatCommandTriggered: Any
    onUpdatePriorityChatCommand: Any
    onRadarInfoReceived: Any
    onTeamInfoRegistered: Any
    onTeamInfoUnregistered: Any
    arenaUniqueID: Any
    _vsePlans: Any
    arenaType: Any
    bonusType: Any
    guiType: Any
    extraData: Any
    battleModifiers: Any
    bonusCapsOverrides: Any
    __arenaBBCollider: Any
    __spaceBBCollider: Any
    componentSystem: Any
    _awaitVehiclesScope: Any
    __avatar: Any
    def __init__(self, arenaUniqueID, arenaTypeID, arenaBonusType, arenaGuiType, arenaExtraData, spaceID, avatar):
        ...
    def destroy(self):
        ...
    def update(self, updateType, argStr):
        ...
    def updateTeamHealthPercent(self, percents):
        ...
    def collideWithArenaBB(self, start, end):
        ...
    def getArenaBB(self):
        ...
    def getClosestPointOnArenaBB(self, point):
        ...
    def collideWithSpaceBB(self, start, end):
        ...
    def getSpaceBB(self):
        ...
    def isPointInsideArenaBB(self, point):
        ...
    def registerArenaInfo(self, arenaInfo):
        ...
    def unregisterArenaInfo(self, arenaInfo):
        ...
    def registerArenaObserverInfo(self, arenaObserverInfo):
        ...
    def unregisterArenaObserverInfo(self, arenaObserverInfo):
        ...
    def registerTeamInfo(self, teamInfo):
        ...
    def unregisterTeamInfo(self, teamInfo):
        ...
    def hasBonusCap(self, bonusCap):
        ...
    @property
    def isAvatarReady(self):
        ...
    def __setupBBColliders(self):
        ...
    def __onArenaSettingsUpdate(self, argStr):
        ...
    def __onPeriodInfoUpdate(self, argStr):
        ...
    def __onViewPoints(self, argStr):
        ...
    def __onRadarInfoReceived(self, argStr):
        ...
    def __getArenaPlans(self):
        ...
    def startVsePlans(self):
        ...
    def __onBasePointsUpdate(self, argStr):
        ...
    def __onBaseCaptured(self, argStr):
        ...
    def __onCombatEquipmentUsed(self, argStr):
        ...
    def __onFlagTeamsReceived(self, argStr):
        ...
    def __onFlagStateChanged(self, argStr):
        ...
    def __onResourcePointStateChanged(self, argStr):
        ...
    def __onOwnVehicleInsideRP(self, argStr):
        ...
    def __onOwnVehicleLockedForRP(self, argStr):
        ...
    def __onInteractiveStats(self, argStr):
        ...
    def runVsePlan(self, planName, params, key='', context=None):
        ...
    def stopVsePlan(self, planName, key=''):
        ...
    def getVseContextInstance(self, contextName):
        ...
    def __preprocessVehicleInfo(self, vehID, info):
        ...
    def getVehicleType(self, vehInfo, compDescr):
        ...
    def updateVehicleInfo(self, vehID, vehInfo):
        ...
    def updateVehiclesList(self, vehInfoList):
        ...
    def addVehInfo(self, vehInfo, notify=True):
        ...
    def updateVehiclesFrags(self, vehicleID, fragsCount):
        ...
    def updateVehiclesTkills(self, vehicleID, tkillsCount):
        ...
    def updateFogOfWar(self, fogOfWar):
        ...
    def invalidateVehiclesPosition(self):
        ...
    def updateVehiclesPosition(self, vehID, position):
        ...
    def __setVehiclePosition(self, vehID, position):
        ...
    def updateVehicleIsAlive(self, vehID, compDescr, isPlayerVehicle):
        ...
    def updateVehicleIsTeamKiller(self, vehID):
        ...
    def updateVehicleIsAvatarReady(self, vehID):
        ...
    # decorador original: @wg_async
    def updateGameModeSpecificStats(self, isStatic, stats):
        ...
    # decorador original: @wg_async
    def awaitVehiclesAdded(self, vehIDs, timeout=None):
        ...

class CollisionResult(object):
    INSIDE = 0
    INTERSECTION = 1
    OUTSIDE = 2

class _BBCollider(object):
    __min: Any
    __max: Any
    __center: Any
    __planes: Any
    def __init__(self, bb, heightLimits):
        ...
    def getMinBounds(self):
        ...
    def getMaxBounds(self):
        ...
    def isPointInsideBB(self, point3D):
        ...
    def getClosestPointOnBB(self, point):
        ...
    def _findClosestPointInside(self, point):
        ...
    def _findClosestPointOutside(self, point):
        ...
    def collide(self, start, end):
        ...

class Plane(object):
    n: Any
    d: Any
    def __init__(self, n, d):
        ...
    def intersectSegment(self, a, b):
        ...
    def testPoint(self, point):
        ...

def _convertToList(vec4):
    ...
