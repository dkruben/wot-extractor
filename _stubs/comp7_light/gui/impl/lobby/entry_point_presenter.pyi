# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/entry_point_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.gui.impl.gen.view_models.views.lobby.entry_point_model import EntryPointModel as EntryPointModel, ProgressionState as ProgressionState
from comp7_light.gui.impl.gen.view_models.views.lobby.tooltips.leaderboard_reward_tooltip_model import State as State
from comp7_light.gui.impl.lobby.comp7_light_helpers.account_settings import setUmgProgressionPointsSeen as setUmgProgressionPointsSeen, getPrevUmgProgressionPointsSeen as getPrevUmgProgressionPointsSeen, markUmgEntryPointSeen as markUmgEntryPointSeen, getUmgEntryPointSeen as getUmgEntryPointSeen
from comp7_light.gui.impl.lobby.tooltips.leaderboard_reward_tooltip import LeaderboardRewardTooltipView as LeaderboardRewardTooltipView
from comp7_light.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import Comp7LightOverlapCtrlMixin as Comp7LightOverlapCtrlMixin
from comp7_light.gui.shared.event_dispatcher import showComp7LightProgressionView as showComp7LightProgressionView
from comp7_light.skeletons.gui.game_control import IComp7LightProgressionController as IComp7LightProgressionController
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin

# base nao representavel no stub: ViewComponent[...]
class EntryPointPresenter(TooltipPositionerMixin, Comp7LightOverlapCtrlMixin, IGlobalListener):
    __comp7LightController: Any
    __comp7LightProgressionController: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _updateViewModel(self):
        ...
    def _rawUpdate(self):
        ...
    def _getEvents(self):
        ...
    def __onAnimationEnd(self):
        ...
    def __onEntryPointAnimationSeen(self):
        ...
    def _finalize(self):
        ...
    @staticmethod
    def __onOpenProgression():
        ...
