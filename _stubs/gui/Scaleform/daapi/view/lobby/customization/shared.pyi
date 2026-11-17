# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import struct as struct
from collections import namedtuple as namedtuple, Counter as Counter
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import Math as Math
import nations as nations
from AccountCommands import isCodeValid as isCodeValid
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import GUI_NATIONS_ORDER_INDICES as GUI_NATIONS_ORDER_INDICES
from gui.Scaleform import getNationsFilterAssetPath as getNationsFilterAssetPath
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION as VEHICLE_CUSTOMIZATION
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.customization.shared import QUANTITY_LIMITED_CUSTOMIZATION_TYPES as QUANTITY_LIMITED_CUSTOMIZATION_TYPES, appliedToFromSlotsIds as appliedToFromSlotsIds, C11nId as C11nId, PurchaseItem as PurchaseItem, AdditionalPurchaseGroups as AdditionalPurchaseGroups, getAvailableRegions as getAvailableRegions, EDITABLE_STYLE_APPLY_TO_ALL_AREAS_TYPES as EDITABLE_STYLE_APPLY_TO_ALL_AREAS_TYPES, EDITABLE_STYLE_IRREMOVABLE_TYPES as EDITABLE_STYLE_IRREMOVABLE_TYPES, C11N_ITEM_TYPE_MAP as C11N_ITEM_TYPE_MAP
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER, VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Money as Money
from gui.shared.utils import code2str as code2str
from helpers import dependency as dependency, int2roman as int2roman
from helpers.i18n import makeString as _ms
from items import parseIntCompactDescr as parseIntCompactDescr
from items.components.c11n_components import getItemSlotType as getItemSlotType
from items.components.c11n_constants import SeasonType as SeasonType, ProjectionDecalFormTags as ProjectionDecalFormTags, CustomizationType as CustomizationType, SLOT_DEFAULT_ALLOWED_MODEL as SLOT_DEFAULT_ALLOWED_MODEL, EMPTY_ITEM_ID as EMPTY_ITEM_ID
from items.customizations import CustomizationOutfit as CustomizationOutfit
from items.vehicles import VEHICLE_CLASS_TAGS as VEHICLE_CLASS_TAGS, getItemByCompactDescr as getItemByCompactDescr
from serializable_types.customizations.projection_decal import ProjectionDecalComponent as ProjectionDecalComponent
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from vehicle_outfit.containers import SlotData as SlotData
from vehicle_outfit.outfit import Area as Area, Outfit as Outfit
from vehicle_outfit.packers import ProjectionDecalPacker as ProjectionDecalPacker
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from gui.shared.gui_items.customization.c11n_items import Style as Style
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from items.components.c11n_components import StyleItem as StyleItem
from typing import Optional as Optional, List as List
_logger: Any
EMPTY_PERSONAL_NUMBER = ''
ITEM_TYPE_TO_TAB: dict
ITEM_TYPE_TO_SLOT_TYPE: dict
REGIONS_SLOTS: Any
APPLIED_TO_TYPES: tuple
SCALE_SIZE: tuple
TYPES_ORDER: tuple
SEASON_TYPE_TO_INFOTYPE_MAP: dict
COMMON_C11N_AUTO_INSTALL_TYPES: tuple
OutfitInfo: Any
CustomizationSlotUpdateVO: Any

class CustomizationTabs(object):
    DEFAULT = -1
    PAINTS = 1
    CAMOUFLAGES = 2
    PROJECTION_DECALS = 3
    EMBLEMS = 4
    INSCRIPTIONS = 5
    MODIFICATIONS = 6
    STYLES_2D = 7
    STYLES_3D = 8
    ATTACHMENTS = 9
    STAT_TRACKERS = 10
    ALL: tuple
    REGIONS: tuple
    ALWAYS_ENABLED: tuple
    STYLES: tuple
    MODES: dict
    TAB_TO_MODE: dict
    TAB_NAMES: dict
    SLOT_TYPES: dict
    ITEM_TYPES: dict
    TABS_WITH_RARITY: tuple

class BillPopoverButtons(object):
    CUSTOMIZATION_CLEAR = 'customizationClear'
    CUSTOMIZATION_CLEAR_LOCKED = 'customizationClearLocked'
    ALL: tuple

