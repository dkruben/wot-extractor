# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import CUSTOM_SHOP_SETTINGS as CUSTOM_SHOP_SETTINGS
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, w2c as w2c

class _KeySchema(W2CSchema):
    key: Any

class _KeyValueSchema(_KeySchema):
    key: Any
    value: Any

class SettingsWebApiMixin(object):
    # decorador original: @w2c(...)
    def getSetting(self, cmd):
        ...
    # decorador original: @w2c(...)
    def setSetting(self, cmd):
        ...
    # decorador original: @w2c(...)
    def remove(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getSettings(self, _):
        ...
    # decorador original: @w2c(...)
    def clear(self, _):
        ...
