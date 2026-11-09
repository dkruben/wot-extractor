# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/OverheatStacksController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import OVERHEAT_GAIN_STATE as STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from math_utils import clamp as clamp
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesComponent as IMechanicStatesComponent, IMechanicState as IMechanicState
from items.components.shared_components import OverheatStacksParams as OverheatStacksParams
from vehicles.mechanics.mechanic_states import MechanicStatesEvents as MechanicStatesEvents
_LOG_OVERHEAT_STACKS_DEBUG = False

# base nao representavel no stub: typing.NamedTuple(...)
# decorador original: @ReprInjector.simple(...)
class OverheatStacksState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, curLevel, gainState, timeElapsed, delayTimerElapsed, timeNextGain, params):
        ...
    @property
    def progress(self):
        ...
    @property
    def delayTimerProgress(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class OverheatStacksController(VehicleDynamicComponent, IMechanicComponent, IMechanicStatesComponent):
    __params: Any
    __mechanicPrefabSpawner: Any
    __statesEvents: Any
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
    def onDestroy(self):
        ...
    def set_curLevel(self, *_, **__):
        ...
    def set_gainState(self, *_, **__):
        ...
    def set_timeElapsed(self, *_, **__):
        ...
    def set_delayTimerElapsed(self, *_, **__):
        ...
    def set_timeNextGain(self, *_, **__):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
