# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/HeroTank.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import random as random
from typing import TYPE_CHECKING as TYPE_CHECKING
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle as ClientSelectableCameraVehicle
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.hangar_vehicle_appearance import HangarVehicleAppearance as HangarVehicleAppearance
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from items.components.c11n_constants import SeasonType as SeasonType
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IHeroTankController as IHeroTankController, ILimitedUIController as ILimitedUIController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from vehicle_systems.tankStructure import ModelStates as ModelStates
from items import vehicles as vehicles
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from vehicle_outfit.outfit import Outfit as TOutfit
from items.vehicles import VehicleDescrType as VehicleDescrType

class _HeroTankAppearance(HangarVehicleAppearance):
    _heroTankCtrl: Any
    _c11nService: Any
    __season: Any
    __turretYaw: Any
    __gunPitch: Any
    __typeDescriptor: Any
    def __init__(self, spaceId, vEntity, turretYaw=0.0, gunPitch=0.0):
        ...
    def _getActiveOutfit(self, vDesc):
        ...
    def _getTurretYaw(self):
        ...
    def _getGunPitch(self):
        ...

class HeroTank(ClientSelectableCameraVehicle):
    _heroTankCtrl: Any
    _hangarSpace: Any
    __c11nService: Any
    __limitedUIController: Any
    __heroTankCD: Any
    typeDescriptor: Any
    def __init__(self, name='HeroTank'):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onMouseClick(self):
        ...
    def removeModelFromScene(self):
        ...
    def recreateVehicle(self, typeDescriptor=None, state=..., callback=None, outfit=None):
        ...
    def _createAppearance(self):
        ...
    def _updateHeroTank(self):
        ...
    def _updateInteractive(self, interactive):
        ...
    def _onVehicleLoaded(self):
        ...
    def _onVehicleDestroy(self):
        ...
    def __updateHeroTankVisibility(self, *_):
        ...
    @staticmethod
    def __getVehicleDescriptorByIntCD(vehicleIntCD):
        ...
    @staticmethod
    def __isInPreview():
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def debugReloadHero(heroName, heroTankCtrl=None):
    ...
