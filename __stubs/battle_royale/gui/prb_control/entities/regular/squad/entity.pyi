# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/squad/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from battle_royale.gui.constants import BattleRoyaleSubMode as BattleRoyaleSubMode
from battle_royale.gui.impl.lobby.br_helpers.utils import isBattleResultsStateEntered as isBattleResultsStateEntered
from battle_royale.gui.prb_control.entities.regular.pre_queue.vehicles_watcher import BattleRoyaleVehiclesWatcher as BattleRoyaleVehiclesWatcher
from battle_royale.gui.prb_control.entities.regular.scheduler import RoyaleScheduler as RoyaleScheduler
from battle_royale.gui.prb_control.entities.regular.squad.actions_validator import BattleRoyaleSquadActionsValidator as BattleRoyaleSquadActionsValidator
from battle_royale.gui.prb_control.entities.regular.squad.action_handler import BattleRoyaleSquadActionsHandler as BattleRoyaleSquadActionsHandler
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint as SquadEntryPoint, SquadEntity as SquadEntity
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.prb_control.storages import prequeue_storage_getter as prequeue_storage_getter
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import BattleRoyalePlatoonEvent as BattleRoyalePlatoonEvent
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyaleSquadEntryPoint(SquadEntryPoint):
    def __init__(self, accountsToInvite=None):
        ...
    def makeDefCtx(self):
        ...
    def _doCreate(self, unitMgr, ctx):
        ...

class BattleRoyaleSquadEntity(SquadEntity):
    __battleRoyaleController: Any
    _VALID_RESTRICTIONS: tuple
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
    def getConfirmDialogMeta(self, ctx):
        ...
    def isVehiclesReadyToBattle(self):
        ...
    def _goToHangar(self):
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
