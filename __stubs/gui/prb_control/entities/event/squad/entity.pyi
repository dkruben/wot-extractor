# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/event/squad/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs import rally_dialog_meta as rally_dialog_meta
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.entities.base.unit.ctx import SetVehicleUnitCtx as SetVehicleUnitCtx, SetReadyUnitCtx as SetReadyUnitCtx
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint as SquadEntryPoint, SquadEntity as SquadEntity
from gui.prb_control.entities.event.squad.actions_handler import EventBattleSquadActionsHandler as EventBattleSquadActionsHandler
from gui.prb_control.entities.event.squad.actions_validator import EventBattleSquadActionsValidator as EventBattleSquadActionsValidator
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.event.squad.scheduler import EventSquadScheduler as EventSquadScheduler
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from helpers import dependency as dependency
from skeletons.gui.game_control import IEventBattlesController as IEventBattlesController

# decorador original: @ReprInjector.withParent(...)
class EventSquadSettingsCtx(SquadSettingsCtx):
    __slots__: tuple
    _keepCurrentView: Any
    def __init__(self, waitingID='', accountsToInvite=None, keepCurrentView=False):
        ...
    def getKeepCurrentView(self):
        ...

class EventBattleSquadEntryPoint(SquadEntryPoint):
    _keepCurrentView: Any
    def __init__(self, accountsToInvite=None):
        ...
    def _doCreate(self, unitMgr, ctx):
        ...
    def setKeepCurrentView(self, keepCurrentView):
        ...
    def makeDefCtx(self):
        ...

class EventBattleSquadEntity(SquadEntity):
    __eventBattlesCtrl: Any
    storage: Any
    ctx: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def getQueueType(self):
        ...
    def getLeaderEventEnqueueData(self):
        ...
    def getConfirmDialogMeta(self, ctx):
        ...
    # decorador original: @vehicleAmmoCheck
    def togglePlayerReadyAction(self, launchChain=False):
        ...
    def _goToHangar(self):
        ...
    @property
    def _showUnitActionNames(self):
        ...
    def _createActionsValidator(self):
        ...
    def _createActionsHandler(self):
        ...
    def _createScheduler(self):
        ...
    def __showDialog(self, ctx):
        ...
