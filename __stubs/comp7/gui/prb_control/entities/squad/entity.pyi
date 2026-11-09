# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/squad/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from future.utils import viewvalues as viewvalues
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from comp7.gui.comp7_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from comp7.gui.prb_control.entities.base.ctx import Comp7PrbAction as Comp7PrbAction
from comp7.gui.prb_control.entities.comp7_prb_helpers import Comp7ViewPresenter as Comp7ViewPresenter
from comp7.gui.prb_control.entities.pre_queue.vehicles_watcher import Comp7VehiclesWatcher as Comp7VehiclesWatcher
from comp7.gui.prb_control.entities.scheduler import Comp7Scheduler as Comp7Scheduler
from comp7.gui.prb_control.entities.squad.action_handler import Comp7SquadActionsHandler as Comp7SquadActionsHandler
from comp7.gui.prb_control.entities.squad.actions_validator import Comp7SquadActionsValidator as Comp7SquadActionsValidator
from comp7_common.comp7_constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint as SquadEntryPoint, SquadEntity as SquadEntity
from gui.prb_control.items.unit_items import DynamicRosterSettings as DynamicRosterSettings
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache

class Comp7SquadEntryPoint(SquadEntryPoint):
    __comp7Ctrl: Any
    __squadSize: Any
    def __init__(self, accountsToInvite=None):
        ...
    def makeDefCtx(self):
        ...
    def configure(self, action):
        ...
    def _doCreate(self, unitMgr, ctx):
        ...

class Comp7SquadEntity(SquadEntity):
    __comp7Controller: Any
    __itemsCache: Any
    __watcher: Any
    __introPresenter: Any
    __validIntCDs: Any
    __toggleAfterPreviewLeave: Any
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
    def getConfirmDialogMeta(self, ctx):
        ...
    @property
    def _showUnitActionNames(self):
        ...
    def _createActionsValidator(self):
        ...
    def _createScheduler(self):
        ...
    def _createActionsHandler(self):
        ...
    def _createRosterSettings(self):
        ...
    def _buildStats(self, unitMgrID, unit):
        ...
    def __onVehicleClientStateChanged(self, intCDs):
        ...
    def __onPreviewVehicleSelected(self):
        ...

class Comp7RosterSettings(DynamicRosterSettings):
    _maxSlots: Any
    def updateSettings(self, unit):
        ...
    def _extractSettings(self, unit):
        ...
