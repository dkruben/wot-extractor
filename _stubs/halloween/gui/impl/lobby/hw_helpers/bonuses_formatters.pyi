# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/hw_helpers/bonuses_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController as IHalloweenTwitchConController
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK
from helpers import dependency as dependency
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from items.components.c11n_constants import Rarity as Rarity
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import CurtailingAwardsComposer as CurtailingAwardsComposer
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES, PreformattedBonus as PreformattedBonus, AwardsPacker as AwardsPacker, getDefaultFormattersMap as getDefaultFormattersMap, ItemsBonusFormatter as ItemsBonusFormatter, SimpleBonusFormatter as SimpleBonusFormatter, PremiumDaysBonusFormatter as PremiumDaysBonusFormatter, formatCountLabel as formatCountLabel, VehiclesBonusFormatter as VehiclesBonusFormatter, TokenBonusFormatter as TokenBonusFormatter, DossierBonusFormatter as DossierBonusFormatter, PostProcessTags as PostProcessTags, GoodiesBonusFormatter as GoodiesBonusFormatter, CustomizationsBonusFormatter as CustomizationsBonusFormatter, BattlePassBonusFormatter as BattlePassBonusFormatter, CrewBooksBonusFormatter as CrewBooksBonusFormatter, TmanTemplateBonusFormatter as TmanTemplateBonusFormatter
from gui.shared.gui_items.customization.c11n_items import ProjectionDecal as ProjectionDecal, Style as Style
from gui.shared.money import Currency as Currency
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN, LABEL_ALIGN as LABEL_ALIGN, TEXT_FORMATTERS as TEXT_FORMATTERS, TEXT_ALIGNS as TEXT_ALIGNS
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.formatters import text_styles as text_styles
from halloween.gui.halloween_gui_constants import HALLOWEEN_CAROUSEL_VEHICLE_TOOLTIP as HALLOWEEN_CAROUSEL_VEHICLE_TOOLTIP
from halloween_common.halloween_constants import ArtefactsSettings as ArtefactsSettings
from gui.shared.missions.packers.bonus import DOSSIER_ACHIEVEMENT_POSTFIX as DOSSIER_ACHIEVEMENT_POSTFIX, DOSSIER_BADGE_POSTFIX as DOSSIER_BADGE_POSTFIX
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from halloween_common.halloween_constants import HWStoryChoiceSettings as HWStoryChoiceSettings
_IMAGE_FORMAT = '.png'
_IMAGE_FORMAT_EXTEND = '.extend.png'
C11BonusArgs: Any

class HWItemsBonusFormatter(ItemsBonusFormatter):
    _OPTIONAL_DEVICE_TYPE = 'optionalDevice'
    _TROPHY_DEVICE_TYPE = 'trophyDevice'
    _MODERNIZED_DEVICE_TYPE = 'modernizedDevice'
    _CREW_BATTLE_BOOSTER_TYPE = 'crewBattleBooster'
    _DEVICE_BATTLE_BOOSTER_TYPE = 'deviceBattleBooster'
    _CONSUMABLE_TYPE = 'consumable'
    _SUBTYPE_ORDER: list
    def _getItemSubType(self, item):
        ...
    def _formatBonusLabel(self, count):
        ...
    def _getItemSortKey(self, item):
        ...
    def _getItems(self, bonus):
        ...

class HWCreditsBonusFormatter(SimpleBonusFormatter):
    @classmethod
    def _getLabel(cls, bonus):
        ...

class HWMetaPremiumDaysBonusFormatter(PremiumDaysBonusFormatter):
    def _format(self, bonus):
        ...

class HWVehiclesBonusFormatter(VehiclesBonusFormatter):
    @classmethod
    def _getLabel(cls, vehicle):
        ...
    def _getItems(self, bonus):
        ...
    def _appendFormattedVehicle(self, bonus, vehicle, vehInfo):
        ...

class HWVehiclesAwardsBonusFormatter(VehiclesBonusFormatter):
    @classmethod
    def _getImages(cls, vehicle, isRent=False):
        ...
    @classmethod
    def _getLabel(cls, vehicle):
        ...

class HWFakeTokenMedalBonusFormatter(TokenBonusFormatter):
    _FAKE_MEDAL_ICON: Any
    def _getFormattedBonus(self, tokenID, token, bonus):
        ...

class HWTokenBonusFormatter(TokenBonusFormatter):
    _KEY_ICON: Any
    _BATTLE_VEHICLE_BONUS_X5_TOKEN_PREFIX1 = 'xpx5_'
    _BATTLE_VEHICLE_BONUS_X5_TOKEN_PREFIX2 = 'expx5'
    def _getFormattedBonus(self, tokenID, token, bonus):
        ...
    def _formatVehicleBattleX5BonusToken(self, name, token, bonus):
        ...
    def _formatComplexToken(self, complexToken, token, bonus):
        ...
    def _crewFormattedBonus(self, tokenID):
        ...

class HWCerfTokenBonusFormatter(TokenBonusFormatter):
    twitchConCtrl: Any
    def _getFormattedBonus(self, tokenID, token, bonus):
        ...

class HWBattleResultBonusFormatter(HWTokenBonusFormatter):
    _KEY_ICON: Any

class HWDossierBonusFormatter(DossierBonusFormatter):
    def _format(self, bonus):
        ...

class HWCustomizationsBonusFormatter(CustomizationsBonusFormatter):
    _ORDER: tuple
    def _getSubtypePriority(self, c11item):
        ...
    def _format(self, bonus):
        ...
    def _getPriority(self, bonus):
        ...

class HWAwardsCustomizationsBonusFormatter(HWCustomizationsBonusFormatter):
    @classmethod
    def _getUserName(cls, c11nItem):
        ...

class HWGoodiesBonusFormatter(GoodiesBonusFormatter):
    _BOOSTERS_ORDER: list
    def _getBoosterSortKey(self, item):
        ...
    def _getBoosters(self, bonus):
        ...
    @classmethod
    def _getIcons(cls, item):
        ...
    @classmethod
    def _getImagesRecertificationForm(cls, form):
        ...
    @classmethod
    def _getMentoringLicenses(cls, item):
        ...
    @classmethod
    def _getDemountKitImages(cls, demountKit):
        ...

class HWBattlePassBonusFormatter(BattlePassBonusFormatter):
    @classmethod
    def _getLabel(cls, bonus):
        ...

class HWCrewBooksBonusFormatter(CrewBooksBonusFormatter):
    def _getItems(self, bonus):
        ...

class HWTmanTemplateBonusFormatter(TmanTemplateBonusFormatter):
    def _format(self, bonus):
        ...
    def __formatTmanTemplateToken(self, tokenID, _, bonus):
        ...

class HalloweenBonusesAwardsComposer(CurtailingAwardsComposer):
    def _packBonus(self, bonus, size=...):
        ...
    def _packMergedBonuses(self, mergedBonuses, size=...):
        ...

def getImgName(path):
    ...
def formatTokenBonusName(tokenID):
    ...
def getHWMetaFormattersMap():
    ...
def getAwardsHWMetaFormattersMap():
    ...
def getHWTwitchFormattersMap():
    ...
def getHWBattleResultFormattersMap():
    ...
def getHWMetaAwardFormatter(isAwardsScreen=False):
    ...
def getHWTwitchAwardFormatter():
    ...
def getHWBattleResultAwardFormatter():
    ...
