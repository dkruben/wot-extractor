# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_performance_analyzers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from gui.shared.utils.graphics import isLowPreset as isLowPreset

class PerformanceGroup(object):
    LOW_RISK = 0
    MEDIUM_RISK = 1
    HIGH_RISK = 2

class IPerformanceAlertHandler(object):
    def analyze(self):
        ...

class GraphicsPresetAnalyzerHandler(IPerformanceAlertHandler):
    __ALERT_LEVELS_KEYS: dict
    def analyze(self):
        ...

class RenderPipelineAnalyzerHandler(IPerformanceAlertHandler):
    def analyze(self):
        ...

class HighPerformanceGroupHandler(IPerformanceAlertHandler):
    def analyze(self):
        ...

class MediumPerformanceGroupHandler(IPerformanceAlertHandler):
    def analyze(self):
        ...
