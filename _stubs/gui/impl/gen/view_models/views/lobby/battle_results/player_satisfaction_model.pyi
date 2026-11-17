# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/player_satisfaction_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class PlayerSatisfactionStates(Enum):
    NONE = 'none'
    WORSE = 'worse'
    USUAL = 'usual'
    BETTER = 'better'

class PlayerSatisfactionModel(ViewModel):
    __slots__: tuple
    onSatisfactionRatingSelected: Any
    def __init__(self, properties=2, commands=1):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getIsPlayerSatisfactionInterfaceEnabled(self):
        ...
    def setIsPlayerSatisfactionInterfaceEnabled(self, value):
        ...
    def _initialize(self):
        ...
