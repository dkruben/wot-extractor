# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/shop/stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w
from web.common import formatWalletCurrencyStatuses as formatWalletCurrencyStatuses, formatBalance as formatBalance

class BalanceEventHandler(C2WHandler):
    __walletController: Any
    __itemsCache: Any
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @c2w(...)
    def __onBalanceUpdate(self, *_):
        ...
    # decorador original: @c2w(...)
    def __onWalletUpdate(self, *_):
        ...
