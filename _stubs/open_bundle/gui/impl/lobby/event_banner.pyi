# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import OPEN_BUNDLE_ENTRY_POINT_ANIMATION_SHOWN as OPEN_BUNDLE_ENTRY_POINT_ANIMATION_SHOWN
from gui.impl import backport as backport
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from helpers import dependency as dependency, time_utils as time_utils
from open_bundle.gui.constants import OPEN_BUNDLE_ENTRY_POINT_NAME as OPEN_BUNDLE_ENTRY_POINT_NAME
from open_bundle.gui.impl.lobby.tooltips.event_banner_tooltip import EventBannerTooltip as EventBannerTooltip
from open_bundle.gui.shared.event_dispatcher import showOpenBundleMainView as showOpenBundleMainView
from open_bundle.helpers.account_settings import isEntryPointShown as isEntryPointShown
from open_bundle.helpers.resources import getBannerImagesPath as getBannerImagesPath, getDefaultTextResource as getDefaultTextResource, getTextResource as getTextResource
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController
from shared_utils import findFirst as findFirst
from typing import List as List

class OpenBundleEventBanner(StandardEventBanner):
    NAME = OPEN_BUNDLE_ENTRY_POINT_NAME
    __eventsService: Any
    __openBundle: Any
    __state: Any
    __timerValue: Any
    __bundleID: Any
    __playAppearAnim: Any
    def __init__(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def borderColor(self):
        ...
    @property
    def title(self):
        ...
    @property
    def iconsPath(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    def prepare(self):
        ...
    @property
    def showTimerBeforeEventEnd(self):
        ...
    @property
    def timerValue(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def __onUpdate(self, *_):
        ...
    def __getText(self, path):
        ...
    def __getState(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isOpenBundleEntryPointAvailable(openBundle=None):
    ...
