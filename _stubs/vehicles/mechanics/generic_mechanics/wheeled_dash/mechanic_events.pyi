# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/wheeled_dash/mechanic_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer, ClientEventsContainerDebugger as ClientEventsContainerDebugger
from vehicles.mechanics.generic_mechanics.wheeled_dash.mechanic_interfaces import IWheeledDashEventsLogic as IWheeledDashEventsLogic

class WheeledDashMiscEvents(ClientEventsContainer, IWheeledDashEventsLogic):
    onImpulseStarted: Any
    def __init__(self):
        ...
    def _createEventsDebugger(self):
        ...

class WheeledDashMiscEventsDebugger(ClientEventsContainerDebugger):
    IGNORED_EVENTS: Any
    _EVENTS_DEBUG_PREFIX = 'WHEELED_DASH_MISC'
