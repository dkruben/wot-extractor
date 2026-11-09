# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/user_subscriptions/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
from future.utils import listvalues as listvalues
from BWUtil import AsyncReturn as AsyncReturn
import wg_async as wg_async
from adisp import adisp_process as adisp_process
from gui.platform.products_fetcher.fetch_result import FetchResult as FetchResult
from gui.platform.products_fetcher.user_subscriptions.fetch_result import UserSubscriptionFetchResult as UserSubscriptionFetchResult
from gui.platform.products_fetcher.user_subscriptions.user_subscription import UserSubscription as UserSubscription, SubscriptionStatus as SubscriptionStatus
from gui.wgcg.utils.contexts import PlatformGetUserSubscriptionsCtx as PlatformGetUserSubscriptionsCtx
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.platform.product_fetch_controller import IUserSubscriptionsFetchController as IUserSubscriptionsFetchController
from skeletons.gui.web import IWebController as IWebController
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from gui.wgcg.web_controller import WebController as WebController
_logger: Any
__doc__: str

class PlatformGetUserSubscriptionsParams(object):
    status: Any
    def __init__(self):
        ...
    def __str__(self):
        ...

class UserSubscriptionsFetchController(IUserSubscriptionsFetchController):
    _webCtrl: Any
    _connectionMgr: Any
    _wotPlusCtrl: Any
    platformFetchCtx = PlatformGetUserSubscriptionsCtx
    _fetchResult: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @wg_async.wg_async
    def getSubscriptions(self, clearCache=False):
        ...
    # decorador original: @adisp_process
    def _requestSubscriptions(self, params, callback):
        ...
    def reset(self):
        ...
