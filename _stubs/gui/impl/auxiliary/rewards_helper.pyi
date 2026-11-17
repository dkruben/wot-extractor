# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/auxiliary/rewards_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import itertools as itertools
from collections import namedtuple as namedtuple
from builtins import range as range
from future.utils import iteritems as iteritems, itervalues as itervalues
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from frameworks.wulf import ViewFlags as ViewFlags
from battle_royale.gui.constants import ROYALE_POSTBATTLE_REWARDS_COUNT as ROYALE_POSTBATTLE_REWARDS_COUNT
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.genConsts.PROGRESSIVEREWARD_CONSTANTS import PROGRESSIVEREWARD_CONSTANTS as prConst
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import BonusNameQuestsBonusComposer as BonusNameQuestsBonusComposer
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import LootBoxBonusComposer as LootBoxBonusComposer
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.compensation_tooltip import CompensationTooltipContent as CompensationTooltipContent
from gui.impl.auxiliary.tooltips.compensation_tooltip import CrewSkinsCompensationTooltipContent as CrewSkinsCompensationTooltipContent
from gui.impl.auxiliary.tooltips.compensation_tooltip import VehicleCompensationTooltipContent as VehicleCompensationTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.progressive_reward.progressive_reward_step_model import ProgressiveRewardStepModel as ProgressiveRewardStepModel
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_model import LootBoxCompensationTooltipModel as LootBoxCompensationTooltipModel
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes as LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel as LootBoxVehicleCompensationTooltipModel
from gui.impl.gen.view_models.views.loot_box_view.blueprint_final_fragment_renderer_model import BlueprintFinalFragmentRendererModel as BlueprintFinalFragmentRendererModel
from gui.impl.gen.view_models.views.loot_box_view.blueprint_fragment_renderer_model import BlueprintFragmentRendererModel as BlueprintFragmentRendererModel
from gui.impl.gen.view_models.views.loot_box_view.crew_book_renderer_model import CrewBookRendererModel as CrewBookRendererModel
from gui.impl.gen.view_models.views.loot_box_view.congrats_view_model import CongratsViewModel as CongratsViewModel
from gui.impl.gen.view_models.views.loot_box_view.loot_compensation_renderer_model import LootCompensationRendererModel as LootCompensationRendererModel
from gui.impl.gen.view_models.views.loot_box_view.loot_congrats_types import LootCongratsTypes as LootCongratsTypes
from gui.impl.gen.view_models.views.loot_box_view.loot_def_renderer_model import LootDefRendererModel as LootDefRendererModel
from gui.impl.gen.view_models.views.loot_box_view.loot_animated_renderer_model import LootAnimatedRendererModel as LootAnimatedRendererModel
from gui.impl.gen.view_models.views.loot_box_view.loot_vehicle_compensation_renderer_model import LootVehicleCompensationRendererModel as LootVehicleCompensationRendererModel
from gui.impl.gen.view_models.views.loot_box_view.loot_conversion_renderer_model import LootConversionRendererModel as LootConversionRendererModel
from gui.impl.gen.view_models.views.loot_box_view.loot_renderer_types import LootRendererTypes as LootRendererTypes
from gui.impl.gen.view_models.views.loot_box_view.loot_vehicle_renderer_model import LootVehicleRendererModel as LootVehicleRendererModel
from gui.impl.lobby.seniority_awards.seniority_awards_bonuses_packers import getSeniorityAwardsBonusPacker as getSeniorityAwardsBonusPacker
from gui.server_events.awards_formatters import getPackRentVehiclesAwardPacker as getPackRentVehiclesAwardPacker, getLootboxesAwardsPacker as getLootboxesAwardsPacker, getRoyaleAwardsPacker as getRoyaleAwardsPacker, AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, BlueprintsBonusSubtypes as BlueprintsBonusSubtypes
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import Vehicle as Vehicle, GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import getCrewSkinIconBig as getCrewSkinIconBig
from gui.shared.gui_items.crew_skin import localizedFullName as localizedFullName
from gui.shared.money import ZERO_MONEY as ZERO_MONEY, Money as Money, Currency as Currency
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.requesters.blueprints_requester import getUniqueBlueprints as getUniqueBlueprints
from helpers import dependency as dependency, int2roman as int2roman
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
STYLES_TAGS: list
VIDEO_TAGS: list
_logger: Any
_DEFAULT_ALIGN = 'center'
_DEFAULT_DISPLAYED_AWARDS_COUNT = 6
TMAN_TOKENS = 'tmanToken'
NEW_STYLE_FORMATTED_BONUSES: Any
_BONUSES_ORDER: tuple
BLUEPRINTS_CONGRAT_TYPES: tuple
_COMPENSATION_TOOLTIP_CONTENT_RES_IDS: tuple
_COMPENSATION_TOOLTIP_CONTENT_CLASSES: dict
_MIN_PROBABILITY = 7
_MAX_PROBABILITY = 15
_MIN_VEHICLE_LVL_BLUEPRINT_AWARD = 8
SeniorityAwards: Any
_DEF_CONGRATS_VALIDATORS: dict
_DEF_MODEL_PRESENTER: Any
DEF_COMPENSATION_PRESENTERS: dict
DEF_MODEL_PRESENTERS: dict
RANKED_MODEL_PRESENTERS: dict

class BlueprintBonusTypes(object):
    BLUEPRINTS = 'blueprints'
    FINAL_BLUEPRINTS = 'finalBlueprints'
    BLUEPRINTS_ANY = 'blueprintsAny'
    ALL: tuple

class CrewBonusTypes(object):
    CREW_BOOK_BONUSES = 'crewBooks'
    CREW_SKIN_BONUSES = 'crewSkins'
    ALL: tuple

