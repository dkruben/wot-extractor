# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/exchange/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from exchange.personal_discounts_constants import EXCHANGE_RATE_TYPES as EXCHANGE_RATE_TYPES
from helpers import dependency as dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w

class PersonalExchangeRatesDiscountsEventHandler(C2WHandler):
    __exchangeRatesProvider: Any
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @c2w(...)
    def __sendNotify(self):
        ...
