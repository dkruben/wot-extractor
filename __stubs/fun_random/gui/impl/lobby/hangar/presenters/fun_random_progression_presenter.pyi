# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_progression_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression
from fun_random.gui.impl.gen.view_models.views.lobby.feature.fun_random_progression_entry_point_model import FunRandomProgressionEntryPointModel as FunRandomProgressionEntryPointModel
from fun_random.gui.impl.lobby.tooltips.fun_random_progression_tooltip_view import FunRandomProgressionTooltipView as FunRandomProgressionTooltipView
from fun_random.gui.impl.lobby.common.fun_view_helpers import defineProgressionStatus as defineProgressionStatus, packProgressionState as packProgressionState, packProgressionActiveStage as packProgressionActiveStage, packInfiniteProgressionState as packInfiniteProgressionState, packInfiniteProgressionStage as packInfiniteProgressionStage
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from fun_random.gui.impl.lobby.hangar.controllers.fun_random_overlap_controller import FunRandomOverlapCtrlMixin as FunRandomOverlapCtrlMixin
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from frameworks.wulf import View as View, ViewEvent as ViewEvent

# base nao representavel no stub: ViewComponent[...]
class FunRandomProgressionPresenter(TooltipPositionerMixin, FunRandomOverlapCtrlMixin, FunProgressionWatcher):
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def setDisabledProgression(self):
        ...
    # decorador original: @hasActiveProgression(...)
    def showActiveProgressionPage(self, *_):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @hasActiveProgression(...)
    def _rawUpdate(self):
        ...
    # decorador original: @hasActiveProgression(...)
    def _updateViewModel(self, *_):
        ...
