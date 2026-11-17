# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TemperatureGunController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.gun_mechanics.temperature.common import createTemperatureStatesEvents as createTemperatureStatesEvents
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import DEFAULT_TEMPERATURE_COMPONENT_PARAMS as DEFAULT_TEMPERATURE_COMPONENT_PARAMS, DEFAULT_TEMPERATURE_MECHANIC_STATE as DEFAULT_TEMPERATURE_MECHANIC_STATE, TemperatureGunComponentParams as TemperatureGunComponentParams, TemperatureGunMechanicState as TemperatureGunMechanicState, TemperatureGunAmmoState as TemperatureGunAmmoState
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunComponentParams as ITemperatureGunComponentParams, ITemperatureGunMechanicState as ITemperatureGunMechanicState
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# decorador original: @ReprInjector.withParent(...)
class TemperatureGunController(VehicleDynamicComponent, IGunMechanicComponent, IMechanicStatesComponent):
    __componentParams: Any
    __mechanicState: Any
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
    def set_stateStatus(self, _=None):
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
