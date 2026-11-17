# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import re as re
import typing as typing
from collections import namedtuple as namedtuple
import nations as nations
from constants import RentType as RentType
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES as ITEM_TYPES
from gui.game_control.veh_comparison_basket import isValidVehicleForComparing as isValidVehicleForComparing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items import CREW_SKILL_TO_KPI_NAME_MAP as CREW_SKILL_TO_KPI_NAME_MAP, GUI_ITEM_TYPE as GUI_ITEM_TYPE, KPI as KPI
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, getShortUserName as getShortUserName, getUserName as getUserName
from gui.shop import SHOP_RENT_SEASON_TYPE_MAP as SHOP_RENT_SEASON_TYPE_MAP, SHOP_RENT_TYPE_MAP as SHOP_RENT_TYPE_MAP
from helpers import dependency as dependency, i18n as i18n, time_utils as time_utils
from helpers.func_utils import replaceImgPrefix as replaceImgPrefix
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from items import vehicles as vehicles
from math_common import decimal_round as decimal_round
from nation_change.nation_change_helpers import getGroupByVehTypeCompactDescr as getGroupByVehTypeCompactDescr, iterVehTypeCDsInNationGroup as iterVehTypeCDsInNationGroup
from rent_common import SeasonRentDuration as SeasonRentDuration
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Union as Union, Any as Any, Optional as Optional
from gui.shared.gui_items.Tankman import Tankman as Tankman
from web.web_client_api.shop.crew import _ShopTankman as _ShopTankman, _ShopRecruit as _ShopRecruit
AnyTankman: _Any
COLOR_TAG_OPEN = '{colorTagOpen}'
COLOR_TAG_CLOSE = '{colorTagClose}'
_WHITESPACE_RE: _Any
_RENT_DURATION_MAP: dict
Field: _Any
idField: _Any
nameField: _Any
nationField: _Any
nationNameField: _Any
typeField: _Any
typeNameField: _Any
descriptionField: _Any
shortDescriptionSpecialField: _Any
longDescriptionSpecialField: _Any
inventoryCountField: _Any
buyPriceField: _Any
sellPriceField: _Any
tagsField: _Any
kpiField: _Any
techNameField: _Any
imagesField: _Any
optDeviceCategoriesField: _Any
optDeviceEffectField: _Any
optDeviceGroupName: _Any
_vehicleComponentsFieldSet: tuple
_vehicleArtifactsFieldSet: _Any
_vehicleOptDeviceFieldSet: _Any

class Formatter(object):
    __slots__: tuple
    __fields: _Any
    def __init__(self, fields):
        ...
    def format(self, item, allowedFields=None):
        ...

def formatValueToColorTag(value):
    ...
def _formatPrice(itemPrice):
    ...
def _formatFloat(val):
    ...
def _formatKPI(kpiList):
    ...
def _formatActionParams(actionInfo):
    ...
def _formatTechName(value):
    ...
def _formatImagePaths(item):
    ...
def _formatVehicleRestore(item):
    ...
def _formatVehicleOwnership(item):
    ...
def _formatVehicleNationChange(vehicle):
    ...
def _formatVehicleComparingAvailability(item):
    ...
def _formatUserName(item):
    ...
def _formatShortUserName(item):
    ...
def _formatOptDeviceCategories(item):
    ...
def _formatOptDeviceEffects(item):
    ...
def _formatTags(item):
    ...
def makeActionFormatter():
    ...
def makeVehicleFormatter(includeInventoryFields=False):
    ...
def makeShopTankmanFormatter():
    ...
def _formatTankmanRole(crewItem):
    ...
def _formatTankmanRank(crewItem):
    ...
def _formatVehicleInfo(crewItem):
    ...
def _formatTankmanNames(crewItem):
    ...
def _formatTankmanNationInfo(crewItem):
    ...
def _formatTankmanIcons(crewItem):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def makeDeviceFormatter(compatVehGetter=None, fittedVehGetter=None, itemsCache=None):
    ...
def makeEquipmentFormatter(fittedVehGetter=None):
    ...
def makeBattleBoosterFormatter(fittedVehGetter=None):
    ...
def makeBoosterFormatter():
    ...
def makeModuleFormatter():
    ...
def makeShellFormatter(includeCount=False):
    ...
def makeCrewFormatter():
    ...
def makePremiumPackFormatter():
    ...
def makeCustomizationFormatter():
    ...
def makeInventoryEnhancementsFormatter():
    ...
def makeInstalledEnhancementsFormatter():
    ...
def makeCrewBooksFormatter():
    ...
