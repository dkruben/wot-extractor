# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/collection/resources/cdn/models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from enum import Enum as Enum, unique as unique
from dict2model.models import Model as Model
from gui.impl.utils.path import normalizeGfImagePath as normalizeGfImagePath
from web.cache.web_cache import generateKey as generateKey
from typing import List as List
from gui.collection.resources.cdn.cache import CollectionsCdnCache as CollectionsCdnCache

# decorador original: @unique
class Group(str, Enum):
    ITEM = 'items'
    BG = 'backgrounds'

# decorador original: @unique
class Sub(str, Enum):
    ICON = '48x48'
    SMALLEST = '232x174'
    SMALL = '296x222'
    MEDIUM = '400x300'
    LARGE = '600x450'
    LARGEST = '1000x680'
    RECEIVED = 'received'
    UNRECEIVED = 'unreceived'
    BP_10 = 'battle_pass_10'
    BP_11 = 'battle_pass_11'
    BP_12 = 'battle_pass_12'

class ImageModel(Model):
    __slots__: tuple
    group: Any
    sub: Any
    name: Any
    url: Any
    __id: Any
    __imageCacheKey: Any
    def __init__(self, group, sub, name, url=None):
        ...
    @property
    def id(self):
        ...
    def isDownloaded(self, fileCache):
        ...
    def getGFPath(self, fileCache):
        ...
    def __repr__(self):
        ...

class ConfigModel(Model):
    __slots__: tuple
    images: Any
    def __init__(self, images):
        ...
    def __repr__(self):
        ...

class CdnCacheParamsModel(object):
    __slots__: tuple
    configUrl: Any
    def __init__(self, configUrl=None):
        ...
    @property
    def isReady(self):
        ...
    def reset(self):
        ...
    def __repr__(self):
        ...

def makeImageID(group, sub, name):
    ...
