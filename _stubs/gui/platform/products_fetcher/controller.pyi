# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from functools import partial as partial
import BigWorld as BigWorld
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
import wg_async as wg_async
from adisp import adisp_process as adisp_process
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.platform.products_fetcher.fetch_result import FetchResult as FetchResult
from gui.platform.products_fetcher.product_descriptor import ProductDescriptor as ProductDescriptor
from gui.wgcg.utils.contexts import PlatformFetchProductListCtx as PlatformFetchProductListCtx
from gui.wgcg.web_controller import WebController as WebController
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.platform.controller import IPlatformRequestController as IPlatformRequestController
from skeletons.gui.platform.product_fetch_controller import IProductFetchController as IProductFetchController
from skeletons.gui.web import IWebController as IWebController
from web.cache.web_downloader import WebDownloader as WebDownloader
from typing import List as List, Optional as Optional, Dict as Dict
_logger: Any

class _PlatformProductListParams(object):
    storefront = ''
    wgid = ''
    language = ''
    additional_data = ''
    country = ''
    response_fields: dict
    response_fields_profile = ''
    product_codes: list
    category = ''
    # decorador original: @wg_async.wg_async
    def setFields(self):
        ...
    # decorador original: @wg_async.wg_async
    def setCountry(self):
        ...
    def __repr__(self):
        ...

class ProductsDownloader(object):
    _DOWNLOAD_WORKERS_LIMIT = 2
    _TIMEOUT = 30
    _downloader: Any
    __downloadQueue: Any
    __onFinishCallback: Any
    __timeoutTimer: Any
    def __init__(self):
        ...
    def download(self, products, callback):
        ...
    def stop(self):
        ...
    def _onProductDownloaded(self, url, productData):
        ...
    @property
    def __isDownloadQueueEmpty(self):
        ...
    def __destroyTimer(self):
        ...
    def __onTimeoutTimer(self):
        ...

class FetchController(IPlatformRequestController):
    _connectionMgr: Any
    _downloader: Any
    _fetchResult: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    @property
    def _fetchResultType(self):
        ...
    def _onDisconnect(self):
        ...

class ProductsFetchController(FetchController, IProductFetchController):
    _webCtrl: Any
    platformParams = _PlatformProductListParams
    platformFetchCtx = PlatformFetchProductListCtx
    defaultProductDescriptor = ProductDescriptor
    productIDToDescriptor: dict
    dataGetKey = 'items'
    downloadRequired = True
    def reset(self):
        ...
    # decorador original: @wg_async.wg_async
    def getProducts(self, showWaiting=False, **kwargs):
        ...
    # decorador original: @adisp_process
    def _requestProducts(self, params, callback):
        ...
    def _createDescriptors(self, productsData):
        ...
