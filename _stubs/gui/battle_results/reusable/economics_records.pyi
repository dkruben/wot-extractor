# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/economics_records.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from ValueReplay import ValueReplay as ValueReplay, ValueReplayConnector as ValueReplayConnector
from debug_utils import LOG_ERROR as LOG_ERROR
from dossiers2.custom.records import RECORD_DB_IDS as RECORD_DB_IDS
from gui.battle_results.reusable import records as records
from gui.battle_results.settings import FACTOR_VALUE as FACTOR_VALUE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from helpers.rest_bonus import getRestBonusData as getRestBonusData
from renewable_subscription_common.settings_constants import WotPlusTier as WotPlusTier
from renewable_subscription_common.settings_helpers import SubscriptionSettingsStorage as SubscriptionSettingsStorage
from skeletons.gui.game_control import IWotPlusController as IWotPlusController, IRestBonusController as IRestBonusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_DEFAULT_FACTORS: dict

class _AdditionalRecords(records.RawRecords):
    __slots__: tuple
    def __init__(self, results):
        ...

class _CrystalRecords(records.RawRecords):
    __slots__: tuple
    def __init__(self, replay, results):
        ...

class _CreditsReplayRecords(records.ReplayRecords):
    __slots__: tuple
    def __init__(self, replay, results, squadCreditsFactor=0):
        ...
    def _getRecord(self, name):
        ...

class _XPReplayRecords(records.ReplayRecords):
    __slots__: tuple
    def __init__(self, replay, isHighScope, achievementXP):
        ...
    def _getRecord(self, name):
        ...

class _FreeXPReplayRecords(records.ReplayRecords):
    __slots__: tuple
    def __init__(self, replay, achievementFreeXP):
        ...
    def _getRecord(self, name):
        ...

class _TmenXPRecordsChains(object):
    __slots__: tuple
    __baseTmenXP: Any
    __premiumTmenXP: Any
    __premiumPlusTmenXP: Any
    __baseTmenXPAdd: Any
    __premiumTmenXPAdd: Any
    __premiumPlusTmenXPAdd: Any
    __isPremTmenXpBonuxEnabled: Any
    def __init__(self, bonusType, bonusCapsOverrides):
        ...
    def addResults(self, connector, results):
        ...
    def getRecords(self, premiumType, addBonusApplied):
        ...
    def __updatePremiumXPFactor(self, replay, results, premType=...):
        ...

class EconomicsRecordsChains(object):
    __slots__: tuple
    _baseCredits: Any
    _premiumCredits: Any
    _premiumPlusCredits: Any
    _baseCreditsWithWotPlus: Any
    _premiumCreditsWithWotPlus: Any
    _premiumPlusCreditsWithWotPlus: Any
    _goldRecords: Any
    _additionalRecords: Any
    _baseXP: Any
    _premiumXP: Any
    _premiumPlusXP: Any
    _baseXPWithWotPlus: Any
    _premiumXPWithWotPlus: Any
    _premiumPlusXPWithWotPlus: Any
    _baseXPAdd: Any
    _premiumXPAdd: Any
    _premiumPlusXPAdd: Any
    _baseXPAddWithWotPlus: Any
    _premiumXPAddWithWotPlus: Any
    _premiumPlusXPAddWithWotPlus: Any
    _baseFreeXP: Any
    _premiumFreeXP: Any
    _premiumPlusFreeXP: Any
    _baseFreeXPWithWotPlus: Any
    _premiumFreeXPWithWotPlus: Any
    _premiumPlusFreeXPWithWotPlus: Any
    _baseFreeXPAdd: Any
    _premiumFreeXPAdd: Any
    _premiumPlusFreeXPAdd: Any
    _baseFreeXPAddWithWotPlus: Any
    _premiumFreeXPAddWithWotPlus: Any
    _premiumPlusFreeXPAddWithWotPlus: Any
    _tmenXPRecordsChains: Any
    _crystal: Any
    _crystalDetails: Any
    __isPremCreditsBonusEnabled: Any
    __isPremXpBonusEnabled: Any
    def __init__(self, bonusType, bonusCapsOverrides):
        ...
    def getBaseCreditsRecords(self):
        ...
    def getPremiumCreditsRecords(self):
        ...
    def getCreditsDiff(self):
        ...
    def getBaseXPRecords(self):
        ...
    def getPremiumXPRecords(self):
        ...
    def getPremiumXPAddRecords(self):
        ...
    def getMoneyRecords(self, premiumType=...):
        ...
    def getCrystalRecords(self):
        ...
    def getCrystalDetails(self):
        ...
    def getXPRecords(self, premiumType=..., addBonusApplied=False):
        ...
    def getXPDiff(self):
        ...
    def getTmenXPRecords(self, premiumType=..., addBonusApplied=False):
        ...
    def addResults(self, _, results):
        ...
    def _addMoneyResults(self, connector, results):
        ...
    def _addXPResults(self, connector, results):
        ...
    def _addCrystalResults(self, connector, results):
        ...
    def __buildCreditsReplayForPremType(self, targetPremiumType, results, replay):
        ...
    def __buildCreditsReplayForWotPlus(self, targetPremiumType, results, replay):
        ...
    def __buildXPReplayForWotPlus(self, isHighScope, results, replay):
        ...
    def __buildFreeXPReplayForWotPlus(self, results, replay):
        ...
    def __updatePremiumXPFactor(self, replay, results, premType=...):
        ...
    @staticmethod
    # decorador original: @dependency.replace_none_kwargs(...)
    def __getPremiumSquadCreditsFactor(results, targetPremiumType, lobbyContext=None):
        ...
    @staticmethod
    # decorador original: @dependency.replace_none_kwargs(...)
    def __getWotPlusFactor(results, factorName, wotPlusCtrl=None):
        ...

def _getPremiumBonusFactor(factor, bonusCaps, isPremBonusEnabled):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _applyRestBonusToDaily(replay, results, restBonusCtrl=None):
    ...
def _updateAdditionalFactorFromReplay(replay, results, setDefault=False):
    ...
