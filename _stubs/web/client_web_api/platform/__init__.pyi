# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/platform/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import dependency as dependency
from skeletons.helpers.platform import IPublishPlatform as IPublishPlatform
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w

class PlatformEventHandler(C2WHandler):
    __platform: Any
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @c2w(...)
    def __onPayment(self, orderID, authorized):
        ...
    # decorador original: @c2w(...)
    def __onOverlay(self, active):
        ...
