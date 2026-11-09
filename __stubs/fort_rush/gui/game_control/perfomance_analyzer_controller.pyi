# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/game_control/perfomance_analyzer_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from backports.functools_lru_cache import lru_cache as lru_cache
from future.utils import viewitems as viewitems
from helpers import dependency as dependency
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
from helpers.statistics import HARDWARE_SCORE_PARAMS as HARDWARE_SCORE_PARAMS
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
PERFORMANCE_GROUP_LIMITS: dict

class LimitType(object):
    SYSTEM_DATA = 0
    HARDWARE_PARAMS = 1

class PerformanceGroup(object):
    HIGH_RISK = 1
    MEDIUM_RISK = 2
    LOW_RISK = 3
    PERFORMANCE_MAP: dict
    @staticmethod
    def getPerformanceRiskMap(risk):
        ...

class PerformanceAnalyzer(object):
    __settingsCore: Any
    # decorador original: @lru_cache(...)
    def getPerformanceGroup(self):
        ...
