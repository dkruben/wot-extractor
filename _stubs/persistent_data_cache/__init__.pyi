# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/persistent_data_cache/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
import typing as typing
import BigWorld as BigWorld
import constants as constants
from helpers import ExitCode as ExitCode
from persistent_data_cache import configs as configs
from persistent_data_cache import fault_tolerance as fault_tolerance
from persistent_data_cache.caches import ThreadSavingPDCache as ThreadSavingPDCache
from persistent_data_cache.manager import ClientForceCreatingPDCManager as ClientForceCreatingPDCManager
from persistent_data_cache.version import getClientPDCVersion as getClientPDCVersion
from persistent_data_cache_common import load as load, start as start, save as save, fini as commonFini, init as commonInit
from persistent_data_cache_common.caches import DefaultPDCache as DefaultPDCache
from persistent_data_cache_common.manager import DefaultPDCManager as DefaultPDCManager
from persistent_data_cache_common.common import getLogger as getLogger
from persistent_data_cache_common.configs import BasePDCConfig as BasePDCConfig
from persistent_data_cache_common.events import DefaultPDCEventsDispatcher as DefaultPDCEventsDispatcher
from ResMgr import DataSection as DataSection
from gui.game_loading import loading as gameLoading
_logger: Any
PDC_CREATE_ARG = 'pdcCreate'
PDC_OFF_ARG = 'pdcOff'
PDC_CACHE_FILE_PATH = './data.wgpdc'
_eventDispatcher = None
__all__: list

def getEventsDispatcher():
    ...
def getForceCreatingParam():
    ...
def hasPDCOffParam():
    ...
def init(scriptsConfig, engineConfig, userPreferences, gameLoadingStep):
    ...
def fini():
    ...
