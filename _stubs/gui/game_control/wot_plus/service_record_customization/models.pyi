# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus/service_record_customization/models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
import ResMgr as ResMgr
from dict2model import fields as fields, schemas as schemas, validate as validate
from dict2model.models import Model as Model
from gui.impl.lobby.offers import getGfImagePath as getGfImagePath
from helpers import getClientLanguage as getClientLanguage
from web.cache.web_cache import generateKey as generateKey
from typing import Any as Any, Dict as Dict, List as List, Optional as Optional
from web.cache.web_cache import BaseExternalCache as BaseExternalCache
_logger: _Any
backgroundSchema: _Any
ribbonUrlsSchema: _Any
ribbonSchema: _Any
configSchema: _Any
backgroundLocalSchema: _Any
ribbonUrlsLocalSchema: _Any
ribbonLocalSchema: _Any
localConfigSchema: _Any

class RibbonUrls(Model):
    __slots__: tuple
    base: _Any
    icon: _Any
    small: _Any
    large: _Any
    _fileCache: _Any
    _urlHashes: _Any
    def __init__(self, base, icon, small, large):
        ...
    def getBaseAsset(self):
        ...
    def getIconAsset(self):
        ...
    def getSmallAsset(self):
        ...
    def getLargeAsset(self):
        ...
    def isDownloaded(self):
        ...
    def setFileCache(self, fileCache):
        ...
    def _getGFPath(self, url):
        ...

class BackgroundModel(Model):
    __slots__: tuple
    id: _Any
    url: _Any
    localization: _Any
    name: _Any
    _langCode: _Any
    _localizationText: _Any
    _urlHash: _Any
    _fileCache: _Any
    def __init__(self, id, name, url, localization):
        ...
    def isDownloaded(self):
        ...
    def getAsset(self):
        ...
    def getLocalization(self):
        ...
    def setFileCache(self, fileCache):
        ...
    def _loadLocalizationText(self):
        ...

class RibbonModel(Model):
    __slots__: tuple
    id: _Any
    urls: _Any
    name: _Any
    _urls: _Any
    def __init__(self, id, name, urls):
        ...
    @property
    def allURLs(self):
        ...
    def isDownloaded(self):
        ...
    def setFileCache(self, fileCache):
        ...

class RibbonUrlsLocal(RibbonUrls):
    __slots__: tuple
    _fileCache: _Any
    _urlHashes: _Any
    def __init__(self, base, icon, small, large):
        ...
    def getBaseAsset(self):
        ...
    def getIconAsset(self):
        ...
    def getSmallAsset(self):
        ...
    def getLargeAsset(self):
        ...
    def isDownloaded(self):
        ...
    def setFileCache(self, fileCache):
        ...

class BackgroundModelLocal(BackgroundModel):
    __slots__: tuple
    _localizationText: _Any
    _urlHash: _Any
    def __init__(self, id, name, url, localization):
        ...
    def getAsset(self):
        ...
    def getLocalization(self):
        ...
    def isDownloaded(self):
        ...
    def setFileCache(self, fileCache):
        ...

class ConfigModel(Model):
    __slots__: tuple
    ribbons: _Any
    backgrounds: _Any
    _fileCache: _Any
    _ribbonURLs: _Any
    _backgroundIDsMap: _Any
    _ribbonsIDsMap: _Any
    def __init__(self, ribbons, backgrounds):
        ...
    @property
    def ribbonURLs(self):
        ...
    def getBackground(self, id_):
        ...
    def getRibbon(self, id_):
        ...
    def setFileCache(self, fileCache):
        ...
    def _setFileCacheForChildren(self, fileCache):
        ...

def createConfigModel(rawData):
    ...
def createLocalConfigModel(rawData):
    ...
