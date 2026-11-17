# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/squad.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field
from web.web_client_api.common import SPA_ID_TYPES as SPA_ID_TYPES

class _CreateSquadSchema(W2CSchema):
    spa_id: Any

class SquadWebApiMixin(object):
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    # decorador original: @w2c(...)
    def createSquad(self, usersIds):
        ...
