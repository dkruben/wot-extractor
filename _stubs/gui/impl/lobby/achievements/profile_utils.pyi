# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/profile_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from advanced_achievements_client.items import VirtualStepAchievement as VirtualStepAchievement, RegularAchievement as RegularAchievement, SteppedAchievement as SteppedAchievement
from dossiers2.custom.dependencies import VEHICLE_ACHIEVEMENTS_DEPENDENCIES as VEHICLE_ACHIEVEMENTS_DEPENDENCIES, CUSTOMIZATION_ACHIEVEMENTS_DEPENDENCIES as CUSTOMIZATION_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.ui.achievements import ACHIEVEMENT_SECTION as ACHIEVEMENT_SECTION, ACHIEVEMENT_SECTIONS_INDICES as ACHIEVEMENT_SECTIONS_INDICES
from gui.impl import backport as backport
from gui.impl.backport import getIntegralFormat as getIntegralFormat
from gui.impl.backport.backport_tooltip import TooltipData as TooltipData
from gui.impl.gen.view_models.constants.date_time_formats import DateTimeFormatsEnum as DateTimeFormatsEnum
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementType as AdvancedAchievementType, AdvancedAchievementModel as AdvancedAchievementModel, AdvancedAchievementIconPosition as AdvancedAchievementIconPosition, AdvancedAchievementIconSizeMap as AdvancedAchievementIconSizeMap
from gui.impl.gen.view_models.views.lobby.achievements.subcategory_advanced_achievement_model import SubcategoryAdvancedAchievementModel as SubcategoryAdvancedAchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.rewards_model import RewardsModel as RewardsModel, DogTagType as DogTagType
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.details_model import DetailsModel as DetailsModel, ProgressType as ProgressType
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.achievement_card_model import AchievementCardModel as AchievementCardModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.breadcrumb_model import BreadcrumbModel as BreadcrumbModel
from gui.impl.gen.view_models.views.lobby.achievements.views.reward_view_rewards_model import RewardViewRewardsModel as RewardViewRewardsModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.dog_tags.catalog_animated_dog_tag_tooltip import CatalogAnimatedDogTagTooltip as CatalogAnimatedDogTagTooltip
from gui.impl.lobby.dog_tags.dog_tag_processors import getCoupledDogTagProgress as getCoupledDogTagProgress
from gui.shared.formatters import text_styles as text_styles
from gui.shared.formatters.date_time import getRegionalDateTime as getRegionalDateTime
from gui.shared.gui_items.Vehicle import getNationLessName as getNationLessName
from helpers import dependency as dependency
from advanced_achievements_client.getters import getAchievementByID as getAchievementByID
from items import vehicles as vehicles
from shared_utils import first as first
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from advanced_achievements_client.constants import AchievementType as AchievementType
from gui.shared.missions.packers.bonus import CustomizationBonusUIPacker as CustomizationBonusUIPacker, BonusUIPacker as BonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, DogTagComponentsUIPacker as DogTagComponentsUIPacker, BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID
from dog_tags_common.components_config import componentConfigAdapter as componentConfig
from dog_tags_common.config.common import ComponentViewType as ComponentViewType, ComponentPurpose as ComponentPurpose
from gui.impl.gen import R as R
from advanced_achievements_client.items import _BaseGuiAchievement as _BaseGuiAchievement, _Progress as _Progress
from dog_tags_common.config.dog_tag_framework import ComponentDefinition as ComponentDefinition
from typing import Optional as Optional, Dict as Dict, Tuple as Tuple, Iterator as Iterator, List as List
from gui.server_events.bonuses import CustomizationsBonus as CustomizationsBonus, DogTagComponentBonus as DogTagComponentBonus
_ACHIEVEMENT_TYPE_MAP: dict
MAX_PERCENT_VALUE = 100

class AdvancedAchievementsCustomizationsBonusPacker(CustomizationBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

class AdvancedAchievementsDogTagsBonusPacker(DogTagComponentsUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getBonusIterator(cls, bonus):
        ...
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
    def _getCoupledDogTagTooltip(cls, component):
        ...
    @classmethod
    def _packDogTag(cls, bonus, component, dogTagRecord):
        ...
    @classmethod
    def _packCoupledDogTag(cls, bonus, component, dogTagRecord):
        ...

class RewardViewDogTagsBonusPacker(AdvancedAchievementsDogTagsBonusPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packDogTag(cls, bonus, component, dogTagRecord):
        ...
    @classmethod
    def _packCoupledDogTag(cls, bonus, component, dogTagRecord):
        ...
    @classmethod
    def _getDogTagProgress(cls, component):
        ...
    @classmethod
    # decorador original: @dependency.replace_none_kwargs(...)
    def _getDossier(cls, itemsCache=None):
        ...

class AdvancedAchievementHintChecker(object):
    __settingsCore: Any
    def check(self, aliasId):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isLayoutEnabled(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isSummaryEnabled(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isWTREnabled(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getStagesOfWTR(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getLayoutLength(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isEditingEnabled(itemsCache=None, lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRating(itemsCache=None, userId=None):
    ...
# decorador original: @adisp_process
def _receiveRating(itemsCache, userId, result):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAllAchievements(itemsCache=None):
    ...
def getProfileCommonInfo(dossier):
    ...
def getMasteryStatistic(dossier):
    ...
def getNormalizedValue(targetValue):
    ...
def getFormattedValue(targetValue):
    ...
def formatPercent(value):
    ...
def fillAdvancedAchievementModel(achievement, achievementModel=None, withCurrentStage=False):
    ...
def fillSubcategoryAdvancedAchievementModel(achievement, bubbles, prevScore, prevValue, achievementModel=None):
    ...
def getAdvancedAchievementsBonusPackersMap():
    ...
def getAdvancedAchievementsBonusPacker():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillDetailsModel(achievement, tooltipData, detailsModel=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillAchievementCardModel(achievement, tooltipData, bubbles, itemsCache=None, achievementCardModel=None):
    ...
def fillBreadcrumbModel(achievement, breadcrumbModel=None):
    ...
def getVehicleByName(name):
    ...
def getTrophiesData():
    ...
def createAdvancedAchievementsCatalogInitAchievementIDs(achievementID, achievementCategory):
    ...
def createBackportTooltipDecorator():
    ...
def createTooltipContentDecorator(uiParent):
    ...
def getRewardViewBonusPacker():
    ...
