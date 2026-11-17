# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/mode_performance_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class PerformanceRiskEnum(Enum):
    LOWRISK = 'lowRisk'
    MEDIUMRISK = 'mediumRisk'
    HIGHRISK = 'highRisk'

class ModePerformanceModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getShowPerfRisk(self):
        ...
    def setShowPerfRisk(self, value):
        ...
    def getPerformanceRisk(self):
        ...
    def setPerformanceRisk(self, value):
        ...
    def _initialize(self):
        ...
