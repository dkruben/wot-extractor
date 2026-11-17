# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/trade_in.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
import typing as typing
import AccountCommands as AccountCommands
from Account import PlayerAccount as PlayerAccount
_logger: Any
_SECONDS_IN_DAY = 86400

class TradeIn(object):
    _account: Any
    def __init__(self):
        ...
    def setAccount(self, account):
        ...
    def addTokenDev(self, tokenID, expiryTimeOffset=...):
        ...
    def removeTokenDev(self, tokenID):
        ...
    def _onCmdResponseReceived(self, resultID, requestID, errorStr, errorMsg=None):
        ...
