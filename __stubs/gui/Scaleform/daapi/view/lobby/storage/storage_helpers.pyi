# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/storage_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import random as random
from itertools import chain as chain
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import nations as nations
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import LAST_STORAGE_VISITED_TIMESTAMP as LAST_STORAGE_VISITED_TIMESTAMP
from gui import g_htmlTemplates as g_htmlTemplates
from gui.Scaleform import MENU as MENU
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES as BUTTON_LINKAGES
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.MENU import MENU as _MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.RES_SHOP import RES_SHOP as RES_SHOP
from gui.Scaleform.locale.STORAGE import STORAGE as STORAGE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showStylePreview as showStylePreview, showStyleProgressionPreview as showStyleProgressionPreview
from gui.shared.formatters import getItemPricesVO as getItemPricesVO, getMoneyVO as getMoneyVO, icons as icons, text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, KPI as KPI, getKpiValueString as getKpiValueString
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, getTypeUserName as getTypeUserName, getVehicleStateIcon as getVehicleStateIcon, getShopVehicleIconPath as getShopVehicleIconPath
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.items_parameters import params_helper as params_helper
from gui.shared.money import Currency as Currency
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency, i18n as i18n, int2roman as int2roman, time_utils as time_utils
from helpers.i18n import makeString as _ms
from helpers.time_utils import getCurrentTimestamp as getCurrentTimestamp
from items import vehicles as vehicles
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from items.vehicles import makeVehicleTypeCompDescrByName as makeVehicleTypeCompDescrByName
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from typing import List as List, Optional as Optional
_logger: Any
_MAX_COMPATIBLE_VEHS_COUNT = 5
_MAX_COMPATIBLE_GUNS_COUNT = 2
_HANDLERS_MAP: dict
OPT_DEVICE_CATEGORIES_ORDER: dict
CATEGORIES_COUNT: Any
_CUSTOMIZATION_VEHICLE_CRITERIA: Any

class OptDeviceBonusesDescriptionBuilder(object):
    KPI_VALUE_TEMPLATE = '{{colorTagOpen}}{}{{colorTagClose}}'
    KPI_HTML_TEMPLATE: Any
    def getDescription(self, item):
        ...
    def getDescriptionByKpiStrings(self, item):
        ...
    def getEffectDescription(self, item):
        ...
    def __createEffectString(self, item):
        ...
    def __createKpiString(self, kpi):
        ...
    def __kpiFormat(self, kpi, value):
        ...

def getTopVehicleByNation(nationName):
    ...
def _getContextMenuHandlerID(item):
    ...
def getStorageItemDescr(item):
    ...
def createStorageDefVO(itemID, title, description, count, price, image, imageAlt, itemType='', nationFlagIcon='', enabled=True, available=True, contextMenuId='', additionalInfo='', actionButtonIcon=None, actionButtonTooltip=None, upgradable=False, upgradeButtonIcon=None, upgradeButtonTooltip='', extraParams=..., specializations=..., sellBtnLabel=None):
    ...
def getStorageVehicleVo(vehicle):
    ...
def getVehicleName(vehicle):
    ...
def _getVehicleDescription(vehicle):
    ...
def _getVehicleInfo(vehicle):
    ...
def _calculateVehicleMaxAdditionalPrice(vehicle):
    ...
def getStorageItemName(item):
    ...
def getStorageShellsCriteria(itemsCache, invVehicles, compatible):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getStorageShellsData(invVehicles, isCompatible, sortKey=None, itemsCache=None):
    ...
def _generateDescr(item, label, moreLabel, paramsNames, maxItemsCount):
    ...
def getStorageItemIcon(item, size=...):
    ...
def dummyFormatter(label, iconSource=..., btnLabel='', btnTooltip='', smallIcon=False):
    ...
def enoughCreditsForRestore(restoreCreditsPrice, itemsCache):
    ...
def getVehicleRestoreInfo(vehicle):
    ...
def _getActionBtnTooltipForOptDevice(item):
    ...
def getItemVo(item):
    ...
def isStorageSessionTimeout():
    ...
def isCustomizationAvailableForSell(item, vehicleCD=None):
    ...
def getAvailableForSellCustomizationCount(item, vehicleCD=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehicleCDForStyle(item, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def customizationPreview(itemCD, itemsCache=None, vehicleCD=None):
    ...
def getItemExtraParams(item):
    ...
def getCategoriesIcons(device):
    ...
