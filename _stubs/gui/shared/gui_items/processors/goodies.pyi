# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/goodies.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from gui.SystemMessages import SM_TYPE as SM_TYPE, CURRENCY_TO_SM_TYPE as CURRENCY_TO_SM_TYPE
from gui.impl import backport as backport
from gui.shared.formatters import formatPrice as formatPrice
from gui.shared.gui_items.processors import Processor as Processor, makeI18nError as makeI18nError, makeI18nSuccess as makeI18nSuccess, plugins as proc_plugs
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Currency as Currency
from gui.shared.utils import code2str as code2str
from gui.SystemMessages import ResultMsg as ResultMsg
_logger: Any

class BoosterProcessor(Processor):
    booster: Any
    opType: Any
    def __init__(self, booster, opType, plugins=None):
        ...
    def _response(self, code, callback, errStr='', ctx=None):
        ...
    def _getMsgCtx(self):
        ...
    def _formMessage(self, msg):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class BoosterActivator(BoosterProcessor):
    def __init__(self, booster):
        ...
    def _getMsgCtx(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class BoosterTradeProcessor(BoosterProcessor):
    count: Any
    def __init__(self, booster, count, opType, plugs=None):
        ...
    def _getMsgCtx(self):
        ...
    def _getOpPrice(self):
        ...

class BoosterBuyer(BoosterTradeProcessor):
    buyCurrency: Any
    doActivation: Any
    def __init__(self, booster, count, currency, doActivation=False):
        ...
    def _getOpPrice(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class BoosterSeller(BoosterTradeProcessor):
    def __init__(self, booster, count):
        ...
    def _getOpPrice(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
