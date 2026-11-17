# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import ResourceWell as ResourceWell
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from helpers import dependency as dependency, time_utils as time_utils
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from resource_well.gui.feature.constants import PurchaseMode as PurchaseMode
from resource_well.gui.feature.resource_well_helpers import isBannerSettingSet as isBannerSettingSet, setBannerSettings as setBannerSettings
from resource_well.gui.impl.lobby.feature.tooltips.event_banner_tooltip import EventBannerTooltip as EventBannerTooltip
from resource_well.gui.shared.event_dispatcher import showMainWindow as showMainWindow
from shared_utils import first as first
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class ResourceWellEventBanner(StandardEventBanner):
    NAME = HANGAR_ALIASES.RESOURCE_WELL_EVENT_BANNER
    __resourceWell: Any
    __eventsService: Any
    _state: Any
    _eventStartDate: Any
    _eventEndDate: Any
    _timerValue: Any
    _playAppearAnim: Any
    _callbackDelayer: Any
    def __init__(self):
        ...
    @property
    def isMode(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    @property
    def borderColor(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def timerValue(self):
        ...
    @property
    def eventStartDate(self):
        ...
    @property
    def eventEndDate(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    @property
    def showTimerBeforeEventEnd(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...
    def prepare(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def __getState(self):
        ...
    def __onUpdate(self, *_):
        ...
    def __getDescriptionText(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isResourceWellEventBannerAvailable(resourceWell=None):
    ...
