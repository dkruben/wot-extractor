# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/platform/steam.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import Steam as Steam
from helpers.platform.base import BasePublishPlatform as BasePublishPlatform
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Literal as Literal
_logger: Any

class SteamPublishPlatform(BasePublishPlatform):
    def init(self):
        ...
    def fini(self):
        ...
    def isInited(self):
        ...
    def isConnected(self):
        ...
    def __onMicroTxnAuthorizationResponse(self, _, orderID, authorized):
        ...
    def __onGameOverlayActivated(self, active):
        ...
