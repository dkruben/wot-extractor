# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/navigation_bar_info_button.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class ButtonType(Enum):
    INFO = 'Info'
    QUESTION = 'Question'
    VIDEO = 'Video'
    DROP_LIST = 'Drop_List'

class NavigationBarInfoButton(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getLabel(self):
        ...
    def setLabel(self, value):
        ...
    def getTooltipHeader(self):
        ...
    def setTooltipHeader(self, value):
        ...
    def getTooltipBody(self):
        ...
    def setTooltipBody(self, value):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def _initialize(self):
        ...
