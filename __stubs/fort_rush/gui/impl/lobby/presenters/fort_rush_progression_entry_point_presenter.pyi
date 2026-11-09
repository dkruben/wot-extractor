# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_progression_entry_point_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.account_helpers.account_settings import getLastSeenProgressionPoints as getLastSeenProgressionPoints
from fort_rush.gui.impl.gen.view_models.views.lobby.hangar_progression_widget_view_model import HangarProgressionWidgetViewModel as HangarProgressionWidgetViewModel
from fort_rush.gui.impl.lobby.tooltips.fort_rush_progression_tooltip import FortRushProgressionWidgetTooltipView as FortRushProgressionWidgetTooltipView
from fort_rush.gui.shared.event_dispatcher import showProgressionView as showProgressionView
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from gui.impl.gen import R as R
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.server_events import IEventsCache as IEventsCache

# base nao representavel no stub: ViewComponent[...]
class FortRushProgressionEntryPointPresenter(UserMissionChildPresenter, TooltipPositionerMixin):
    __ctrl: Any
    __itemsCache: Any
    __eventsCache: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def hasDeferModelUpdate(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _updateModel(self, *_):
        ...
    def __onSyncCompleted(self, reason, _):
        ...
    def __onWidgetClick(self):
        ...
