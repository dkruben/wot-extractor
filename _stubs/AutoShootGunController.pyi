# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AutoShootGunController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from auto_shoot_guns.auto_shoot_guns_common import AutoShootGunState as AutoShootGunState
from constants import UNKNOWN_GUN_INDEX as UNKNOWN_GUN_INDEX
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from items.components.component_constants import DEFAULT_GUN_AUTOSHOOT as DEFAULT_GUN_AUTOSHOOT
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.common import IMechanicComponentLogic as IMechanicComponentLogic
from vehicles.parts.guns.auto_shoot import IAutoShootDispersionState as IAutoShootDispersionState, IAutoShootGunComponentState as IAutoShootGunComponentState, IAutoShootGunComponent as IAutoShootGunComponent, createAutoShootingEvents as createAutoShootingEvents
from items.components.component_constants import AutoShoot as AutoShoot
from vehicles.parts.guns.auto_shoot import IAutoShootingEvents as IAutoShootingEvents

class AutoShootDispersionState(IAutoShootDispersionState):
    __updateTime: Any
    __dispersionFactor: Any
    __shotDispersionPerSec: Any
    __maxShotDispersion: Any
    def __init__(self, updateTime, dispersionFactor, shotDispersionPerSec, maxShotDispersion):
        ...
    @classmethod
    def fromDispersionStatus(cls, status):
        ...
    def getCurrentDispersionFactor(self):
        ...

class AutoShootGunComponentState(IAutoShootGunComponentState):
    __state: Any
    __defaultShotRatePerSecond: Any
    __groupShotInterval: Any
    __shotRatePerSecond: Any
    def __init__(self, state, defaultShotRatePerSecond, groupShotInterval, shotRatePerSecond):
        ...
    @classmethod
    def fromComponentStatus(cls, status, defaultShotRate, params):
        ...
    def isShooting(self):
        ...
    def isContinuousShooting(self):
        ...
    def getDefaultShotRatePerSecond(self):
        ...
    def getGroupShotInterval(self):
        ...
    def getShotRatePerSecond(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class AutoShootGunController(VehicleDynamicComponent, IAutoShootGunComponent, IMechanicComponentLogic):
    DEFAULT_COMPONENT_STATE: Any
    DEFAULT_DISPERSION_STATE: Any
    __componentParams: Any
    __componentState: Any
    __dispersionState: Any
    __shootingEvents: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def shootingEvents(self):
        ...
    def getComponentState(self):
        ...
    def getDispersionState(self):
        ...
    def set_defaultShotRate(self, _=None):
        ...
    def set_stateStatus(self, _=None):
        ...
    def set_dispersionStatus(self, _=None):
        ...
    def onDestroy(self):
        ...
    def onDiscreteShot(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onAppearanceReset(self):
        ...
    def _onAvatarReady(self, player):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __updateComponentState(self):
        ...
    def __updateDispersionState(self):
        ...
