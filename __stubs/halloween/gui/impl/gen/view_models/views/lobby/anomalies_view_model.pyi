# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/anomalies_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from halloween.gui.impl.gen.view_models.views.common.anomalies_matrix.anomalies_matrix_model import AnomaliesMatrixModel as AnomaliesMatrixModel

class AnomaliesViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=2, commands=1):
        ...
    @property
    def matrix(self):
        ...
    @staticmethod
    def getMatrixType():
        ...
    def getSkinId(self):
        ...
    def setSkinId(self, value):
        ...
    def _initialize(self):
        ...
