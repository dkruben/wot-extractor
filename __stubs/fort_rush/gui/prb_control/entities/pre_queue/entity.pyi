# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/prb_control/entities/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from fort_rush.gui.fort_rush_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from fort_rush.gui.prb_control.entities.pre_queue.actions_validator import FortRushBattleActionsValidator as FortRushBattleActionsValidator
from fort_rush.gui.prb_control.entities.pre_queue.ctx import FortRushBattleQueueCtx as FortRushBattleQueueCtx
from gui.prb_control.entities.base.scheduler import BaseScheduler as BaseScheduler
from gui.shared.event_dispatcher import showHangar as showHangar
from fort_rush_common.fort_rush_constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.storages import storage_getter as storage_getter, RECENT_PRB_STORAGE as RECENT_PRB_STORAGE
from gui.prb_control.entities.base.pre_queue.entity import PreQueueSubscriber as PreQueueSubscriber, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueEntity as PreQueueEntity
from gui.prb_control.items import SelectResult as SelectResult
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from helpers import dependency as dependency
from fort_rush.gui.prb_control.entities.pre_queue.vehicles_watcher import FortRushVehicleWatcher as FortRushVehicleWatcher
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController

class FortRushBattleEntryPoint(PreQueueEntryPoint):
    def __init__(self):
        ...

class FortRushBattleEntity(PreQueueEntity):
    __battleController: Any
    __watcher: Any
    def __init__(self):
        ...
    # decorador original: @storage_getter(...)
    def storage(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def doSelectAction(self, action):
        ...
    def canInvite(self, prbType):
        ...
    @property
    def _accountComponent(self):
        ...
    def _doQueue(self, ctx):
        ...
    def _doDequeue(self, ctx):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
    def _goToHangar(self):
        ...
    def _makeQueueCtxByAction(self, action=None):
        ...
    def _createActionsValidator(self):
        ...
    def _createScheduler(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def canSelectPrbEntity(ctrl=None):
    ...
