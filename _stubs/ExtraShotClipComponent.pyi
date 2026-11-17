# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ExtraShotClipComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ExtraShotClipStates as ExtraShotClipStates
from events_handler import eventHandler as eventHandler
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState, AmmoShootPossibility as AmmoShootPossibility
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent

class ExtraShotAmmoState(DefaultComponentAmmoState):
    __reloadState: Any
    def __init__(self, reloadState):
        ...
    @property
    def extraReloadState(self):
        ...
    def isReloadAfterShot(self, timeLeft, baseTime):
        ...
    def getShootPossibility(self, currentShells):
        ...

# decorador original: @ReprInjector.withParent(...)
class ExtraShotClipComponent(VehicleDynamicComponent, IGunMechanicComponent):
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
