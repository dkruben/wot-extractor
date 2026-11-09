# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/bonuses_packers.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
from battle_pass_common import CurrencyBP as CurrencyBP
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from gui import GUI_NATIONS as GUI_NATIONS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.customization.shared import getSingleVehicleForCustomization as getSingleVehicleForCustomization
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.bonus_model import BonusModel as BonusModel, BonusRarity as BonusRarity, VehicleType as VehicleType
from gui.lootbox_system.base.awards_manager import AwardsManager as AwardsManager
from gui.lootbox_system.base.common import LOOTBOX_RANDOM_NATIONAL_BLUEPRINT as LOOTBOX_RANDOM_NATIONAL_BLUEPRINT, LOOTBOX_RANDOM_NATIONAL_BROCHURE as LOOTBOX_RANDOM_NATIONAL_BROCHURE, LOOTBOX_RANDOM_NATIONAL_CREW_BOOK as LOOTBOX_RANDOM_NATIONAL_CREW_BOOK, LOOTBOX_RANDOM_NATIONAL_GUIDE as LOOTBOX_RANDOM_NATIONAL_GUIDE, LOOTBOX_COMPENSATION_BONUS as LOOTBOX_COMPENSATION_BONUS
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN, CREW_BONUS_X3_TOKEN as CREW_BONUS_X3_TOKEN
from gui.server_events.bonuses import BlueprintsBonusSubtypes as BlueprintsBonusSubtypes, LootBoxRandomNationalBonus as LootBoxRandomNationalBonus, PlusPremiumDaysBonus as PlusPremiumDaysBonus, VehiclesBonus as VehiclesBonus, _BONUSES as _BONUSES, LootBoxTokensBonus as LootBoxTokensBonus
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.Vehicle import getIconResourceName as getIconResourceName, getNationLessName as getNationLessName, getUnicName as getUnicName
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker as BaseBonusUIPacker, BlueprintBonusUIPacker as BlueprintBonusUIPacker, BonusUIPacker as BonusUIPacker, CrewBookBonusUIPacker as CrewBookBonusUIPacker, CrewSkinBonusUIPacker as CrewSkinBonusUIPacker, GoodiesBonusUIPacker as GoodiesBonusUIPacker, ItemBonusUIPacker as ItemBonusUIPacker, SimpleBonusUIPacker as SimpleBonusUIPacker, TokenBonusUIPacker as TokenBonusUIPacker, VehiclesBonusUIPacker as VehiclesBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, getLocalizedBonusName as getLocalizedBonusName, CurrenciesBonusUIPacker as CurrenciesBonusUIPacker
from gui.shared.money import Currency as Currency, Money as Money
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency, int2roman as int2roman
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, List as List, Optional as Optional, Tuple as Tuple, Union as Union
from frameworks.wulf import Array as Array
from gui.impl.wrappers.user_list_model import UserListModel as UserListModel
from gui.server_events.bonuses import CustomizationsBonus as CustomizationsBonus, SimpleBonus as SimpleBonus, TokensBonus as TokensBonus
BonusModelsList: Any
_logger: Any
VEH_COMP_R_ID: Any
_LOOTBOX_BONUS_NAME: Any
_EXTRA_BONUSES_NAMES: Any
_MAIN_REWARD_COUNT_RARE_OR_EPIC: Any
_MAIN_REWARD_COUNT: Any

