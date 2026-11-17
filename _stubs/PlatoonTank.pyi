# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PlatoonTank.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import TYPE_CHECKING as TYPE_CHECKING
from collections import namedtuple as namedtuple
import logging as logging
import math as math
import AccountCommands as AccountCommands
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle as ClientSelectableCameraVehicle
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from gui.hangar_vehicle_appearance import HangarVehicleAppearance as HangarVehicleAppearance
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core.settings_constants import GAME as GAME
from vehicle_systems.tankStructure import ModelStates as ModelStates, ColliderTypes as ColliderTypes
from vehicle_systems import camouflages as camouflages
from items import vehicles as vehicles
from items.components.c11n_constants import SeasonType as SeasonType
from vehicle_outfit.outfit import Outfit as TOutfit
from items.vehicles import VehicleDescrType as VehicleDescrType
_logger: Any
PlatoonTankInfo: Any

class _PlatoonTankAppearance(HangarVehicleAppearance):
    _c11nService: Any
    __tankInfo: Any
    __turretYaw: Any
    __gunPitch: Any
    def __init__(self, spaceId, vEntity, tankInfo, turretYaw=0.0, gunPitch=0.0):
        ...
    def updateTankInfo(self, tankInfo):
        ...
    def _getActiveOutfit(self, vDesc):
        ...
    def _requestClanDBIDForStickers(self, callback):
        ...
    def _getThisVehicleDossierInsigniaRank(self):
        ...
    def _getTurretYaw(self):
        ...
    def _getGunPitch(self):
        ...
    def _reloadColliderType(self, state, collisions):
        ...
    def _getColliderType(self):
        ...

class PlatoonTank(ClientSelectableCameraVehicle):
    _platoonCtrl: Any
    _hangarSpace: Any
    _settingsCore: Any
    __tankInfo: Any
    typeDescriptor: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onMouseClick(self):
        ...
    def setEnable(self, enabled):
        ...
    def recreateVehicle(self, typeDescriptor=None, state=..., callback=None, outfit=None):
        ...
    def getStFrags(self):
        ...
    def debugDisplayTankModel(self, tankTypeName):
        ...
    def _createAppearance(self):
        ...
    def _updatePlatoonTank(self, updatedTankInfoDict):
        ...
    def _onVehicleLoaded(self):
        ...
    def _onVehicleDestroy(self):
        ...
    def _setVisible(self, visible):
        ...
    def __onPlatoonTankRemove(self, slotIndex):
        ...
    @staticmethod
    def __getVehicleDescriptorByIntCD(vehicleIntCD):
        ...
