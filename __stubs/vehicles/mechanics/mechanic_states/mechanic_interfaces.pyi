# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_states/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from events_containers.common.containers import IClientEventsContainer as IClientEventsContainer, IClientEventsContainerListener as IClientEventsContainerListener

class IMechanicState(object):
    def isTransition(self, other):
        ...

class IMechanicStatesComponent(object):
    @property
    def statesEvents(self):
        ...
    def getMechanicState(self):
        ...

class IMechanicStatesEventsLogic(object):
    onStatePrepared = None
    onStateObservation = None
    onStateTransition = None
    onStateTick = None
    def processStatePrepared(self):
        ...
    def updateMechanicState(self, state):
        ...

class IMechanicStatesEvents(IClientEventsContainer, IMechanicStatesEventsLogic):
    ...

class IMechanicStatesListenerLogic(object):
    def onStatePrepared(self, state):
        ...
    def onStateObservation(self, state):
        ...
    def onStateTransition(self, prevState, newState):
        ...
    def onStateTick(self, state):
        ...

class IMechanicStatesListener(IClientEventsContainerListener, IMechanicStatesListenerLogic):
    ...
