# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ChargeableBurstComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from events_handler import eventHandler as eventHandler
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesEvents as IMechanicStatesEvents

class ChargeableBurstAmmoState(DefaultComponentAmmoState):
    __isBurstActive: Any
    __burstCount: Any
    __shots: Any
    def __init__(self, isBurstActive, shots, burstCount):
        ...
    @property
    def isBurstActive(self):
        ...
    @property
    def burstCount(self):
        ...
    @property
    def shots(self):
        ...

# base nao representavel no stub: namedtuple(...)
# decorador original: @ReprInjector.simple(...)
class ChargeableBurstModeState(IMechanicState):
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChargeableBurstComponent(VehicleDynamicComponent, IGunMechanicComponent, IMechanicStatesComponent):
    __penetrationCount: Any
    __burstCount: Any
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
    def set_charges(self, prev):
        ...
    def set_shots(self, prev):
        ...
    def set_isBurstActive(self, prev):
        ...
    def onDestroy(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
