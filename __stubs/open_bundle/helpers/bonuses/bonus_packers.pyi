# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/helpers/bonuses/bonus_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
from battle_pass_common import CurrencyBP as CurrencyBP
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.customization.shared import getSingleVehicleForCustomization as getSingleVehicleForCustomization
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN, CREW_BONUS_X3_TOKEN as CREW_BONUS_X3_TOKEN
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, BlueprintsBonusSubtypes as BlueprintsBonusSubtypes, mergeBonuses as mergeBonuses, splitBonuses as splitBonuses, AttachmentsSetTokenBonus as AttachmentsSetTokenBonus, parseAttachmentsSetToken as parseAttachmentsSetToken, processAttachmentsSetTokens as processAttachmentsSetTokens
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.Vehicle import getUnicName as getUnicName
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import SimpleBonusUIPacker as SimpleBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, BonusUIPacker as BonusUIPacker, VehiclesBonusUIPacker as VehiclesBonusUIPacker, BaseBonusUIPacker as BaseBonusUIPacker, BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, CrewSkinBonusUIPacker as CrewSkinBonusUIPacker, CurrenciesBonusUIPacker as CurrenciesBonusUIPacker, GoodiesBonusUIPacker as GoodiesBonusUIPacker, TokenBonusUIPacker as TokenBonusUIPacker, ItemBonusUIPacker as ItemBonusUIPacker, BlueprintBonusUIPacker as BlueprintBonusUIPacker, CrewBookBonusUIPacker as CrewBookBonusUIPacker, AttachmentsSetTokenBonusPacker as AttachmentsSetTokenBonusPacker
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from open_bundle.gui.impl.gen.view_models.views.lobby.bonus_model import BonusModel as BonusModel, VehicleType as VehicleType
from open_bundle.helpers.bonuses.bonuses_constants import ATTACHMENTS_TOKEN_NAME as ATTACHMENTS_TOKEN_NAME
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import Array as Array
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from typing import Dict as Dict, List as List, Optional as Optional
_logger: Any

class OpenBundleSlotsBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...

class OpenBundleCurrencyBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...

class OpenBundleVehiclesBonusUIPacker(VehiclesBonusUIPacker):
    @classmethod
    def _packVehicles(cls, bonus, vehicles):
        ...
    @classmethod
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        ...
    @classmethod
    def __fillVehicleInfo(cls, model, vehicle):
        ...

class OpenBundleLootBoxBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, _):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class OpenBundleCustomizationsBonusUIPacker(BaseBonusUIPacker):
    __itemsCache: Any
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, data):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def __isLockedStyle(cls, bonus, item):
        ...

class OpenBundleCrewSkinBonusUIPacker(CrewSkinBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, crewSkin, count, label):
        ...

class OpenBundleCurrenciesBonusUIPacker(CurrenciesBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class OpenBundleBPCoinBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class OpenBundleItemBonusUIPacker(ItemBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, count):
        ...

class OpenBundleGoodiesBonusUIPacker(GoodiesBonusUIPacker):
    @classmethod
    def _packSingleBoosterBonus(cls, bonus, booster, count):
        ...
    @classmethod
    def _packIconBonusModel(cls, bonus, icon, count, label, description=''):
        ...

class OpenBundlePremiumBonusUIPacker(BaseBonusUIPacker):
    _ICONS_AVAILABLE: tuple
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...

class OpenBundleTokenBonusUIPacker(TokenBonusUIPacker):
    @classmethod
    def _packToken(cls, bonusPacker, bonus, *args):
        ...
    @classmethod
    def _getTokenBonusPackers(cls):
        ...
    @classmethod
    def _getTooltipsPackers(cls):
        ...
    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        ...
    @classmethod
    def __packCrewBonusX3Token(cls, model, bonus, *args):
        ...

class OpenBundleBlueprintBonusUIPacker(BlueprintBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @staticmethod
    def getTooltip(bonuses):
        ...

class OpenBundleCrewBookBonusUIPacker(CrewBookBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, book, count):
        ...

class OpenBundleTmanTemplateBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def __packTmanTemplateToken(cls, tokenID, bonus, count):
        ...
    @classmethod
    def __getBonusImageName(cls, recruitInfo):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class OpenBundleAttachmentsSetTokenBonusPacker(AttachmentsSetTokenBonusPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, tokenID, token, bonus):
        ...

def composeBonuses(rewards):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hideInvisible(bonuses, openBundle=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def sortBonuses(bonuses, reverse=True, openBundle=None):
    ...
def findVehicleCD(bonuses):
    ...
def getOpenBundleBonusPacker():
    ...
def packBonusModelAndTooltipData(bonuses, bonusModelsList, tooltipData=None, packer=None, showAttachmentsSets=False):
    ...
