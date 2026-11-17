# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/postmorten_panel/rating_button_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen import R as R

class RateButtonEnum(Enum):
    WORSE = 'worse'
    USUAL = 'usual'
    BETTER = 'better'
    UNSET = 'unset'

class RatingButtonModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getButtonVariant(self):
        ...
    def setButtonVariant(self, value):
        ...
    def getFeedbackString(self):
        ...
    def setFeedbackString(self, value):
        ...
    def _initialize(self):
        ...
