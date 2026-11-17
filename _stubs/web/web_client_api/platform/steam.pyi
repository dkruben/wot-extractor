# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/platform/steam.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import Steam as Steam
from constants import DISTRIBUTION_PLATFORM as DISTRIBUTION_PLATFORM
from web.web_client_api.platform.base import IPlatformWebApi as IPlatformWebApi
_logger: Any

class SteamPlatformWebApi(IPlatformWebApi):
    def getType(self):
        ...
    def isInited(self):
        ...
    def isConnected(self):
        ...
    @staticmethod
    def isOverlayEnabled():
        ...
