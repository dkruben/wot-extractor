# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/crest_moving_effects_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
import CGF as CGF
from Event import Event as Event
from Sound import Sound3DComponent as Sound3DComponent
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListenerLogic as IVehicleMechanicsTrackerListenerLogic
_logger: Any

# decorador original: @registerComponent
class CrestMovingEffectsComponent(ContainersListener, IVehicleMechanicsTrackerListenerLogic, IMechanicStatesListenerLogic):
    category = 'Vehicle Mechanics'
    editorTitle = 'Crest Moving Effects Component'
    domain: Any
    soundMoveUp: Any
    soundMoveDown: Any
    soundStopUp: Any
    soundStopDown: Any
    onStateTransitionEvent: Any
    activeSound: Any
    stopSound: Any
    vehicleID: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
