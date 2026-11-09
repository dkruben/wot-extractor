# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/squad/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import json as json
from frameworks.wulf import WindowLayer as WindowLayer
from wg_async import wg_await as wg_await, wg_async as wg_async
import account_helpers as account_helpers
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control import prb_getters as prb_getters, prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint as SquadEntryPoint, SquadEntity as SquadEntity
from gui.prb_control.storages import storage_getter as storage_getter, RECENT_PRB_STORAGE as RECENT_PRB_STORAGE
from gui.prb_control.settings import REQUEST_TYPE as REQUEST_TYPE
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.impl.gen import R as R
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.dialogs.gf_builders import ResDialogBuilder as ResDialogBuilder
from last_stand.gui.ls_account_settings import getFirstNewStatusUnlockLevel as getFirstNewStatusUnlockLevel
from last_stand.gui.prb_control.entities.squad.ctx import SetDifficultyLevelUnitCtx as SetDifficultyLevelUnitCtx, LastStandSquadSettingsCtx as LastStandSquadSettingsCtx
from last_stand.gui.prb_control.entities.vehicles_watcher import VehiclesWatcher as VehiclesWatcher
from last_stand.gui.shared.event_dispatcher import showHangar as showHangar
from last_stand.skeletons.ls_vehicle_selection_controller import ILSVehicleSelectionController as ILSVehicleSelectionController
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from helpers import dependency as dependency
from last_stand.gui.prb_control.entities.squad.actions_validator import LastStandSquadActionsValidator as LastStandSquadActionsValidator, LastStandSquadActionsHandler as LastStandSquadActionsHandler
from last_stand.gui.prb_control.entities.squad.scheduler import LastStandSquadScheduler as LastStandSquadScheduler
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from last_stand.gui.ls_gui_constants import DifficultyLevel as DifficultyLevel, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from last_stand.gui.ls_gui_constants import QUEUE_TYPE_TO_DIFFICULTY_LEVEL as QUEUE_TYPE_TO_DIFFICULTY_LEVEL
from last_stand_common.last_stand_constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE, CURRENT_QUEUE_TYPE_KEY as CURRENT_QUEUE_TYPE_KEY, CLIENT_UNIT_CMD as CLIENT_UNIT_CMD
from last_stand.skeletons.ls_controller import ILSController as ILSController

class LastStandEntryPoint(SquadEntryPoint):
    __difficultyLevelCtrl: Any
    arenaUniqueID: Any
    def __init__(self, accountsToInvite=None):
        ...
    def makeDefCtx(self):
        ...
    def setExtData(self, extData):
        ...
    def _doCreate(self, unitMgr, ctx):
        ...

class LastStandSquadEntity(SquadEntity):
    __difficultyLevelCtrl: Any
    eventsCache: Any
    lobbyContext: Any
    lsCtrl: Any
    lsVehicleCtrl: Any
    _mmData: Any
    __watcher: Any
    _arenaUniqueID: Any
    def __init__(self):
        ...
    def setReserve(self, ctx, callback=None):
        ...
    # decorador original: @storage_getter(...)
    def storage(self):
        ...
    @property
    def currentQueueType(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def leave(self, ctx, callback=None):
        ...
    def getQueueType(self):
        ...
    def doAction(self, action=None):
        ...
    def doBattleQueue(self, ctx, callback=None):
        ...
    def unit_onUnitVehicleChanged(self, dbID, vehInvID, vehTypeCD):
        ...
    def unit_onUnitVehiclesChanged(self, dbID, vehicles):
        ...
    def unit_onUnitPlayerRoleChanged(self, playerID, prevRoleFlags, nextRoleFlags):
        ...
    def unit_onUnitPlayerRemoved(self, playerID, playerData):
        ...
    def unit_onUnitExtraChanged(self, extras):
        ...
    def getConfirmDialogMeta(self, ctx):
        ...
    def showDialog(self, meta, callback, parent=None):
        ...
    def loadHangar(self):
        ...
    def _onServerSettingChanged(self, *args, **kwargs):
        ...
    def _onInventoryVehiclesUpdated(self, diff):
        ...
    def _setDifficultyLevel(self, ctx, callback=None):
        ...
    def _onUnitMemberVehiclesChanged(self, accoundDbID):
        ...
    def _createActionsHandler(self):
        ...
    def _createActionsValidator(self):
        ...
    def _createScheduler(self):
        ...
    def _goToHangar(self):
        ...
    def _updateEntityType(self, *args, **kwargs):
        ...
    def _onLevelsInfoReady(self):
        ...
    @property
    def _showUnitActionNames(self):
        ...
    def __createUnitLeaveMeta(self, unlockCtx, isSwitching=False):
        ...
    def __getLeaveSquadBuilder(self, key):
        ...
    # decorador original: @wg_async
    def __showBuilderDialog(self, builder, callback):
        ...
    def __updateVehiclesWatcher(self):
        ...
    def __updateQueueTypeFromUnit(self):
        ...
