# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/wgm_balance_info_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewkeys as viewkeys
from functools import partial as partial
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.shared.utils.requesters.common import RequestProcessor as RequestProcessor
from gui.shared.money import Currency as Currency
from debug_utils import LOG_WARNING as LOG_WARNING
from helpers import isPlayerAccount as isPlayerAccount
_REQUEST_COOLDOWN = 5.0
_TOKEN_CURRENCY_CODE = 'code'
_TOKEN_IS_PAID = 'is_paid'
_TOKEN_AMOUNT = 'amount'
_TOKEN_GOLD = Currency.GOLD
_TOKEN_CREDITS = Currency.CREDITS
_ACTION_PURCHASED = '_purchased'
_ACTION_EARNED = '_earned'
GOLD_PURCHASED: Any
GOLD_EARNED: Any
CREDITS_PURCHASED: Any
CREDITS_EARNED: Any

class WGMBalanceInfoRequester(object):
    __request: Any
    __lastResponseTime: Any
    __receivedData: Any
    __callbacks: Any
    def __init__(self):
        ...
    def isRequestInProgress(self):
        ...
    def getLastReceivedData(self):
        ...
    def clearCallbacks(self):
        ...
    # decorador original: @adisp_process
    def requestInfo(self, callback):
        ...
    # decorador original: @adisp_async
    def __requestWGMBalanceInfo(self, callback):
        ...
    def __cooldownCallback(self, callback):
        ...
    def __nextRequestTime(self):
        ...
    def __processResponse(self, callback, resultID, errorStr, ext):
        ...
    @staticmethod
    def __checkFields(row):
        ...
