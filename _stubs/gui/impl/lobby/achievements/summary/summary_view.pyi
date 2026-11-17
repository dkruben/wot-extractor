# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/summary/summary_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ACHIEVEMENTS_VISITED as ACHIEVEMENTS_VISITED
from achievements20.WTRStageChecker import WTRStageChecker as WTRStageChecker
from adisp import adisp_process as adisp_process
from constants import AchievementsLayoutStates as AchievementsLayoutStates, Configs as Configs
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.config.common import ComponentViewType as ComponentViewType
from dog_tags_common.player_dog_tag import PlayerDogTag as PlayerDogTag
from dossiers2.ui.achievements import ACHIEVEMENT_SECTION as ACHIEVEMENT_SECTION
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.achievements.achievements_helper import fillAchievementModel as fillAchievementModel, convertDbIdsToAchievements as convertDbIdsToAchievements
from gui.clans.clan_cache import ClanInfo as ClanInfo
from gui.clans.formatters import getClanRoleString as getClanRoleString
from gui.dog_tag_composer import DogTagComposerClient as DogTagComposerClient
from gui.game_control.wot_plus.service_record_customization.service_record_customization import ServiceRecordAssetManager as ServiceRecordAssetManager
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.achievements.achievements_constants import KPITypes as KPITypes
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.background_model import BackgroundModel as BackgroundModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.ribbon_model import RibbonModel as RibbonModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.statistic_item_model import StatisticItemModel as StatisticItemModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.summary_view_model import SummaryViewModel as SummaryViewModel, EditState as EditState
from gui.impl.lobby.achievements.profile_utils import getProfileCommonInfo as getProfileCommonInfo, formatPercent as formatPercent, getFormattedValue as getFormattedValue, getNormalizedValue as getNormalizedValue, isSummaryEnabled as isSummaryEnabled, isWTREnabled as isWTREnabled, getRating as getRating, isEditingEnabled as isEditingEnabled, isLayoutEnabled as isLayoutEnabled, getMasteryStatistic as getMasteryStatistic
from gui.impl.lobby.achievements.tooltips.battles_kpi_tooltip import BattlesKPITooltip as BattlesKPITooltip
from gui.impl.lobby.achievements.tooltips.editing_tooltip import EditingTooltip as EditingTooltip
from gui.impl.lobby.achievements.tooltips.kpi_tooltip import KPITooltip as KPITooltip
from gui.impl.lobby.achievements.tooltips.wotpr_main_tooltip import WOTPRMainTooltip as WOTPRMainTooltip
from gui.impl.lobby.achievements.tooltips.wtr_info_tooltip import WTRInfoTooltip as WTRInfoTooltip
from gui.impl.lobby.achievements.tooltips.wtr_main_tooltip import WTRMainTooltip as WTRMainTooltip
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.dog_tags.animated_dog_tag_grade_tooltip import AnimatedDogTagGradeTooltip as AnimatedDogTagGradeTooltip
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showAchievementEditView as showAchievementEditView, showClanProfileWindow as showClanProfileWindow, showAchievementCustomisationEditView as showAchievementCustomisationEditView
from gui.shared.gui_items.dossier import dumpDossier as dumpDossier
from gui.shared.gui_items.dossier.achievements.abstract import isRareAchievement as isRareAchievement
from gui.shared.view_helpers.emblems import getClanEmblemURL as getClanEmblemURL, EmblemSize as EmblemSize
from helpers import dependency as dependency, server_settings as server_settings
from skeletons.gui.game_control import IAchievements20Controller as IAchievements20Controller
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Tuple as Tuple, List as List
from Event import Event as Event
_logger: Any
_STATISTIC_LIST_ORDER: tuple
_CDN_SYNC_TIMEOUT = 10

class SummaryView(SubModelPresenter):
    __slots__: tuple
    __itemsCache: Any
    __lobbyContext: Any
    __achvmntCtrl: Any
    _wotPlusCtrl: Any
    __dossier: Any
    __uniqueAwardsCount: Any
    __prevRatingRank: Any
    __prevRatingSubRank: Any
    __userId: Any
    def __init__(self, summaryModel, parentView, userId):
        ...
    @property
    def viewModel(self):
        ...
    def getParentWindow(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    # decorador original: @adisp_process
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getCustomizationData(self):
        ...
    def _onSetIsInCustomizationMode(self, _):
        ...
    def __updatePage(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateSettings(self, model=None):
        ...
    def __updateUserInfo(self):
        ...
    def __getStatistic(self):
        ...
    def __fillStatistic(self):
        ...
    def __getAchievementsStats(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateSignificantAchievements(self, model=None):
        ...
    def __getSignificantAchievementsList(self):
        ...
    def __updateRating(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
    def __onAchievementsSettings(self):
        ...
    def __dossierResyncHandler(self, *_):
        ...
    def __getEditState(self):
        ...
    def __getDogTagBackportTooltipData(self, compId):
        ...
    def __getAchievementsBackportTooltipData(self, name, block):
        ...
    def __getPrevStates(self):
        ...
    def __setPrevStates(self):
        ...
    def __setPrevAchievementList(self):
        ...
    def __showNotification(self):
        ...
    def __updateClanInfo(self):
        ...
    def __fillDogTagModel(self, model):
        ...
    def __openClanStatistic(self):
        ...
    def __onAchievementLayoutChanged(self, ctx):
        ...
    def __onEditViewClose(self, ctx):
        ...
    @property
    def __isOtherPlayer(self):
        ...
    def __updateCustomizationsOptions(self):
        ...
    def __updateCustomizationsVisuals(self):
        ...
    def __onRenewableSubscriptionStatusChanged(self):
        ...
