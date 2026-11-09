# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/uilogging/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from helpers import dependency as dependency
from skeletons.ui_logging import IUILoggingCore as IUILoggingCore
from uilogging.constants import LogLevels as LogLevels
from web.web_client_api import w2c as w2c, w2capi as w2capi, W2CSchema as W2CSchema, Field as Field

class _UILoggingLogSchema(W2CSchema):
    feature: Any
    group: Any
    log_action: Any
    log_level: Any
    params: Any

# decorador original: @w2capi(...)
class UILoggingWebApi(object):
    _logger: Any
    # decorador original: @w2c(...)
    def log(self, cmd):
        ...
