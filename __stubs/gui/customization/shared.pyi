# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/customization/shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple, Counter as Counter, defaultdict as defaultdict
import logging as logging
import typing as typing
import Math as Math
from frameworks.wulf.gui_constants import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.SEASONS_CONSTANTS import SEASONS_CONSTANTS as SEASONS_CONSTANTS
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.money import Currency as Currency, ZERO_MONEY as ZERO_MONEY
from items.components.c11n_components import getVehicleSlotParams as getVehicleSlotParams
from items.components.c11n_constants import CustomizationType as CustomizationType, C11N_MASK_REGION as C11N_MASK_REGION, MAX_USERS_PROJECTION_DECALS as MAX_USERS_PROJECTION_DECALS, ProjectionDecalFormTags as ProjectionDecalFormTags, SeasonType as SeasonType, ApplyArea as ApplyArea, C11N_GUN_APPLY_REGIONS as C11N_GUN_APPLY_REGIONS, UNBOUND_VEH_KEY as UNBOUND_VEH_KEY, EMPTY_ITEM_ID as EMPTY_ITEM_ID, CustomizationTypeNames as CustomizationTypeNames, HIDDEN_CAMOUFLAGE_ID as HIDDEN_CAMOUFLAGE_ID, SLOT_DEFAULT_ALLOWED_MODEL as SLOT_DEFAULT_ALLOWED_MODEL
from shared_utils import CONST_CONTAINER as CONST_CONTAINER, isEmpty as isEmpty
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes, TankPartNames as TankPartNames
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from vehicle_outfit.outfit import Area as Area, SLOT_TYPE_TO_ANCHOR_TYPE_MAP as SLOT_TYPE_TO_ANCHOR_TYPE_MAP, scaffold as scaffold, Outfit as Outfit
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from items import vehicles as vehicles
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
from gui.shared.utils.requesters import InventoryRequester as InventoryRequester
from items.basic_item import BasicItem as BasicItem
from items.vehicles import VehicleDescriptor as VehicleDescriptor
_logger: Any
C11nId: Any
C11N_ITEM_TYPE_MAP: dict
PURCHASE_ITEMS_ORDER: tuple
_EDITED_ITEM_ORDER_SHIFT = 8
EDITABLE_STYLE_IRREMOVABLE_TYPES: tuple
EDITABLE_STYLE_APPLY_TO_ALL_AREAS_TYPES: dict
COMMON_C11N_TYPE_TO_OUTFIT_FIELD_MAP: dict
MODE_TO_C11N_TYPE: dict
REGIONS_BY_AREA_ID: dict
AREA_ID_BY_REGION: dict
QUANTITY_LIMITED_CUSTOMIZATION_TYPES: dict
PROJECTION_DECAL_IMAGE_FORM_TAG: dict
PROJECTION_DECAL_TEXT_FORM_TAG: dict
PROJECTION_DECAL_FORM_TO_UI_ID: dict
SEASON_IDX_TO_TYPE: dict
SEASON_TYPE_TO_NAME: dict
SEASON_TYPE_TO_IDX: dict
SEASONS_ORDER: tuple
CartInfo: Any

class PurchaseItem(object):
    __slots__: tuple
    item: Any
    price: Any
    areaID: Any
    slotType: Any
    regionIdx: Any
    selected: Any
    group: Any
    isFromInventory: Any
    component: Any
    locked: Any
    isEdited: Any
    progressionLevel: Any
    def __init__(self, item, price, areaID, slotType, regionIdx, selected, group, isFromInventory=False, component=None, locked=False, isEdited=False, progressionLevel=-1):
        ...
    def getOrderKey(self):
        ...

class HighlightingMode(CONST_CONTAINER):
    PAINT_REGIONS = 0
    CAMO_REGIONS = 1
    WHOLE_VEHICLE = 2
    REPAINT_REGIONS_MERGED = 3
    CAMO_REGIONS_SKIP_TURRET = 4

class _PurchaseItemRecord(object):
    boughtCount: Any
    totalPrice: Any
    def __init__(self):
        ...

class MoneyForPurchase(object):
    NOT_ENOUGH = 0
    ENOUGH_WITH_EXCHANGE = 1
    ENOUGH = 2

class AdditionalPurchaseGroups(object):
    STYLES_GROUP_ID = -1
    UNASSIGNED_GROUP_ID = -2

class CustomizationTankPartNames(TankPartNames):
    MASK = 'mask'
    ALL: Any

class _QuestGroupWrapper(object):
    item: Any
    def __init__(self, item):
        ...
    def getGroupID(self):
        ...
    def getGroupName(self):
        ...

class _ClassicGroupWrapper(object):
    item: Any
    def __init__(self, item):
        ...
    def getGroupID(self):
        ...
    def getGroupName(self):
        ...

class VehicleC11nFilterHintChecker(object):
    __appLoader: Any
    def check(self, _):
        ...

class NewC11nSectionHintChecker(object):
    def check(self, _):
        ...

class C11nVehicleListHintChecker(object):
    def check(self, _):
        ...

def chooseMode(itemTypeID, modeId, vehicle):
    ...
def getAvailableRegions(areaId, slotType, vehicleDescr=None, vehicleOutfit=None):
    ...
def getCustomizationTankPartName(areaId, regionIdx):
    ...
def createCustomizationBaseRequestCriteria(vehicle, progress, season=None, itemTypeID=None):
    ...
def isOutfitVisuallyEmpty(oufit):
    ...
def fromWorldCoordsToHangarVehicle(worldCoords):
    ...
def fromHangarVehicleToWorldCoords(hangarVehicleCoords):
    ...
def slotsIdsFromAppliedTo(appliedTo, slotType):
    ...
def appliedToFromSlotsIds(slotsIds):
    ...
def getVehiclePartByIdx(vehicleDescriptor, partIdx):
    ...
def getTotalPurchaseInfo(purchaseItems):
    ...
def containsVehicleBound(purchaseItems):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPurchaseGoldForCredits(price, exchangeProvider=None):
    ...
def getPurchaseMoneyStateShortage(price):
    ...
def getPurchaseMoneyState(price):
    ...
def isTransactionValid(moneyState, price):
    ...
def isVehicleCanBeCustomized(vehicle, itemTypeID, itemsFilter=None):
    ...
def getBaseStyleItems():
    ...
def getInheritors(intCD, styleDependencies):
    ...
def getAncestors(intCD, styleDependencies):
    ...
def checkIsFirstProgressionDecalOnVehicle(vehicleCD, newItemsCDs):
    ...
def __isTurretCustomizable(vhicleDescriptor):
    ...
def __getAvailableDecalRegions(areaId, slotType, vehicleDescr):
    ...
def __getAvailableAttachmentRegions(areaId, slot, slotType, vehicleDescr):
    ...
def __getAppliedToRegions(areaId, slotType, vehicleDescr):
    ...
def getGroupHelper(item):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def validateOutfitComponent(vehicleDescr, outfitComponent, service=None):
    ...
def getSingleVehicleForCustomization(customization):
    ...
