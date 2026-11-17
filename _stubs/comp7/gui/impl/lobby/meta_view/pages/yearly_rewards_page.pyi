# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/yearly_rewards_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
from shared_utils import first as first, findFirst as findFirst
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior as GuiSettingsBehavior
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews, Rank as Rank, SeasonPointState as SeasonPointState
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.yearly_rewards_card_model import YearlyRewardsCardModel as YearlyRewardsCardModel, RewardsState as RewardsState
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.yearly_rewards_model import YearlyRewardsModel as YearlyRewardsModel, BannerState as BannerState
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_base_model import ProgressionItemBaseModel as ProgressionItemBaseModel
from comp7.gui.impl.gen.view_models.views.lobby.season_point_model import SeasonPointModel as SeasonPointModel
from comp7.gui.impl.gen.view_models.views.lobby.year_model import YearState as YearState
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import packYearlyRewardMetaView as packYearlyRewardMetaView
from comp7.gui.impl.lobby.comp7_helpers.comp7_c11n_helpers import getStylePreviewVehicle as getStylePreviewVehicle
from comp7.gui.impl.lobby.comp7_helpers.comp7_model_helpers import SEASONS_NUMBERS_BY_NAME as SEASONS_NUMBERS_BY_NAME
from comp7.gui.impl.lobby.comp7_helpers.comp7_model_helpers import setElitePercentage as setElitePercentage
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import hasAvailableOfferYearlyRewardGiftTokens as hasAvailableOfferYearlyRewardGiftTokens, hasYearlyRewardToken as hasYearlyRewardToken
from comp7.gui.impl.lobby.comp7_helpers.comp7_shared import getPlayerDivisionByRating as getPlayerDivisionByRating, getRankEnumValue as getRankEnumValue, getPlayerDivision as getPlayerDivision
from comp7.gui.impl.lobby.meta_view.meta_view_helper import getRankDivisions as getRankDivisions, setDivisionData as setDivisionData, setRankData as setRankData
from comp7.gui.impl.lobby.meta_view.pages import PageSubModelPresenter as PageSubModelPresenter
from comp7.gui.impl.lobby.tooltips.crew_members_tooltip import CrewMembersTooltip as CrewMembersTooltip
from comp7.gui.impl.lobby.tooltips.fifth_rank_tooltip import FifthRankTooltip as FifthRankTooltip
from comp7.gui.impl.lobby.tooltips.general_rank_tooltip import GeneralRankTooltip as GeneralRankTooltip
from comp7.gui.impl.lobby.tooltips.season_point_tooltip import SeasonPointTooltip as SeasonPointTooltip
from comp7.gui.impl.lobby.tooltips.sixth_rank_tooltip import SixthRankTooltip as SixthRankTooltip
from comp7.gui.impl.lobby.tooltips.style3d_tooltip import Style3dTooltip as Style3dTooltip
from comp7.gui.shared.event_dispatcher import showComp7YearlyRewardsSelectionWindow as showComp7YearlyRewardsSelectionWindow, showComp7StylePreview as showComp7StylePreview, showComp7MetaRootTab as showComp7MetaRootTab
from comp7_common_const import seasonPointsCodeBySeasonNumber as seasonPointsCodeBySeasonNumber
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum as getSeasonNameEnum
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_shared import getProgressionYearState as getProgressionYearState
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView as VehicleRolesTooltipView
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from items.vehicles import makeVehicleTypeCompDescrByName as makeVehicleTypeCompDescrByName
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
_DEFAULT_PREVIEW_VEHICLE = 'uk:GB91_Super_Conqueror'

class YearlyRewardsPage(PageSubModelPresenter):
    __slots__: tuple
    __comp7Controller: Any
    __c11nService: Any
    __itemsCache: Any
    __settingsCore: Any
    __tooltips: Any
    __bonusData: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def pageId(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def ranksConfig(self):
        ...
    def initialize(self, **params):
        ...
    def finalize(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def __onQualificationStateUpdated(self):
        ...
    def __onSeasonPointsUpdated(self):
        ...
    def __onSeasonPointsReloaded(self, isSuccess):
        ...
    def __onRankUpdated(self, *_):
        ...
    def __onConfigChanged(self):
        ...
    def __onRanksConfigChanged(self):
        ...
    def __onRewardsConfigChanged(self):
        ...
    def __onEntitlementsUpdated(self):
        ...
    # decorador original: @args2params(...)
    def __onStylePreviewOpen(self, cardIndex):
        ...
    # decorador original: @args2params(...)
    def __onVehiclePreviewOpen(self, cd, cardIndex):
        ...
    def __showStylePreview(self, styleBonus, cardIndex, vehicleCD=None):
        ...
    # decorador original: @args2params(...)
    def __onGoToRewardsSelection(self, name, cardIndex):
        ...
    def __setInitialAnimationViewed(self):
        ...
    def __onSyncCompleted(self, reason, *_):
        ...
    def __updateAllData(self):
        ...
    def __setCommonData(self, model):
        ...
    def __areActualSeasonPointsReceived(self):
        ...
    def __setSeasonData(self, model):
        ...
    def __setLegendData(self, model):
        ...
    def __setCards(self, model):
        ...
    def __getRewardStateForCard(self, cardSeasonPoints):
        ...
    def __fillRewards(self, cardModel, bonuses):
        ...
    @staticmethod
    def __setCardSeasonPoints(cardModel, cardSeasonPoints):
        ...
    def __setCardVehicleData(self, model, bonuses):
        ...
    def __setYearlyAnimationSeen(self):
        ...
    def __isYearlyAnimationSeen(self):
        ...

class _SeasonPointsGenerator(object):
    __comp7Controller: Any
    __allPointsStates: Any
    def __init__(self, areActualSeasonPointsReceived):
        ...
    def getNext(self, rewardsCount):
        ...
    def __composePointsStates(self, areActualSeasonPointsReceived):
        ...
    def __getAchievedPoints(self):
        ...
