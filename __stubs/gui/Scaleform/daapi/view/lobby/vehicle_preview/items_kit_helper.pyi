# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/items_kit_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import viewvalues as viewvalues
from sys import maxsize as maxsize
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from gui.Scaleform.genConsts.SLOT_HIGHLIGHT_TYPES import SLOT_HIGHLIGHT_TYPES as SLOT_HIGHLIGHT_TYPES
from gui.Scaleform.locale.COMMON import COMMON as COMMON
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_SHOP import RES_SHOP as RES_SHOP
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW as VEHICLE_PREVIEW
from gui.shared.gui_items.Tankman import CrewTypes as CrewTypes
from gui.shared.money import Currency as Currency, Money as Money, MONEY_ZERO_GOLD as MONEY_ZERO_GOLD
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.impl import backport as backport
from gui.impl.gen import R as R
from items import makeIntCompactDescrByID as makeCD
from items.components.c11n_constants import CustomizationType as CustomizationType
from items.vehicles import MAX_OPTIONAL_DEVICES_SLOTS as MAX_OPTIONAL_DEVICES_SLOTS, NUM_SHELLS_SLOTS as NUM_SHELLS_SLOTS
from py2to3.moves.collections.abc import Container as Container
from shared_utils import findFirst as findFirst, first as first, CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from web.web_client_api.common import ItemPackType as ItemPackType, ItemPackTypeGroup as ItemPackTypeGroup, ItemPackEntry as ItemPackEntry
from gui.shared.gui_items import vehicle_adjusters as vehicle_adjusters
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from skeletons.gui.shared import IItemsCache as IItemsCache
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.formatters import text_styles as text_styles, icons as icons
OFFER_CHANGED_EVENT = 'offerChanged'
_UNLIMITED_ITEMS_COUNT = -1
_EXCLUDE_ITEMS: Any
_ANY_ITEM_TYPE: Any
_FRONTLINE_GIFTS: Any
_NATIVE_ITEM_TYPE: Any
_CUSTOMIZATION_ITEM_TYPE: Any
_CUSTOMIZATION_TYPES_MAP: dict
_BOOSTER_ITEM_TYPE: Any
_UNCOUNTABLE_ITEM_TYPE: set
_PACK_ITEMS_SORT_ORDER: Any
_TOOLTIP_TYPE: dict
_ICONS: dict
_NOT_FOUND_ICONS: dict
_PREM_ICONS: dict
_BOX_ITEM = None
BOX_TYPE = 'box'
_OPEN_QUOTES: Any
_DOUBLE_OPEN_QUOTES: Any
_CLOSE_QUOTES: Any
_DOUBLE_CLOSE_QUOTES: Any
StyleInstallInfo: Any

class ItemSortRule(CONST_CONTAINER):
    REGULAR = 'regular'
    FRONTLINE = 'frontline'

class BoosterGUIItemProxy(object):
    __booster: Any
    def __init__(self, booster):
        ...
    @property
    def intCD(self):
        ...
    @property
    def icon(self):
        ...
    @property
    def userName(self):
        ...
    @property
    def itemTypeID(self):
        ...
    @property
    def itemTypeName(self):
        ...
    @property
    def mayInstall(self):
        ...
    @staticmethod
    def getHighlightType():
        ...

class _NodeContainer(object):
    itemsCache: Any
    goodiesCache: Any
    _maxChildCount: Any
    _nextNode: Any
    _children: Any
    _itemTypeOrGroup: Any
    def __init__(self, childCount, itemTypeOrGroup, nextNode=None):
        ...
    def getVO(self):
        ...
    def getNextNode(self):
        ...
    def destroy(self):
        ...
    def addItem(self, item, vehicle, vehicleGroupId):
        ...
    @staticmethod
    def wrapVO(items):
        ...
    def _install(self, item, vehicle, slotIdx):
        ...
    def _addItemToNextNode(self, item, vehicle, vehicleGroupId):
        ...
    def _sortChildren(self):
        ...

