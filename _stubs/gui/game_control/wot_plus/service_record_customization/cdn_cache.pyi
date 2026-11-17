# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus/service_record_customization/cdn_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import os as os
import typing as typing
from future.moves.urllib import parse as urlparse
from future.utils import viewitems as viewitems
import ResMgr as ResMgr
from gui.game_control.wot_plus.service_record_customization import _updateConfig as _updateConfig, getConfig as getConfig, IResourceCacheManager as IResourceCacheManager
from helpers import dependency as dependency, getClientLanguage as getClientLanguage
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from web.cache.web_cache import BaseExternalCache as BaseExternalCache, CachePrefetchResult as CachePrefetchResult, createManifestRecord as createManifestRecord, BaseExternalCacheManager as BaseExternalCacheManager
from typing import Any as Any, Optional as Optional, List as List, Dict as Dict, Tuple as Tuple
from gui.game_control.wot_plus.service_record_customization.models import ConfigModel as ConfigModel, RibbonModel as RibbonModel, BackgroundModel as BackgroundModel
_logger: _Any

class ServiceRecordCustomizationCache(BaseExternalCache):
    _lobbyCtx: _Any
    _langCode: _Any
    _CONFIGS_DIR_NAME = 'config'
    _EXTERNAL_CONFIG_URL: _Any
    def __init__(self, cacheName, workersLimit):
        ...
    def _processFailedManifest(self):
        ...
    def _onManifestDownloadFailed(self):
        ...
    def _onManifestParsingFailed(self):
        ...
    def _getHostAndPathFromURL(self, url):
        ...
    def _restoreManifestFromLocalConfig(self):
        ...
    def _createManifest(self, config=None):
        ...

class CdnResourcesCacheManager(BaseExternalCacheManager, IResourceCacheManager):
    _REQUEST_TIMEOUT = 60
    _CDN_WORKERS = 2
    _CDN_CACHE_DIR = 'service_record_cache'
    def getRibbons(self):
        ...
    def getBackgrounds(self):
        ...
    def getDownloadedBackgrounds(self):
        ...
    def getDownloadedRibbons(self):
        ...
    def getDownloadedBackgroundIDs(self):
        ...
    def getDownloadedRibbonIDs(self):
        ...
    def getConfigModel(self):
        ...
    def isCacheReady(self):
        ...
    def getBackground(self, id_):
        ...
    def getRibbon(self, id_):
        ...
    def registerCaller(self, caller, timeout):
        ...
    def _createCache(self):
        ...
