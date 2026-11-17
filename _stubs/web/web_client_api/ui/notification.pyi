# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/notification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
from gui.SystemMessages import SM_TYPE as SM_TYPE, pushI18nMessage as pushI18nMessage, pushMessage as pushMessage
from web.web_client_api import WebCommandException as WebCommandException, w2c as w2c, W2CSchema as W2CSchema, Field as Field

class _NotificationSchema(W2CSchema):
    __unions__: tuple
    type: Any
    message: Any
    message_data: Any
    i18n_key: Any
    i18n_data: Any
    key: Any
    def hasKey(self):
        ...
    def hasMessage(self):
        ...
    def hasI18nKey(self):
        ...

class NotificationWebApiMixin(object):
    # decorador original: @w2c(...)
    def notification(self, cmd):
        ...
