# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from collections import defaultdict as defaultdict
import typing as typing
from future.utils import viewitems as viewitems
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE_TO_QUEUE_TYPE as ARENA_BONUS_TYPE_TO_QUEUE_TYPE
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import WotPlusTypeEnum as WotPlusTypeEnum
from gui.prb_control.settings import PREBATTLE_TYPE_TO_QUEUE_TYPE as PREBATTLE_TYPE_TO_QUEUE_TYPE
from helpers import dependency as dependency
from renewable_subscription_common.settings_constants import WotPlusTier as WotPlusTier
from skeletons.gui.game_control import IWotPlusController as IWotPlusController, IHangarGuiController as IHangarGuiController, ISteamCompletionController as ISteamCompletionController
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from renewable_subscription_common.settings_helpers import SubscriptionSettingsStorage as SubscriptionSettingsStorage
from typing import Optional as Optional
WOT_PLUS_TIER_MAP: dict

class ProBoostUtils(object):
    _QUEUE_TYPE_TO_ARENA_BONUS_TYPES = None
    @classmethod
    # decorador original: @dependency.replace_none_kwargs(...)
    def isGameModeCompatibleForProBoost(cls, hangarGuiCtrl=None):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getExcludedMapsPromoData(wotPlusController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAdditionalXPPromoData(wotPlusController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hasAdditionalXPPromoData(wotPlusController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hasFreeDeluxeEquipDemountPromo(wotPlusController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hasFreeEquipDemountPromo(wotPlusController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getMaxGoldReserveCapacityFromAllTiers(wotPlusController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def shouldRedirectToSteamInfoPage(wotPlusController=None, steamCompletionCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPassiveCrewXPPerMinuteFromAllTiers(wotPlusController=None):
    ...
