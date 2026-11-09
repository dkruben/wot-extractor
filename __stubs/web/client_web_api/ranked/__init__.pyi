# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/ranked/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared import g_eventBus as g_eventBus
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w
from web.web_client_api.ranked_battles import BROWSER_BRIDGE_EVENT as BROWSER_BRIDGE_EVENT
_ALLOWED_TOKENS: set

class RankedEventHandler(C2WHandler):
    def init(self):
        ...
    def fini(self):
        ...
    def __onTokensUpdate(self, diff):
        ...
    # decorador original: @c2w(...)
    def __sendTokens(self, tokens):
        ...

class BrowsersBridgeC2W(C2WHandler):
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @c2w(...)
    def __handleProxyData(self, event):
        ...
