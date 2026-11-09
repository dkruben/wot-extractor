# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/dyn_currencies_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from battle_pass_common import CurrencyBP as CurrencyBP
from gui.game_control.seniority_awards_controller import WDR_CURRENCY as WDR_CURRENCY
from gui.shared.money import Currency as Currency, Money as Money
from gui.shared import event_dispatcher as event_dispatcher
from gui.shop import showBuyProductOverlay as showBuyProductOverlay
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from typing import Dict as Dict, Iterable as Iterable, Callable as Callable, Optional as Optional, Union as Union
_BUY_PRODUCT_USING_DYN: dict
_DYN_CURRENCIES: Any

class DynMoney(object):
    _values: Any
    def __init__(self, values):
        ...
    def get(self, currency, default=None):
        ...
    def getCurrency(self):
        ...
    def isDefined(self):
        ...

def isCurrency(currency):
    ...
def isDynCurrency(currency):
    ...
def isMoney(money):
    ...
def isDynMoney(money):
    ...
def getMoney(price, dynPrice):
    ...
def getBuyProductMethod(money):
    ...
def separatePrice(price):
    ...
def mayObtainForMoney(money):
    ...
def mayObtainWithMoneyExchange(money):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getUserMoney(currency, itemsCache=None):
    ...
def _mayObtainForDynCurrency(money):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getUserDynCurrency(currency, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getUserMoney(currency, itemsCache=None):
    ...
