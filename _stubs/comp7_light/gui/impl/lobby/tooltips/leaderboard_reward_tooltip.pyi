# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/leaderboard_reward_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.gui.impl.gen.view_models.views.lobby.tooltips.leaderboard_reward_tooltip_model import LeaderboardRewardTooltipModel as LeaderboardRewardTooltipModel, State as State
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class LeaderboardRewardTooltipView(ViewImpl):
    __slots__: tuple
    __comp7LightController: Any
    __state: Any
    def __init__(self, state=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillViewModel(self):
        ...
