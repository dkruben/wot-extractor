# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/catalog_service/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import listitems as listitems
import BigWorld as BigWorld
import adisp as adisp
from gui.macroses import getLanguageCode as getLanguageCode
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache as IPurchaseCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from web.cache.web_downloader import WebDownloader as WebDownloader
_logger: Any
_DEFAULT_SYNC_TIMEOUT = 180
_WORKERS_LIMIT = 2
TOKEN_ENTITLEMENT_PREFIX = 'token_'
_TokenDescriptor: Any
_DisplayWays: Any

class _ProductExtraData(object):
    _MAX_ORDER_INDEX = 10000
    _SPECIAL_CURRENCIES: dict
    _EXTRA_ENTITLEMENTS: tuple
    __items: Any
    def __init__(self, entitlements=None, currencies=None):
        ...
    def iterItems(self):
        ...
    def __addItem(self, incomeOrder, incomeItem):
        ...
    def __getField(self, target, key, default):
        ...

class _PurchaseDescriptor(object):
    __slots__: tuple
    __isEntitlementsInvalid: Any
    __entitlements: Any
    __metadataWot: Any
    __currencies: Any
    __titleID: Any
    __productName: Any
    __iconID: Any
    __mainAmount: Any
    __productExtraData: Any
    __tokens: Any
    __displayWays: Any
    def __init__(self, entitlements=None, currencies=None, metadataWot=None):
        ...
    def destroy(self):
        ...
    def getDisplayWays(self):
        ...
    def getExtraData(self):
        ...
    def getProductName(self):
        ...
    def getIconID(self):
        ...
    def getTitleID(self):
        ...
    def getMainAmount(self):
        ...
    def getEntitlements(self):
        ...
    def getTokenData(self, tID):
        ...
    def __getMetadataValueByName(self, name, default=None):
        ...
    def __getDataValueByName(self, name, targetSection, default=None):
        ...
    def __extractValue(self, section):
        ...
    def __getMetadataDisplayWays(self):
        ...

class _PurchasePackage(object):
    __descriptorUrl: Any
    __descriptor: Any
    __downloader: Any
    __pendingCallbacks: Any
    __timeoutBwCbId: Any
    def __init__(self, descriptorURL):
        ...
    def requestDescriptor(self, callback, timeout=...):
        ...
    def getDescriptor(self):
        ...
    def destroy(self):
        ...
    def _initDescriptor(self, dataDict):
        ...
    def __onDescriptorLoaded(self, url, data):
        ...
    def __notifyListeners(self):
        ...
    def __onTimeout(self):
        ...
    def __clearDownloader(self):
        ...
    def __clearTimeoutBwCbId(self):
        ...

class PurchaseCache(IPurchaseCache):
    __lobbyContext: Any
    __purchaseById: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @adisp.adisp_async
    def requestPurchaseByID(self, productCode, callback=None):
        ...
    def getCachedPurchase(self, productCode):
        ...
    def getProductCode(self, metaData):
        ...
    def canBeRequestedFromProduct(self, data):
        ...
    def __constructFullUrl(self, productCode):
        ...

def _getEmptyDescriptor():
    ...
