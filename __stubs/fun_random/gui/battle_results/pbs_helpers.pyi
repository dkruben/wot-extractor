# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/pbs_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID as UNKNOWN_EVENT_ID
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_random_reward_item_model import FunRewardTypes as FunRewardTypes
from gui.impl import backport as backport
from gui.battle_results.pbs_helpers.economics import getDirectMoneyRecords as getDirectMoneyRecords
from gui.battle_results.settings import CurrenciesConstants as CurrenciesConstants
from gui.Scaleform.genConsts.BATTLE_RESULTS_PREMIUM_STATES import BATTLE_RESULTS_PREMIUM_STATES as BRPS
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from frameworks.wulf import PyResAccessor as PyResAccessor
from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode as IFunSubMode
_CURRENCY_TO_PREM_BONUS_CAPS_MAP: dict
_ADD_XP_BONUS_AVAILABLE_STATUSES: set
_ADD_XP_BONUS_AVAILABLE_STATUSES_FOR_PREM: set

def isCreditsShown(value, hasFines, _, reusable):
    ...
def isCrystalShown(value, hasFines, _, __):
    ...
def isGoldShown(value, hasFines, rewardValues, reusable):
    ...
def isXpShown(value, hasFines, _, reusable):
    ...
def isFreeXpShown(value, hasFines, rewardValues, reusable):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isTmenXpShown(value, _, __, reusable, funRandomCtrl=None):
    ...
def isPremiumAdvertisingShown(currencyType, battleResults):
    ...
def getAdvertising(extractor, record, label, battleResults):
    ...
def getEventID(reusable):
    ...
def getTmenXp(reusable):
    ...
def getTotalTMenXPToShow(reusable, _=None, __=None):
    ...
def getTotalGoldToShow(reusable):
    ...
def isFunAddXpBonusStatusAcceptable(status, reusable, hasPremiumPlus):
    ...
