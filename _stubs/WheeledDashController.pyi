# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/WheeledDashController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from constants import PHASED_MECHANIC_STATE as MECHANIC_STATE
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.generic_mechanics.wheeled_dash import createWheeledDashMiscEvents as createWheeledDashMiscEvents
from vehicles.mechanics.mechanic_commands import createMechanicCommandsEvents as createMechanicCommandsEvents, IMechanicCommandsComponent as IMechanicCommandsComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_inputs import createMechanicSingleInput as createMechanicSingleInput
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents
from vehicles.mechanics.generic_mechanics.wheeled_dash import IWheeledDashEvents as IWheeledDashEvents

# base nao representavel no stub: namedtuple(...)
class WheeledDashState(IMechanicState):
    @classmethod
    def fromPublicStatus(cls, publicStatus, params):
        ...
    @classmethod
    def fromComponentStatus(cls, status):
        ...
    @property
    def progress(self):
        ...
    @property
    def timeLeft(self):
        ...
    def isTransition(self, other):
        ...

class WheeledDashController(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    _INPUT_ACTION_NAME = 'ABILITY_1_INPUT_ACTION'
    _INPUT_PROFILE_NAME = 'ABILITY_1_INPUT_PROFILE'
    DEFAULT_MODE_STATE: Any
    __commandsEvents: Any
    __statesEvents: Any
    __impulseEvents: Any
    __prefabSpawner: Any
    __params: Any
    __singleInput: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def commandsEvents(self):
        ...
    @property
    def statesEvents(self):
        ...
    @property
    def impulseEvents(self):
        ...
    def getMechanicState(self):
        ...
    def set_status(self, _):
        ...
    def set_publicStatus(self, _):
        ...
    def onImpulseStarted(self, direction):
        ...
    def onDestroy(self):
        ...
    def tryActivate(self):
        ...
    def _onAvatarReady(self, player):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
