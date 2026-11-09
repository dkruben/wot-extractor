# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/CrestMovingController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from constants import CREST_MOVING_STATE as CREST_MOVING_STATE
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents
from typing import Any as Any
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents
_logger: _Any

# base nao representavel no stub: typing.NamedTuple(...)
class CrestMovingState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status):
        ...
    def isTransition(self, other):
        ...

class CrestMovingController(VehicleDynamicComponent, IMechanicComponent, IMechanicStatesComponent):
    DEFAULT_MODE_STATE: _Any
    __statesEvents: _Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def statesEvents(self):
        ...
    def getMechanicState(self):
        ...
    def set_state(self, prevState=None):
        ...
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
