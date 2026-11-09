# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/events_containers/components/life_cycle/interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.containers import IClientEventsContainer as IClientEventsContainer, IClientEventsContainerListener as IClientEventsContainerListener

class ILifeCycleComponent(object):
    @property
    def lifeCycleEvents(self):
        ...
    def getComponentParams(self):
        ...

class IComponentLifeCycleEventsLogic(object):
    onComponentAvatarReady = None
    onComponentParamsCollected = None
    onComponentAppearanceReady = None
    onComponentAppearanceReset = None
    onComponentDestroyed = None
    def processComponentAvatarReady(self):
        ...
    def processAppearanceReady(self):
        ...
    def processAppearanceReset(self):
        ...
    def processParamsCollected(self):
        ...

class IComponentLifeCycleEvents(IClientEventsContainer, IComponentLifeCycleEventsLogic):
    ...

class IComponentLifeCycleListenerLogic(object):
    def onComponentAvatarReady(self, component):
        ...
    def onComponentParamsCollected(self, params):
        ...
    def onComponentAppearanceReady(self, component):
        ...
    def onComponentAppearanceReset(self, component):
        ...
    def onComponentDestroyed(self, component):
        ...

class IComponentLifeCycleListener(IClientEventsContainerListener, IComponentLifeCycleListenerLogic):
    ...
