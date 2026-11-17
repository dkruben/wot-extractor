# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/ranked_season_efficiency_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel

class RankedSeasonEfficiencyModel(ViewModel):
    __slots__: tuple
    PERIOD_PAST = 0
    PERIOD_CURRENT = 1
    PERIOD_FUTURE = 2
    EFFICIENCY_DEFAULT = 0
    EFFICIENCY_BEST = 1
    EFFICIENCY_OUT_OF_LEAGUE = 2
    WAITING_AWARDS = 3
    def __init__(self, properties=3, commands=0):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    def getPeriodState(self):
        ...
    def setPeriodState(self, value):
        ...
    def getEfficiencyState(self):
        ...
    def setEfficiencyState(self, value):
        ...
    def _initialize(self):
        ...
