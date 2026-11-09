# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/BattleFuryController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import BigWorld as BigWorld
import typing as typing
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_states import createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesComponent as IMechanicStatesComponent, IMechanicState as IMechanicState
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents
from typing import Optional as Optional, Dict as Dict, Any as Any

# base nao representavel no stub: typing.NamedTuple(...)
class BattleFuryState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status):
        ...
    @property
    def progress(self):
        ...
    @property
    def duration(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class BattleFuryController(VehicleDynamicComponent, IMechanicComponent, IMechanicStatesComponent):
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
