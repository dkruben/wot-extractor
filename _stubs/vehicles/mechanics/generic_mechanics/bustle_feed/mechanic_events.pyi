# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/bustle_feed/mechanic_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from events_handler import eventHandler as eventHandler
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from vehicles.components.component_events import VehicleComponentEventsCoreIntegration as VehicleComponentEventsCoreIntegration
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic, MechanicStatesEvents as MechanicStatesEvents
from vehicles.mechanics.generic_mechanics.bustle_feed.mechanic_interfaces import IBustleFeedEventsLogic as IBustleFeedEventsLogic, IBustleFeedListenerLogic as IBustleFeedListenerLogic
from vehicle_systems.components.vehicle_variable_storage import update as updateVariable
_logger: Any
_INIT_VAR_VAL = -1

class BustleFeedStatesEvents(MechanicStatesEvents, IBustleFeedEventsLogic):
    onReloadTriggered: Any
    def __init__(self, component, tickInterval):
        ...
    def processReloadTriggered(self, shell, side, duration):
        ...
    def _createCoreIntegration(self):
        ...

class BustleFeedVfxCoreIntegration(VehicleComponentEventsCoreIntegration, IMechanicStatesListenerLogic, IBustleFeedListenerLogic):
    __component: Any
    __callbackDelayer: Any
    def __init__(self, events, component):
        ...
    # decorador original: @eventHandler
    def onReloadTriggered(self, shell, side, duration):
        ...
    # decorador original: @eventHandler
    def onEventsContainerDestroy(self, events):
        ...
    def __updateVariables(self, shell, side):
        ...
    def __updateVariablesDelayed(self, shell, side):
        ...
