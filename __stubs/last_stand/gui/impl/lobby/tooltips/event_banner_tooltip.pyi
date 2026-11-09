# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/event_banner_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import PerformanceRiskEnum as PerformanceRiskEnum
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency, time_utils as time_utils
from last_stand.gui.impl.gen.view_models.views.lobby.event_banner_view_model import EventBannerViewModel as EventBannerViewModel
from last_stand.gui.shared.utils.performance_analyzer import PerformanceGroup as PerformanceGroup
from last_stand.skeletons.ls_controller import ILSController as ILSController
PERFORMANCE_MAP: dict

class EventBannerTooltipView(ViewImpl):
    lsCtrl: Any
    __slots__: tuple
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
