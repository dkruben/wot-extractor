# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/auxiliary/exchanger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.shared.gui_items.processors.common import GoldToCreditsExchanger as GoldToCreditsExchanger
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_TYPE_TO_SUBMITTER_MAP: dict

class ExchangeSubmitterBase(object):
    def submit(self, fromItemCount, withConfirm=False, callback=None):
        ...
    def getCurrentRate(self):
        ...
    def getDefaultRate(self):
        ...
    def calculateToItemCount(self, fromExchangeAmount):
        ...
    def calculateFromItemCount(self, toExchangeAmount):
        ...

class ExchangeCreditsSubmitter(ExchangeSubmitterBase):
    __itemsCache: Any
    __exchangeRatesProvider: Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def submit(self, fromItemCount, withConfirm=True, callback=None):
        ...
    @property
    def exchangeRate(self):
        ...
    def getCurrentRate(self):
        ...
    def getDefaultRate(self):
        ...
    def calculateToItemCount(self, fromExchangeAmount):
        ...
    def calculateFromItemCount(self, toExchangeAmount):
        ...

class Exchanger(object):
    __slots__: tuple
    __submitter: Any
    __fromItemType: Any
    __toItemType: Any
    def __init__(self, fromItemType, toItemType):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def tryExchange(self, fromItemCount, withConfirm=True, callback=None):
        ...
    def calculateToItemCount(self, fromItemCount):
        ...
    def calculateFromItemCount(self, toItemCount):
        ...
    def getCurrentRate(self):
        ...
    def getDefaultRate(self):
        ...
