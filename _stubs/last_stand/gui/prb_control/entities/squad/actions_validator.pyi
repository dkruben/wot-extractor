# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from BWUtil import AsyncReturn as AsyncReturn
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.squad.actions_handler import SquadActionsHandler as SquadActionsHandler
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from last_stand.gui.prb_control.entities import checkVehicleAbilitiesFull as checkVehicleAbilitiesFull
from last_stand.gui.prb_control.entities.squad.ctx import LastStandSquadSettingsCtx as LastStandSquadSettingsCtx
from last_stand.gui.shared.event_dispatcher import showBattleResult as showBattleResult
from last_stand_common.last_stand_constants import UNIT_LS_EXTRA_DATA_KEY as UNIT_LS_EXTRA_DATA_KEY, UNIT_DIFFICULTY_LEVELS_KEY as UNIT_DIFFICULTY_LEVELS_KEY, CURRENT_QUEUE_TYPE_KEY as CURRENT_QUEUE_TYPE_KEY, DEFAULT_UNIT_DIFFICULTY_LEVELS as DEFAULT_UNIT_DIFFICULTY_LEVELS
from helpers import dependency as dependency
from gui.prb_control.items import ValidationResult as ValidationResult
from last_stand.skeletons.ls_controller import ILSController as ILSController
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from wg_async import await_callback as await_callback, wg_async as wg_async

class LastStandSquadActionsHandler(SquadActionsHandler):
    def _updateSquadCtx(self, initCtx, squadCtx):
        ...
    def _loadWindow(self, ctx):
        ...
    def setUnitChanged(self, loadHangar=False):
        ...
    # decorador original: @wg_async
    def _checkVehicleAmmo(self, vehicle):
        ...
    @staticmethod
    def _isSquadHavePlayersInBattle(slotPlayer, playerInfo):
        ...

class LastStandStateValidator(SquadVehiclesValidator):
    lsCtrl: Any
    __platoonCtrl: Any
    def _validate(self):
        ...

class LastStandSquadActionsValidator(SquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
