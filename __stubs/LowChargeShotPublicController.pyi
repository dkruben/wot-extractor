# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/LowChargeShotPublicController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.component_interfaces import IVehicleGunSlotComponent as IVehicleGunSlotComponent
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.gun_mechanics.low_charge_shot.public import LowChargeShotPublicMechanicState as LowChargeShotPublicMechanicState, DEFAULT_MECHANIC_STATE as DEFAULT_MECHANIC_STATE, createLowChargeShotPublicStatesEvents as createLowChargeShotPublicStatesEvents
from items.components.shared_components import LowChargeShotParams as LowChargeShotParams

# decorador original: @ReprInjector.withParent(...)
class LowChargeShotPublicController(VehicleDynamicComponent, IVehicleGunSlotComponent, IMechanicStatesComponent):
    __mechanicState: Any
    __params: Any
    __statesEvents: Any
    def __init__(self):
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
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __updateMechanicState(self):
        ...
