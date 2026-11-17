# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/shared/utils/performance_analyzer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from enum import IntEnum as IntEnum
from helpers.statistics import HARDWARE_SCORE_PARAMS as HARDWARE_SCORE_PARAMS
import BigWorld as BigWorld
from gui.shared.utils.graphics import getGraphicsEngineValue as getGraphicsEngineValue
from typing import Optional as Optional, Dict as Dict
_logger: Any
DEFAULT_PERFORMANCE_GROUP_LIMITS: dict

class LimitType(IntEnum):
    SYSTEM_DATA = 0
    HARDWARE_PARAMS = 1

class PerformanceGroup(object):
    LOW_RISK = 0
    MEDIUM_RISK = 1
    HIGH_RISK = 2

class PerformanceAnalyzerMixin(object):
    __performanceGroup = None
    __lastLimitMap: Any
    def __init__(self, *args, **kwargs):
        ...
    def getPerformanceGroup(self, groupLimitMap=None, defaultGroup=...):
        ...
    def __analyzeClientSystem(self, groupLimitMap, defaultGroup):
        ...
