# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/winback/tooltips/selected_rewards_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes as BlueprintBonusTypes
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.winback.tooltips.selected_rewards_tooltip_model import SelectedRewardsTooltipModel as SelectedRewardsTooltipModel
from gui.impl.gen.view_models.views.lobby.winback.winback_reward_view_model import RewardName as RewardName
from gui.impl.lobby.winback.winback_helpers import getDiscountFromGoody as getDiscountFromGoody, getDiscountFromBlueprint as getDiscountFromBlueprint
from gui.impl.pub import ViewImpl as ViewImpl

class SelectedRewardsTooltip(ViewImpl):
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, selectedRewards):
        ...
