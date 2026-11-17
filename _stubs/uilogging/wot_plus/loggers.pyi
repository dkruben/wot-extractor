# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/wot_plus/loggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
from typing import TYPE_CHECKING as TYPE_CHECKING
from constants import WoTPlusBonusType as WoTPlusBonusType, PREMIUM_TYPE as PREMIUM_TYPE
from helpers import dependency as dependency
from renewable_subscription_common.settings_constants import WotPlusState as WotPlusState
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.wot_plus.logging_constants import FEATURE as FEATURE, WotPlusLogActions as WotPlusLogActions, MIN_VIEW_TIME as MIN_VIEW_TIME, RewardScreenTooltips as RewardScreenTooltips, WotPlusKeys as WotPlusKeys, WotPlusStateStr as WotPlusStateStr, AccountDashboardFeature as AccountDashboardFeature, PremiumAccountStateStr as PremiumAccountStateStr, SubscriptionStateMixinKeys as SubscriptionStateMixinKeys
from wotdecorators import noexcept as noexcept
from typing import Optional as Optional
from uilogging.types import ParentScreenType as ParentScreenType, ItemType as ItemType
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource as WotPlusInfoPageSource, InfoPageInfo as InfoPageInfo, SubscriptionPageKeys as SubscriptionPageKeys, ReservesKeys as ReservesKeys
_logger: Any
BONUS_NAME_TO_ITEM_MAP: dict
WOT_PLUS_STATE_TO_LOG_STATE_MAP: dict

class SubscriptionsStateMixin(object):
    __slots__: tuple
    _itemsCache: Any
    _wotPlusCtrl: Any
    @staticmethod
    def _formatState(key, value):
        ...
    def _getWotPlusStateSerialized(self):
        ...
    def _getPremiumAccountStateSerialized(self):
        ...
    def getSubscriptionsStatesSerialized(self):
        ...

class WotPlusViewLogger(MetricsLogger):
    __slots__: tuple
    _item: Any
    _viewParent: Any
    def __init__(self, parent, item):
        ...
    def onViewInitialize(self):
        ...
    # decorador original: @noexcept
    def onViewFinalize(self, itemState=None):
        ...

class WotPlusEventLogger(MetricsLogger):
    __slots__: tuple
    _eventParent: Any
    def __init__(self, parent):
        ...
    def logCloseEvent(self):
        ...
    def logClickEvent(self, item):
        ...

class WotPlusViewCloseLogger(WotPlusViewLogger):
    def logCloseEvent(self):
        ...

class WotPlusInfoPageLogger(MetricsLogger, SubscriptionsStateMixin):
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logInfoPage(self, source, includeSubscriptionInfo=False):
        ...

class WotPlusRewardScreenLogger(WotPlusViewCloseLogger):
    def __init__(self):
        ...

class WotPlusRewardTooltipLogger(WotPlusViewLogger):
    def __init__(self, parent, bonusName):
        ...

class WotPlusHeaderLogger(MetricsLogger):
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logClickEvent(self, state):
        ...

class WotPlusHeaderTooltipLogger(WotPlusViewLogger):
    def __init__(self):
        ...
    # decorador original: @noexcept
    def onViewFinalize(self, itemState):
        ...

class WotPlusAccountDashboardLogger(WotPlusViewCloseLogger, SubscriptionsStateMixin):
    def __init__(self):
        ...
    def onViewFinalize(self, itemState=None):
        ...

class WotPlusAccountDashboardWidgetLogger(MetricsLogger, SubscriptionsStateMixin):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @noexcept
    def logWidgetClickEvent(self, widget):
        ...

class WotPlusReservesLogger(WotPlusViewCloseLogger, SubscriptionsStateMixin):
    def __init__(self):
        ...
    def onViewFinalize(self, itemState=None):
        ...
    def logClickEvent(self, item):
        ...

class WotPlusSubscriptionViewLogger(WotPlusViewCloseLogger, SubscriptionsStateMixin):
    def __init__(self):
        ...
    def onViewFinalize(self, itemState=None):
        ...
    def logClickEvent(self, item):
        ...
