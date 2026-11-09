# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_entry_point_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from fun_random.gui.feature.fun_constants import FunSubModesState as FunSubModesState
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_entry_point_tooltip_view_model import FunRandomEntryPointTooltipViewModel as FunRandomEntryPointTooltipViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import packPerformanceAlertInfo as packPerformanceAlertInfo, getFunRandomEventState as getFunRandomEventState
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R
from helpers import time_utils as time_utils

class FunRandomEntryPointTooltipView(ViewImpl, FunAssetPacksMixin, FunSubModesWatcher):
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
