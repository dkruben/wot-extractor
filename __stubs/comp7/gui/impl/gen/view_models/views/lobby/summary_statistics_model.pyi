# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/summary_statistics_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class SummaryStatisticsType(Enum):
    BATTLES = 'battles'
    DAMAGE = 'damage'
    MAXPRESTIGEPOINTS = 'maxPrestigePoints'
    MAXFRAGS = 'maxFrags'
    WINSERIES = 'winSeries'

class SummaryStatisticsModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getMain(self):
        ...
    def setMain(self, value):
        ...
    def getAdditional(self):
        ...
    def setAdditional(self, value):
        ...
    def _initialize(self):
        ...