class LootRewardDefModelPresenter(object):
    __slots__: tuple
    _reward: Any
    def __init__(self):
        ...
    def getModel(self, reward, ttId, isSmall=False, showCongrats=False, isEpic=False):
        ...
    def _setReward(self, reward):
        ...
    def _createModel(self):
        ...
    def _getRendererType(self):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...

class LootRewardAnimatedModelPresenter(LootRewardDefModelPresenter):
    __slots__: tuple
    __anmType: Any
    __anmRes: Any
    __soundId: Any
    def __init__(self, anmType, anmUrl=..., soundId=...):
        ...
    def _createModel(self):
        ...
    def _getRendererType(self):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...

class LootRewardConversionModelPresenter(LootRewardAnimatedModelPresenter):
    __slots__: tuple
    __iconFrom: Any
    def __init__(self, iconFrom, soundId=...):
        ...
    def _createModel(self):
        ...
    def _getRendererType(self):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...

class CompensationModelPresenter(LootRewardAnimatedModelPresenter):
    __slots__: tuple
    def __init__(self, soundId=...):
        ...
    def _createModel(self):
        ...
    def _getRendererType(self):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...

class CrewSkinsCompensationModelPresenter(CompensationModelPresenter):
    __slots__: tuple
    def _getRendererType(self):
        ...

class VehicleCompensationModelPresenter(CompensationModelPresenter):
    __slots__: tuple
    itemsCache: Any
    def _createModel(self):
        ...
    def _getRendererType(self):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...

class BlueprintFinalFragmentModelPresenter(LootRewardAnimatedModelPresenter):
    __slots__: tuple
    __itemsCache: Any
    __vehicle: Any
    def __init__(self):
        ...
    def _createModel(self):
        ...
    def _getRendererType(self):
        ...
    def _setReward(self, reward):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...
    def _formatVehicle(self, vehicle, model, showCongrats):
        ...
    @classmethod
    def validate(cls, reward, rewardType):
        ...

class CrewBookModelPresenter(LootRewardDefModelPresenter):
    __slots__: tuple
    __itemsCache: Any
    def _createModel(self):
        ...
    def _getRendererType(self):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...
    @classmethod
    def validate(cls, reward, rewardType):
        ...

class BlueprintFragmentRewardPresenter(LootRewardDefModelPresenter):
    __slots__: tuple
    __itemsCache: Any
    _vehicle: Any
    def __init__(self):
        ...
    def _setReward(self, reward):
        ...
    def _getRendererType(self):
        ...
    def _createModel(self):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...
    def _formatVehicle(self, vehicle, model, showCongrats):
        ...
    @classmethod
    def validate(cls, reward, rewardType):
        ...

class LootVehicleRewardPresenter(LootRewardDefModelPresenter):
    __itemsCache: Any
    __slots__: tuple
    _vehicle: Any
    def __init__(self):
        ...
    def _setReward(self, reward):
        ...
    def _getRendererType(self):
        ...
    def _createModel(self):
        ...
    def _formatModel(self, model, ttId, showCongrats):
        ...
    def _formatVehicle(self, vehicle, model, showCongrats):
        ...

def getVehicleStrID(vehicleName):
    ...
def preparationRewardsCurrency(rewards):
    ...
def checkAndFillVehicles(bonus, alwaysVisibleBonuses, bonuses):
    ...
def checkAndFillCustomizations(bonus, alwaysVisibleBonuses, bonuses):
    ...
def checkAndFillTokens(bonus, alwaysVisibleBonuses, bonuses):
    ...
def formatEliteVehicle(isElite, typeName):
    ...
def splitPremiumDays(days):
    ...
def getRewardsBonuses(rewards, size=..., awardsCount=...):
    ...
def getRewardRendererModelPresenter(reward, presenters=None, compensationPresenters=None, defPresenter=...):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRewardTooltipContent(event, storedTooltipData=None, itemsCache=None):
    ...
def getSeniorityAwardsVehicles(vehiclesRewards, sortKey=None):
    ...
def getSeniorityAwardsBonuses(rewards, excluded=..., sortKey=None):
    ...
def getProgressiveRewardBonuses(rewards, size='big', maxAwardCount=..., packBlueprints=False, ctx=None):
    ...
def getRoyaleBonuses(bonuses, size='big'):
    ...
def getRoyaleBonusesFromDict(rewards, size='big'):
    ...
def fillStepsModel(currentStep, probability, maxSteps, hasCompleted, stepsModel):
    ...
def getProgressiveRewardVO(currentStep, probability, maxSteps, descText='', isEnabled=True, showBg=False, align=..., isHighTitle=False, hasCompleted=False):
    ...
def getLastCongratsIndex(bonuses, rewardType):
    ...
def _getProgressiveSteps(currentStep, probability, maxSteps, hasCompleted=False):
    ...
def _getProgressiveStepsVO(currentStep, probability, maxSteps, hasCompleted=False):
    ...
def _isVideoVehicle(vehicle):
    ...
def _getStyleCDByVehCD(vehCD):
    ...
def _getVehiclesWithStyle(styleTags):
    ...
def _hasSpecialTag(entity, tags):
    ...
def _isSpecialStyle(styleIntCD):
    ...
def _checkAndFillBlueprints(blueprintsList, alwaysVisibleBonuses, bonuses):
    ...
def checkAndFillItems(itemsList, alwaysVisibleBonuses, bonuses):
    ...
def _getCompensationMoney(bonuses):
    ...
def _keySortOrder(bonus):
    ...
def _getVehicleFromReward(reward):
    ...
def _fillVehicleBlueprintCongratsModel(vehicle, model, itemsCache, congratsType, showCongrats):
    ...
def _fillCrewBookCongratsModel(model, congratsType, showCongrats):
    ...
def _packBlueprints(rewards):
    ...
