# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/common/anomalies_view_mixin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from halloween.gui.impl.gen.view_models.views.common.anomaly_model import AnomalyModel as AnomalyModel, AnomalyState as AnomalyState, AnomalyType as AnomalyType
from halloween.gui.impl.gen.view_models.views.common.anomalies_matrix.recipe_model import RecipeModel as RecipeModel
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from helpers import dependency as dependency
from typing import Optional as Optional, Set as Set
from halloween.gui.impl.gen.view_models.views.common.anomalies_matrix.anomalies_matrix_model import AnomaliesMatrixModel as AnomaliesMatrixModel
from halloween.gui.game_control.halloween_anomalies_controller import RecipeData as RecipeData, AnomalyData as AnomalyData

class AnomaliesViewMixin(object):
    hwAnomaliesCtrl: Any
    def getAnomalyState(self, anomalyData):
        ...
    @property
    def knownAnomaliesIDs(self):
        ...
    def isAnomalyKnown(self, anomalyData):
        ...
    def refreshMatrix(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __createRecipeModel(self, recipeData):
        ...
    def __createAnomalyModel(self, anomaly=None, anomalyID=None):
        ...
