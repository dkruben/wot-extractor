# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings, BATTLE_ROYALE_BANNER_FIRST_APPEARANCE_TIMESTAMP as BATTLE_ROYALE_BANNER_FIRST_APPEARANCE_TIMESTAMP
from battle_royale.gui.constants import BattleRoyaleModeState as BattleRoyaleModeState
from battle_royale.gui.impl.lobby.tooltips.banner_tooltip_view import BannerTooltipView as BannerTooltipView
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from gui.shared.utils.SelectorBattleTypesUtils import isKnownBattleType as isKnownBattleType, setBattleTypeAsUnknown as setBattleTypeAsUnknown
from helpers import dependency as dependency
from helpers.time_utils import getCurrentLocalServerTimestamp as getCurrentLocalServerTimestamp
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyaleEventBanner(StandardEventBanner):
    NAME = 'BattleRoyaleEntryPoint'
    __battleRoyaleController: Any
    __eventsService: Any
    __state: Any
    __timerValue: Any
    __playAppearAnim: Any
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
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    @property
    def timerValue(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    def prepare(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def _onUpdate(self, *_):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isBattleRoyaleEntryPointAvailable(battleRoyaleController=None):
    ...
