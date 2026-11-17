# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from fort_rush.account_helpers.account_settings import isBannerSeen as isBannerSeen, setBannerSeen as setBannerSeen
from fort_rush.gui.fort_rush_gui_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES, FORT_RUSH_HANGAR_ALIASES as FORT_RUSH_HANGAR_ALIASES
from fort_rush.gui.impl.lobby.tooltips.fort_rush_event_banner_tooltip import FortRushEventBannerTooltipView as FortRushEventBannerTooltipView
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.shared.utils.SelectorBattleTypesUtils import isKnownBattleType as isKnownBattleType
from helpers import dependency as dependency
from helpers.time_utils import getTimestampFromUTC as getTimestampFromUTC, utcToLocalDatetime as utcToLocalDatetime
from skeletons.gui.server_events import IEventsCache as IEventsCache
_logger: Any

class FortRushEventBanner(StandardEventBanner):
    NAME = FORT_RUSH_HANGAR_ALIASES.FORT_RUSH_ENTRY_POINT
    __frCtrl: Any
    __eventsService: Any
    __eventsCache: Any
    _state: Any
    _timerValue: Any
    _playAppearAnim: Any
    def __init__(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def isMode(self):
        ...
    @property
    def borderColor(self):
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
    def __onUpdate(self, *_):
        ...

def isFortRushEntryPointAvailable():
    ...
