# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/vehicle_mechanics_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import IS_VS_EDITOR as IS_VS_EDITOR, UNKNOWN_VEHICLE_ID as UNKNOWN_VEHICLE_ID
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, MECHANIC_KEY_BY_NAME as MECHANIC_KEY_BY_NAME
from visual_script.block import Block as Block, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import ASPECT as ASPECT, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.vehicle_mechanics_blocks import VehicleMechanicsMeta as VehicleMechanicsMeta
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
from _weakref import ProxyType as ProxyType
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
cgf_helpers: Any
mechanic_trackers: Any

class VehiclesTrackingWatcher(object):
    @classmethod
    def startVehicleMechanicsTracking(cls, vehicleID, mechanics, listener):
        ...
    @classmethod
    def stopVehicleMechanicsTracking(cls, vehicleID, mechanics, listener):
        ...

class IVehicleMechanicsTrackerListenerLogic(object):
    ...

class IComponentLifeCycleListenerLogic(object):
    ...

class IMechanicStatesListenerLogic(object):
    ...

class VehicleMechanicEventsBlock(Block, VehicleMechanicsMeta, ContainersListener, VehiclesTrackingWatcher, IVehicleMechanicsTrackerListenerLogic):
    _EVENTS_NAME = ''
    __vehicleID: Any
    _vehicleMechanicKey: Any
    _subscribe: Any
    _unsubscribe: Any
    _object: Any
    _subscribeOut: Any
    _unsubscribeOut: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def captionText(self):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...

class VehicleSelectableMechanicEventsBlock(VehicleMechanicEventsBlock):
    @classmethod
    def initParams(cls):
        ...
    @classmethod
    def _getInitParamMechanics(cls):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...

class VehicleMechanicLifeCycleEventsBlock(VehicleMechanicEventsBlock, IComponentLifeCycleListenerLogic):
    _EVENTS_NAME = 'lifeCycle'
    _onComponentAvatarReadySlot: Any
    _onComponentParamsCollectedSlot: Any
    _onComponentDestroyedSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    # decorador original: @eventHandler
    def onComponentAvatarReady(self, component):
        ...
    # decorador original: @eventHandler
    def onComponentParamsCollected(self, params):
        ...
    # decorador original: @eventHandler
    def onComponentDestroyed(self, component):
        ...
    def _onComponentAvatarReady(self, component):
        ...
    def _onComponentParamsCollected(self, params):
        ...
    def _onComponentDestroyed(self, component):
        ...

class VehicleMechanicStateEventsBlock(VehicleMechanicEventsBlock, IMechanicStatesListenerLogic):
    _EVENTS_NAME = 'states'
    _onStatePreparedSlot: Any
    _onStateObservationSlot: Any
    _onStateTransitionSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
