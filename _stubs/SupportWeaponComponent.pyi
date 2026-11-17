# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SupportWeaponComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from constants import SECONDARY_GUN_STATE as SECONDARY_GUN_STATE, UNKNOWN_GUN_INSTALLATION_INDEX as UNKNOWN_GUN_INSTALLATION_INDEX
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import createMechanicCommandsEvents as createMechanicCommandsEvents, IMechanicCommandsComponent as IMechanicCommandsComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# base nao representavel no stub: namedtuple(...)
class SupportWeaponState(IMechanicState):
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

# decorador original: @ReprInjector.withParent(...)
class SupportWeaponComponent(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    DEFAULT_WEAPON_STATE: Any
    __mechanicPrefabSpawner: Any
    __commandsEvents: Any
    __statesEvents: Any
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
    def getMechanicState(self):
        ...
    def getSupportInstallationIndex(self):
        ...
    def set_status(self, _):
        ...
    def onDestroy(self):
        ...
    def tryActivate(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
