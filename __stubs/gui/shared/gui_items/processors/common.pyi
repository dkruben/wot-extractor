# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import copy as copy
import time as time
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from BWUtil import AsyncReturn as AsyncReturn
from constants import EMPTY_GEOMETRY_ID as EMPTY_GEOMETRY_ID, PREMIUM_TYPE as PREMIUM_TYPE
from exchange.personal_discounts_helper import getDiscountsRequiredForExchange as getDiscountsRequiredForExchange
from gui import SystemMessages as SystemMessages
from gui.customization.shared import validateOutfitComponent as validateOutfitComponent
from gui.game_control.exchange_rates_with_discounts import getCurrentTime as getCurrentTime
from gui.impl.lobby.exchange.exchange_rates_helper import createSystemExchangeNotification as createSystemExchangeNotification
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.Scaleform.locale.MESSENGER import MESSENGER as MESSENGER
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.SystemMessages import SM_TYPE as SM_TYPE, CURRENCY_TO_SM_TYPE as CURRENCY_TO_SM_TYPE
from gui.shared.formatters import formatPrice as formatPrice, formatGoldPrice as formatGoldPrice, text_styles as text_styles, icons as icons
from gui.shared.gui_items.processors import Processor as Processor, makeError as makeError, makeSuccess as makeSuccess, makeI18nError as makeI18nError, makeI18nSuccess as makeI18nSuccess, plugins as plugins, GroupedRequestProcessor as GroupedRequestProcessor
from gui.shared.money import Money as Money, Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket, IWotPlusController as IWotPlusController, IEpicBattleMetaGameController as IEpicBattleMetaGameController, IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from wg_async import wg_async as wg_async, wg_await as wg_await, await_callback as await_callback
from shared_utils import first as first
_logger: Any

class TankmanBerthsBuyer(Processor):
    berthsPrice: Any
    countPacksBerths: Any
    def __init__(self, berthsPrice, countPacksBerths):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class PremiumAccountBuyer(Processor):
    wasPremium: Any
    premiumPrice: Any
    period: Any
    arenaUniqueID: Any
    def __init__(self, period, price, arenaUniqueID=0, withoutBenefits=False, requireConfirm=True):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
    def __getConfirmator(self, withoutBenefits, period, price):
        ...

class GoldToCreditsExchanger(Processor):
    __exchangeRatesProvider: Any
    gold: Any
    baseRate: Any
    discounts: Any
    credits: Any
    def __init__(self, gold, withConfirm=True):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class FreeXPExchanger(Processor):
    __exchangeRatesProvider: Any
    xp: Any
    baseRate: Any
    vehiclesCD: Any
    gold: Any
    discounts: Any
    def __init__(self, xp, vehiclesCD):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
    def __makeConfirmator(self):
        ...

class BattleResultsGetter(Processor):
    __arenaUniqueID: Any
    def __init__(self, arenaUniqueID):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class OutfitApplier(Processor):
    vehicle: Any
    outfitData: Any
    def __init__(self, vehicle, outfitData):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class CustomizationsBuyer(Processor):
    vehicle: Any
    item: Any
    count: Any
    def __init__(self, vehicle, item, count):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...
    def _getTotalPrice(self):
        ...
    def _getMsgCtx(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class CustomizationsSeller(Processor):
    vehicle: Any
    item: Any
    count: Any
    def __init__(self, vehicle, item, count=1):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _getTotalPrice(self):
        ...
    def _getMsgCtx(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class BadgesSelector(Processor):
    __badges: Any
    def __init__(self, badges=None):
        ...
    def _getMessagePrefix(self):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class ConvertBlueprintFragmentProcessor(Processor):
    __vehicleCD: Any
    __position: Any
    __count: Any
    __usedNationalFragments: Any
    def __init__(self, vehicleCD, count, fragmentPosition, usedNationalFragments):
        ...
    def _request(self, callback):
        ...

class _MapsBlackListSelector(Processor):
    _SKIPPED_MAP_ID_LOWER_BOUND = EMPTY_GEOMETRY_ID
    __toAddMapID: Any
    __toRemoveMapId: Any
    def __init__(self, toAddMapID=..., toRemoveMapID=...):
        ...
    def _getMessagePrefix(self):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class MapsBlackListSetter(_MapsBlackListSelector):
    def __init__(self, selectedMapID):
        ...

class MapsBlackListRemover(_MapsBlackListSelector):
    def __init__(self, removeMapID):
        ...

class MapsBlackListChanger(_MapsBlackListSelector):
    def __init__(self, srcMapID, destMapID):
        ...

class PremiumBonusApplier(Processor):
    __arenaUniqueID: Any
    __vehTypeCompDescr: Any
    def __init__(self, arenaUniqueID=None, vehTypeCompDescr=None):
        ...
    def _getMessagePrefix(self):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class UseCrewBookProcessor(GroupedRequestProcessor):
    __crewBookCD: Any
    __crewBookCount: Any
    __vehInvID: Any
    __tmanInvID: Any
    def __init__(self, crewBookCD, crewBookCount, vehInvID, tmanInvID, groupID=0, groupSize=1):
        ...
    def _makeSuccessData(self, *args, **kwargs):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class ClaimRewardForPostProgression(Processor):
    def __init__(self, xppToConvert):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class FillingAllUntrainedPerksProcessor(Processor):
    _fillInBarracks: Any
    def __init__(self, fillInBarracks):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class VehicleChangeNation(Processor):
    _comparisonBasket: Any
    _cvh: Any
    _nvh: Any
    def __init__(self, cvh, nvh):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class BuyBattleAbilitiesProcessor(Processor):
    __epicMetaGameCtrl: Any
    __skillIds: Any
    def __init__(self, skillIds):
        ...
    # decorador original: @wg_async
    def _request(self, callback):
        ...
    # decorador original: @wg_async
    def _requestChain(self):
        ...
