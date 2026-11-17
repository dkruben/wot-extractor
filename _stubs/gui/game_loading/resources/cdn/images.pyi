# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/cdn/images.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.base import BaseResources as BaseResources
from gui.game_loading.resources.cdn.models import LocalSlideModel as LocalSlideModel
from gui.game_loading.resources.cdn.cache import GameLoadingCdnCacheMgr as GameLoadingCdnCacheMgr
from gui.game_loading.resources.cdn.models import CdnCacheDefaultsModel as CdnCacheDefaultsModel
_logger: Any

class CdnImagesResources(BaseResources):
    __slots__: tuple
    _cdnCacheMgr: Any
    def __init__(self, defaults):
        ...
    def destroy(self):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    def get(self):
        ...
