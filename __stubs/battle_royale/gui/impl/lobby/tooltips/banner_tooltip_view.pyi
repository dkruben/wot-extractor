# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/banner_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.constants import BattleRoyalePerfProblems as BattleRoyalePerfProblems, BattleRoyaleModeState as BattleRoyaleModeState
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.banner_tooltip_view_model import BannerTooltipViewModel as BannerTooltipViewModel, PerformanceRisk as PerformanceRisk
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
PERFORMANCE_RISK_MAPPING: dict

class BannerTooltipView(ViewImpl):
    __battleController: Any
    __modeState: Any
    def __init__(self, modeState, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
