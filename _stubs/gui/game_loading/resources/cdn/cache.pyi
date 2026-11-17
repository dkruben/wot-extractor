# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/cdn/cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import random as random
import itertools as itertools
import typing as typing
import urlparse as urlparse
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.cdn import history as history
from gui.game_loading.resources.cdn.consts import CDN_CACHE_SYNC_TIMEOUT as CDN_CACHE_SYNC_TIMEOUT, DOWNLOAD_SLIDES_MULTIPLAYER as DOWNLOAD_SLIDES_MULTIPLAYER, NEWBIES_BATTLES_LIMIT as NEWBIES_BATTLES_LIMIT, SequenceOrders as SequenceOrders, SequenceCohorts as SequenceCohorts
from gui.game_loading.resources.cdn.models import LocalSlideModel as LocalSlideModel, CdnCacheParamsModel as CdnCacheParamsModel
from gui.game_loading.resources.cdn.config import createConfigModel as createConfigModel
from PlayerEvents import g_playerEvents as playerEvents
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from web.cache.web_cache import BaseExternalCache as BaseExternalCache, BaseExternalCacheManager as BaseExternalCacheManager, createManifestRecord as createManifestRecord, CachePrefetchResult as CachePrefetchResult
from gui.game_loading.resources.cdn.types import SequenceType as SequenceType
from gui.game_loading.resources.cdn.models import CdnCacheDefaultsModel as CdnCacheDefaultsModel, ConfigSlideModel as ConfigSlideModel, ConfigSequenceModel as ConfigSequenceModel
_logger: Any

class GameLoadingCdnCache(BaseExternalCache):
    _CACHE_DIR_NAME = 'game_loading_cache'
    _RESOURCES_SUB_DIR_NAME = 'cdn'
    _WORKERS_LIMIT = 2
    _CONFIGS_DIR_NAME = None
    defaults: Any
    _EXTERNAL_CONFIG_URL: Any
    _historyDirPath: Any
    _cohort: Any
    _isLoaded: Any
    def __init__(self, defaults, externalConfigUrl=None, cohort=None):
        ...
    def load(self):
        ...
    def getLoaded(self):
        ...
    def nextSlide(self):
        ...
    @property
    def _history(self):
        ...
    def _selectSlideFromSequence(self, sequence):
        ...
    def _safeSelectSlideFromSequence(self, sequence):
        ...
    def _selectSlideFromDefaultSequence(self):
        ...
    def _createManifest(self, config=None):
        ...

class GameLoadingCdnCacheMgr(BaseExternalCacheManager):
    _REQUEST_TIMEOUT = CDN_CACHE_SYNC_TIMEOUT
    _DEFAULT_SYNC_TIMEOUT = _REQUEST_TIMEOUT
    _itemsCache: Any
    _lobbyCtx: Any
    _cacheParams: Any
    _downloadResult: Any
    _defaults: Any
    def __init__(self, defaults):
        ...
    def destroy(self):
        ...
    def stopSync(self, *args, **kwargs):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    def nextSlide(self):
        ...
    def _tryToDownload(self, *args, **kwargs):
        ...
    def _createCache(self):
        ...
    def _onSynced(self, result):
        ...
    def _onItemsCacheUpdated(self, *args, **kwargs):
        ...
    def _onServerSettingsChanged(self, *args, **kwargs):
        ...
    def _onServerSettingsUpdated(self, *args, **kwargs):
        ...
    def _getCohort(self):
        ...
    def _getExternalConfigUrl(self):
        ...
