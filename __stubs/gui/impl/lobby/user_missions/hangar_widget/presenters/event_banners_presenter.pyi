# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/presenters/event_banners_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banner_model import EventBannerModel as EventBannerModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banners_list_model import EventBannersListModel as EventBannersListModel
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin as OverlapCtrlMixin
from gui.impl.lobby.user_missions.hangar_widget.presenters.constants import UserMissionGroups as UserMissionGroups
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner as BaseEventBanner
_MAX_BANNERS = 5
_SPACE_CREATED_UPDATE_DELAY = 0.7

# base nao representavel no stub: ViewComponent[...]
class EventBannersPresenter(UserMissionChildPresenter, TooltipPositionerMixin, OverlapCtrlMixin):
    GROUP = UserMissionGroups.EVENTS
    __hangarSpace: Any
    _eventsService: Any
    __bannersContainer: Any
    __pendingToAppear: Any
    __readyForAnimations: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def isVisible(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onEventsUpdated(self):
        ...
    def _onEventClicked(self, args):
        ...
    def _onAppearAnimationPlayed(self, args):
        ...
    def _onSpaceCreate(self):
        ...
    def _delayedUpdateAfterSpaceCreated(self):
        ...
    def _getEventEntries(self):
        ...
    def _rawUpdate(self):
        ...
    def _fillBannerModel(self, banner):
        ...
    def _pickPendingAnimationIfExist(self, bannerName):
        ...
    def _allBannersOnDisappear(self):
        ...
    def _onBannerUpdate(self, banner):
        ...
    def _updateBanner(self, banner):
        ...
