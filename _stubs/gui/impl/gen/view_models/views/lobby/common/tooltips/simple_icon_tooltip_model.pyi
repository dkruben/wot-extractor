# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/tooltips/simple_icon_tooltip_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class HeaderType(Enum):
    NORMAL = 'normal'
    ATTENTION = 'attention'
    ALERT = 'alert'
    BLOCKER = 'blocker'

class SimpleIconTooltipModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getIcon(self):
        ...
    def setIcon(self, value):
        ...
    def getHeader(self):
        ...
    def setHeader(self, value):
        ...
    def getBody(self):
        ...
    def setBody(self, value):
        ...
    def getHeaderType(self):
        ...
    def setHeaderType(self, value):
        ...
    def _initialize(self):
        ...
