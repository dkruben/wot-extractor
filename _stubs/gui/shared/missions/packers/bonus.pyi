# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/missions/packers/bonus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from builtins import range as range, zip as zip
from future.utils import iteritems as iteritems, iterkeys as iterkeys, lzip as lzip, viewitems as viewitems, viewkeys as viewkeys, viewvalues as viewvalues
import constants as constants
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from collections_common import g_collectionsRelatedItems as g_collectionsRelatedItems
from exchange.personal_discounts_constants import EXCHANGE_RATE_FREE_XP_NAME as EXCHANGE_RATE_FREE_XP_NAME, EXCHANGE_RATE_GOLD_NAME as EXCHANGE_RATE_GOLD_NAME
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.dog_tag_composer import dogTagComposer as dogTagComposer
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.blueprint_bonus_model import BlueprintBonusModel as BlueprintBonusModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel as TokenBonusModel
from gui.ranked_battles.constants import YEAR_POINTS_TOKEN as YEAR_POINTS_TOKEN
from gui.server_events.bonuses import TmanTemplateTokensBonus as TmanTemplateTokensBonus
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.server_events.finders import isPMPoints as isPMPoints, PM_POINTS_TOKEN as PM_POINTS_TOKEN
from gui.server_events.bonuses import AttachmentsSetTokenBonus as AttachmentsSetTokenBonus, parseAttachmentsSetToken as parseAttachmentsSetToken
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN, GOLD_MISSION as GOLD_MISSION, ItemsBonusFormatter as ItemsBonusFormatter, TOKEN_SIZES as TOKEN_SIZES, TokenBonusFormatter as TokenBonusFormatter, formatCountLabel as formatCountLabel, CREW_BONUS_X3_TOKEN as CREW_BONUS_X3_TOKEN
from gui.server_events.formatters import COMPLEX_TOKEN as COMPLEX_TOKEN, TokenComplex as TokenComplex, parseComplexToken as parseComplexToken
from gui.shared.gui_items.crew_skin import localizedFullName as localizedFullName
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.gui_items.customization.c11n_items import Style as Style
from gui.shared.money import Currency as Currency
from gui.shared.system_factory import collectBonusPackers as collectBonusPackers
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency, i18n as i18n, time_utils as time_utils
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import first as first
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Dict as Dict, List as List, Callable as Callable, Optional as Optional
from frameworks.wulf.view.array import Array as Array
from gui.goodies.goodie_items import BoosterUICommon as BoosterUICommon, RecertificationForm as RecertificationForm, Booster as Booster, MentoringLicense as MentoringLicense
from gui.server_events.bonuses import CustomizationsBonus as CustomizationsBonus, CrewSkinsBonus as CrewSkinsBonus, TokensBonus as TokensBonus, SimpleBonus as SimpleBonus, ItemsBonus as ItemsBonus, DossierBonus as DossierBonus, VehicleBlueprintBonus as VehicleBlueprintBonus, CrewBooksBonus as CrewBooksBonus, GoodiesBonus as GoodiesBonus, TankmenBonus as TankmenBonus, VehiclesBonus as VehiclesBonus, DogTagComponentBonus as DogTagComponentBonus, BattlePassPointsBonus as BattlePassPointsBonus, CurrenciesBonus as CurrenciesBonus, PersonalExchangeRateTokensBonus as PersonalExchangeRateTokensBonus, UndefinedAmountBonus as UndefinedAmountBonus
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
from gui.shared.gui_items.fitting_item import FittingItem as FittingItem
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
DOSSIER_BADGE_ICON_PREFIX = 'badge_'
DOSSIER_ACHIEVEMENT_POSTFIX = '_achievement'
DOSSIER_BADGE_POSTFIX = '_badge'
EXCHANGE_RATE_TOKEN = 'exchangeRateToken'
VEHICLE_RENT_ICON_POSTFIX = '_rent'
BACKPORT_TOOLTIP_CONTENT_ID: Any
_logger: Any
WEEKLY_REWARDS_ORDER: tuple

