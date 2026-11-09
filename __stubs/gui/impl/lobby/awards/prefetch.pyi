# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/awards/prefetch.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.impl.lobby.awards import SupportedTokenTypes as SupportedTokenTypes
from helpers import dependency as dependency
from WebBrowser import getWebCache as getWebCache
from gui.impl.lobby.offers import getGfImagePath as getGfImagePath
from gui.wgnc.image_notification_helper import WebImageHelper as WebImageHelper
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache as IPurchaseCache
from gui.platform.catalog_service.controller import _PurchaseDescriptor as _PurchaseDescriptor
_LOCAL_FOLDER_NAME = 'multiple_awards'
_logger: Any
PREFETCHERS: dict

class _IPrefetcher(object):
    _productID: Any
    def __init__(self, productID):
        ...
    def prefetch(self, data):
        ...

class TokenDataPrefetcher(_IPrefetcher):
    __purchaseCache: Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def prefetch(self, bonus, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getImageData(self, tID, callback=None):
        ...
