# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/manageable_xp_multiplier.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from shared_utils import first as first
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from gui.battle_results.pbs_helpers.additional_bonuses import getAdditionalXpBonusStatus as getAdditionalXpBonusStatus, getAdditionalXPFactor10FromResult as getAdditionalXPFactor10FromResult, getLeftAdditionalBonus as getLeftAdditionalBonus, isAdditionalXpBonusAvailable as isAdditionalXpBonusAvailable, isAddXpBonusStatusAcceptable as isAddXpBonusStatusAcceptable, getAdditionalXpBonusDiff as getAdditionalXpBonusDiff
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker as IBattleResultsPacker
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.game_control.wot_plus.utils import WOT_PLUS_TIER_MAP as WOT_PLUS_TIER_MAP
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import PremiumXpBonusRestriction as PremiumXpBonusRestriction
from helpers import dependency as dependency
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class ManageableXpMultiplier(IBattleResultsPacker):
    __itemsCache: Any
    __lobbyContext: Any
    __wotPlusController: Any
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def updateModel(cls, model, battleResults, ctx=None, isFullUpdate=True):
        ...
    @classmethod
    def _updateLeftCount(cls, model, wasPremiumPlusInBattle, hasPremiumPlus, hasWotPlus):
        ...
    @classmethod
    def _getXpAdditionalBonusStatus(cls, arenaUniqueID, reusable, hasPremiumPlus):
        ...
