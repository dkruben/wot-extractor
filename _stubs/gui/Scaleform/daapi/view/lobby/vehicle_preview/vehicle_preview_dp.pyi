# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/vehicle_preview_dp.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
import nations as nations
from gui.Scaleform import MENU as MENU
from gui import GUI_NATIONS_ORDER_INDEX_REVERSED as GUI_NATIONS_ORDER_INDEX_REVERSED
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import collapseItemsPack as collapseItemsPack, getCompensateItemsCount as getCompensateItemsCount, getDataOneVehicle as getDataOneVehicle, getDataMultiVehicles as getDataMultiVehicles, getCouponDiscountForItemPack as getCouponDiscountForItemPack, getCouponBonusesForItemPack as getCouponBonusesForItemPack
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, moneyWithIcon as moneyWithIcon, icons as icons
from gui.shared.formatters.currency import getBWFormatter as getBWFormatter, getStyle as getStyle
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.money import Money as Money, Currency as Currency, MONEY_UNDEFINED as MONEY_UNDEFINED
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils import vehicle_collector_helper as vehicle_collector_helper
from helpers import dependency as dependency, int2roman as int2roman
from helpers.i18n import makeString as _ms
from helpers.time_utils import getTillTimeString as getTillTimeString
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api.common import CompensationType as CompensationType, ItemPackTypeGroup as ItemPackTypeGroup
from typing import Dict as Dict, Any as Any
_logger: _Any
_CUSTOM_OFFER_ACTION_PERCENT = 100

class IVehPreviewDataProvider(object):
    def getBuyType(self, vehicle):
        ...
    def getBuyingPanelData(self, item, data=None, isHeroTank=False, itemsPack=None):
        ...

class DefaultVehPreviewDataProvider(IVehPreviewDataProvider):
    __itemsCache: _Any
    def getBuyType(self, vehicle):
        ...
    def getBuyingPanelData(self, item, data=None, isHeroTank=False, itemsPack=None):
        ...
    def getItemPackBuyingPanelData(self, data, itemsPack, couponSelected, price):
        ...
    def getOffersBuyingPanelData(self, data):
        ...
    def getOffersData(self, offers, activeID):
        ...
    @staticmethod
    def separateItemsPack(packItems):
        ...
    def getItemsPackData(self, vehicle, items, vehicleItems):
        ...
    def packCouponData(self, itemsPack, price):
        ...
    def __getCompensationData(self, itemsPack):
        ...
    @staticmethod
    def __packCompensation(value, currency):
        ...
    @staticmethod
    def __getCustomOfferData(data):
        ...
    @staticmethod
    def __getWarningInfo(data, item):
        ...

def _createVehicleVO(rawItem, itemsCache):
    ...
def _createOfferVO(offer, setActive=False):
    ...
def _getRentTooltipData(offer):
    ...
def _vehicleComparisonKey(vehicle):
    ...
