# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PropellantGunController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.component_wrappers import ifPlayerVehicle as ifPlayerVehicle
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.gun_mechanics.propellant_gun import DEFAULT_PROPELLANT_GUN_PARAMS as DEFAULT_PROPELLANT_GUN_PARAMS, DEFAULT_PROPELLANT_GUN_MECHANIC_STATE as DEFAULT_PROPELLANT_GUN_MECHANIC_STATE, PropellantGunMechanicState as PropellantGunMechanicState, PropellantGunComponentParams as PropellantGunComponentParams, createPropellantStatesEvents as createPropellantStatesEvents
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents
from vehicles.mechanics.gun_mechanics.propellant_gun import IPropellantGunComponentParams as IPropellantGunComponentParams, IPropellantGunMechanicState as IPropellantGunMechanicState

# decorador original: @ReprInjector.withParent(...)
class PropellantGunController(VehicleDynamicComponent, IGunMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    __componentParams: Any
    __mechanicState: Any
    __mechanicPrefabSpawner: Any
    __statesEvents: Any
    __commandsEvents: Any
    __isForbiddenShell: Any
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
    def getComponentParams(self):
        ...
    def getMechanicState(self):
        ...
    def set_status(self, _=None):
        ...
    def onDestroy(self):
        ...
    # decorador original: @eventHandler
    # decorador original: @ifPlayerVehicle
    def onCurrentShellChanged(self, _, intCD):
        ...
    def tryActivate(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __updateMechanicState(self):
        ...
