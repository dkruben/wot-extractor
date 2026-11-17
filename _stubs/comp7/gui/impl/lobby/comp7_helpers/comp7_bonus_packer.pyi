# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_bonus_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from shared_utils import findFirst as findFirst, first as first
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.impl.gen.view_models.views.lobby.comp7_bonus_model import Comp7BonusModel as Comp7BonusModel, DogTagType as DogTagType
from comp7.gui.impl.gen.view_models.views.lobby.comp7_style_bonus_model import Comp7StyleBonusModel as Comp7StyleBonusModel
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_helpers import BonusTypes as BonusTypes, getBonusType as getBonusType, splitDossierBonuses as splitDossierBonuses, CustomizationsBonusHelper as CustomizationsBonusHelper
from comp7.gui.impl.lobby.comp7_helpers.comp7_c11n_helpers import getComp7ProgressionStyleCamouflage as getComp7ProgressionStyleCamouflage
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import isComp7OfferYearlyRewardToken as isComp7OfferYearlyRewardToken
from comp7.gui.selectable_reward.common import Comp7SelectableRewardManager as Comp7SelectableRewardManager
from comp7.gui.server_events.bonuses import COMP7_TOKEN_WEEKLY_REWARD_NAME as COMP7_TOKEN_WEEKLY_REWARD_NAME
from comp7_common_const import offerRewardGiftToken as offerRewardGiftToken
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.config.common import ComponentViewType as ComponentViewType
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.selectable_reward.constants import SELECTABLE_BONUS_NAME as SELECTABLE_BONUS_NAME
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, splitBonuses as splitBonuses, C11nProgressTokenBonus as C11nProgressTokenBonus, getVehicleCrewReward as getVehicleCrewReward, CountableIntegralBonus as CountableIntegralBonus, CustomizationsBonus as CustomizationsBonus, VehiclesBonus as VehiclesBonus, _BONUSES as _BONUSES, TankmenBonus as TankmenBonus
from gui.shared.gui_items.Tankman import getFullUserName as getFullUserName
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import DossierBonusUIPacker as DossierBonusUIPacker, DogTagComponentsUIPacker as DogTagComponentsUIPacker, BonusUIPacker as BonusUIPacker, BaseBonusUIPacker as BaseBonusUIPacker, BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, SimpleBonusUIPacker as SimpleBonusUIPacker, CustomizationBonusUIPacker as CustomizationBonusUIPacker, VehiclesBonusUIPacker as VehiclesBonusUIPacker, TokenBonusUIPacker as TokenBonusUIPacker, TankmenBonusUIPacker as TankmenBonusUIPacker
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap as getDefaultBonusPackersMap, getWeeklyMissionsMapping as getWeeklyMissionsMapping
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from items import tankmen as tankmen
from items.tankmen import getNationConfig as getNationConfig
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.common.bonus_model import BonusModel as BonusModel
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.server_events.bonuses import SelectableBonus as SelectableBonus
_logger: Any
_DOG_TAG_VIEW_TYPE_TO_DOG_TAG_TYPE_ENUM: dict
_RANK_REWARDS_BONUSES_ORDER: tuple
_TOKENS_REWARDS_BONUSES_ORDER: tuple
_QUALIFICATION_REWARDS_BONUSES_ORDER: tuple
_YEARLY_REWARDS_BONUSES_ORDER: tuple
_YEARLY_REWARD_META_BONUSES_ORDER: tuple
_OFFER_REWARDS_ORDER: tuple

class Comp7DossierBonusUIPacker(DossierBonusUIPacker):
    @classmethod
    def _getBadgeTooltip(cls, bonus):
        ...

class Comp7DogTagUIPacker(DogTagComponentsUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packDogTag(cls, bonus, dogTagRecord):
        ...

class Comp7CrystalBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class Comp7StyleProgressBonusUIPacker(BaseBonusUIPacker):
    __c11nService: Any
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, level=None):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _packTooltip(cls, bonus, level=None):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @staticmethod
    def __getIcon(styleID, progressLevel):
        ...
    @staticmethod
    def __getLabel(camo):
        ...

class Comp7YearlyStylePacker(Comp7StyleProgressBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class Comp7CustomizationBonusUIPacker(CustomizationBonusUIPacker):
    _ICON_NAME = 'style'
    _ICON_NAME_PROGRESSION = 'progressionStyle'
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class Comp7VehicleBonusUIPacker(VehiclesBonusUIPacker):
    @classmethod
    def _getLabel(cls, vehicle):
        ...
    @classmethod
    def _packTooltip(cls, bonus, vehicle, vehInfo):
        ...

class Comp7TankmenBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def __getTankmanGroupName(cls, tankmanData):
        ...

class Comp7YearlyCrewBonusUIPacker(TankmenBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class Comp7TokenWeeklyRewardUIPacker(TokenBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class Comp7OfferBonusUIPacker(BaseBonusUIPacker):
    _selectableRewardManager = Comp7SelectableRewardManager
    _offersDataProvider: Any
    _comp7Controller: Any
    _itemsCache: Any
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class Comp7YearlyMetaOfferPacker(Comp7OfferBonusUIPacker):
    @classmethod
    def _getGiftCount(cls, bonus):
        ...

class Comp7YearlySlotsBonus(CountableIntegralBonus):
    def isShowInGUI(self):
        ...

class Comp7YearlyCustomizationsBonus(CustomizationsBonus):
    def isShowInGUI(self):
        ...

class Comp7YearlyCustomizationsBonus3D(CustomizationsBonus):
    def isShowInGUI(self):
        ...

class Comp7YearlyCustomizationsBonus2D(CustomizationsBonus):
    def isShowInGUI(self):
        ...

def _getComp7BonusPackersMap():
    ...
def getComp7BonusPacker():
    ...
def getComp7YearlyBonusPacker():
    ...
def getComp7YearlyMetaBonusPacker():
    ...
def getWeeklyPBSBonusPacker():
    ...
def _getComp7YearlyBonuses(specificCustomization=None):
    ...
def packQuestBonuses(bonuses, bonusPacker, order=None):
    ...
def mergeOffers(bonuses):
    ...
def packRanksRewardsQuestBonuses(quest, periodicQuest=None):
    ...
def packTokensRewardsQuestBonuses(quest):
    ...
def packQualificationRewardsQuestBonuses(quests):
    ...
def packYearlyRewardsBonuses(bonuses):
    ...
def packYearlyRewardVehicleBonuses(bonuses):
    ...
def packYearlyRewardMetaView(bonuses):
    ...
def packSelectedRewardsBonuses(bonuses):
    ...
def _getSortKey(order):
    ...
def _getOfferRewardTokensSortKey(order):
    ...
