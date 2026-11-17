# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/seniority_awards/seniority_reward_award_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import SENIORITY_AWARDS_COINS_REMINDER_SHOWN_TIMESTAMP as SENIORITY_AWARDS_COINS_REMINDER_SHOWN_TIMESTAMP
from frameworks.wulf import ViewSettings as ViewSettings, WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getPlayerSeniorityAwardsUrl as getPlayerSeniorityAwardsUrl
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.game_control.seniority_awards_controller import WDR_CURRENCY as WDR_CURRENCY
from gui.impl import backport as backport
from gui.impl.auxiliary.rewards_helper import getRewardTooltipContent as getRewardTooltipContent
from gui.impl.auxiliary.rewards_helper import getSeniorityAwardsBonuses as getSeniorityAwardsBonuses
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_screen_tooltips import BlueprintScreenTooltips as BlueprintScreenTooltips
from gui.impl.gen.view_models.views.lobby.seniority_awards.seniority_reward_award_view_model import SeniorityRewardAwardViewModel as SeniorityRewardAwardViewModel, ShopOnOpenState as ShopOnOpenState
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.seniority_awards.seniority_awards_helper import getVehicleCD as getVehicleCD, getRewardCategoryForUI as getRewardCategoryForUI
from gui.impl.lobby.seniority_awards.seniority_awards_sounds import SENIORITY_REWARD_SOUND_SPACE as SENIORITY_REWARD_SOUND_SPACE
from gui.impl.lobby.seniority_awards.tooltip.seniority_awards_tooltip import SeniorityAwardsTooltip as SeniorityAwardsTooltip
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.event_dispatcher import showShop as showShop
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import ISeniorityAwardsController as ISeniorityAwardsController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_T50_2_STYLE_NAME: Any
_AT_BADGE: Any
_BT_BADGE: Any
_AT_NICKNAME_BADGE: Any
_BT_NICKNAME_BADGE: Any
_EXCLUDED_BONUSES: tuple
_BONUSES_ORDER: tuple

class SeniorityRewardAwardView(ViewImpl):
    __slots__: tuple
    _COMMON_SOUND_SPACE = SENIORITY_REWARD_SOUND_SPACE
    __itemsCache: Any
    __lobbyContext: Any
    __seniorityAwardsCtrl: Any
    __bonuses: Any
    __specialCurrencies: Any
    __tooltipData: Any
    def __init__(self, contentResId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, data, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __getShopOnOpenState(self):
        ...
    @property
    def __needBlockShopTransition(self):
        ...
    def __setBonuses(self, viewModel):
        ...
    def __setSpecialCurrency(self, viewModel):
        ...
    def __getBackportTooltipData(self, event):
        ...
    def __updateBonuses(self, data):
        ...
    def __onOpenBtnClick(self):
        ...
    def __onShopBtnClick(self):
        ...
    def __onSettingsChange(self):
        ...

class SeniorityRewardAwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, data=None, viewID=None):
        ...

def _keySortOrder(bonus, _):
    ...
