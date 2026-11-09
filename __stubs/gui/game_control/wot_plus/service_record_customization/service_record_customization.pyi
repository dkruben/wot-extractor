# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus/service_record_customization/service_record_customization.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
import BigWorld as BigWorld
from gui.game_control.wot_plus.service_record_customization.cdn_cache import CdnResourcesCacheManager as CdnResourcesCacheManager
from gui.game_control.wot_plus.service_record_customization.local_fallback_cache import LocalResourceCacheManager as LocalResourceCacheManager
from gui.shared.gui_items.processors import Processor as Processor
from gui.shared.gui_items.processors.plugins import SyncValidator as SyncValidator, makeSuccess as makeSuccess, makeError as makeError
from gui.shared.utils.decorators import adisp_async as adisp_async
from helpers import dependency as dependency
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from web.cache.web_cache import CachePrefetchResult as CachePrefetchResult, CacheStates as CacheStates
from gui.shared.gui_items.processors.plugins import PluginResult as PluginResult
from typing import Optional as Optional, Callable as Callable, List as List
from gui.game_control.wot_plus.service_record_customization.models import BackgroundModel as BackgroundModel, RibbonModel as RibbonModel
_logger: Any

class _HasWotPlusValidator(SyncValidator):
    _wotPlusCtrl: Any
    def _validate(self):
        ...

class _IsSRCustomizationEnabledValidator(SyncValidator):
    _wotPlusCtrl: Any
    def _validate(self):
        ...

class _AssetExistenceValidator(SyncValidator):
    _optionsList: Any
    _option: Any
    def __init__(self, optionsList, option, isEnabled=True):
        ...
    def _validate(self):
        ...

class ServiceRecordProcessor(Processor):
    _wotPlusCtrl: Any
    _ribbonID: Any
    _backgroundID: Any
    def __init__(self, backgroundID, ribbonID):
        ...
    def _request(self, callback):
        ...

class ServiceRecordAssetManager(object):
    _cdnCache: Any
    _localCache: Any
    _currentCache: Any
    def __init__(self):
        ...
    def init(self, useCdnResourceCache=True, autoSync=True):
        ...
    def clear(self):
        ...
    def getBackground(self, id_):
        ...
    def getRibbon(self, id_):
        ...
    def getDownloadedRibbons(self):
        ...
    def getDownloadedBackgrounds(self):
        ...
    def getDownloadedBackgroundIDs(self):
        ...
    def getDownloadedRibbonIDs(self):
        ...
    def isSyncing(self):
        ...
    def isUsingOfflineMode(self):
        ...
    # decorador original: @adisp_async
    def sync(self, callback=None, timeout=None):
        ...
    def _onSyncFinished(self, callback, result):
        ...
