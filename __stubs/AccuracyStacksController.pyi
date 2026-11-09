# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AccuracyStacksController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import BigWorld as BigWorld
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents
from typing import Any as Any, Optional as Optional
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# base nao representavel no stub: typing.NamedTuple(...)
# decorador original: @ReprInjector.simple(...)
class AccuracyStacksState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status, stackDuration, speedThreshold):
        ...
    @property
    def progress(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class AccuracyStacksController(VehicleDynamicComponent, IMechanicComponent, IMechanicStatesComponent):
    __stackDuration: _Any
    __speedThreshold: _Any
    __mechanicPrefabSpawner: _Any
    __statesEvents: _Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def statesEvents(self):
        ...
    def getComponentParams(self):
        ...
    def getMechanicState(self):
        ...
    def set_abilityState(self, *_):
        ...
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
