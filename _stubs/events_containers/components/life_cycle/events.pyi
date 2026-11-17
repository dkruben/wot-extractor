# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/events_containers/components/life_cycle/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer
from events_containers.components.common import ClientComponentEventsDebugger as ClientComponentEventsDebugger
from events_containers.components.life_cycle.interfaces import IComponentLifeCycleEventsLogic as IComponentLifeCycleEventsLogic
from events_containers.components.life_cycle.interfaces import ILifeCycleComponent as ILifeCycleComponent, IComponentLifeCycleListener as IComponentLifeCycleListener

class ComponentLifeCycleEvents(ClientEventsContainer, IComponentLifeCycleEventsLogic):
    __componentRef: Any
    __isParamsCollected: Any
    __isAppearanceReady: Any
    onComponentAvatarReady: Any
    onComponentParamsCollected: Any
    onComponentAppearanceReady: Any
    onComponentAppearanceReset: Any
    onComponentDestroyed: Any
    def __init__(self, component):
        ...
    def destroy(self):
        ...
    def lateSubscribe(self, listener):
        ...
    def processComponentAvatarReady(self):
        ...
    def processAppearanceReady(self):
        ...
    def processAppearanceReset(self):
        ...
    def processParamsCollected(self):
        ...
    def _createEventsDebugger(self):
        ...
    def _getComponent(self):
        ...
    def __lateAppearanceReady(self, handler):
        ...
    def __lateParamsCollected(self, handler):
        ...

class ComponentLifeCycleEventsDebugger(ClientComponentEventsDebugger):
    _EVENTS_DEBUG_PREFIX = 'COMPONENT_LC'
    def onComponentDestroyed(self, _):
        ...
