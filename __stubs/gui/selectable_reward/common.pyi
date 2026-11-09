# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/selectable_reward/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
from adisp import adisp_process as adisp_process
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import TooltipData as TooltipData
from gui.selectable_reward.constants import FEATURE_TO_PREFIX as FEATURE_TO_PREFIX, Features as Features
from gui.server_events.bonuses import SelectableBonus as SelectableBonus
from gui.shared.gui_items.processors import makeError as makeError
from gui.shared.gui_items.processors.offers import ReceiveMultipleOfferGiftsProcessor as ReceiveMultipleOfferGiftsProcessor, ReceiveOfferGiftProcessor as ReceiveOfferGiftProcessor, BattleMattersOfferProcessor as BattleMattersOfferProcessor, WinbackMultipleOfferProcessor as WinbackMultipleOfferProcessor
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.game_control import IWinbackController as IWinbackController
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
from account_helpers.offers.events_data import OfferEventData as OfferEventData, OfferGift as OfferGift
from typing import Callable as Callable, Dict as Dict, List as List, Optional as Optional, Tuple as Tuple, Generator as Generator
from gui.SystemMessages import ResultMsg as ResultMsg
_logger: Any

class SelectableRewardManager(object):
    __itemsCache: Any
    __offersDataProvider: Any
    _FEATURE = None
    _SINGLE_GIFT_PROCESSOR = ReceiveOfferGiftProcessor
    _MULTIPLE_GIFT_PROCESSOR = ReceiveMultipleOfferGiftsProcessor
    @classmethod
    def isFeatureReward(cls, tokenID):
        ...
    @classmethod
    # decorador original: @adisp_process
    def chooseReward(cls, bonus, giftID, callback):
        ...
    @classmethod
    # decorador original: @adisp_process
    def chooseRewards(cls, bonusChoices, callback):
        ...
    @classmethod
    def getBonusOptions(cls, bonus):
        ...
    @staticmethod
    def defaultGiftExtractor(gift, count):
        ...
    @staticmethod
    def giftBonusesExtractor(gift, *_):
        ...
    @staticmethod
    def giftRawBonusesExtractor(gift, *_):
        ...
    @staticmethod
    def _getGiftTokenFromOffer(offerToken):
        ...
    @classmethod
    def getBonusReceivedOptions(cls, bonus, extractor=None):
        ...
    @classmethod
    def __isAvailableBonus(cls, condition, tokenID):
        ...
    @classmethod
    def getAvailableSelectableBonuses(cls, condition=...):
        ...
    @classmethod
    def getSelectableBonuses(cls, condition=...):
        ...
    @classmethod
    def getRemainedChoices(cls, bonus):
        ...
    @classmethod
    def getRemainedChoicesForFeature(cls):
        ...
    @classmethod
    def getTabTooltipData(cls, selectableBonus):
        ...
    @classmethod
    def _getBonusOffer(cls, bonus):
        ...
    @classmethod
    def _getBonusOfferToken(cls, bonus):
        ...
    @classmethod
    def _packTokenData(cls, token):
        ...
    @classmethod
    def _iterAvailableTokens(cls):
        ...
    @classmethod
    def _getFeatureTokens(cls):
        ...

class BattlePassSelectableRewardManager(SelectableRewardManager):
    _FEATURE = Features.BATTLE_PASS
    @classmethod
    def getTabTooltipData(cls, selectableBonus):
        ...

class RankedSelectableRewardManager(SelectableRewardManager):
    _FEATURE = Features.RANKED
    @classmethod
    def getTabTooltipData(cls, selectableBonus):
        ...

class EpicSelectableRewardManager(SelectableRewardManager):
    _FEATURE = Features.EPIC
    @classmethod
    def getSelectableBonuses(cls, condition=None):
        ...
    @classmethod
    def getTabTooltipData(cls, selectableBonus):
        ...

class BattleMattersSelectableRewardManager(SelectableRewardManager):
    _battleMattersController: Any
    _SINGLE_GIFT_PROCESSOR = BattleMattersOfferProcessor
    @classmethod
    def isFeatureReward(cls, tokenID):
        ...
    @classmethod
    def getTabTooltipData(cls, selectableBonus):
        ...
    @classmethod
    def getBonusOffer(cls, bonus):
        ...

class WinbackSelectableRewardManager(SelectableRewardManager):
    _MULTIPLE_GIFT_PROCESSOR = WinbackMultipleOfferProcessor
    _winbackController: Any
    @classmethod
    def isFeatureReward(cls, tokenID):
        ...
    @classmethod
    def getRawBonusOptions(cls, bonus):
        ...
    @classmethod
    def getFirstOfferGift(cls, bonus):
        ...
    @classmethod
    def getBonusOffer(cls, bonus):
        ...
