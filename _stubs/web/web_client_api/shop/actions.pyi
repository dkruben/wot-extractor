# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/actions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.store.actions_formatters import getAllActionsInfoIterator as getAllActionsInfoIterator
from helpers import dependency as dependency
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema
from skeletons.gui.server_events import IEventsCache as IEventsCache
from web.web_client_api.shop import formatters as formatters

class ActionsWebApiMixin(object):
    eventsCache: Any
    # decorador original: @w2c(...)
    def getActions(self, _):
        ...

def _filterActions(act):
    ...
