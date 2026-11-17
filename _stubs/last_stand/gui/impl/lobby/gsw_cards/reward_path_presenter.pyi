# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/gsw_cards/reward_path_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen import R as R
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.reward_path_view_model import RewardPathViewModel as RewardPathViewModel
from last_stand.gui.impl.lobby.ls_helpers import fillRewardPathWidgetViewModel as fillRewardPathWidgetViewModel
from last_stand.gui.impl.lobby.tooltips.reward_path_tooltip import RewardPathTooltip as RewardPathTooltip
from last_stand.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import LastStandOverlapCtrlMixin as LastStandOverlapCtrlMixin
from last_stand.gui.shared.event_dispatcher import showRewardPathView as showRewardPathView
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from frameworks.wulf import ViewEvent as ViewEvent, View as View

# base nao representavel no stub: ViewComponent[...]
class RewardPathCardPresenter(UserMissionChildPresenter, TooltipPositionerMixin, LastStandOverlapCtrlMixin):
    lsArtefactsCtrl: Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def __onClick(self):
        ...
    def __fillMetaWidget(self):
        ...
    def __onArtefactStatusUpdated(self, _):
        ...
    def __onPointsUpdated(self):
        ...