class BaseBonusUIPacker(object):
    __collections: Any
    @classmethod
    def pack(cls, bonus):
        ...
    @classmethod
    def getToolTip(cls, bonus):
        ...
    @classmethod
    def getContentId(cls, bonus):
        ...
    def isAsync(self):
        ...
    def asyncPack(self, bonus, callback=None):
        ...
    def asyncGetToolTip(self, bonus, callback=None):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packCommon(cls, bonus, model):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _isCollectionItem(cls, collectionItemID):
        ...

class SimpleBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class TokenBonusUIPacker(BaseBonusUIPacker):
    _eventsCache: Any
    _RANKED_TOKEN_SOURCE = 'rankedPoint'
    _PM_POINTS_TOKEN_SOURCE = 'personal_missions_points'
    _BATTLE_BONUS_X5_TOKEN_SOURCE = 'bonus_battle_task'
    _CREW_BONUS_X3_TOKEN_SOURCE = 'crew_bonus_x3'
    _GOLD_MISSION_TOKEN_SOURCE = 'gold_mission'
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _isTokenForTooltipValid(cls, tokenID):
        ...
    @classmethod
    def _getTokenBonusPackers(cls):
        ...
    @classmethod
    def _packToken(cls, bonusPacker, bonus, *args):
        ...
    @classmethod
    def _getTokenBonusType(cls, tokenID, complexToken):
        ...
    @classmethod
    def _getTooltipsPackers(cls):
        ...
    @classmethod
    def __packComplexToken(cls, model, bonus, complexToken, token):
        ...
    @classmethod
    def __packRankedToken(cls, model, bonus, *args):
        ...
    @classmethod
    def __packBonusQuestToken(cls, name):
        ...
    @classmethod
    def __packGoldMissionToken(cls, model, bonus, *args):
        ...
    @classmethod
    def __packExchangeRateToken(cls, model, bonus, _, token):
        ...
    @staticmethod
    def __getBonusFactorTooltip(name):
        ...
    @classmethod
    def __getComplexToolTip(cls, complexToken, *_):
        ...
    @classmethod
    def __getRankedPointToolTip(cls, *_):
        ...
    @classmethod
    def __getGoldMissionTooltip(cls, complexToken, token):
        ...
    @classmethod
    def __getExchangeRateTooltip(cls, _, token):
        ...
    @classmethod
    def __getPMPointsTooltip(cls, *_):
        ...

class ItemBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @staticmethod
    def _itemsSortFunction(item):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, count):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class GoodiesBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBoosterBonus(cls, bonus, booster, count):
        ...
    @classmethod
    def _packSingleDemountKitBonus(cls, bonus, demountkit, count):
        ...
    @classmethod
    def _packRecertificationFormsBonus(cls, bonus, form, count):
        ...
    @classmethod
    def _packMentorLicensesBonus(cls, bonus, item, count):
        ...
    @classmethod
    def _packIconBonusModel(cls, bonus, icon, count, label):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class BlueprintBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class ExtendedBlueprintBonusUIPacker(BlueprintBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...

class CrewBookBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, book, count):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class CrewSkinBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, crewSkin, count, label):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class CustomizationBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getToolTipData(cls, itemCustomization):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class Customization3Dand2DbonusUIPacker(CustomizationBonusUIPacker):
    _3D_STYLE_ICON_NAME = 'style_3d'
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

class DossierBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packAchievements(cls, bonus):
        ...
    @classmethod
    def _packSingleAchievement(cls, achievement, bonus):
        ...
    @classmethod
    def _packBadges(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, dossierIconName, dossierNamePostfix, dossierValue, dossierLabel, recordName=None):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getAchievementTooltip(cls, bonus):
        ...
    @classmethod
    def _getBadgeTooltip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class TankmenBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getLabel(cls, group):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class TmanTemplateBonusPacker(BaseBonusUIPacker):
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

