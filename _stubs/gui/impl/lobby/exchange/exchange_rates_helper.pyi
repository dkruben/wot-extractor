# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/exchange_rates_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import EXCHANGE_GOLD_RATE_DISCOUNT_ANIMATION_SHOWED as EXCHANGE_GOLD_RATE_DISCOUNT_ANIMATION_SHOWED, EXCHANGE_XP_RATE_DISCOUNT_ANIMATION_SHOWED as EXCHANGE_XP_RATE_DISCOUNT_ANIMATION_SHOWED
from exchange.personal_discounts_constants import EXCHANGE_RATE_GOLD_NAME as EXCHANGE_RATE_GOLD_NAME, EXCHANGE_RATE_FREE_XP_NAME as EXCHANGE_RATE_FREE_XP_NAME, EXCHANGE_NAME_TO_GAME_PARAM_NAME as EXCHANGE_NAME_TO_GAME_PARAM_NAME, MAX_DISCOUNT_VALUE as MAX_DISCOUNT_VALUE, ExchangeRate as ExchangeRate, ExchangeDiscountType as ExchangeDiscountType
from exchange.personal_discounts_helper import sortExchangeRatesDiscounts as sortExchangeRatesDiscounts
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.exchange.discount_presentation import DiscountPresentation as DiscountPresentation
from gui.shared.gui_items.processors import makeI18nSuccess as makeI18nSuccess
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider, IExchangeRateWithDiscounts as IExchangeRateWithDiscounts
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional, Tuple as Tuple, Dict as Dict, List as List
from gui.SystemMessages import ResultMsg as ResultMsg
from exchange.personal_discounts_constants import ExchangeDiscountInfo as ExchangeDiscountInfo
MAX_SHOW_DISCOUNTS_INDEX = 5
DISCOUNT_ANIMATION_TIME = 15.0
EXCHANGE_RATE_NAME_TO_CURRENCIES: dict
NEED_ITEMS_TYPE_TO_EXCHANGE_RATE: dict
EXCHANGE_RATE_TO_UI_KEY: dict

def getCurrentTime():
    ...
def isDiscountViewed(discountType):
    ...
def getRateNameFromCurrencies(currencies):
    ...
def setDiscountViewed(exchangeRate, forced=False):
    ...
def isGoldExchangeRateDiscountViewed():
    ...
def isExperienceTranslationRateDiscountViewed():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _setDiscountViewed(exchangeName, uiFlag, forced=False, exchangeDiscountCtr=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _isDiscountViewed(exchangeName, exchangeDiscountCtr=None):
    ...
def _getDiscountUID(discount):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getExchangeRate(exchangeName, default=False, itemsCache=None):
    ...
def convertToGuiLimit(discount, amount):
    ...
def getAllLimitedDiscountsAmount(allDiscounts):
    ...
def getShowFormatRate(discount):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def convertGoldToGuiLimit(discount, goldAmount, exchangeProvider=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def handleUserValuesInput(selectedGold=0, selectedCurrency=0, validateGold=True, exchangeProvider=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def calculateMaxPossibleFreeXp(xpFromVehicles, validateGold=True, itemsCache=None, exchangeProvider=None):
    ...
def showAllPersonalDiscountsWindow(exchangeRateType, selectedValue):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillAllDiscountsModel(allDiscountsModel, allLimitedDiscounts, selectedPrice, exchangeProvider=None):
    ...
def createSystemExchangeNotification(discounts, goldAmount, defaultRate, baseRate, isPersonalUnlimRate, exchangeType):
    ...
def handleAndRoundStepperInput(params, exchangeRate, validateGold=True):
    ...
