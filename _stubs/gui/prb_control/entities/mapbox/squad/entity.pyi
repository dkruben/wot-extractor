# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/mapbox/squad/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import account_helpers as account_helpers
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint as SquadEntryPoint, SquadEntity as SquadEntity
from gui.prb_control.entities.base.squad.mixins import SquadRestrictionsMixin as SquadRestrictionsMixin
from gui.prb_control.entities.mapbox.pre_queue.vehicles_watcher import MapboxVehiclesWatcher as MapboxVehiclesWatcher
from gui.prb_control.entities.mapbox.scheduler import MapboxScheduler as MapboxScheduler
from gui.prb_control.entities.mapbox.squad.action_handler import MapboxSquadActionsHandler as MapboxSquadActionsHandler
from gui.prb_control.entities.mapbox.squad.actions_validator import MapboxSquadActionsValidator as MapboxSquadActionsValidator
from gui.prb_control.entities.random.squad.entity import BalancedSquadDynamicRosterSettings as BalancedSquadDynamicRosterSettings
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import IMapboxController as IMapboxController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache

class MapboxSquadEntryPoint(SquadEntryPoint):
    def __init__(self, accountsToInvite=None):
        ...
    def makeDefCtx(self):
        ...
    def _doCreate(self, unitMgr, ctx):
        ...

class MapboxSquadEntity(SquadEntity, SquadRestrictionsMixin):
    __eventsCache: Any
    __lobbyContext: Any
    __mapboxCtrl: Any
    _isBalancedSquad: Any
    __watcher: Any
    storage: Any
    _isUseSPGValidateRule: Any
    _isUseScoutValidateRule: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    @property
    def squadRestrictions(self):
        ...
    def isBalancedSquadEnabled(self):
        ...
    def leave(self, ctx, callback=None):
        ...
    def getConfirmDialogMeta(self, ctx):
        ...
    def getQueueType(self):
        ...
    def getSquadLevelBounds(self):
        ...
    def unit_onUnitVehiclesChanged(self, dbID, vehicles):
        ...
    def unit_onUnitVehicleChanged(self, dbID, vehInvID, vehTypeCD):
        ...
    def unit_onUnitPlayerRoleChanged(self, playerID, prevRoleFlags, nextRoleFlags):
        ...
    def unit_onUnitPlayerRemoved(self, playerID, playerData):
        ...
    @property
    def _showUnitActionNames(self):
        ...
    def _createActionsHandler(self):
        ...
    def _createActionsValidator(self):
        ...
    def _createRosterSettings(self):
        ...
    def _createScheduler(self):
        ...
    def _vehicleStateCondition(self, v):
        ...
    def _onServerSettingChanged(self, *args, **kwargs):
        ...
    def _onInventoryVehiclesUpdated(self, diff):
        ...
    def _onUnitMemberVehiclesChanged(self, accountDBID):
        ...
    def __onVehicleClientStateChanged(self, _):
        ...
