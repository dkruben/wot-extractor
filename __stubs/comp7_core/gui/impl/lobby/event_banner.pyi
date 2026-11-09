# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/impl/lobby/event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_shared as comp7_core_shared
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from helpers.time_utils import getCurrentLocalServerTimestamp as getCurrentLocalServerTimestamp
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from helpers import int2roman as int2roman, dependency as dependency

class Comp7CoreEventBanner(StandardEventBanner):
    __eventsService: Any
    _state: Any
    _eventStartDate: Any
    _eventEndDate: Any
    _timerValue: Any
    _playAppearAnim: Any
    def __init__(self):
        ...
    @property
    def _modeController(self):
        ...
    @property
    def _seasonStateClazz(self):
        ...
    @property
    def _accountSettingsTimestampFlag(self):
        ...
    @property
    def _selectorBattleType(self):
        ...
    @staticmethod
    def _selectMode():
        ...
    @property
    def _vehicleLevel(self):
        ...
    @property
    def isMode(self):
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
    @staticmethod
    def isEntryPointAvailable(modeCtrl=None):
        ...
    def prepare(self):
        ...
    def onClick(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def createToolTipContent(self, event):
        ...
    def __onUpdate(self, *_):
        ...
