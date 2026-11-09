# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/strongholds/web_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from web.web_client_api import webApiCollection as webApiCollection
from web.web_client_api.clans import ClansWebApi as ClansWebApi
from web.web_client_api.exchange import PersonalExchangeRatesDiscountsWebApi as PersonalExchangeRatesDiscountsWebApi
from web.web_client_api.reactive_comm import ReactiveCommunicationWebApi as ReactiveCommunicationWebApi
from web.web_client_api.request import RequestWebApi as RequestWebApi
from web.web_client_api.shop import ShopWebApi as ShopWebApi
from web.web_client_api.sound import SoundWebApi as SoundWebApi, SoundStateWebApi as SoundStateWebApi
from web.web_client_api.strongholds import StrongholdsWebApi as StrongholdsWebApi
from web.web_client_api.ui import NotificationWebApi as NotificationWebApi, OpenWindowWebApi as OpenWindowWebApi, OpenTabWebApi as OpenTabWebApi, ContextMenuWebApi as ContextMenuWebApi, CloseWindowWebApi as CloseWindowWebApi, UtilWebApi as UtilWebApi
from web.web_client_api.vehicles import VehiclesWebApi as VehiclesWebApi
from web.web_client_api.arenas import ArenasWebApi as ArenasWebApi
from web.web_client_api.uilogging import UILoggingWebApi as UILoggingWebApi

class _OpenWindowWebApi(OpenWindowWebApi):
    __onBrowserOpen: Any
    __onBrowserClose: Any
    def __init__(self, onOpen=None, onClose=None):
        ...
    def _createHandlers(self):
        ...
    def _onBrowserOpen(self, alias):
        ...

class _CloseWindowWebApi(CloseWindowWebApi):
    __onBrowserClose: Any
    def __init__(self, close=None):
        ...
    def _onBrowserClose(self):
        ...

def _createOpenWindowWebApi(onBrowserOpen=None, onBrowserClose=None):
    ...
def _createCloseWindowWebApi(onBrowserClose=None):
    ...
def createStrongholdsWebHandlers(onBrowserOpen=None, onBrowserClose=None):
    ...
