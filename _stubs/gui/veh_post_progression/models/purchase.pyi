# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/models/purchase.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from account_helpers import isLongDisconnectedFromCenter as isLongDisconnectedFromCenter
from gui.veh_post_progression.models.ext_money import ExtendedMoney as ExtendedMoney
from gui.veh_post_progression.models.ext_money import ExtendedCurrency as _ExtCurrency
from gui.veh_post_progression.models.ext_money import ExtendedGuiItemEconomyCode as _ExtEconomyCode
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
VALID_CHECK_RESULT: Any

# base nao representavel no stub: namedtuple(...)
class PurchaseCheckResult:
    def __nonzero__(self):
        ...

class PurchaseProvider(object):
    __wallet: Any
    _EXCHANGE_PROCESSORS: dict
    @classmethod
    def isEnoughMoney(cls, balance, price):
        ...
    @classmethod
    def mayConsume(cls, balance, price):
        ...
    @classmethod
    def mayConsumeWithExhange(cls, balance, price, creditsRate):
        ...

def _exchangeCredits(balance, creditsRate):
    ...
