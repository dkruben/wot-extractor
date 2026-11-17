# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/offers/cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.moves.urllib import parse as parse
from future.utils import viewitems as viewitems
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from web.cache.web_cache import createManifestRecord as createManifestRecord, BaseExternalCache as BaseExternalCache, BaseExternalCacheManager as BaseExternalCacheManager
_logger: Any
_CDN_CACHE_DIR = 'offers_cache'
_CDN_WORKERS = 2

class ExternalCache(BaseExternalCache):
    _lobbyCtx: Any
    _offersProvider: Any
    _cdnRootUrl: Any
    def __init__(self, cacheName, workersLimit):
        ...
    def get(self, url, appName=None):
        ...
    def _createManifest(self, config=None):
        ...

class CdnResourcesCache(BaseExternalCacheManager):
    _REQUEST_TIMEOUT = 300.0
    _DEFAULT_SYNC_TIMEOUT = 180.0
    def _createCache(self):
        ...
