# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/halloween_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings, setSettings as setSettings
from halloween.gui.impl.lobby.tooltips.event_banner_tooltip import EventBannerTooltipView as EventBannerTooltipView
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES as HALLOWEEN_HANGAR_ALIASES
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from helpers import dependency as dependency, time_utils as time_utils
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController

class HalloweenEventBanner(StandardEventBanner):
    NAME = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_ENTRY_POINT
    _halloweenCtrl: Any
    _hwArtefactsCtrl: Any
    _eventsService: Any
    _state: Any
    _timerValue: Any
    _playAppearAnim: Any
    __uiLogger: Any
    def __init__(self):
        ...
    @property
    def isMode(self):
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

# decorador original: @dependency.replace_none_kwargs(...)
def isHalloweenEntryPointAvailable(ctrl=None):
    ...
