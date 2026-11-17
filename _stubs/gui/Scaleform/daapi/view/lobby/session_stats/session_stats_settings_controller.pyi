# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/session_stats_settings_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import logging as logging
import Event as Event
from account_helpers.settings_core.settings_constants import SESSION_STATS as SESSION_STATS
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
MAX_STATS = 8
DEFAULT_CORE_SETTINGS: dict

class SessionStatsSettingsController(object):
    settingsCore: Any
    itemsCache: Any
    __cacheSettings: Any
    onSettingsUpdated: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def setSettings(self, settings):
        ...
    def setCurrentTab(self, currentTab):
        ...
    def getSettings(self):
        ...
    def setDefaultSettings(self):
        ...
    def getDefaultSettings(self):
        ...
    @staticmethod
    def validateSettings(settings):
        ...
    def __updateSettingsCache(self, reason, diff):
        ...
