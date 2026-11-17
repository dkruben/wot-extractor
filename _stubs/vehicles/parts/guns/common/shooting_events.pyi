# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/common/shooting_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from cgf_events import gun_events as gun_events
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer
from events_containers.components.common import ClientComponentEventsDebugger as ClientComponentEventsDebugger
from events_handler import eventHandler as eventHandler
from vehicles.components.component_events import VehicleComponentEventsCoreIntegration as VehicleComponentEventsCoreIntegration
from vehicles.parts.guns.common.guns_interfaces import IGunShootingEventsLogic as IGunShootingEventsLogic, IGunShootingListenerLogic as IGunShootingListenerLogic
from vehicles.parts.guns.common.guns_interfaces import IGunComponent as IGunComponent, IGunShootingListener as IGunShootingListener

class GunShootingEvents(ClientEventsContainer, IGunShootingEventsLogic):
    __componentRef: Any
    _isAppearanceReady: Any
    onAppearanceReady: Any
    onDiscreteShot: Any
    onMultiShot: Any
    def __init__(self, component):
        ...
    def destroy(self):
        ...
    def lateSubscribe(self, listener):
        ...
    def processAppearanceReady(self):
        ...
    def processAppearanceReset(self):
        ...
    def processDiscreteShot(self, gunIndex):
        ...
    def processMultiShot(self, gunIndexes):
        ...
    def _getComponent(self):
        ...
    def _createCoreIntegration(self):
        ...
    def _createEventsDebugger(self):
        ...
    def _lateSubscribe(self, listener):
        ...
    def __lateAppearanceReady(self, handler):
        ...

class GunShootingCoreIntegration(VehicleComponentEventsCoreIntegration, IGunShootingListenerLogic):
    # decorador original: @eventHandler
    def onDiscreteShot(self, gunIndex):
        ...
    # decorador original: @eventHandler
    def onMultiShot(self, gunIndexes):
        ...

class GunShootingEventsDebugger(ClientComponentEventsDebugger):
    IGNORED_EVENTS: Any
    _EVENTS_DEBUG_PREFIX = 'GUN'
