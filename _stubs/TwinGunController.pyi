# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TwinGunController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import DUPLET_GUN_INDEXES_TUPLE as DUPLET_GUN_INDEXES_TUPLE
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicle_appearance.constants import AppearanceState as AppearanceState
from vehicles.components.component_wrappers import ifAppearanceReady as ifAppearanceReady
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.entities import ShotParams as ShotParams
from vehicles.mechanics.common import IMechanicComponentLogic as IMechanicComponentLogic
from vehicles.parts.guns.twin_shoot import ITwinShootGunComponent as ITwinShootGunComponent, createTwinShootingEvents as createTwinShootingEvents
from vehicles.parts.guns.twin_shoot import ITwinShootingEvents as ITwinShootingEvents

class TwinGunAmmoState(DefaultComponentAmmoState):
    __shotsAmount: Any
    def __init__(self, shotsAmount):
        ...
    def getShotsAmount(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class TwinGunController(VehicleDynamicComponent, ITwinShootGunComponent, IMechanicComponentLogic):
    APPEARANCE_READY_STATE = AppearanceState.COMPONENTS_CREATED
    __afterShotDelay: Any
    __shootingEvents: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def shootingEvents(self):
        ...
    def isDoubleBarrelMode(self):
        ...
    def getActiveGunIndexes(self):
        ...
    def getAfterShotDelay(self):
        ...
    def getComponentParams(self):
        ...
    def getNextGunIndexes(self):
        ...
    # decorador original: @ifAppearanceReady
    def set_activeGunIndexes(self, _=None):
        ...
    # decorador original: @ifAppearanceReady
    def set_nextGunIndexes(self, _=None):
        ...
    def onDestroy(self):
        ...
    def onDiscreteShot(self, gunIndex):
        ...
    def onDoubleShot(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    # decorador original: @eventHandler
    def onCollectShotParams(self, shotParamsList):
        ...
    def _onAppearanceReady(self):
        ...
    def _onAppearanceReset(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __updateActiveGunIndexes(self):
        ...
    def __updateNextGunIndexes(self):
        ...
