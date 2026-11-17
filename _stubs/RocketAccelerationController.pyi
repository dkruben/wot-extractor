# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/RocketAccelerationController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
from typing import List as List
import BigWorld as BigWorld
import CGF as CGF
from constants import ROCKET_ACCELERATION_STATE as ROCKET_ACCELERATION_STATE
from Event import Event as Event
from events_containers.components.life_cycle import createComponentLifeCycleEvents as createComponentLifeCycleEvents, ILifeCycleComponent as ILifeCycleComponent
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from wotdecorators import noexcept as noexcept
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicle_systems.model_assembler import loadAppearancePrefab as loadAppearancePrefab
from events_containers.components.life_cycle import IComponentLifeCycleEvents as IComponentLifeCycleEvents
_logger: Any
_DEFAULT_OUTFIT = 'default'

# decorador original: @ReprInjector.withParent(...)
class RocketAccelerationController(BigWorld.DynamicScriptComponent, ILifeCycleComponent, IMechanicComponent):
    __prefabGameObject: Any
    __lifeCycleEvents: Any
    __onStateChanged: Any
    __onTryActivate: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def lifeCycleEvents(self):
        ...
    def tryActivate(self):
        ...
    # decorador original: @noexcept
    def set_stateStatus(self, _=None):
        ...
    def onDestroy(self):
        ...
    def onLeaveWorld(self):
        ...
    def subscribe(self, callback=None, tryActivateCallback=None):
        ...
    def unsubscribe(self, callback=None, tryActivateCallback=None):
        ...
    def sendStateToAllSubscribers(self):
        ...
    def cleanup(self):
        ...
    def __initAppearance(self):
        ...
    def __onLoaded(self, path, root, _, queue):
        ...
    def __tryUpdatePrefab(self):
        ...
