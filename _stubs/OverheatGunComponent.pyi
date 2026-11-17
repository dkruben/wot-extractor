# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/OverheatGunComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.gun_mechanics.temperature.overheat_gun import DEFAULT_OVERHEAT_MECHANIC_STATE as DEFAULT_OVERHEAT_MECHANIC_STATE, DEFAULT_OVERHEAT_COMPONENT_PARAMS as DEFAULT_OVERHEAT_COMPONENT_PARAMS, OverheatGunComponentParams as OverheatGunComponentParams, OverheatGunMechanicState as OverheatGunMechanicState, OverheatGunAmmoState as OverheatGunAmmoState
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.gun_mechanics.temperature.overheat_gun import IOverheatGunComponentParams as IOverheatGunComponentParams, IOverheatGunMechanicState as IOverheatGunMechanicState
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# decorador original: @ReprInjector.withParent(...)
class OverheatGunComponent(VehicleDynamicComponent, IGunMechanicComponent, IMechanicStatesComponent):
    __componentParams: Any
    __mechanicState: Any
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
    def set_state(self, _=None):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __updateMechanicState(self):
        ...
