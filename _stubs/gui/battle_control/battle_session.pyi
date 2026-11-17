# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/battle_session.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import Event as Event
import BattleReplay as BattleReplay
from PlayerEvents import g_playerEvents as g_playerEvents
from adisp import adisp_async as adisp_async
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import g_tankActiveCamouflage as g_tankActiveCamouflage
from gui.battle_control import arena_visitor as arena_visitor
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control import controllers as controllers
from gui.battle_control.arena_info import invitations as invitations
from gui.battle_control.arena_info.arena_dp import ArenaDataProvider as ArenaDataProvider
from gui.battle_control.arena_info.listeners import ListenersCollection as ListenersCollection
from gui.battle_control.battle_cache import BattleClientCache as BattleClientCache
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control.battle_constants import VIEW_COMPONENT_RULE as VIEW_COMPONENT_RULE
from gui.battle_control.battle_ctx import BattleContext as BattleContext
from gui.battle_control.requests import AvatarRequestsController as AvatarRequestsController
from gui.battle_control.view_components import createComponentsBridge as createComponentsBridge
from items.components.c11n_constants import SeasonType as SeasonType
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
BattleExitResult: Any

class BattleSessionProvider(IBattleSessionProvider):
    __slots__: tuple
    __ctx: Any
    __sharedRepo: Any
    __dynamicRepo: Any
    __requestsCtrl: Any
    __arenaDP: Any
    __arenaVisitor: Any
    __arenaListeners: Any
    __viewComponentsBridge: Any
    __invitations: Any
    __isReplayPlaying: Any
    __battleCache: Any
    onBattleSessionStart: Any
    onBattleSessionStop: Any
    onUpdateObservedVehicleData: Any
    def __init__(self):
        ...
    @property
    def shared(self):
        ...
    @property
    def dynamic(self):
        ...
    @property
    def arenaVisitor(self):
        ...
    @property
    def invitations(self):
        ...
    @property
    def battleCache(self):
        ...
    @property
    def isReplayPlaying(self):
        ...
    def getCtx(self):
        ...
    # decorador original: @adisp_async
    def sendRequest(self, ctx, callback, allowDelay=None):
        ...
    def setPlayerVehicle(self, vID, vDesc):
        ...
    def switchVehicle(self, vehicleID):
        ...
    def updateObservedVehicleData(self, vehicle):
        ...
    def updateVehicleEffects(self, vehicle):
        ...
    def getArenaDP(self):
        ...
    def addArenaCtrl(self, controller):
        ...
    def removeArenaCtrl(self, controller):
        ...
    def registerViewComponentsCtrl(self, controller):
        ...
    def registerViewComponents(self, *data):
        ...
    def addViewComponent(self, componentID, component, rule=...):
        ...
    def removeViewComponent(self, componentID):
        ...
    def getExitResult(self):
        ...
    def exit(self):
        ...
    def start(self, setup):
        ...
    def stop(self):
        ...
    def switchToPostmortem(self, noRespawnPossible=True, respawnAvailable=False):
        ...
    def updateVehicleQuickShellChanger(self, isActive):
        ...
    def movingToRespawnBase(self, vehicle=None):
        ...
    def invalidateVehicleState(self, state, value, vehicleID=0):
        ...
    def setVehicleHealth(self, isPlayerVehicle, vehicleID, newHealth, attackerID, attackReasonID):
        ...
    def repairPointAction(self, repairPointIndex, action, nextActionTime):
        ...
    def updateAvatarPrivateStats(self, stats):
        ...
    def addHitDirection(self, hitDirYaw, attackerID, damage, isBlocked, critFlags, isHighExplosive, damagedID, attackReasonID):
        ...
    def startVehicleVisual(self, vProxy, isImmediate=False):
        ...
    def stopVehicleVisual(self, vehicleID, isPlayerVehicle):
        ...
    def handleShortcutChatCommand(self, key):
        ...
    def handleContexChatCommand(self, key):
        ...
    def __pe_onBattleResultsReceived(self, isActiveVehicle, _):
        ...
    def __onMapsTrainingExit(self):
        ...
