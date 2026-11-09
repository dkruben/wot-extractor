# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/random/random_reward_item_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.battle_results.reward_item_model import RewardItemModel as RewardItemModel

class RandomRewardTypes(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTALS = 'crystal'
    XP = 'xp'

class RandomRewardItemModel(RewardItemModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def _initialize(self):
        ...
