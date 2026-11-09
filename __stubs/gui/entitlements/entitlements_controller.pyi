# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/entitlements/entitlements_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from BWUtil import AsyncReturn as AsyncReturn
from Event import Event as Event
from adisp import adisp_process as adisp_process
from wg_async import wg_async as wg_async, await_callback as await_callback
from gui.entitlements.entitlement_common import ENTITLEMENTS as ENTITLEMENTS, iterConsumers as iterConsumers
from gui.entitlements.entitlement_model import AgateEntitlementsModel as AgateEntitlementsModel
from gui.wgcg.agate.contexts import InventoryEntitlementsCtx as InventoryEntitlementsCtx
from gui.wgcg.states import WebControllerStates as WebControllerStates
from helpers import dependency as dependency
from shared_utils import nextTick as nextTick
from skeletons.gui.game_control import IEntitlementsController as IEntitlementsController
from skeletons.gui.web import IWebController as IWebController
_logger: Any

class EntitlementsController(IEntitlementsController):
    __slots__: tuple
    __webController: Any
    __cache: Any
    __cacheWaitSync: Any
    __lastFailedEntitlements: Any
    onCacheUpdated: Any
    def __init__(self):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onLobbyInited(self, event):
        ...
    def fini(self):
        ...
    def isCacheInited(self):
        ...
    def getBalanceEntitlementFromCache(self, code):
        ...
    def getConsumedEntitlementFromCache(self, code):
        ...
    def getGrantedEntitlementFromCache(self, code):
        ...
    def updateCache(self, codes):
        ...
    def isCodesWasFailedInLastRequest(self, codes):
        ...
    # decorador original: @wg_async
    def forceUpdateCache(self, codes):
        ...
    # decorador original: @nextTick
    # decorador original: @adisp_process
    def __sendRequest(self, codes, callback):
        ...
    def __onResponse(self, *_):
        ...
