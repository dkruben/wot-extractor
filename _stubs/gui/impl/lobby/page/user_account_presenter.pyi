# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/user_account_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
import constants as constants
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from frameworks.wulf import ViewFlags as ViewFlags
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getWotPlusShopUrl as getWotPlusShopUrl, getBuyPremiumUrl as getBuyPremiumUrl
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.page.header.premium_account_subscription_model import PremiumTypeEnum as PremiumTypeEnum, PremiumStateEnum as PremiumStateEnum
from gui.impl.gen.view_models.views.lobby.page.header.subscriptions_model import SubscriptionsModel as SubscriptionsModel
from gui.impl.gen.view_models.views.lobby.page.header.user_account_model import UserAccountModel as UserAccountModel
from gui.impl.gen.view_models.views.lobby.page.header.user_info_model import SteamEmailStatusEnum as SteamEmailStatusEnum
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_bonus_model import WotPlusSubscriptionBonusModel as WotPlusSubscriptionBonusModel
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusStateEnum as WotPlusStateEnum, WotPlusTypeEnum as WotPlusTypeEnum, WotPlusPeriodicityEnum as WotPlusPeriodicityEnum
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes
from gui.server_events.bonuses_wot_plus import getAvailableCoreBonuses as getAvailableCoreBonuses, getUniqueAvailableProBonuses as getUniqueAvailableProBonuses
from gui.shared.event_dispatcher import showDashboardView as showDashboardView, showSubscriptionsPage as showSubscriptionsPage, showShop as showShop, closeViewsWithFlags as closeViewsWithFlags
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import WotPlusState as WotPlusState, WotPlusTier as WotPlusTier
from renewable_subscription_common.settings_helpers import SubscriptionSettingsStorage as SubscriptionSettingsStorage
from skeletons.gui.game_control import IBadgesController as IBadgesController, IWotPlusController as IWotPlusController, IGameSessionController as IGameSessionController, ISteamCompletionController as ISteamCompletionController, IAnonymizerController as IAnonymizerController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController as IWGNPSteamAccRequestController
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.wot_plus.loggers import WotPlusHeaderLogger as WotPlusHeaderLogger
from wg_async import wg_await as wg_await, wg_async as wg_async
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.page.header.user_info_model import UserInfoModel as UserInfoModel
from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus as SteamAccEmailStatus
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusSubscriptionModel as WotPlusSubscriptionModel
from typing import List as List, Callable as Callable
from gui.server_events.bonuses import WoTPlusBonus as WoTPlusBonus
_STATUS_TYPES_MAP: dict
_WOT_PLUS_TIER_MAP: dict
_WOT_PLUS_STATES_MAP: dict
_PREMIUM_TYPE_MAP: dict

# base nao representavel no stub: ViewComponent[...]
class UserAccountPresenter:
    __itemsCache: Any
    __badgesController: Any
    __gameSession: Any
    __lobbyContext: Any
    __wotPlusCtrl: Any
    __steamRegistrationCtrl: Any
    __wgnpSteamAccCtrl: Any
    __anonymizerController: Any
    __wotPlusUILogger: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _getCallbacks(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateClanInfo(self, _=None):
        ...
    # decorador original: @wg_async
    def __updateUserInfo(self):
        ...
    def __updateBadgeInfo(self, _=None):
        ...
    @staticmethod
    def __setBadge(setter, badge):
        ...
    def __updatePremiumInfo(self):
        ...
    def __updateWotPlusInfo(self):
        ...
    def __setModelBenefits(self, getEnabledBonuses, getBenefits):
        ...
    def __setModelBenefitsList(self, enabledBonuses, benefitsList):
        ...
    def __onWotPlusStatusChanged(self, _):
        ...
    def __onPremiumChanged(self, *_):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __onUserInfoUpdate(self):
        ...
    # decorador original: @adisp_process
    def __onOpenAccountDashboard(self):
        ...
    # decorador original: @adisp_process
    def __onOpenPremium(self):
        ...
    def __onOpenWotPlus(self):
        ...
    def __updateAnonymizedState(self, **_):
        ...
    def __updateSteamEmailStatus(self, status=None):
        ...
