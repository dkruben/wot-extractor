# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/difficulty_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel as DifficultyItemModel

class DifficultyViewModel(ViewModel):
    __slots__: tuple
    onSwitchLevel: Any
    def __init__(self, properties=3, commands=1):
        ...
    def getDifficulties(self):
        ...
    def setDifficulties(self, value):
        ...
    @staticmethod
    def getDifficultiesType():
        ...
    def getIsDisabled(self):
        ...
    def setIsDisabled(self, value):
        ...
    def getIsSearchingPlatoon(self):
        ...
    def setIsSearchingPlatoon(self, value):
        ...
    def _initialize(self):
        ...
