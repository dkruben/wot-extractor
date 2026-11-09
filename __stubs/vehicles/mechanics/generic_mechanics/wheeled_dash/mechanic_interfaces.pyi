# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/wheeled_dash/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.containers import IClientEventsContainer as IClientEventsContainer
from constants import WheeledDashDirection as WheeledDashDirection

class IWheeledDashEventsLogic(object):
    onImpulseStarted = None

class IWheeledDashListenerLogic(object):
    def onImpulseStarted(self, direction):
        ...

class IWheeledDashEvents(IClientEventsContainer, IWheeledDashEventsLogic):
    ...
