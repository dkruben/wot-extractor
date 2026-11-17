# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/reward_item_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class RewardTypes(Enum):
    CREDITS = 'credits'
    CRYSTALS = 'crystal'
    XP = 'xp'

class RewardItemModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    def _initialize(self):
        ...
