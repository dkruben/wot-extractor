# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_progression_quests_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression
from fun_random.gui.fun_account_settings import FunAccountSettings as FunAccountSettings
from fun_random.gui.impl.gen.view_models.views.lobby.feature.fun_random_progression_quests_model import FunRandomProgressionQuestsModel as FunRandomProgressionQuestsModel
from fun_random.gui.impl.lobby.tooltips.fun_random_progression_quest_tooltip_view import FunRandomProgressionQuestTooltipView as FunRandomProgressionQuestTooltipView
from fun_random.gui.impl.lobby.tooltips.fun_random_no_quests_tooltip_view import FunRandomNoQuestsTooltipView as FunRandomNoQuestsTooltipView
from fun_random.gui.impl.lobby.common.fun_view_helpers import defineProgressionStatus as defineProgressionStatus, packProgressionState as packProgressionState, packFullProgressionConditions as packFullProgressionConditions, packFullInfiniteProgressionConditions as packFullInfiniteProgressionConditions
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from fun_random.gui.impl.lobby.hangar.controllers.fun_random_overlap_controller import FunRandomOverlapCtrlMixin as FunRandomOverlapCtrlMixin
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from frameworks.wulf import View as View, ViewEvent as ViewEvent

# base nao representavel no stub: ViewComponent[...]
class FunRandomProgressionQuestsPresenter(TooltipPositionerMixin, FunRandomOverlapCtrlMixin, FunAssetPacksMixin, FunProgressionWatcher):
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def setDisabledProgression(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @hasActiveProgression(...)
    def __onMarkAsViewed(self):
        ...
    # decorador original: @hasActiveProgression(...)
    def _rawUpdate(self):
        ...
    # decorador original: @hasActiveProgression(...)
    def _updateViewModel(self, *_):
        ...
