# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/mechanic_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from cache import last_cached_method as last_cached_method
from cgf_events import gun_events as gun_events
from events_handler import eventHandler as eventHandler
from vehicles.components.component_events import VehicleComponentEventsCoreIntegration as VehicleComponentEventsCoreIntegration
from vehicles.mechanics.mechanic_states import MechanicStatesEvents as MechanicStatesEvents, IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher.mechanic_models import AuxiliaryRocketLauncherState as AuxiliaryRocketLauncherState

class AuxiliaryRocketLauncherStatesEvents(MechanicStatesEvents):
    def _createCoreIntegration(self):
        ...

class AuxiliaryRocketLauncherStatesCoreIntegration(VehicleComponentEventsCoreIntegration, IMechanicStatesListenerLogic):
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @last_cached_method(...)
    def __postReloadEvent(self, isReloaded, reloadStartTime):
        ...
