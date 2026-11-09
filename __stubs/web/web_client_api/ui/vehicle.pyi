# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/vehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
from functools import partial as partial
from itertools import groupby as groupby
from logging import getLogger as getLogger
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import STYLE_PREVIEW_VEHICLES_POOL as STYLE_PREVIEW_VEHICLES_POOL
from debug_utils import LOG_ERROR as LOG_ERROR
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.vehicle_preview.configurable_vehicle_preview import OptionalBlocks as OptionalBlocks
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import canInstallStyle as canInstallStyle, getCDFromId as getCDFromId
from gui.Scaleform.daapi.view.lobby.vehicle_preview.preview_bottom_panel_constants import ObtainingMethods as ObtainingMethods
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW as VEHICLE_PREVIEW
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_preview.top_panel.top_panel_tabs_model import TabID as TabID
from gui.server_events.events_dispatcher import showMissionsMarathon as showMissionsMarathon
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.event_dispatcher import showHangar as showHangar, showMarathonRewardScreen as showMarathonRewardScreen, showStyleBuyingPreview as showStyleBuyingPreview, showStylePreview as showStylePreview, showStyleProgressionPreview as showStyleProgressionPreview
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency, MONEY_UNDEFINED as MONEY_UNDEFINED, Money as Money
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from helpers.time_utils import getCurrentLocalServerTimestamp as getCurrentLocalServerTimestamp, getDateTimeInLocal as getDateTimeInLocal, getDateTimeInUTC as getDateTimeInUTC, getTimeStructInLocal as getTimeStructInLocal, getTimestampFromISO as getTimestampFromISO, utcToLocalDatetime as utcToLocalDatetime
from items import ITEM_TYPES as ITEM_TYPES, vehicles as vehicles
from items.components.c11n_constants import CustomizationNamesToTypes as CustomizationNamesToTypes
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController, IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, w2c as w2c
from web.web_client_api.common import CompensationSpec as CompensationSpec, CompensationType as CompensationType, ItemPackEntry as ItemPackEntry, ItemPackType as ItemPackType, ItemPackTypeGroup as ItemPackTypeGroup, VehicleOfferEntry as VehicleOfferEntry
_logger: Any
REQUIRED_ITEM_FIELDS: set
REQUIRED_COMPENSATION_FIELDS: set
REQUIRED_CUSTOMCREW_FIELDS: set
REQUIRED_TANKMAN_FIELDS: set
DEFAULT_STYLED_VEHICLES: tuple
_CUSTOM_CREW_KEYS: set

class _ItemPackValidationError(SoftException):
    ...

class _ItemPackEntry(ItemPackEntry):
    def replace(self, values):
        ...

class _VehicleOfferEntry(VehicleOfferEntry):
    def replace(self, values):
        ...

class _VehicleSchema(W2CSchema):
    vehicle_id: Any

class _VehiclePreviewSchema(W2CSchema):
    vehicle_id: Any
    back_url: Any
    items: Any
    hidden_blocks: Any

class _VehicleOffersPreviewSchema(W2CSchema):
    vehicle_id: Any
    offers: Any
    buy_params: Any
    back_url: Any

class _VehiclePackPreviewSchema(W2CSchema):
    title: Any
    end_date: Any
    buy_price: Any
    items: Any
    back_url: Any
    buy_params: Any
    obtaining_method: Any

class _MarathonVehiclePackPreviewSchema(W2CSchema):
    title: Any
    items: Any
    marathon_prefix: Any

class _VehicleStylePreviewSchema(W2CSchema):
    vehicle_cd: Any
    style_id: Any
    back_btn_descr: Any
    back_url: Any
    level: Any
    price: Any
    buy_params: Any
    alternate_item: Any

class _ShowcaseVehicleStylePreviewSchema(W2CSchema):
    vehicle_cd: Any
    style_id: Any
    back_btn_descr: Any
    back_url: Any
    level: Any
    price: Any
    buy_params: Any
    alternate_item: Any
    original_price: Any
    discount_percent: Any
    end_date: Any
    obtaining_method: Any

class _VehicleMarathonStylePreviewSchema(W2CSchema):
    vehicle_cd: Any
    style_id: Any
    back_btn_descr: Any
    back_url: Any
    marathon_prefix: Any

class _VehicleListStylePreviewSchema(W2CSchema):
    style_id: Any
    vehicle_min_level: Any
    vehicle_list: Any
    back_btn_descr: Any
    back_url: Any
    level: Any
    price: Any
    buy_params: Any

