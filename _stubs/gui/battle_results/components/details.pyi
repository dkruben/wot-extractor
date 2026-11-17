# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/details.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
import typing as typing
from constants import IGR_TYPE as IGR_TYPE, PREMIUM_TYPE as PREMIUM_TYPE
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.battle_results.components import base as base
from gui.battle_results.components import style as style
from gui.battle_results.pbs_helpers.additional_bonuses import isWotPlusBonusEnabledInConfig as isWotPlusBonusEnabledInConfig, isGoldPiggyBankAvailaible as isGoldPiggyBankAvailaible, getAdditionalXpBonusStatus as getAdditionalXpBonusStatus, getLeftAdditionalBonus as getLeftAdditionalBonus, getAdditionalXPFactor10FromResult as getAdditionalXPFactor10FromResult
from gui.battle_results.pbs_helpers.economics import getCreditsToShow as getCreditsToShow
from gui.battle_results.reusable.records import convertFactorToPercent as convertFactorToPercent
from gui.impl import backport as backport
from gui.impl.backport.backport_system_locale import getIntegralFormat as getIntegralFormat
from gui.impl.lobby.premacc import premacc_helpers as premacc_helpers
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import PremiumXpBonusRestriction as PremiumXpBonusRestriction
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.formatters.icons import makeImageTag as makeImageTag
from gui.shared.money import Currency as Currency
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import i18n as i18n, dependency as dependency
from shared_utils import first as first
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.battle_results.reusable.records import RecordsIterator as RecordsIterator

class _GainResourceInBattleItem(base.StatsItem):
    __slots__: tuple
    __records: Any
    __method: Any
    __styler: Any
    def __init__(self, records, method, styler, field, *path):
        ...
    def _convert(self, value, reusable):
        ...

class GainCreditsInBattleItem(_GainResourceInBattleItem):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class GainCreditsValueInBattleItem(_GainResourceInBattleItem):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class GainCrystalInBattleItem(_GainResourceInBattleItem):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class GainCrystalValueInBattleItem(_GainResourceInBattleItem):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class GainXPInBattleItem(_GainResourceInBattleItem):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class GainXPValueInBattleItem(_GainResourceInBattleItem):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class TotalBRReward(base.StatsItem):
    __slots__: tuple
    __record: Any
    def __init__(self, record, field, *path):
        ...
    def _convert(self, value, reusable):
        ...

class BRCredits(TotalBRReward):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class BRXp(TotalBRReward):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class BRCrystal(TotalBRReward):
    __slots__: tuple
    def __init__(self, field, *path):
        ...

class BaseCreditsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PremiumCreditsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class XPTitleBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class XPTitleTooltipBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class BaseXPBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PremiumXPBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class _EconomicsDetailsBlock(base.StatsBlock):
    __slots__: tuple
    _lobbyContext: Any
    _wotPlusCtrl: Any
    hasAnyPremium: Any
    isWotPlus: Any
    canResourceBeFaded: Any
    penaltyDetails: Any
    igrType: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def _addEmptyRow(self):
        ...
    def _addStatsRow(self, label, labelArgs=None, column1=None, column2=None, column3=None, column4=None, htmlKey=''):
        ...
    def _addAOGASFactor(self, baseRecords, allColumns=True):
        ...

class MoneyDetailsBlock(_EconomicsDetailsBlock):
    __slots__: tuple
    __intermediateTotalRecords: tuple
    def setRecord(self, result, reusable):
        ...
    def __addStatsItem(self, label, baseRecords, premiumRecords, *names):
        ...
    def __addStatsItemIfExists(self, label, baseRecords, premiumRecords, acceptAllIfExist, labelArgs=None, *names):
        ...
    def __addBaseCredits(self, baseRecords, premiumRecords):
        ...
    def __addSquadBonus(self, baseRecords, premiumRecords):
        ...
    def __addPiggyBankInfo(self, premiumRecords, additionalRecords, reusable):
        ...
    def __addReferralSystemFactor(self, baseCredits, premiumCredits):
        ...
    def __addEventsMoney(self, baseCredits, premiumCredits, goldRecords):
        ...
    def __addViolationPenalty(self):
        ...
    def __addAOGASFactor(self, baseRecords):
        ...
    def __addBattleResults(self, baseRecords, premiumRecords, goldRecords):
        ...
    def __addAutoCompletion(self, label, additionalRecords, creditsRecord, goldRecord):
        ...
    def __addTotalResults(self, baseCredits, premiumCredits, goldRecords, additionalRecords):
        ...
    def __addWotPlusBattleBonusCredits(self, baseRecords, premiumRecords, baseCreditsWithWotPlus, premiumCreditsWithWotPlus):
        ...
    def __addWotPlusProboostBonusCredits(self, baseCredits, premiumCredits):
        ...

