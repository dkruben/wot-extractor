# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/ls_entry_point.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from helpers import dependency as dependency, time_utils as time_utils
from last_stand.gui.impl.lobby.tooltips.event_banner_tooltip import EventBannerTooltipView as EventBannerTooltipView
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings, setSettings as setSettings
from last_stand.gui.scaleform.genConsts.LAST_STAND_HANGAR_ALIASES import LAST_STAND_HANGAR_ALIASES as LAST_STAND_HANGAR_ALIASES
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from last_stand.skeletons.ls_difficulty_missions_controller import ILSDifficultyMissionsController as ILSDifficultyMissionsController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from typing import Optional as Optional
from frameworks.wulf import View as View, ViewEvent as ViewEvent

class LSEventBanner(StandardEventBanner):
    NAME = LAST_STAND_HANGAR_ALIASES.LS_ENTRY_POINT
    _lsCtrl: Any
    _lsArtefactsCtrl: Any
    _lsDifficultyMissionsCtrl: Any
    __eventsService: Any
    _state: Any
    _timerValue: Any
    _playAppearAnim: Any
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
def isLSEntryPointAvailable(ctrl=None):
    ...
