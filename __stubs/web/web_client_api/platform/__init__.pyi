# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/platform/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from web.web_client_api import w2capi as w2capi
from constants import WGC_PUBLICATION as WGC_PUBLICATION
from helpers import dependency as dependency
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from soft_exception import SoftException as SoftException
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema
from web.web_client_api.platform.china360 import China360PlatformWebApi as China360PlatformWebApi
from web.web_client_api.platform.steam import SteamPlatformWebApi as SteamPlatformWebApi
from web.web_client_api.platform.wg import WgPlatformWebApi as WgPlatformWebApi
from web.web_client_api.platform.base import IPlatformWebApi as IPlatformWebApi

# decorador original: @w2capi(...)
class PlatformWebApi(object):
    __slots__: tuple
    __loginManager: Any
    __mapping: Any
    def __init__(self):
        ...
    # decorador original: @w2c(...)
    def getType(self, _):
        ...
    # decorador original: @w2c(...)
    def isInited(self, _):
        ...
    # decorador original: @w2c(...)
    def isConnected(self, _):
        ...
    # decorador original: @w2c(...)
    def isOverlayEnabled(self, _):
        ...
    def __getApi(self):
        ...
