# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/shop.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from gui.shared import event_dispatcher as event_dispatcher, g_eventBus as g_eventBus, events as events
from gui.shared.event_dispatcher import hideWebBrowserOverlay as hideWebBrowserOverlay
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field

class _OpenShopSchema(W2CSchema):
    path: Any

class ShopWebApiMixin(object):
    # decorador original: @w2c(...)
    def openShop(self, cmd):
        ...
    # decorador original: @w2c(...)
    def openShopExternalBrowser(self, *_):
        ...
