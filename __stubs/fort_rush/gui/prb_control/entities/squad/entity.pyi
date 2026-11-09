# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/prb_control/entities/squad/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import account_helpers as account_helpers
from fort_rush.gui.prb_control.entities.pre_queue.vehicles_watcher import FortRushVehicleWatcher as FortRushVehicleWatcher
from gui.shared.event_dispatcher import showHangar as showHangar
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from fort_rush_common.configs.fort_rush_battles_config import fortRushBattlesConfigGameParamsSchema as fortRushBattlesConfigGameParamsSchema
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint as SquadEntryPoint, SquadEntity as SquadEntity
from gui.prb_control.entities.base.squad.mixins import SquadRestrictionsMixin as SquadRestrictionsMixin
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.storages import storage_getter as storage_getter, RECENT_PRB_STORAGE as RECENT_PRB_STORAGE
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from fort_rush.gui.fort_rush_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from fort_rush.gui.prb_control.entities.squad.actions_validator import FortRushSquadActionsValidator as FortRushSquadActionsValidator
from fort_rush.gui.prb_control.entities.squad.components import FortRushSquadRestrictionsProvider as FortRushSquadRestrictionsProvider
from fort_rush_common.fort_rush_constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE, CLIENT_UNIT_CMD as CLIENT_UNIT_CMD

class FortRushEntryPoint(SquadEntryPoint):
    def __init__(self, accountsToInvite=None):
        ...
    def _doCreate(self, unitMgr, ctx):
        ...

class FortRushSquadEntity(SquadEntity, SquadRestrictionsMixin):
    frCtrl: Any
    eventsCache: Any
    lobbyContext: Any
    _mmData: Any
    __watcher: Any
    def __init__(self):
        ...
    def setReserve(self, ctx, callback=None):
        ...
    # decorador original: @storage_getter(...)
    def storage(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    @property
    def squadRestrictions(self):
        ...
    def getConfirmDialogMeta(self, ctx):
        ...
    def getQueueType(self):
        ...
    def doSelectAction(self, action):
        ...
    def doAction(self, action=None):
        ...
    def doBattleQueue(self, ctx, callback=None):
        ...
    def canInvite(self, prbType):
        ...
    def unit_onUnitVehicleChanged(self, dbID, vehInvID, vehTypeCD):
        ...
    def unit_onUnitVehiclesChanged(self, dbID, vehicles):
        ...
    def unit_onUnitPlayerRoleChanged(self, playerID, prevRoleFlags, nextRoleFlags):
        ...
    def unit_onUnitPlayerRemoved(self, playerID, playerData):
        ...
    def unit_onUnitReadyMaskChanged(self, prevMask, nextMask):
        ...
    def _doStartBattleRequest(self, ctx, flags, callback):
        ...
    def _onServerSettingChanged(self, *args, **kwargs):
        ...
    def _onInventoryVehiclesUpdated(self, diff):
        ...
    def _onUnitMemberVehiclesChanged(self, accoundDbID):
        ...
    def _createActionsValidator(self):
        ...
    @classmethod
    def _createSquadRestrictionsProvider(cls):
        ...
    def _goToHangar(self):
        ...
    def _vehicleStateCondition(self, v):
        ...
