# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/components/vehicle_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent as ReplicableDynamicScriptComponent
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import createComponentLifeCycleEvents as createComponentLifeCycleEvents, ILifeCycleComponent as ILifeCycleComponent
from events_handler import eventHandler as eventHandler, EventsQuery as EventsQuery
from PlayerEvents import g_playerEvents as g_playerEvents
from shared_utils import skipInEditor as skipInEditor
from vehicle_appearance.constants import AppearanceState as AppearanceState
from vehicles.components.component_wrappers import ifAppearanceReady as ifAppearanceReady, ifPlayerVehicle as ifPlayerVehicle
from vehicles.entities.vehicle_events import IVehicleEventsListenerLogic as IVehicleEventsListenerLogic
from Avatar import PlayerAvatar as PlayerAvatar
from events_containers.components.life_cycle import IComponentLifeCycleEvents as IComponentLifeCycleEvents
from Vehicle import Vehicle as Vehicle
from vehicle_systems.CompoundAppearance import CompoundAppearance as CompoundAppearance
_logger: Any

class VehicleDynamicComponent(ReplicableDynamicScriptComponent, ILifeCycleComponent, EventsQuery, ContainersListener, IVehicleEventsListenerLogic):
    EVENTS_PROPERTY_NAME = 'events'
    APPEARANCE_READY_STATE = AppearanceState.CONSTRUCTED
    __appearanceReady: Any
    __componentDestroyed: Any
    __lifeCycleEvents: Any
    # decorador original: @skipInEditor
    def __init__(self):
        ...
    @property
    def lifeCycleEvents(self):
        ...
    def isAppearanceReady(self):
        ...
    def isComponentDestroyed(self):
        ...
    def isPlayerVehicle(self, player):
        ...
    def isObservedVehicle(self, player, vehicle):
        ...
    def onDestroy(self):
        ...
    def onLeaveWorld(self):
        ...
    # decorador original: @eventHandler
    def onAppearanceReady(self):
        ...
    # decorador original: @eventHandler
    def onAppearanceComponentsReady(self):
        ...
    # decorador original: @eventHandler
    # decorador original: @ifAppearanceReady
    def onAppearanceReset(self):
        ...
    # decorador original: @eventHandler
    # decorador original: @ifAppearanceReady
    def onSiegeStateUpdated(self, newState, timeToNextMode):
        ...
    def _initComponent(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onAppearanceReset(self):
        ...
    def _onAvatarReady(self, player):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    # decorador original: @ifPlayerVehicle
    def _updateComponentAvatar(self, player=None):
        ...
    # decorador original: @ifAppearanceReady
    def _updateComponentAppearance(self, **kwargs):
        ...
    def __initComponentAvatar(self):
        ...
    def __initComponentAppearance(self):
        ...
    def __isAvatarReady(self, player=None):
        ...
    def __isAppearanceReady(self):
        ...
    # decorador original: @ifPlayerVehicle
    def __onAvatarReady(self, player=None):
        ...
    def __processAppearanceReady(self):
        ...
    @classmethod
    def __appearanceReadyState(cls):
        ...
