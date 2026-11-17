# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/reactive_comm/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import listvalues as listvalues
from past.builtins import basestring as basestring
import adisp as adisp
import wg_async as wg_async
from gui.game_control.reactive_comm import Subscription as Subscription, SubscriptionClientStatus as SubscriptionClientStatus, SubscriptionServerStatus as SubscriptionServerStatus
from helpers import dependency as dependency
from skeletons.gui.game_control import IReactiveCommunicationService as IReactiveCommunicationService
from web.web_client_api import w2c as w2c, w2capi as w2capi, Field as Field, W2CSchema as W2CSchema

class _SubscriptionSchema(W2CSchema):
    channel_name: Any

# decorador original: @w2capi(...)
class ReactiveCommunicationWebApi(object):
    __service: Any
    __subscriptions: Any
    def __init__(self):
        ...
    # decorador original: @w2c(...)
    def isSubscriptionAvailable(self, _):
        ...
    # decorador original: @w2c(...)
    def subscribe(self, cmd):
        ...
    # decorador original: @w2c(...)
    def unsubscribe(self, cmd):
        ...
    def _finiSubscriptionsHandler(self):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @wg_async.wg_async
    def __doSubscribe(self, subscription, callback):
        ...
    def __onSubscriptionClosed(self, subscription, _):
        ...
