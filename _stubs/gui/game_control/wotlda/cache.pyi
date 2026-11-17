# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wotlda/cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import os as os
import logging as logging
from typing import Dict as Dict, Any as Any
from helpers.local_cache import FileLocalCache as FileLocalCache
from gui.game_control.wotlda.constants import LAST_UPDATE_TIMESTAMP as LAST_UPDATE_TIMESTAMP, SupportedWTRRange as SupportedWTRRange
_logger: _Any

class WotldaCache(FileLocalCache):
    _CACHE_TYPE = ''
    _filePath: _Any
    _cache: _Any
    def __init__(self):
        ...
    def update(self, data):
        ...
    def clear(self):
        ...
    def getUpdatedAtTimestamp(self):
        ...
    def isCacheEmpty(self):
        ...
    def clearCache(self):
        ...
    def getLoadout(self, vehicleID, *args, **kwargs):
        ...
    def deleteCacheFile(self):
        ...
    def _getCache(self):
        ...
    def _setCache(self, data):
        ...

class EasyTankEquipCache(WotldaCache):
    _CACHE_TYPE = 'easy_tank_equip'
    def getLoadout(self, vehicleID, *args, **kwargs):
        ...

class EquipmentForSubscribersCache(WotldaCache):
    _CACHE_TYPE = 'subscription'
    def getLoadout(self, vehicleID, *args, **kwargs):
        ...

class CrewCache(WotldaCache):
    _CACHE_TYPE = 'crew'
    def getLoadout(self, vehicleID, *args, **kwargs):
        ...
