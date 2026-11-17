# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/IntSettingsRequester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from copy import copy as copy
from future.utils import viewitems as viewitems
from functools import wraps as wraps
from account_helpers.AccountSettings import MAPBOX_CAROUSEL_FILTER_1 as MAPBOX_CAROUSEL_FILTER_1, MAPBOX_CAROUSEL_FILTER_2 as MAPBOX_CAROUSEL_FILTER_2, FUN_RANDOM_CAROUSEL_FILTER_1 as FUN_RANDOM_CAROUSEL_FILTER_1, FUN_RANDOM_CAROUSEL_FILTER_2 as FUN_RANDOM_CAROUSEL_FILTER_2, COMP7_CAROUSEL_FILTER_1 as COMP7_CAROUSEL_FILTER_1, COMP7_CAROUSEL_FILTER_2 as COMP7_CAROUSEL_FILTER_2, CAROUSEL_FILTER_3 as CAROUSEL_FILTER_3, RANKED_CAROUSEL_FILTER_3 as RANKED_CAROUSEL_FILTER_3, EPICBATTLE_CAROUSEL_FILTER_3 as EPICBATTLE_CAROUSEL_FILTER_3, MAPBOX_CAROUSEL_FILTER_3 as MAPBOX_CAROUSEL_FILTER_3, COMP7_CAROUSEL_FILTER_3 as COMP7_CAROUSEL_FILTER_3, FUN_RANDOM_CAROUSEL_FILTER_3 as FUN_RANDOM_CAROUSEL_FILTER_3, COMP7_LIGHT_CAROUSEL_FILTER_1 as COMP7_LIGHT_CAROUSEL_FILTER_1, COMP7_LIGHT_CAROUSEL_FILTER_2 as COMP7_LIGHT_CAROUSEL_FILTER_2, COMP7_LIGHT_CAROUSEL_FILTER_3 as COMP7_LIGHT_CAROUSEL_FILTER_3, HOLIDAY_OPS as HOLIDAY_OPS, PERSONAL_MISSION_4 as PERSONAL_MISSION_4
import BigWorld as BigWorld
import constants as constants
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.shared.utils import code2str as code2str
_logger: Any

class IntSettingsRequester(object):
    __SETTINGS: dict
    __isSynced: Any
    __cache: Any
    def __init__(self):
        ...
    def isSynced(self):
        ...
    def clear(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def request(self, callback=None):
        ...
    def getCacheValue(self, key, defaultValue=None):
        ...
    # decorador original: @requireSync
    # decorador original: @adisp_process
    def setSetting(self, key, value):
        ...
    # decorador original: @requireSync
    # decorador original: @adisp_process
    def setSettings(self, settings):
        ...
    # decorador original: @requireSync
    def getSetting(self, key, defaultValue=None):
        ...
    # decorador original: @requireSync
    # decorador original: @adisp_process
    def delSettings(self, settings):
        ...
    def _response(self, resID, value, callback):
        ...
    # decorador original: @adisp_async
    def _requestCache(self, callback=None):
        ...
    # decorador original: @adisp_async
    def _addIntSettings(self, settings, callback=None):
        ...
    # decorador original: @adisp_async
    def _delIntSettings(self, settings, callback=None):
        ...

def requireSync(func):
    ...
