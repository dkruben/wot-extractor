# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/client_web_api/reactive_comm/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.game_control import IReactiveCommunicationService as IReactiveCommunicationService
from web.client_web_api.api import C2WHandler as C2WHandler, c2w as c2w

class ReactiveCommunicationEventHandler(C2WHandler):
    __service: Any
    @property
    def preventIdentical(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @c2w(...)
    def __onChannelMessage(self, name, message):
        ...
    # decorador original: @c2w(...)
    def __onSubscriptionClosed(self, subscription, reason):
        ...