class VehiclesBonusUIPacker(BaseBonusUIPacker):
    _SPECIAL_ALIAS = TOOLTIPS_CONSTANTS.AWARD_VEHICLE
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getCompensation(cls, vehicle, bonus):
        ...
    @classmethod
    def _packVehicles(cls, bonus, vehicles):
        ...
    @classmethod
    def _packTooltips(cls, bonus, vehicles):
        ...
    @classmethod
    def _packCompensationTooltip(cls, bonusComp, vehicle):
        ...
    @classmethod
    def _packVehicle(cls, bonus, vehInfo, vehicle):
        ...
    @classmethod
    def _packTooltip(cls, bonus, vehicle, vehInfo):
        ...
    @staticmethod
    def _getRentExpiryTime(rentDays):
        ...
    @classmethod
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _createUIName(cls, bonus, isRent):
        ...
    @classmethod
    def _getLabel(cls, vehicle):
        ...

class DailyMissionsVehiclesBonusUIPacker(VehiclesBonusUIPacker):
    _SPECIAL_ALIAS = TOOLTIPS_CONSTANTS.EXTENDED_AWARD_VEHICLE
    @classmethod
    def _packTooltip(cls, bonus, vehicle, vehInfo):
        ...
    @classmethod
    def _packVehicleBonusModel(cls, bonus, vehInfo, isRent, vehicle):
        ...
    @classmethod
    def _getLabel(cls, vehicle):
        ...

class WeeklyMissionPremiumDaysPacker(SimpleBonusUIPacker):
    _ICONS_AVAILABLE: tuple
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...

class DogTagComponentsUIPacker(BaseBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packDogTag(cls, bonus, dogTagRecord):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _getDogTagTooltip(cls, dogTagRecord):
        ...

class GroupsBonusUIPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getIcon(cls, bonus):
        ...

class BattlePassPointsBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class CurrenciesBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packCommon(cls, bonus, model):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...

class BonusUIPacker(object):
    __packers: Any
    def __init__(self, packers=None):
        ...
    def pack(self, bonus):
        ...
    def getPackers(self):
        ...
    def _getBonusPacker(self, bonusName):
        ...
    def getToolTip(self, bonus):
        ...
    def getContentId(self, bonus):
        ...

class AsyncBonusUIPacker(BonusUIPacker):
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def requestData(self, bonus, callback=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def requestToolTip(self, bonus, callback=None):
        ...

class WoTPlusBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...

class UndefinedAmountBonusPacker(WoTPlusBonusPacker):
    @classmethod
    def _pack(cls, bonus):
        ...

class ExcludedMapsBonusPacker(UndefinedAmountBonusPacker):
    ...

class ExclusiveVehicleBonusPacker(UndefinedAmountBonusPacker):
    ...

class AttachmentsSetTokenBonusPacker(BaseBonusUIPacker):
    _ATTACHMENTS_SET_NAME_RES = R.strings.quests.bonusName.attachments_set
    _ATTACHMENTS_SET_TOOLTIP_RES = R.strings.tooltips.quests.bonuses.attachments_set
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, tokenID, token, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

def weeklyBonusSortKey(bonus):
    ...
def _bonusSortKey(sequence, bonus):
    ...
def getDefaultBonusPackersMap():
    ...
def getLocalizedBonusName(name):
    ...
def getDefaultBonusPacker():
    ...
def getDailyMissionsBonusPacker():
    ...
def getDailyMissionsMapping():
    ...
def getWeeklyMissionsBonusPacker():
    ...
def getWeeklyMissionsMapping():
    ...
def getPersonalMissionsBonusPacker():
    ...
def packMissionsBonusModelAndTooltipData(bonuses, packer, model, tooltipData=None, sortKey=None):
    ...