# gerado do bytecode: classes base desconhecidas
class LootBoxSimpleBonusUIPacker:
    _LootBoxSimpleBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _packSingleBonus(cls, bonus, label):
        ...
    def _getToolTip(cls, bonus):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxSpecialRandomBonusUIPacker:
    _LootBoxSpecialRandomBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _pack(cls, bonus):
        ...
    def _packSingleBonus(cls, bonus, label):
        ...
    def _getContentId(cls, bonus):
        ...
    def _getToolTip(cls, bonus):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxSlotsBonusUIPacker:
    _LootBoxSlotsBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _packSingleBonus(cls, bonus, label):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxTmanTemplateBonusUIPacker:
    _LootBoxTmanTemplateBonusUIPacker__eventName: Any
    _LootBoxTmanTemplateBonusUIPacker__packTmanTemplateToken: Any
    _LootBoxTmanTemplateBonusUIPacker__getBonusImageName: Any
    def init(cls, eventName):
        ...
    def _pack(cls, bonus):
        ...
    def __packTmanTemplateToken(cls, tokenID, bonus, count):
        ...
    def __getBonusImageName(cls, recruitInfo):
        ...
    def _getToolTip(cls, bonus):
        ...
    def _getContentId(cls, bonus):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxCustomizationsBonusUIPacker:
    _LootBoxCustomizationsBonusUIPacker__eventName: Any
    _LootBoxCustomizationsBonusUIPacker__itemsCache: Any
    _LootBoxCustomizationsBonusUIPacker__isLockedStyle: Any
    def init(cls, eventName):
        ...
    def _pack(cls, bonus):
        ...
    def _packSingleBonus(cls, bonus, item, data):
        ...
    def _getToolTip(cls, bonus):
        ...
    def _getContentId(cls, bonus):
        ...
    def _getLabel(cls, customizationItem):
        ...
    def __isLockedStyle(cls, bonus, item):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxGoodiesBonusUIPacker:
    _LootBoxGoodiesBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _packSingleBoosterBonus(cls, bonus, booster, count):
        ...
    def _packIconBonusModel(cls, bonus, icon, count, label, description=...):
        ...
    def _getToolTip(cls, bonus):
        ...
    def _getContentId(cls, bonus):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxBlueprintBonusUIPacker:
    _LootBoxBlueprintBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _pack(cls, bonus):
        ...
    def getTooltip(bonuses):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxItemBonusUIPacker:
    _LootBoxItemBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _packSingleBonus(cls, bonus, item, count):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxCrewBookBonusUIPacker:
    _LootBoxCrewBookBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _packSingleBonus(cls, bonus, book, count):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxCrewSkinBonusUIPacker:
    _LootBoxCrewSkinBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _packSingleBonus(cls, bonus, crewSkin, count, label):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxesLootBoxBonusUIPacker:
    _LootBoxesLootBoxBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _pack(cls, bonus):
        ...
    def _packSingleBonus(cls, bonus):
        ...
    def _getContentId(cls, _):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxTokenBonusUIPacker:
    _LootBoxTokenBonusUIPacker__eventName: Any
    _LootBoxTokenBonusUIPacker__packBattleBonusX5Token: Any
    _LootBoxTokenBonusUIPacker__packCrewBonusX3Token: Any
    def init(cls, eventName):
        ...
    def _packToken(cls, bonusPacker, bonus, *args):
        ...
    def _getTokenBonusPackers(cls):
        ...
    def _getTooltipsPackers(cls):
        ...
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        ...
    def __packCrewBonusX3Token(cls, model, bonus, *args):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxPremiumBonusUIPacker:
    _LootBoxPremiumBonusUIPacker__eventName: Any
    _ICONS_AVAILABLE: Any
    def init(cls, eventName):
        ...
    def _pack(cls, bonus):
        ...
    def _packSingleBonus(cls, bonus):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxVehiclesBonusUIPacker:
    _LootBoxVehiclesBonusUIPacker__eventName: Any
    _LootBoxVehiclesBonusUIPacker__fillVehicleInfo: Any
    _LootBoxVehiclesBonusUIPacker__convertCompensationTooltip: Any
    _LootBoxVehiclesBonusUIPacker__getCompensation: Any
    def init(cls, eventName):
        ...
    def _packVehicles(cls, bonus, vehicles):
        ...
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        ...
    def __fillVehicleInfo(cls, model, vehicle):
        ...
    def _packTooltips(cls, bonus, vehicles):
        ...
    def _packTooltip(cls, bonus, vehicle, vehInfo):
        ...
    def _packCompensationTooltip(cls, bonusComp, vehicle):
        ...
    def _getContentId(cls, bonus):
        ...
    def __convertCompensationTooltip(cls, bonusComp, vehicle, tooltipData):
        ...
    def __getCompensation(cls, bonus, vehInfo):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxCurrenciesBonusUIPacker:
    _LootBoxCurrenciesBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _packSingleBonus(cls, bonus, label):
        ...
    def _getContentId(cls, bonus):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxBPCoinBonusUIPacker:
    _LootBoxBPCoinBonusUIPacker__eventName: Any
    def init(cls, eventName):
        ...
    def _packSingleBonus(cls, bonus, label):
        ...
    def _getContentId(cls, bonus):
        ...

# gerado do bytecode: classes base desconhecidas
class LootBoxCompensationPacker:
    _LootBoxCompensationPacker__eventName: Any
    _LootBoxCompensationPacker__VEHICLE_BONUS_NAME: Any
    def init(cls, eventName):
        ...
    def _pack(cls, bonus):
        ...
    def _packSingleBonus(cls, bonus, label):
        ...
    def _getContentId(cls, bonus):
        ...
    def _getToolTip(cls, bonus):
        ...

def getLootBoxesBonusPackerMap():
    ...
def getLootBoxesBonusPacker(eventName):
    ...
def packBonusModelAndTooltipData(bonuses, bonusModelsList, eventName, tooltipData=..., merge=..., packer=..., showLootboxCompensation=...):
    ...
def mergeNeededBonuses(bonuses, eventName):
    ...
def processCompensationsWithLootbox(bonuses, eventName, showLootboxCompensation):
    ...
def splitBonusesToExtra(bonuses, eventName):
    ...
def _getBonusCount(bonusModel):
    ...
def _getVehicleUIData(vehicle):
    ...
def getPreparedBonusModel(bonus, eventName):
    ...
def _injectSpecialRewardName(item, postfix=...):
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
