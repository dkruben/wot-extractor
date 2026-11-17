# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/waiting.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from gui.Scaleform.Waiting import Waiting as Waiting
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field

class _WaitingToggleControlSchema(W2CSchema):
    enabled: Any

class _WaitingToggleSchema(W2CSchema):
    show: Any

class _GlobalWaitingToggleSchema(W2CSchema):
    show: Any
    messageID: Any

class WaitingWebApiMixin(object):
    # decorador original: @w2c(...)
    def waitingToggleControl(self, cmd, ctx):
        ...
    # decorador original: @w2c(...)
    def waitingToggle(self, cmd, ctx):
        ...
    # decorador original: @w2c(...)
    def globalWaitingToggle(self, cmd):
        ...
