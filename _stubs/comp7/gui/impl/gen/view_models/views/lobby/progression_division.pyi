# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/progression_division.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import Division as Division
from frameworks.wulf import ViewModel as ViewModel

class State(IntEnum):
    ACHIEVED = 0
    CURRENT = 1
    INACTIVE = 2

class ProgressionDivision(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getName(self):
        ...
    def setName(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
