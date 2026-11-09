# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/presenters/packers/manageable_xp_multiplier.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/presenters/packers/manageable_xp_multiplier.py
from shared_utils import first
from constants import PREMIUM_TYPE
from gui.battle_results.pbs_helpers.additional_bonuses import getAdditionalXpBonusStatus, getAdditionalXPFactor10FromResult, getLeftAdditionalBonus, isAdditionalXpBonusAvailable, isAddXpBonusStatusAcceptable, getAdditionalXpBonusDiff
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.game_control.wot_plus.utils import WOT_PLUS_TIER_MAP
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import PremiumXpBonusRestriction
from helpers import dependency
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class ManageableXpMultiplier(IBattleResultsPacker):
    __itemsCache = dependency.descriptor(IItemsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __wotPlusController = dependency.descriptor(IWotPlusController)

    @classmethod
    def packModel(cls, model, battleResults):
        reusable = battleResults.reusable
        model.setWotPlusType(WOT_PLUS_TIER_MAP[reusable.personal.wotPlusTier])
        model.setHasAnyPremium(reusable.personal.hasAnyPremium)
        hasPremiumPlus = cls.__itemsCache.items.stats.isActivePremium(PREMIUM_TYPE.PLUS)
        model.setHasPremium(hasPremiumPlus)
        hasBasicPremium = cls.__itemsCache.items.stats.isActivePremium(PREMIUM_TYPE.BASIC)
        model.setHasBasicPremium(hasBasicPremium)
        arenaUniqueID = reusable.arenaUniqueID
        isXpBonusAvailable = cls._getXpAdditionalBonusStatus(arenaUniqueID, reusable, hasPremiumPlus)
        model.setIsXpBonusEnabled(isXpBonusAvailable)
        if not isXpBonusAvailable:
            model.setRestriction(PremiumXpBonusRestriction.NORESTRICTION)
            return
        wasPremiumPlusInBattle = reusable.personal.isPremiumPlus
        model.setWasPremium(wasPremiumPlusInBattle)
        hasWotPlus = cls.__wotPlusController.hasSubscription()
        cls._updateLeftCount(model, wasPremiumPlusInBattle, hasPremiumPlus, hasWotPlus)
        model.setBonusMultiplier(getAdditionalXPFactor10FromResult(battleResults.results[_RECORD.PERSONAL], reusable))
        isPersonalTeamWin = reusable.isPersonalTeamWin()
        _, vehicle = first(reusable.personal.getVehicleItemsIterator())
        vehicleCD = vehicle.intCD
        addXpBonusStatus = getAdditionalXpBonusStatus(arenaUniqueID, isPersonalTeamWin, vehicleCD, isXpBonusAvailable)
        model.setRestriction(addXpBonusStatus)
        model.setXpDiff(getAdditionalXpBonusDiff(arenaUniqueID))

    @classmethod
    def updateModel(cls, model, battleResults, ctx=None, isFullUpdate=True):
        if isFullUpdate:
            cls.packModel(model, battleResults)
            return
        else:
            isBonusApplied = ctx.get('isBonusApplied', True) if ctx is not None else True
            if not isBonusApplied:
                model.setRestriction(PremiumXpBonusRestriction.NOTAPPLYINGERROR)
            else:
                cls.packModel(model, battleResults)
            return

    @classmethod
    def _updateLeftCount(cls, model, wasPremiumPlusInBattle, hasPremiumPlus, hasWotPlus):
        _, leftCount, _ = getLeftAdditionalBonus(hasWotPlus, hasPremiumPlus)
        model.setLeftBonusCount(leftCount)

    @classmethod
    def _getXpAdditionalBonusStatus(cls, arenaUniqueID, reusable, hasPremiumPlus):
        return isAdditionalXpBonusAvailable(arenaUniqueID, reusable, hasPremiumPlus, isAddXpBonusStatusAcceptable)