class _VehicleCustomizationPreviewSchema(W2CSchema):
    style_id: Any

class _MarathonRewardScreen(W2CSchema):
    marathon_prefix: Any

class _BPBitStylePreviewSchema(W2CSchema):
    vehicle_cd: Any
    style_id: Any
    back_btn_descr: Any
    back_url: Any
    level: Any
    price: Any
    buy_params: Any
    alternate_item: Any

class _VehicleStylePreviewWithTabsSchema(W2CSchema):
    vehicle_cd: Any
    style_id: Any
    back_btn_descr: Any
    back_url: Any
    items: Any

class VehicleSellWebApiMixin(object):
    itemsCache: Any
    # decorador original: @w2c(...)
    def vehicleSellDialog(self, cmd):
        ...

class VehicleCompareWebApiMixin(object):
    comparisonBasket: Any
    # decorador original: @w2c(...)
    def addVehicleToCompare(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getVehicleComparisonBasket(self, cmd):
        ...

class VehicleComparisonBasketWebApiMixin(object):
    # decorador original: @w2c(...)
    def openVehicleComparisonBasket(self, _):
        ...

class VehiclePreviewWebApiMixin(object):
    __itemsCache: Any
    __c11n: Any
    # decorador original: @w2c(...)
    def openVehiclePreview(self, cmd, ctx):
        ...
    # decorador original: @w2c(...)
    def openVehicleOffersPreview(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openMarathonVehiclePackPreview(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openVehiclePackPreview(self, cmd, ctx):
        ...
    # decorador original: @w2c(...)
    def openVehicleStylePreview(self, cmd, ctx):
        ...
    # decorador original: @w2c(...)
    def openShowcaseVehicleStylePreview(self, cmd, ctx):
        ...
    # decorador original: @w2c(...)
    def openMarathonVehicleStylePreview(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openVehicleListStylePreview(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openVehicleCustomizationPreview(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openMarathonRewardScreen(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openBPBitStylePreview(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openVehicleStylePreviewWithTabs(self, cmd, ctx):
        ...
    def _openVehicleStylePreview(self, cmd, showStyleFunc=None, **additionalStyleFuncKwargs):
        ...
    @staticmethod
    def __setBackUrl(cmd, ctx):
        ...
    @staticmethod
    def __getLocalEndTime(date):
        ...
    def __getStyledVehicleCD(self, styleId):
        ...
    def __getVehiclesForStylePreview(self, criteria=None):
        ...
    def _getVehicleStylePreviewCallback(self, cmd):
        ...
    def _getVehiclePreviewReturnCallback(self, cmd):
        ...
    def _getVehiclePreviewReturnAlias(self, cmd):
        ...
    def __showStylePreview(self, vehicleCD, cmd, showStyleFunc=None, **additionalStyleFuncKwargs):
        ...
    def __getVehiclesIDs(self, items):
        ...
    def __validVehiclePreview(self, intCD):
        ...
    def __validVehiclePreviewPack(self, vehiclesID):
        ...

def _doesVehicleCDExist(vehicleCD):
    ...
def _validateVehiclesCDList(vehiclesCDs):
    ...
def _isValidObtainingMethod(obtainingMethod, _):
    ...
def _validateItemsPack(items, *_):
    ...
def _validateItemsRequiredFields(items):
    ...
def _validateItemsPackTypes(items):
    ...
def _validateItemsCompensationRequiredFields(items):
    ...
def _validateItemsCustomCrewRequiredFields(items):
    ...
def _validateItemsCompensation(items):
    ...
def _getItemKey(item):
    ...
def _equalsCompensations(itemA, itemB):
    ...
def _parseItemsPack(items):
    ...
def _parseOffers(offers):
    ...
def _getOfferID(offer):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getOfferStr(offer, getKey, epicCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getRentLeft(offer, epicCtrl=None):
    ...
def _parseRent(offer):
    ...
def _getOfferCrew(offer):
    ...
def _parseBuyPrice(buyPrice):
    ...
def _buyPriceValidator(value, *_):
    ...
def _validatePrice(tData, errorStr=''):
    ...
def _validateBlocks(hiddenBlocks, *_):
    ...
def _pushInvalidPreviewMessage():
    ...
def _getStylePreviewShowFunc(styleInfo, price):
    ...
