# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/button_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class ButtonType(Enum):
    CREWOPERATIONS = 'crewOperations'
    CREWBOOKS = 'crewBooks'
    ACCELERATEDTRAINING = 'acceleratedTraining'
    WOTPLUS = 'wotPlus'

class ButtonModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=1, commands=0):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def _initialize(self):
        ...
