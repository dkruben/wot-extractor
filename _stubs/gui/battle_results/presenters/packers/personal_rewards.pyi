# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/personal_rewards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker as IBattleResultsPacker
from gui.battle_results.pbs_helpers.economics import hasAogasFine as hasAogasFine
from gui.impl.gen.view_models.views.lobby.battle_results.reward_item_model import RewardItemModel as RewardItemModel

class PersonalRewards(IBattleResultsPacker):
    _AVAILABLE_REWARDS: list
    _ITEM_MODEL_CLS = RewardItemModel
    _REWARD_GETTERS: dict
    _REWARDS_TO_CONDITION_MAP: dict
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def _getAllRewardValues(cls, reusable):
        ...
    @classmethod
    def _getShownRewards(cls, battleResults):
        ...
    @classmethod
    def _hasFines(cls, battleResults):
        ...
