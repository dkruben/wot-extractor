# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/base_block_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.tab_id import TabId as TabId
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.lobby.user_missions.hub.update_children_mixin import UpdateChildrenMixin as UpdateChildrenMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.pub.view_impl import TViewModel as TViewModel
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import UserMissionsEvent as UserMissionsEvent
from helpers import dependency as dependency
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.server_events import IEventsCache as IEventsCache

# base nao representavel no stub: ViewComponent[...]
class BaseBlockPresenter(UpdateChildrenMixin):
    eventsCache: Any
    gameSession: Any
    __isInRequiredTab: Any
    _tooltipData: Any
    _rewardsGetterByQuestID: Any
    def __init__(self, model):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def isInRequiredTab(self):
        ...
    def _onLoaded(self, *_, **__):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getTooltipData(self, event):
        ...
    def _markQuestsAsVisited(self):
        ...
    def _onLeaveTab(self):
        ...
    def _onSyncCompleted(self, *_):
        ...
    def _finalize(self):
        ...
    def __onTabChange(self, ume):
        ...
