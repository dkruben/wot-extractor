# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/login/social_networks/WebBridge.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import socket as socket
from urllib import urlencode as urlencode, quote_plus as quote_plus
import BigWorld as BigWorld
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from Event import Event as Event
from .DataServer import ThreadedDataServer as ThreadedDataServer, EncryptingThreadedDataServer as EncryptingThreadedDataServer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.Waiting import Waiting as Waiting
from helpers import dependency as dependency
from helpers import getLanguageCode as getLanguageCode
from py2to3.compat import base64compat as base64compat
from skeletons.connection_mgr import IConnectionManager as IConnectionManager

class _STATUS(object):
    OK = 0
    HTTP_SERVER_ERROR = 1
    WEB_BROWSER_ERROR = 2

class WebBridge(object):
    connectionMgr: Any
    __dataServer: Any
    __preferences: Any
    __loginParams: Any
    dataServerReceivedData: Any
    def __init__(self, preferences):
        ...
    def fini(self):
        ...
    def initiateLogin(self, loginParams, isExternal, isRegistration):
        ...
    def __onDataServerReceivedData(self, token, spaID, socialNetwork):
        ...
    def __getWgniParams(self, isExternal, isRegistration):
        ...
    @staticmethod
    def __getWgniBaseURL(isRegistration=False):
        ...
    def __initDataServer(self, enableEncryption):
        ...
    def __finiDataServer(self, *args, **kwargs):
        ...
