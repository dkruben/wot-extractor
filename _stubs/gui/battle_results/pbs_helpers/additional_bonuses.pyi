# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/pbs_helpers/additional_bonuses.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui.game_control.wot_plus.utils import hasAdditionalXPPromoData as hasAdditionalXPPromoData
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import PremiumXpBonusRestriction as PremiumXpBonusRestriction
from gui.Scaleform.genConsts.BATTLE_RESULTS_PREMIUM_STATES import BATTLE_RESULTS_PREMIUM_STATES as BRPS
from gui.battle_results.settings import FACTOR_VALUE as FACTOR_VALUE
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
ACCOUNT_STATUS_TO_BRPS: dict
_ADDITIONAL_BONUS_AVAILABLE_STATUSES: set

# decorador original: @dependency.replace_none_kwargs(...)
def getAccountStatusToBRPS(hadPremiumPlus, isBonusAppliedAlready, hasXpInBonusCaps, hasXpBonusInBonusCaps, negativeImpact=False, itemsCache=None, lobbyContext=None, wotPlusController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isAdditionalXpBonusAvailable(arenaUniqueID, reusable, hasPremiumPlus, statusChecker, battleResults=None, lobbyContext=None):
    ...
def isAddXpBonusStatusAcceptable(status, _, __):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isGoldPiggyBankAvailaible(reusable, wotPlusCtrl=None):
    ...
def isWotPlusBonusEnabledInConfig():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAdditionalXpBonusDiff(arenaUniqueID, battleResults=None):
    ...
def getAdditionalXPFactor10FromResult(result, reusable):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getLeftAdditionalBonus(hasWotPlus, hasPremiumPlus, wasPremiumPlus=False, lobbyContext=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAdditionalXpBonusStatus(arenaUniqueID, isPersonalTeamWin, vehicleCD, isBonusAvailable, itemsCache=None, battleResults=None):
    ...
