# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/prb_control/entities/squad/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from BWUtil import AsyncReturn as AsyncReturn
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.prb_control.entities.base.squad.actions_handler import SquadActionsHandler as SquadActionsHandler
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator as SquadActionsValidator, SquadVehiclesValidator as SquadVehiclesValidator
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from halloween.gui.prb_control.entities import checkVehicleAbilitiesFull as checkVehicleAbilitiesFull
from halloween.gui.prb_control.entities.squad.ctx import HalloweenSquadSettingsCtx as HalloweenSquadSettingsCtx
from halloween.gui.shared.event_dispatcher import showBattleResult as showBattleResult
from halloween_common.halloween_constants import UNIT_HALLOWEEN_EXTRA_DATA_KEY as UNIT_HALLOWEEN_EXTRA_DATA_KEY, UNIT_DIFFICULTY_LEVELS_KEY as UNIT_DIFFICULTY_LEVELS_KEY, CURRENT_QUEUE_TYPE_KEY as CURRENT_QUEUE_TYPE_KEY
from helpers import dependency as dependency
from gui.prb_control.items import ValidationResult as ValidationResult
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from wg_async import await_callback as await_callback, wg_async as wg_async

class HalloweenSquadActionsHandler(SquadActionsHandler):
    def _updateSquadCtx(self, initCtx, squadCtx):
        ...
    def _loadWindow(self, ctx):
        ...
    def setUnitChanged(self, loadHangar=False):
        ...
    # decorador original: @wg_async
    def _checkVehicleAmmo(self, vehicle):
        ...

class HalloweenStateValidator(SquadVehiclesValidator):
    __halloweenBattleCtrl: Any
    __platoonCtrl: Any
    def _validate(self):
        ...

class HalloweenSquadActionsValidator(SquadActionsValidator):
    def _createVehiclesValidator(self, entity):
        ...
