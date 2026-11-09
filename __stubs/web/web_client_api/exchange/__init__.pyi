# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/exchange/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from exchange.personal_discounts_constants import ExchangeDiscountType as ExchangeDiscountType, EXCHANGE_RATE_GOLD_NAME as EXCHANGE_RATE_GOLD_NAME, EXCHANGE_RATE_FREE_XP_NAME as EXCHANGE_RATE_FREE_XP_NAME
from gui.impl.lobby.exchange.exchange_rates_helper import convertToGuiLimit as convertToGuiLimit, getShowFormatRate as getShowFormatRate
from helpers import dependency as dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from web.web_client_api import w2capi as w2capi, w2c as w2c, W2CSchema as W2CSchema, Field as Field
_selectedAmountValidator: Any

class _GoldSchema(W2CSchema):
    gold_amount: Any

class _CreditsSchema(W2CSchema):
    credits_amount: Any

# decorador original: @w2capi(...)
class PersonalExchangeRatesDiscountsWebApi(object):
    __exchangeRatesProvider: Any
    EXCHNAGE_RATES_MAPPING: dict
    # decorador original: @w2c(...)
    def calculateGoldToCreditsExchange(self, cmd):
        ...
    # decorador original: @w2c(...)
    def calculateCreditsToGoldExchange(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getPersonalDiscounts(self, _):
        ...
    @staticmethod
    def __serializePersonalDiscountToDict(discount):
        ...
