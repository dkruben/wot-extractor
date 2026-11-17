# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/wot_plus/logging_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from enum import Enum as Enum
InfoPageInfo: Any
FEATURE = 'wot_plus'
MIN_VIEW_TIME = 2.0

class WotPlusLogActions(Enum):
    CLOSE = 'close'
    CLICK = 'click'
    VIEWED = 'viewed'

class WotPlusKeys(Enum):
    HANGAR = 'hangar'
    REWARD_SCREEN = 'reward_screen'
    RESERVE_VIEW = 'reserve_view'
    RESERVE_AWARD_VIEW = 'reserve_award_view'
    HEADER_TOOLTIP = 'header_tooltip'
    CLOSE_BUTTON = 'close_button'
    DETAILS_BUTTON = 'details_button'
    INFO_BUTTON = 'info_button'
    ACCOUNT_DASHBOARD = 'account_dashboard'
    SUBSCRIPTION_PAGE = 'subscription_page'

class RewardScreenTooltips(Enum):
    EXCLUSIVE_VEHICLE = 'exclusive_vehicle_tooltip'
    GOLD_RESERVE = 'gold_reserve_tooltip'
    PASSIVE_CREW_XP = 'passive_crew_xp_tooltip'
    EXCLUDED_MAP = 'excluded_map_tooltip'
    FREE_EQUIPMENT_MOVEMENT = 'free_equipment_movement_tooltip'
    ATTENDANCE_REWARD = 'attendance_reward_tooltip'

class ReservesKeys(Enum):
    GOLD_ACTIVATE = 'activate_wp_button'
    CREDITS_ACTIVATE = 'activate_pa_button'
    INFO_TOOLTIP = 'info_tooltip'
    GOLD_INFO = 'wp_info_button'
    CREDITS_INFO = 'pa_info_button'

class WotPlusStateStr(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    SUSPENDED = 'suspended'

class PremiumAccountStateStr(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

class WotPlusInfoPageSource(Enum):
    SHOP: Any
    REWARD_SCREEN: Any
    SUBSCRIPTION_PAGE: Any
    GOLD_RESERVES: Any

class AccountDashboardFeature(Enum):
    SUBSCRIPTION_WIDGET = 'subscription_widget'
    RESERVE_WIDGET = 'reserve_widget'
    EXCLUDED_MAPS_WIDGET = 'excluded_maps_widget'

class SubscriptionPageKeys(Enum):
    INFO_BUTTON = WotPlusKeys.INFO_BUTTON
    CTA_BUTTON = 'cta_button'

class SubscriptionStateMixinKeys(Enum):
    WOT_PLUS = 'wotp'
    PREMIUM = 'pa'