class XPDetailsBlock(_EconomicsDetailsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...
    def __addXPsItem(self, label, baseXP, premiumXP, xpRecord, labelArgs=None):
        ...
    def __addWotPlusBattleBonusXPs(self, result):
        ...
    def __addWotPlusProboostBonusXPs(self, baseFreeXP, baseXP, premiumFreeXP, premiumXP):
        ...
    def __addFreeXPsItem(self, label, baseFreeXP, premiumFreeXP, freeXPRecord):
        ...
    def __addComplexXPsItem(self, label, baseXP, premiumXP, baseFreeXP, premiumFreeXP, xpRecord, freeXPRecord, htmlKey=''):
        ...
    def __addXPsItemIfExists(self, label, baseXP, premiumXP, xpRecord):
        ...
    def __addFreeXPsItemIfExists(self, label, baseFreeXP, premiumFreeXP, freeXPRecord):
        ...
    def __addComplexXPsItemIfExists(self, label, baseXP, premiumXP, baseFreeXP, premiumFreeXP, xpRecord, freeXPRecord):
        ...
    def __addBaseXPs(self, baseXP, premiumXP, baseFreeXP, premiumFreeXP):
        ...
    def __addBoosterXPs(self, baseXP, premiumXP, baseFreeXP, premiumFreeXP):
        ...
    def __addEventXPs(self, baseXP, premiumXP, baseFreeXP, premiumFreeXP):
        ...
    def __addXPsViolationPenalty(self):
        ...
    def __addIGRFactor(self, baseXP):
        ...
    def __addDailyXPFactor(self, baseXP):
        ...
    def __addAdditionalXPBonus(self, baseXP, premiumXP, baseFreeXP, premiumFreeXP):
        ...
    def __addSquadXPDetails(self, baseXP, premiumXP):
        ...
    def __addReferralSystemFactor(self, baseXP, premiumXP):
        ...
    def __addTotalResults(self, result):
        ...
    @staticmethod
    def __getFormattedColumnsWithFreeXP(factors):
        ...

class CrystalDetailsBlock(_EconomicsDetailsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...
    def __addRecordField(self, key, result, label, force=False):
        ...
    def __addTotalResults(self, value):
        ...
    def _addRecord(self, res, value):
        ...

class _TotalEconomicsDetailsBlock(base.StatsBlock):
    __slots__: tuple
    __iteratorName: Any
    __blockClass: Any
    def __init__(self, iterator, block, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class TotalMoneyDetailsBlock(_TotalEconomicsDetailsBlock):
    __slots__: tuple
    def __init__(self, meta=None, field='', *path):
        ...

class TotalXPDetailsBlock(_TotalEconomicsDetailsBlock):
    __slots__: tuple
    def __init__(self, meta=None, field='', *path):
        ...

class TotalCrystalDetailsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PremiumBonusDetailsBlock(base.StatsBlock):
    __slots__: tuple
    __itemsCache: Any
    __battleResults: Any
    __wotPlusController: Any
    __lobbyContext: Any
    __arenaUniqueID: Any
    __isPersonalTeamWin: Any
    __arenaBonusType: Any
    __isBonusAvailable: Any
    __xpFactor: Any
    __vehicleCD: Any
    bonusIcon: Any
    description: Any
    bonusLeft: Any
    detailsLink: Any
    additionalBonusLeft: Any
    wotPlusBonusLeft: Any
    xpValue: Any
    statusBonusLabel: Any
    statusBonusTooltip: Any
    premiumAndPlusExhausted: Any
    hasWotPremium: Any
    hasWotPlus: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def getVO(self):
        ...
    def setRecord(self, result, reusable):
        ...
    def __getIsApplied(self):
        ...
    def __updateStatus(self):
        ...
    def __setBlockedByArenaType(self):
        ...
    def __setBlockedByVehicle(self):
        ...
    def __setBlockedByXPToTman(self, status):
        ...
    def __setBlockedByCrew(self):
        ...
    def __setBaseState(self):
        ...
    def __setBonusLeft(self):
        ...
    def __setAppliedState(self):
        ...
    def __setExcludedState(self):
        ...
    def __setLostBattleState(self):
        ...
    def __setShowButtonState(self):
        ...
    def __getAddXPBonusIcon(self, multiplier):
        ...
    @staticmethod
    def __getBonusLeftStr(applyAdditionalXPCount):
        ...
    @staticmethod
    def __getAdditionalBonusLeftStr(hasPremiumPlus, hasWotPlus, isWotPlusBonusEnabled):
        ...
    @staticmethod
    def __getWotPlusBonusEarningsStr(applyWoTPlusAdditionalXPCount):
        ...
    @staticmethod
    def __getPremiumAndPlusExhaustedStr():
        ...
    @staticmethod
    def __getDetailsLinkStr(hasPremiumPlus, hasWotPlus, isWotPlusBonusEnabled):
        ...
