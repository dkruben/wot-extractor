# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/reward_selection_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.reward_view_model import RewardViewModel as RewardViewModel

class GenderEnum(Enum):
    MALE = 'male'
    FEMALE = 'female'

class RewardSelectionViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onClaim: Any
    def __init__(self, properties=3, commands=2):
        ...
    def getMaxCertificates(self):
        ...
    def setMaxCertificates(self, value):
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def getGender(self):
        ...
    def setGender(self, value):
        ...
    def _initialize(self):
        ...
