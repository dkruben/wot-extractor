# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/seniority_awards/seniority_awards_bonuses_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel as TokenBonusModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel as RewardItemModel
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN
from gui.server_events.bonuses import TokensBonus as TokensBonus
from gui.shared.missions.packers.bonus import TokenBonusUIPacker as TokenBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, BonusUIPacker as BonusUIPacker, CustomizationBonusUIPacker as CustomizationBonusUIPacker

class _SeniorityAwardsTokenBonusUIPacker(TokenBonusUIPacker):
    @classmethod
    def _packToken(cls, bonusPacker, bonus, *args):
        ...
    @classmethod
    def _getTokenBonusPackers(cls):
        ...
    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        ...

class _SeniorityAwardsCustomizationBonusUIPacker(CustomizationBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

def getSeniorityAwardsBonusPacker():
    ...
