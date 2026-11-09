# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/components/vehicle_prefabs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import weakref as weakref
from functools import partial as partial
import CGF as CGF
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from vehicle_systems.model_assembler import loadAppearancePrefab as loadAppearancePrefab
from events_containers.components.life_cycle import ILifeCycleComponent as ILifeCycleComponent
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from Vehicle import Vehicle as Vehicle
_logger: Any

class VehiclePrefabSpawner(ContainersListener, IComponentLifeCycleListenerLogic):
    _DEFAULT_OUTFIT = 'default'
    __vehicle: Any
    __vehicleID: Any
    __idGen: Any
    __prefabRoot: Any
    __prefabPath: Any
    def __init__(self, vehicle):
        ...
    # decorador original: @eventHandler
    def onComponentParamsCollected(self, params):
        ...
    # decorador original: @eventHandler
    def onComponentAppearanceReady(self, component):
        ...
    # decorador original: @eventHandler
    def onComponentAppearanceReset(self, component):
        ...
    # decorador original: @eventHandler
    def onComponentDestroyed(self, component):
        ...
    def _getPrefabPath(self, typeDescriptor, skin):
        ...
    def __onComponentPrefabLoaded(self, sequenceID, root, _, queue):
        ...
    def __logMessage(self, logMethod, message):
        ...
    def __removePrefabRoot(self, source):
        ...

class VehiclePrefabSetsSpawner(VehiclePrefabSpawner):
    _PREFABS_SET_KEY = ''
    def _getPrefabPath(self, typeDescriptor, skin):
        ...
    def _getPrefabsSets(self, typeDescriptor):
        ...

class VehicleMechanicPrefabSpawner(VehiclePrefabSetsSpawner):
    _PREFABS_SET_KEY = 'mechanicEffects'
    def _getPrefabsSets(self, typeDescriptor):
        ...

def createMechanicPrefabSpawner(vehicle, component):
    ...
