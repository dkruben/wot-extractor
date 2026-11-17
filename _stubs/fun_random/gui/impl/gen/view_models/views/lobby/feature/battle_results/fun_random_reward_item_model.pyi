# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/battle_results/fun_random_reward_item_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.battle_results.reward_item_model import RewardItemModel as RewardItemModel

class FunRewardTypes(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTALS = 'crystal'
    XP = 'xp'
    FREE_XP = 'freeXP'
    TANKMEN_XP = 'tankmenXP'

class FunRandomRewardItemModel(RewardItemModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def _initialize(self):
        ...
