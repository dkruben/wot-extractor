# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_progression_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunProgressionWatcher as FunProgressionWatcher, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_progression_tooltip_view_model import FunRandomProgressionTooltipViewModel as FunRandomProgressionTooltipViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import packProgressionActiveStage as packProgressionActiveStage, packProgressionState as packProgressionState, packInfiniteProgressionState as packInfiniteProgressionState, packInfiniteProgressionStage as packInfiniteProgressionStage, packInfiniteProgressionConditions as packInfiniteProgressionConditions, packProgressionConditions as packProgressionConditions
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl

class FunRandomProgressionTooltipView(ViewImpl, FunAssetPacksMixin, FunProgressionWatcher, FunSubModesWatcher):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidateAll(self, *_):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidateTimer(self, *_):
        ...
