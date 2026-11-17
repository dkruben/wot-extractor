# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/event_banner_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class PerformanceRiskEnum(Enum):
    LOWRISK = 'lowRisk'
    MEDIUMRISK = 'mediumRisk'
    HIGHRISK = 'highRisk'

class EventBannerViewModel(ViewModel):
    __slots__: tuple
    onClick: Any
    def __init__(self, properties=3, commands=1):
        ...
    def getDate(self):
        ...
    def setDate(self, value):
        ...
    def getEndDate(self):
        ...
    def setEndDate(self, value):
        ...
    def getPerformanceRisk(self):
        ...
    def setPerformanceRisk(self, value):
        ...
    def _initialize(self):
        ...
