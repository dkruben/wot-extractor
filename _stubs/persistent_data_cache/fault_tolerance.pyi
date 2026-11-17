# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/persistent_data_cache/fault_tolerance.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import base64_utils as base64_utils
from persistent_data_cache_common.common import getLogger as getLogger
from ResMgr import DataSection as DataSection
from persistent_data_cache_common.types import TPDCVersion as TPDCVersion
_logger: Any
_PREFS_NAME = 'pdcFaultTolerance'
_VERSION_KEY = 'version'
_FAILED_TO_LOAD_COUNT_KEY = 'failedToLoadCount'
_FAILED_TO_SAVE_COUNT_KEY = 'failedToSaveCount'
_FAILED_TO_LOAD_COUNT_LIMIT = 5
_FAILED_TO_SAVE_COUNT_LIMIT = 5
_g_faultTolerance = None

class FaultTolerance(object):
    __slots__: tuple
    _version: Any
    _userPrefs: Any
    _data: Any
    _modified: Any
    def __init__(self, version, userPrefs):
        ...
    def isLimitsReached(self):
        ...
    def increaseFailedToLoadCount(self, error):
        ...
    def resetFailedToLoadCount(self):
        ...
    def increaseFailedToSaveCount(self, error):
        ...
    def resetFailedToSaveCount(self):
        ...
    def fini(self):
        ...
    def _resetCount(self, key):
        ...
    def _increaseCount(self, key):
        ...

def _loadData(version, userPrefs):
    ...
def init(version, userPrefs):
    ...
def fini():
    ...
