# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/challenges/challenges_bonuses_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
from battle_pass_common import CurrencyBP as CurrencyBP
from challenges_common import ChallengeMainRewardTypes as ChallengeMainRewardTypes
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.customization.shared import getSingleVehicleForCustomization as getSingleVehicleForCustomization
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel as TokenBonusModel
from gui.impl.gen.view_models.views.lobby.challenges.bonus_model import BonusModel as BonusModel, VehicleType as VehicleType
from gui.impl.gen.view_models.views.lobby.challenges.skill_model import SkillModel as SkillModel
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN, CREW_BONUS_X3_TOKEN as CREW_BONUS_X3_TOKEN
from gui.server_events.bonuses import _BONUSES as _BONUSES, AttachmentsSetTokenBonus as AttachmentsSetTokenBonus, BlueprintsBonusSubtypes as BlueprintsBonusSubtypes, VehiclesBonus as VehiclesBonus
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.Vehicle import getIconResourceName as getIconResourceName, getUnicName as getUnicName
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, AttachmentsSetTokenBonusPacker as AttachmentsSetTokenBonusPacker, BaseBonusUIPacker as BaseBonusUIPacker, BlueprintBonusUIPacker as BlueprintBonusUIPacker, BonusUIPacker as BonusUIPacker, CrewBookBonusUIPacker as CrewBookBonusUIPacker, CrewSkinBonusUIPacker as CrewSkinBonusUIPacker, CurrenciesBonusUIPacker as CurrenciesBonusUIPacker, Customization3Dand2DbonusUIPacker as Customization3Dand2DbonusUIPacker, GoodiesBonusUIPacker as GoodiesBonusUIPacker, ItemBonusUIPacker as ItemBonusUIPacker, SimpleBonusUIPacker as SimpleBonusUIPacker, TokenBonusUIPacker as TokenBonusUIPacker, VehiclesBonusUIPacker as VehiclesBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, getLocalizedBonusName as getLocalizedBonusName
from gui.shared.money import Currency as Currency, Money as Money
from helpers import dependency as dependency, int2roman as int2roman
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from typing import List as List
_logger: Any
VEH_COMP_R_ID: Any

class ChallengesSlotsBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...

class ChallengesCurrencyBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...

class ChallengesVehiclesBonusUIPacker(VehiclesBonusUIPacker):
    __customizationService: Any
    @classmethod
    def _packVehicles(cls, bonus, vehicles):
        ...
    @classmethod
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        ...
    @classmethod
    def __fillVehicleInfo(cls, model, vehicle):
        ...
    @classmethod
    def _packTooltips(cls, bonus, vehicles):
        ...
    @classmethod
    def _packTooltip(cls, bonus, vehicle, vehInfo):
        ...
    @classmethod
    def _packCompensationTooltip(cls, compensationBonus, vehicle, vehicleInfo):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def __getCompensation(cls, bonus, vehInfo):
        ...

class ChallengesLootBoxBonusUIPacker(SimpleBonusUIPacker):
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

class ChallengesCustomizationsBonusUIPacker(BaseBonusUIPacker):
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
    @classmethod
    def __getCompensation(cls, bonus):
        ...

class ChallengesCrewSkinBonusUIPacker(CrewSkinBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, crewSkin, count, label):
        ...

class ChallengesCurrenciesBonusUIPacker(CurrenciesBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class ChallengesBPCoinBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class ChallengesItemBonusUIPacker(ItemBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, count):
        ...
    @classmethod
    def __getDescription(cls, item):
        ...

class ChallengesGoodiesBonusUIPacker(GoodiesBonusUIPacker):
    @classmethod
    def _packSingleBoosterBonus(cls, bonus, booster, count):
        ...
    @classmethod
    def _packIconBonusModel(cls, bonus, icon, count, label, description=''):
        ...

class ChallengesPremiumBonusUIPacker(BaseBonusUIPacker):
    _ICONS_AVAILABLE: tuple
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus):
        ...

class ChallengesTokenBonusUIPacker(TokenBonusUIPacker):
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

class ChallengesBlueprintBonusUIPacker(BlueprintBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @staticmethod
    def getTooltip(bonuses):
        ...

class ChallengesCrewBookBonusUIPacker(CrewBookBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, book, count):
        ...

class ChallengesTmanTemplateBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packTmanTemplateToken(cls, tokenID, bonus, count):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def __packTmanSkills(cls, skillsArrayModel, recruit):
        ...
    @classmethod
    def __getBonusImageName(cls, recruitInfo):
        ...

class ChallengesAttachmentsSetTokenBonusPacker(AttachmentsSetTokenBonusPacker):
    @classmethod
    def _packSingleBonus(cls, tokenID, token, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class ChallengesPostBattlePremiumBonusUIPacker(SimpleBonusUIPacker):
    _ICONS_AVAILABLE: tuple
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...

class ChallengesPostBattleLootBoxBonusUIPacker(TokenBonusUIPacker):
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

class ChallengesPostBattleTmanTemplateBonusUIPacker(ChallengesTmanTemplateBonusUIPacker):
    @classmethod
    def _packTmanTemplateToken(cls, tokenID, bonus, count):
        ...

def _getVehicleUIData(vehicle):
    ...
def getChallengesPostBattleBonusPacker():
    ...
def getChallengesBonusPacker():
    ...
