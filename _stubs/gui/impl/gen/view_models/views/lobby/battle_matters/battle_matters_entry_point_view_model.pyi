# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_entry_point_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel

class State(IntEnum):
    NORMAL = 0
    HASTOKEN = 1
    ERROR = 2

class BattleMattersEntryPointViewModel(ViewModel):
    __slots__: tuple
    onClick: Any
    def __init__(self, properties=5, commands=1):
        ...
    def getCurrentProgress(self):
        ...
    def setCurrentProgress(self, value):
        ...
    def getMaxProgress(self):
        ...
    def setMaxProgress(self, value):
        ...
    def getQuestNumber(self):
        ...
    def setQuestNumber(self, value):
        ...
    def getIsCompleted(self):
        ...
    def setIsCompleted(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
