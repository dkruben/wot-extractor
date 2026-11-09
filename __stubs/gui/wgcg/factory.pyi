# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/factory.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from client_request_lib.requester import Requester as WebRequester
from constants import TOKEN_TYPE as TOKEN_TYPE
from gui.shared.utils.requesters import TokenRequester as TokenRequester, getTokenRequester as getTokenRequester
from gui.wgcg.requests import WgcgRequester as WgcgRequester, WgcgRequestsController as WgcgRequestsController
from helpers.server_settings import _Wgcg as _Wgcg
g_webFactory: Any

class _WebFactory(object):
    def createWebRequester(self, settings, *args, **kwargs):
        ...
    def createTokenRequester(self):
        ...
    def createWgcgRequester(self, webRequester):
        ...
    def createWgcgRequestsController(self, webCtrl, clanRequester):
        ...

class WebFactory(_WebFactory):
    def createWebRequester(self, settings, *args, **kwargs):
        ...
    def createTokenRequester(self):
        ...
    def createWgcgRequester(self, webRequester):
        ...
    def createWgcgRequestsController(self, webCtrl, clanRequester):
        ...

class FakeWebFactory(_WebFactory):
    def createWebRequester(self, settings, *args, **kwargs):
        ...
    def createTokenRequester(self):
        ...
    def createWgcgRequester(self, webRequester):
        ...
    def createWgcgRequestsController(self, webCtrl, clanRequester):
        ...

def _webUrlFetcher(url, callback, headers=None, timeout=30.0, method='GET', postData=''):
    ...
