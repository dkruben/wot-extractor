# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/components/component_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_containers.common.containers import ClientEventsContainerCoreIntegration as ClientEventsContainerCoreIntegration
from events_containers.common.containers.interfaces import IClientEventsContainer as IClientEventsContainer

class VehicleComponentEventsCoreIntegration(ClientEventsContainerCoreIntegration):
    _spaceID: Any
    _vehicleID: Any
    _slotName: Any
    def __init__(self, events, component):
        ...
    def _attachToEventsContainer(self, events):
        ...
