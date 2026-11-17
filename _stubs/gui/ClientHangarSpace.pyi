# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ClientHangarSpace.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import itertools as itertools
from future.utils import viewkeys as viewkeys
from logging import getLogger as getLogger
import BigWorld as BigWorld
import Math as Math
import MusicControllerWWISE as MusicControllerWWISE
import ResMgr as ResMgr
import constants as constants
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.hangar_config import HangarConfig as HangarConfig
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IIGRController as IIGRController, IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from skeletons.gui.turret_gun_angles import ITurretAndGunAngles as ITurretAndGunAngles
from skeletons.map_activities import IMapActivities as IMapActivities
from visual_script.multi_plan_provider import makeMultiPlanProvider as makeMultiPlanProvider, CallableProviderType as CallableProviderType
from visual_script.misc import ASPECT as ASPECT, VisualScriptTag as VisualScriptTag, readVisualScriptPlans as readVisualScriptPlans
from SpaceVisibilityFlags import SpaceVisibilityFlagsFactory as SpaceVisibilityFlagsFactory
from constants import HANGAR_VISIBILITY_TAGS as HANGAR_VISIBILITY_TAGS
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
_DEFAULT_SPACES_PATH = 'spaces'
SERVER_CMD_CHANGE_HANGAR = 'cmd_change_hangar'
SERVER_CMD_CHANGE_HANGAR_PREM = 'cmd_change_hangar_prem'
SERVER_CMD_CHANGE_HANGAR_ALT = 'cmd_change_hangar_alt'
_CUSTOMIZATION_HANGAR_SETTINGS_SEC = 'customizationHangarSettings'
_LOGIN_BLACK_BG_IMG = 'gui/maps/login/blackBg.png'
_SECONDARY_HANGAR_SETTINGS_SEC = 'secondaryHangarSettings'
FULL_VISIBILITY_TAG_IDS: Any
_CFG: Any
_HANGAR_CFGS: Any
_EVENT_HANGAR_PATHS: dict
_IGR_HANGAR_PATH_KEY: Any
_logger: Any
g_clientHangarSpaceOverride: Any

class ClientHangarSpace(object):
    igrCtrl: Any
    settingsCore: Any
    itemsFactory: Any
    mapActivities: Any
    turretAndGunAngles: Any
    epicController: Any
    __space: Any
    __waitCallback: Any
    __loadingStatus: Any
    __spaceMappingId: Any
    __onLoadedCallback: Any
    __vEntityId: Any
    __selectedEmblemInfo: Any
    __showMarksOnGun: Any
    __prevDirection: Any
    __onVehicleLoadedCallback: Any
    __spacePath: Any
    __spaceVisibilityMask: Any
    __geometryID: Any
    _vsePlans: Any
    def __init__(self, onVehicleLoadedCallback):
        ...
    def create(self, isPremium, onSpaceLoadedCallback=None, environment=''):
        ...
    def recreateVehicle(self, vDesc, vState, onVehicleLoadedCallback=None, outfit=None):
        ...
    def removeVehicle(self):
        ...
    def moveVehicleTo(self, position):
        ...
    def setVehicleSelectable(self, flag):
        ...
    def updateVehicleCustomization(self, outfit):
        ...
    def updateVehicleDescriptor(self, descr):
        ...
    def getCentralPointForArea(self, areaId):
        ...
    def destroy(self):
        ...
    def spaceLoaded(self):
        ...
    def spaceLoading(self):
        ...
    def updateAnchorsParams(self, *args):
        ...
    def getAnchorParams(self, slotId, areaId, regionId):
        ...
    def getVehicleEntity(self):
        ...
    @property
    def vehicleEntityId(self):
        ...
    def __destroy(self):
        ...
    def __waitLoadingSpace(self):
        ...
    def __closeOptimizedRegion(self):
        ...
    def getSpace(self):
        ...
    def getSpaceID(self):
        ...
    @property
    def spacePath(self):
        ...
    @property
    def visibilityMask(self):
        ...

class _ClientHangarSpacePathOverride(object):
    hangarSpace: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def setPremium(self, isPremium):
        ...
    def setPath(self, path, visibilityMask=None, isPremium=None, isReload=True, event=None):
        ...
    def __onDisconnected(self):
        ...

def getDefaultHangarPath(isPremium):
    ...
def _getHangarPath(isPremium, isPremIGR):
    ...
def _getHangarKey(path):
    ...
def _getHangarType(isPremium):
    ...
def getHangarFullVisibilityMask(spacePath):
    ...
def _getHangarVisibilityMask(isPremium, spacePath):
    ...
def hangarCFG():
    ...
def customizationHangarCFG():
    ...
def secondaryHangarCFG():
    ...
def _readHangarSettings():
    ...
def _loadVisualScript(cfg, section):
    ...
def _getSpaceNameFromPath(path):
    ...
def _createMatrix(scale, angles, pos):
    ...
