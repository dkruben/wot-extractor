# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/shop/telecom_rentals.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from telecom_rentals_common import PARTNERSHIP_TOKEN_NAME as PARTNERSHIP_TOKEN_NAME, TELECOM_RENTALS_CONFIG as TELECOM_RENTALS_CONFIG, PARTNERSHIP_BLOCKED_TOKEN_NAME as PARTNERSHIP_BLOCKED_TOKEN_NAME
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w

class TelecomTokenEventHandler(C2WHandler):
    _lobbyContext: Any
    def init(self):
        ...
    def fini(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __onTokensUpdate(self, diff):
        ...
    # decorador original: @c2w(...)
    def __sendNotify(self):
        ...
