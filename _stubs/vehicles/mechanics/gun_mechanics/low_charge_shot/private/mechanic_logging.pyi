# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/private/mechanic_logging.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import LowChargeShotReloadingState as LowChargeShotReloadingState
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR as CANT_SHOOT_ERROR
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from uilogging.vehicle_mechanics.low_charge_shot.logger import LowChargeShotUILogger as LowChargeShotUILogger
from helpers import dependency as dependency

class LowChargeShotUILogging(ContainersListener, IMechanicStatesListenerLogic):
    __sessionProvider: Any
    __uiLogger: Any
    __reloadingState: Any
    __arenaUniqueID: Any
    __logOnceSet: Any
    def __init__(self):
        ...
    def subscribe(self, mechanicComponent, arenaUniqueID):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onEventsContainerDestroy(self, events):
        ...
    def __onShotBlocked(self, error):
        ...
