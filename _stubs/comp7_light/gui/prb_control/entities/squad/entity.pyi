# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/entities/squad/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from future.utils import viewvalues as viewvalues
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from comp7_light.gui.comp7_light_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from comp7_light.gui.prb_control.entities.base.ctx import Comp7LightPrbAction as Comp7LightPrbAction
from comp7_light.gui.prb_control.entities.comp7_light_prb_helpers import Comp7LightViewPresenter as Comp7LightViewPresenter
from comp7_light.gui.prb_control.entities.pre_queue.vehicles_watcher import Comp7LightVehiclesWatcher as Comp7LightVehiclesWatcher
from comp7_light.gui.prb_control.entities.scheduler import Comp7LightScheduler as Comp7LightScheduler
from comp7_light.gui.prb_control.entities.squad.action_handler import Comp7LightSquadActionsHandler as Comp7LightSquadActionsHandler
from comp7_light.gui.prb_control.entities.squad.actions_validator import Comp7LightSquadActionsValidator as Comp7LightSquadActionsValidator
from comp7_light_constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint as SquadEntryPoint, SquadEntity as SquadEntity
from gui.prb_control.items.unit_items import DynamicRosterSettings as DynamicRosterSettings
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from skeletons.gui.shared import IItemsCache as IItemsCache

class Comp7LightSquadEntryPoint(SquadEntryPoint):
    __comp7LightController: Any
    __squadSize: Any
    def __init__(self, accountsToInvite=None):
        ...
    def makeDefCtx(self):
        ...
    def configure(self, action):
        ...
    def _doCreate(self, unitMgr, ctx):
        ...

class Comp7LightSquadEntity(SquadEntity):
    __comp7LightController: Any
    __itemsCache: Any
    __watcher: Any
    __validIntCDs: Any
    __introPresenter: Any
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

class Comp7LightRosterSettings(DynamicRosterSettings):
    _maxSlots: Any
    def updateSettings(self, unit):
        ...
    def _extractSettings(self, unit):
        ...
