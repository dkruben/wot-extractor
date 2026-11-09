# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/request/access_token.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.web import IWebController as IWebController
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field

class _RequestAccessTokenSchema(W2CSchema):
    force: Any

class AccessTokenWebApiMixin(object):
    _connectionMgr: Any
    _webCtrl: Any
    # decorador original: @w2c(...)
    def accessToken(self, cmd):
        ...