class _OptDeviceNodeContainer(_NodeContainer):
    def __init__(self, nextNode=None):
        ...
    def _install(self, item, vehicle, slotIdx):
        ...

class _ShellNodeContainer(_NodeContainer):
    __vehicle: Any
    def __init__(self, nextNode=None):
        ...
    def _install(self, item, vehicle, slotIdx):
        ...
    def _sortChildren(self):
        ...

class _EquipmentNodeContainer(_NodeContainer):
    def __init__(self, nextNode=None):
        ...
    def _install(self, item, vehicle, slotIdx):
        ...

class _BuiltinEquipmentNodeContainer(_NodeContainer):
    def __init__(self, nextNode=None):
        ...
    def _install(self, item, vehicle, slotIdx):
        ...

class _PriorityNodeContainer(_NodeContainer):
    _children: Any
    def __init__(self, childCount, nextNode=None):
        ...
    def addItem(self, item, vehicle, vehicleGroupId):
        ...
    def getVO(self):
        ...

class _FrontlineNodeContainer(_NodeContainer):
    def __init__(self, nextNode=None):
        ...
    def addItem(self, item, vehicle, vehicleGroupId):
        ...
    @staticmethod
    def wrapVO(items):
        ...

class _GiftNodeContainer(_NodeContainer):
    _children: Any
    def __init__(self, nextNode=None):
        ...
    def addItem(self, item, vehicle, vehicleGroupId):
        ...
    @staticmethod
    def wrapVO(items):
        ...
    def _sortChildren(self):
        ...

class _CustomCrewSkillsNodeContainer(_NodeContainer):
    CREW_COUNT = 1
    def __init__(self, nextNode=None):
        ...
    def getVO(self):
        ...
    def parseCrewSkills(self, item):
        ...
    def _install(self, item, vehicle, slotIdx):
        ...

def __getPremiumPlusIcon(days):
    ...
def __getPremiumPlusIconExists(days):
    ...
def getCompensateItemsCount(rawItem, itemsCache):
    ...
def _getSuitableShellsForVehicle(vehicle):
    ...
def getCDFromId(itemType, itemId):
    ...
def lookupItem(rawItem, itemsCache, goodiesCache):
    ...
def getItemIcon(rawItem, item):
    ...
def getItemTitle(rawItem, item, forBox=False, additionalInfo=False):
    ...
def getItemDescription(rawItem, item):
    ...
def getTooltipText(item):
    ...
def getItemTooltipType(rawItem, item):
    ...
def showItemTooltip(toolTipMgr, rawItem, item):
    ...
def showAwardsTooltip(toolTipMgr, itemType, data):
    ...
def collapseItemsPack(items):
    ...
def _getItemKey(item):
    ...
def _createItemVO(rawItem, itemsCache, goodiesCache, slotIndex, rawTooltipData=None):
    ...
def _getBoxTooltipVO(rawItems, itemsCache, goodiesCache):
    ...
def _checkItemType(a, b):
    ...
def getDataOneVehicle(itemsPack, vehicle, vehicleGroupId):
    ...
def getCouponDiscountForItemPack(itemsPack, price=...):
    ...
def getCouponBonusesForItemPack(itemsPack):
    ...
def getDataMultiVehicles(itemsPack, vehicle):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def addCompensationInfo(itemsVOs, itemsPack, itemsCache=None):
    ...
def getActiveOffer(offers):
    ...
def addBuiltInEquipment(packItems, itemsCache, vehicleCD):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def mayObtainWithMoneyExchange(itemPrice, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def mayObtainForMoney(itemPrice, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def canInstallStyle(styleId, service=None):
    ...
def _sortItemsByOrder(items, rule=None):
    ...
def _packDataOneVehicle(root, itemsPack, vehicle, vehicleGroupId):
    ...
def _packDataMultiVehicles(itemsPack, vehicle):
    ...
def __getItemsSortRule(itemsPack):
    ...
def __getDefaultPackRule():
    ...
def __getFrontlinePackRule():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def __findVehicle(style, itemsCache=None):
    ...
