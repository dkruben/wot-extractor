# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/public/mechanic_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from constants import LowChargeShotVisualState as LowChargeShotVisualState
from events_handler import eventHandler as eventHandler
from vehicles.components.component_events import VehicleComponentEventsCoreIntegration as VehicleComponentEventsCoreIntegration
from vehicles.mechanics.mechanic_states import MechanicStatesEvents as MechanicStatesEvents, IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from cgf_events import gun_events as gun_events
from vehicles.mechanics.gun_mechanics.low_charge_shot.public import LowChargeShotPublicMechanicState as LowChargeShotPublicMechanicState
_INSTANT_ANIMATION_TIMESTAMP = -10.0

class LowChargeShotPublicStatesEvents(MechanicStatesEvents):
    def _createCoreIntegration(self):
        ...

class LowChargeShotPublicStatesCoreIntegration(VehicleComponentEventsCoreIntegration, IMechanicStatesListenerLogic):
    __visualState: Any
    __fullShotAnimationTimerID: Any
    __fullShotAnimationEventHappened: Any
    def __init__(self, events, component):
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
    def __postLowChargeShotChangedEvent(self, state):
        ...
    def __fullShotAnimationEnd(self):
        ...

def _makeEvent(quickShot=None, fullShot=None, fullShotChangeTime=None):
    ...
def postLowChargeShotInitialEvent(visualState, spaceID, vehicleID, slotName):
    ...
