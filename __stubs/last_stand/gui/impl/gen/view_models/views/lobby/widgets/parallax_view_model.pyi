# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/parallax_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.parallax_model import ParallaxModel as ParallaxModel

class ParallaxViewModel(ViewModel):
    __slots__: tuple
    onSlide: Any
    def __init__(self, properties=2, commands=1):
        ...
    @property
    def parallax(self):
        ...
    @staticmethod
    def getParallaxType():
        ...
    def getIsParallaxEnabled(self):
        ...
    def setIsParallaxEnabled(self, value):
        ...
    def _initialize(self):
        ...