# decorador original: @dependency.replace_none_kwargs(...)
def getCommonPurchaseItems(commonOutfit, c11nService=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getCustomPurchaseItems(season, modifiedOutfits, c11nService=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getStylePurchaseItems(style, modifiedOutfits, c11nService=None, prolongRent=False, progressionLevel=-1):
    ...
def correctSlot(slotId):
    ...
def fitOutfit(outfit, availableRegionsMap):
    ...
def getOutfitWithoutItems(outfitsInfo, intCD, count):
    ...
def getOutfitWithoutItemsNoDiff(outfits, intCD, count):
    ...
def fromWorldCoordsToHangarVehicle(worldCoords):
    ...
def fromHangarVehicleToWorldCoords(hangarVehicleCoords):
    ...
def getSuitableText(item, currentVehicle=None, formatVehicle=True):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def makeVehiclesShortNamesString(vehiclesCDs, currentVehicle, flat=False, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isC11nEnabled(lobbyContext=None, hangarSpace=None):
    ...
def formatPersonalNumber(number, digitsCount):
    ...
def fitPersonalNumber(number, digitsCount):
    ...
def getProjectionSlotFormfactor(slotId):
    ...
def getMultiSlot(outfit, slotId):
    ...
def getSlotDataFromSlot(outfit, slotId):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getItemFromSlot(outfit, slotId, service=None):
    ...
def getComponentFromSlot(outfit, slotId):
    ...
def isSlotFilled(outfit, slotId):
    ...
def isItemLimitReached(item, outfits=None, customizationMode=None):
    ...
def getPurchaseLimit(item, outfits=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isItemsQuantityLimitReached(outfit, itemType, service=None):
    ...
def getEmptyRegions(outfit, slotType):
    ...
def getCurrentVehicleAvailableRegionsMap():
    ...
def checkSlotsFilling(outfit, slotType):
    ...
def isSlotLocked(outfit, slotId):
    ...
def isPurchaseItemLocked(item, style):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isItemUsedUp(item, appliedItems=None, service=None):
    ...
def getItemInventoryCount(item, outfits=None):
    ...
def getItemAppliedCount(item, outfits):
    ...
def getItemInstalledCount(item):
    ...
def getProgressionItemStatusText(level):
    ...
def vehicleHasSlot(slotType, vehicle=None, modelsSet=None):
    ...
def getItemTypesAvailableForVehicle(vehicle=None):
    ...
def customizationSlotIdToUid(slotId):
    ...
def getEditableStyleOutfitDiffComponent(outfit, baseOutfit):
    ...
def getEditableStyleOutfitDiff(outfit, baseOutfit):
    ...
def isStyleEditedForCurrentVehicle(outfits, style):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getUnsuitableDependentData(outfit, selCamoItemID, styleDependencies, service=None):
    ...
def resetC11nItemsNovelty(items):
    ...
def removeUnselectedItemsFromEditableStyle(modifiedOutfits, baseOutfits, purchaseItems):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def removeItemFromEditableStyle(outfit, baseOutfit, slotId, season, service=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def removeItemsFromOutfit(outfit, filterMethod, service=None):
    ...
def __removeItemFromEditableStyleAllAreas(outfit, baseOutfit, slotType):
    ...
def __removeItemFromEditableStyleOutfit(outfit, baseOutfit, slotId):
    ...
def __doItemRemoveFromEditableStyleOutfit(outfit, baseOutfit, slotId, isSetToDefault):
    ...
def __getItemInventoryCount(item, outfits=None):
    ...
def __getStyleInventoryCount(item, outfits=None):
    ...
def __getItemAppliedCount(item, outfits):
    ...
def __getStyleAppliedCount(item, outfits):
    ...
def __isStyleInstalled(style):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def __getInventoryCounts(modifiedOutfits, vehicleCD, itemsCache=None, c11nService=None):
    ...
def changePartsOutfit(season, outfit, intCD, removeIntCD):
    ...
def addPartsToOutfit(season, outfit, intCDs=None):
    ...
def removePartsFromOutfit(season, outfit, intCDs=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getStyledModeRequestData(requestData, style, vehicle, purchaseItems=None, stylesDiffsCache=None, styleProgressionLevel=None, customizationService=None):
    ...
def remove3DStyleIncompatibleCommonItems(outfit, style=None, vehicle=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isStatTrackerTabEnabled(c11nService=None):
    ...
def getAvailableSlots(slotType, vehicleDescr=None):
    ...
def removeUncommonItems(outfit):
    ...
