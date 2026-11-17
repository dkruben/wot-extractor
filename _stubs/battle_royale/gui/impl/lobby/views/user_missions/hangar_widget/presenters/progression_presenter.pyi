# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/progression_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.impl.gen.view_models.views.lobby.views.widget.progression_model import ProgressionModel as ProgressionModel, ProgressionStatus as ProgressionStatus
from battle_royale.gui.impl.lobby.tooltips.progression_widget_tooltip import ProgressionWidgetTooltipView as ProgressionWidgetTooltipView
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.overlap_ctrl import BattleRoyaleOverlapCtrlMixin as BattleRoyaleOverlapCtrlMixin
from battle_royale.gui.shared.event_dispatcher import showProgressionView as showProgressionView
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency

# base nao representavel no stub: ViewComponent[...]
class BattleRoyaleProgressionPresenter(UserMissionChildPresenter, TooltipPositionerMixin, BattleRoyaleOverlapCtrlMixin):
    GROUP = 'progressionEntryPoint'
    __brProgression: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __updateModel(self):
        ...
    def __onProgressionAnimationCompleted(self):
        ...
    def __onShowProgressionClick(self):
        ...
