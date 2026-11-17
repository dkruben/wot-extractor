# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/battle_pass_bonuses_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import logging as logging
from contextlib import contextmanager as contextmanager
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
from battle_pass_common import BATTLE_PASS_Q_CHAIN_BONUS_NAME as BATTLE_PASS_Q_CHAIN_BONUS_NAME, BATTLE_PASS_RANDOM_QUEST_BONUS_NAME as BATTLE_PASS_RANDOM_QUEST_BONUS_NAME, BATTLE_PASS_SELECT_BONUS_NAME as BATTLE_PASS_SELECT_BONUS_NAME, BATTLE_PASS_STYLE_PROGRESS_BONUS_NAME as BATTLE_PASS_STYLE_PROGRESS_BONUS_NAME, CurrencyBP as CurrencyBP
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.battle_pass.battle_pass_helpers import getOfferTokenByGift as getOfferTokenByGift, getStyleForChapter as getStyleForChapter
from gui.customization.shared import getSingleVehicleForCustomization as getSingleVehicleForCustomization
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel as TokenBonusModel
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel as RewardItemModel
from gui.impl.gen.view_models.views.lobby.battle_pass.vehicle_bonus_model import VehicleBonusModel as VehicleBonusModel
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN, CREW_BONUS_X3_TOKEN as CREW_BONUS_X3_TOKEN
from gui.server_events.bonuses import BlueprintsBonusSubtypes as BlueprintsBonusSubtypes, GoldBonus as GoldBonus, CreditsBonus as CreditsBonus, CustomizationsBonus as CustomizationsBonus, VehiclesBonus as VehiclesBonus, processAttachmentsSetTokens as processAttachmentsSetTokens
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker as BaseBonusUIPacker, BlueprintBonusUIPacker as BlueprintBonusUIPacker, BonusUIPacker as BonusUIPacker, CrewBookBonusUIPacker as CrewBookBonusUIPacker, DossierBonusUIPacker as DossierBonusUIPacker, GoodiesBonusUIPacker as GoodiesBonusUIPacker, ItemBonusUIPacker as ItemBonusUIPacker, SimpleBonusUIPacker as SimpleBonusUIPacker, TokenBonusUIPacker as TokenBonusUIPacker, VehiclesBonusUIPacker as VehiclesBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap
from gui.shared.money import Currency as Currency, Money as Money
from helpers import dependency as dependency
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import first as first
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from typing import List as List, Dict as Dict
from gui.server_events.bonuses import BattlePassQuestChainTokensBonus as BattlePassQuestChainTokensBonus, BattlePassRandomQuestTokensBonus as BattlePassRandomQuestTokensBonus, SimpleBonus as SimpleBonus, TmanTemplateTokensBonus as TmanTemplateTokensBonus, PlusPremiumDaysBonus as PlusPremiumDaysBonus, DossierBonus as DossierBonus, BattlePassSelectTokensBonus as BattlePassSelectTokensBonus, BattlePassStyleProgressTokenBonus as BattlePassStyleProgressTokenBonus, VehicleBlueprintBonus as VehicleBlueprintBonus, GoodiesBonus as GoodiesBonus, CurrenciesBonus as CurrenciesBonus, TokensBonus as TokensBonus
from account_helpers.offers.events_data import OfferEventData as OfferEventData, OfferGift as OfferGift
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.goodies.goodie_items import Booster as Booster
_logger: Any

class _BattlePassFinalBonusPacker(BaseBonusUIPacker):
    __isBigImageUsed = False
    @classmethod
    def setIsBigAward(cls, isBig):
        ...
    @classmethod
    def _injectAwardID(cls, item, postfix=None):
        ...

class TmanTemplateBonusPacker(_BattlePassFinalBonusPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packTmanTemplateToken(cls, tokenID, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def __getBonusImageName(cls, recruitInfo):
        ...

class BattlePassCustomizationsBonusPacker(_BattlePassFinalBonusPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, data):
        ...
    @classmethod
    def _createBonusModel(cls):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _getLabel(cls, customizationItem):
        ...
    @classmethod
    def _getUserName(cls, customizationItem):
        ...

class BattlePassPremiumDaysPacker(BaseBonusUIPacker):
    _ICONS_AVAILABLE: tuple
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...

class BattlePassDossierBonusPacker(DossierBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, dossierIconName, dossierNamePostfix, dossierValue, dossierLabel, recordName=None):
        ...

class SelectBonusPacker(BaseBonusUIPacker):
    __offersProvider: Any
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...
    @classmethod
    def getValue(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class BattlePassStyleProgressTokenBonusPacker(_BattlePassFinalBonusPacker):
    _ICON_NAME_TEMPLATE = 'style_3d_{}'
    _STYLE_FIRST_LEVEL = 1
    _STYLE_MAX_LEVEL = 4
    _rStyleProgression = R.strings.battle_pass.styleProgression
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...
    @classmethod
    def _isCollectionItem(cls, collectionItemID):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class ExtendedItemBonusUIPacker(ItemBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, count):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class ExtendedCrewBookBonusUIPacker(CrewBookBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, book, count):
        ...

class ExtendedCurrencyBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...

class ExtendedCurrenciesBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class CoinBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class QuestChainBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class RandomQuestBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class BattlePassSlotsBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class BattlePassVehiclesBonusUIPacker(VehiclesBonusUIPacker):
    @classmethod
    def _packVehicles(cls, bonus, vehicles):
        ...
    @classmethod
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        ...
    @classmethod
    def __fillVehicle(cls, model, vehicle):
        ...
    @classmethod
    def _packTooltip(cls, bonus, vehicle, vehInfo):
        ...
    @classmethod
    def _packTooltips(cls, bonus, vehicles):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def __packCompensationTooltip(cls, compensationBonus, vehicle, vehicleInfo):
        ...

class BattlePassFreeXPPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class BattlePassBlueprintsBonusPacker(BlueprintBonusUIPacker):
    __INTELLIGENCE_BLUEPRINT = 'intelligence'
    __ICON_NAME_PREFIX = 'blueprint_{}'
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...

class BattlePassGoodiesBonusPacker(GoodiesBonusUIPacker):
    @classmethod
    def _packIconBonusModel(cls, bonus, icon, count, label):
        ...
    @classmethod
    def _packSingleBoosterBonus(cls, bonus, booster, count):
        ...

class BattlePassTokenBonusPacker(TokenBonusUIPacker):
    @classmethod
    def _packToken(cls, bonusPacker, bonus, *args):
        ...
    @classmethod
    def _getTokenBonusPackers(cls):
        ...
    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        ...
    @classmethod
    def __packCrewBonusX3Token(cls, model, bonus, *args):
        ...

class BattlePassBerthsBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class BattlePassLootBoxBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getContentId(cls, _):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

def getBattlePassBonusPacker():
    ...
def packBonusModelAndTooltipData(bonuses, bonusModelsList, tooltipData=None, packer=None, showAttachmentsSets=False):
    ...
def packSpecialTooltipData(specialReward, specialRewardItems, *args):
    ...
def changeBonusTooltipData(bonusData, tooltipData):
    ...
def _getCompensation(bonus, item):
    ...
# decorador original: @contextmanager
def useBigAwardInjection():
    ...
