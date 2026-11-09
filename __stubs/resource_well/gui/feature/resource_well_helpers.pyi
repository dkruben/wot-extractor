# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/feature/resource_well_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import iteritems as iteritems
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ResourceWell as ResourceWell
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency, time_utils as time_utils
from resource_well.gui.feature.constants import CHANNEL_NAME_PREFIX as CHANNEL_NAME_PREFIX, PurchaseMode as PurchaseMode
from resource_well.gui.impl.gen.view_models.views.lobby.enums import EventMode as EventMode
from resource_well.gui.impl.gen.view_models.views.lobby.vehicle_counter_model import VehicleCounterModel as VehicleCounterModel
from resource_well_common.feature_constants import RESOURCE_WELL_FORBIDDEN_TOKEN as RESOURCE_WELL_FORBIDDEN_TOKEN
from shared_utils import findFirst as findFirst
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional, List as List
from gui.shared.gui_items.customization.c11n_items import Style as Style
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from resource_well.helpers.server_settings import RewardConfig as RewardConfig
_logger: Any
_PurchaseModeToEventModeMap: dict

def convertPurchaseToEventMode(mode):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isEventEndingsSoon(resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getForbiddenAccountToken(resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getSerialNumber(rewardID, resourceWell=None, itemsCache=...):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getNextSerialRewardID(rewardID, resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRewardStyle(rewardID, resourceWell=None, c11nService=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hasRequiredStyle(rewardID, rewardConfig=None, resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getNumberChannelName(rewardID, resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillVehicleCounter(rewardID, vehicleCounterModel, resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRewardVehiclesInInventory(resourceWell=None):
    ...
def getNotificationSettings():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isNotificationShown(sectionName, resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setIsNotificationShown(sectionName, resourceWell=None):
    ...
def isStartNotificationShown():
    ...
def isFinishNotificationShown():
    ...
def setStartNotificationShown():
    ...
def setFinishNotificationShown():
    ...
def getSettings(settingName, defaultValue=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def setBannerSettings(settingName, resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isBannerSettingSet(settingName, resourceWell=None):
    ...
