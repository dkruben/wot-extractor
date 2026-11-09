# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/shared/hud_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class HudDisplay(Enum):
    ALL = 'all'
    NONE = 'none'

class HudViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=1, commands=0):
        ...
    def getDisplay(self):
        ...
    def setDisplay(self, value):
        ...
    def _initialize(self):
        ...
