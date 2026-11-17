# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/cdn/models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from datetime import datetime as datetime
import typing as typing
from typing import Optional as Optional, Union as Union
import ResMgr as ResMgr
from dict2model.models import Model as BaseConfigModel
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.cdn.consts import MIN_SLIDES_COUNT_TO_VIEW as MIN_SLIDES_COUNT_TO_VIEW, SequenceCohorts as SequenceCohorts
from gui.game_loading.resources.consts import ImageVfxs as ImageVfxs
from gui.game_loading.resources.models import LocalImageModel as LocalImageModel
from helpers import getClientLanguage as getClientLanguage, time_utils as time_utils
from web.cache.web_cache import generateKey as generateKey
from gui.game_loading.resources.cdn.consts import SequenceOrders as SequenceOrders
from gui.game_loading.resources.cdn.cache import GameLoadingCdnCache as GameLoadingCdnCache
_logger: Any

class LocalSlideModel(LocalImageModel):
    __slots__: tuple
    _historyKey: Any
    def __init__(self, imageRelativePath, vfx=None, localizationText=None, descriptionText=None, minShowTimeSec=0, transition=0, imageAbsolutePath=None):
        ...
    @property
    def historyKey(self):
        ...
    @staticmethod
    def isDownloaded(*args):
        ...

class LocalSequenceModel(object):
    __slots__: tuple
    name: Any
    order: Any
    slides: Any
    def __init__(self, name, order, slides):
        ...
    @property
    def minSlidesCountToView(self):
        ...
    def __repr__(self):
        ...

class ConfigSlideModel(BaseConfigModel):
    __slots__: tuple
    image: Any
    vfx: Any
    localization: Any
    _imageCacheKey: Any
    _cacheKeysToUrls: Any
    _langCode: Any
    _localizationCacheKey: Any
    def __init__(self, image, vfx, localization):
        ...
    @property
    def historyKey(self):
        ...
    @property
    def urls(self):
        ...
    def isDownloaded(self, fileCache):
        ...
    def convertToLocal(self, fileCache, minShowTimeSec=0, transition=0):
        ...
    def __repr__(self):
        ...

class ConfigSequenceModel(BaseConfigModel):
    __slots__: tuple
    name: Any
    order: Any
    slides: Any
    start: Any
    finish: Any
    priority: Any
    views: Any
    enabled: Any
    cohorts: Any
    def __init__(self, name, order, slides, start, finish, priority, views, enabled, cohorts):
        ...
    @property
    def isActive(self):
        ...
    @property
    def minSlidesCountToView(self):
        ...
    def __repr__(self):
        ...

class ConfigModel(BaseConfigModel):
    __slots__: tuple
    sequences: Any
    enabled: Any
    def __init__(self, enabled, sequences):
        ...
    def __repr__(self):
        ...

class CdnCacheDefaultsModel(object):
    __slots__: tuple
    sequence: Any
    minShowTimeSec: Any
    transition: Any
    def __init__(self, sequence, minShowTimeSec=0, transition=0):
        ...
    def __repr__(self):
        ...

class CdnCacheParamsModel(object):
    __slots__: tuple
    configUrl: Any
    cohort: Any
    def __init__(self, configUrl=None, cohort=None):
        ...
    @property
    def isItemsCacheParamsReady(self):
        ...
    @property
    def isServerSettingsParamsReady(self):
        ...
    @property
    def isReady(self):
        ...
    def reset(self):
        ...
    def __repr__(self):
        ...
