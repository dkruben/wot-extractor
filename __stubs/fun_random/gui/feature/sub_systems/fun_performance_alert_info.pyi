# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_performance_alert_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from fun_random.gui.feature.sub_systems.fun_performance_analyzers import GraphicsPresetAnalyzerHandler as GraphicsPresetAnalyzerHandler, RenderPipelineAnalyzerHandler as RenderPipelineAnalyzerHandler, PerformanceGroup as PerformanceGroup, MediumPerformanceGroupHandler as MediumPerformanceGroupHandler, HighPerformanceGroupHandler as HighPerformanceGroupHandler
from fun_random_common.fun_constants import FunPerformanceParameter as FunPerformanceParameter
_logger: Any
_ALERT_HANDLERS: dict

class PerformanceAlertInfo(object):
    _DEFAULT_ALERT_GROUP = PerformanceGroup.LOW_RISK
    _performanceGroup: Any
    def __init__(self, alertType=None):
        ...
    @property
    def performanceGroup(self):
        ...
    def _analyzeClientSystem(self, alertType):
        ...
