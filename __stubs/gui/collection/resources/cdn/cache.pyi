# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/collection/resources/cdn/cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import urlparse as urlparse
import typing as typing
import BigWorld as BigWorld
from gui.collection import loggers as loggers
from gui.collection.resources.cdn.config import createConfigModel as createConfigModel
from gui.collection.resources.cdn.models import CdnCacheParamsModel as CdnCacheParamsModel, ImageModel as ImageModel
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from web.cache.web_cache import BaseExternalCache as BaseExternalCache, BaseExternalCacheManager as BaseExternalCacheManager, CachePrefetchResult as CachePrefetchResult, CacheStates as CacheStates, createManifestRecord as createManifestRecord
from typing import Any as Any, Dict as Dict, List as List, Optional as Optional, Union as Union
from gui.collection.resources.cdn.models import ConfigModel as ConfigModel
_logger: _Any
_g_config = None

class CollectionsCdnCache(BaseExternalCache):
    __collectionsSystem: _Any
    __CDN_CACHE_DIR = 'collections_cache'
    __CDN_WORKERS = 16
    _EXTERNAL_CONFIG_URL: _Any
    __toDownloadImages: _Any
    _state: _Any
    _timeoutTimerID: _Any
    def __init__(self, externalConfigUrl, toDownloadImages):
        ...
    def getImages(self, imagesIDs):
        ...
    def _startSync(self, timeout=0.0):
        ...
    def _prepareToUpdate(self, config=None, manifest=None):
        ...
    def _createManifest(self, config=None):
        ...

class CollectionsCdnCacheMgr(BaseExternalCacheManager):
    __lobbyCtx: _Any
    _REQUEST_TIMEOUT = 30.0
    _DEFAULT_SYNC_TIMEOUT = 1200.0
    _cache: _Any
    _downloadResult: _Any
    __cacheParams: _Any
    __toDownloadImages: _Any
    def __init__(self):
        ...
    def startSync(self, *args, **kwargs):
        ...
    def stopSync(self, *args, **kwargs):
        ...
    def _createCache(self):
        ...
    def getImagesPaths(self, imagesIDs, callback=None):
        ...
    def __packImages(self, images):
        ...
    def __onServerSettingsChanged(self, *args, **kwargs):
        ...
    def __update(self):
        ...
    def __getExternalConfigUrl(self):
        ...
    def __tryToDownload(self):
        ...
    def __onSynced(self, result):
        ...

def _getConfig():
    ...
def _updateConfig(config):
    ...
