# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/common/anomalies_matrix/anomalies_matrix_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from halloween.gui.impl.gen.view_models.views.common.anomalies_matrix.recipe_model import RecipeModel as RecipeModel
from halloween.gui.impl.gen.view_models.views.common.anomaly_model import AnomalyModel as AnomalyModel

class AnomaliesMatrixModel(ViewModel):
    __slots__: tuple
    onAnomalyAcknowledged: Any
    onAnomalyClick: Any
    def __init__(self, properties=2, commands=2):
        ...
    def getRecipesList(self):
        ...
    def setRecipesList(self, value):
        ...
    @staticmethod
    def getRecipesListType():
        ...
    def getIndividualAnomaliesList(self):
        ...
    def setIndividualAnomaliesList(self, value):
        ...
    @staticmethod
    def getIndividualAnomaliesListType():
        ...
    def _initialize(self):
        ...
