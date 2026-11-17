# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/hubs/base/gifter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import isLongDisconnectedFromCenter as isLongDisconnectedFromCenter
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.gift_system.constants import GifterResponseState as GifterResponseState
from gui.gift_system.hubs.subsystems import BaseHubSubsystem as BaseHubSubsystem
from gui.wgcg.gift_system.contexts import GiftSystemSendGiftCtx as GiftSystemSendGiftCtx
from helpers import dependency as dependency
from skeletons.gui.web import IWebController as IWebController
from helpers.server_settings import GiftEventConfig as GiftEventConfig

class IGiftEventGifter(BaseHubSubsystem):
    def getActiveRequest(self):
        ...
    def getRequestRestriction(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def sendGift(self, entitlementCode, receiverID, metaInfo, callback):
        ...

class GiftEventBaseGifter(IGiftEventGifter):
    __slots__: tuple
    __webController: Any
    __responseCallback: Any
    __requestCtx: Any
    def __init__(self, eventSettings, responseCallback):
        ...
    def destroy(self):
        ...
    def getActiveRequest(self):
        ...
    def getRequestRestriction(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def sendGift(self, entitlementCode, receiverID, metaInfo, callback=None):
        ...
    def _isRequestsEnabled(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __doExternalRequest(self, requestCtx, callback):
        ...
