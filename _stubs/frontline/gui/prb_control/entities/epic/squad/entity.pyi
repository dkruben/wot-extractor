# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic/squad/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frontline.gui.prb_control.entities.epic.pre_queue.vehicles_watcher import EpicVehiclesWatcher as EpicVehiclesWatcher
from frontline.gui.prb_control.entities.epic.squad.actions_validator import EpicSquadActionsValidator as EpicSquadActionsValidator
from frontline.gui.prb_control.entities.epic.squad.components import EpicSquadRestrictionsProvider as EpicSquadRestrictionsProvider
import account_helpers as account_helpers
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint as SquadEntryPoint, SquadEntity as SquadEntity
from gui.prb_control.entities.base.squad.mixins import SquadRestrictionsMixin as SquadRestrictionsMixin
from gui.prb_control.entities.random.squad.actions_handler import BalancedSquadActionsHandler as BalancedSquadActionsHandler
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache

class EpicSquadEntryPoint(SquadEntryPoint):
    def __init__(self, accountsToInvite=None):
        ...
    def makeDefCtx(self):
        ...
    def _doCreate(self, unitMgr, ctx):
        ...

class EpicSquadEntity(SquadEntity, SquadRestrictionsMixin):
    eventsCache: Any
    lobbyContext: Any
    _isBalancedSquad: Any
    __watcher: Any
    storage: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def leave(self, ctx, callback=None):
        ...
    def getQueueType(self):
        ...
    @property
    def _showUnitActionNames(self):
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
    def squadRestrictions(self):
        ...
    @classmethod
    def _createSquadRestrictionsProvider(cls):
        ...
    def _createActionsHandler(self):
        ...
    def _createActionsValidator(self):
        ...
    def _vehicleStateCondition(self, v):
        ...
    def _onServerSettingChanged(self, *args, **kwargs):
        ...
    def _onInventoryVehiclesUpdated(self, diff):
        ...
    def _onUnitMemberVehiclesChanged(self, accountDBID):
        ...
