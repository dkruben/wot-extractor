# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/tooltips/fort_rush_event_banner_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.gui.impl.gen.view_models.views.lobby.fort_rush_event_banner_view_model import FortRushEventBannerViewModel as FortRushEventBannerViewModel, State as State, PerformanceRiskEnum as PerformanceRiskEnum
from fort_rush.gui.impl.lobby.mode_selector.fort_rush_mode_selector_item import PERFORMANCE_MAP as PERFORMANCE_MAP
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency, time_utils as time_utils
_BANNER_STATE_TO_TOOLTIP_STATE: dict

class FortRushEventBannerTooltipView(ViewImpl):
    __frCtrl: Any
    __bannerState: Any
    def __init__(self, bannerState=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
