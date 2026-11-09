# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/random/squad/actions_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from BWUtil import AsyncReturn as AsyncReturn
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from gui.impl.gen import R as R
from gui.prb_control.entities.base.squad.actions_handler import SquadActionsHandler as SquadActionsHandler
from gui.shared.event_dispatcher import showPlatoonWarningDialog as showPlatoonWarningDialog
from wg_async import wg_async as wg_async, wg_await as wg_await

class RandomSquadActionsHandler(SquadActionsHandler):
    ...

class BalancedSquadActionsHandler(RandomSquadActionsHandler):
    # decorador original: @wg_async
    def _validateUnitState(self, entity):
        ...
    @staticmethod
    def _isSquadHavePlayersInBattle(slotPlayer, playerInfo):
        ...
