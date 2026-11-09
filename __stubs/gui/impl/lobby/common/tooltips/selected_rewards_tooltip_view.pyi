# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/tooltips/selected_rewards_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_category_model import SelectedRewardsTooltipCategoryModel as SelectedRewardsTooltipCategoryModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_reward_model import SelectedRewardsTooltipRewardModel as SelectedRewardsTooltipRewardModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_view_model import SelectedRewardsTooltipViewModel as SelectedRewardsTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl

class SelectedRewardsTooltipView(ViewImpl):
    __slots__: tuple
    __cart: Any
    __count: Any
    def __init__(self, cart, count):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
