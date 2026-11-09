# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/currency_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
import typing as typing
from Event import Event as Event, EventManager as EventManager
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import List as List, Optional as Optional
_logger: Any
CurrencyInfo: Any
_CURRENCY_TOOLTIPS: dict

class CurrencyProvider(object):
    _adventController: Any
    _em: Any
    onBalanceUpdated: Any
    def __init__(self):
        ...
    @property
    def icon(self):
        ...
    @property
    def name(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def getCodes(self):
        ...
    def getCurrencies(self):
        ...
    def getCurrency(self, code):
        ...
    def getPrimary(self):
        ...
    def getMax(self):
        ...
    def getMaxBalance(self):
        ...
    def isEnough(self, price):
        ...
    def getBalance(self, code):
        ...

class StandardCurrencyProvider(CurrencyProvider):
    __DYNAMIC_CURRENCIES_KEY = 'cache.dynamicCurrencies'
    _itemsCache: Any
    def init(self):
        ...
    def fini(self):
        ...
    def getBalance(self, code):
        ...
    def __onBalanceChanged(self, *_):
        ...
