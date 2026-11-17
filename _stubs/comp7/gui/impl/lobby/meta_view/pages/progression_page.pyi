# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.AccountSettings import COMP7_UI_SECTION as COMP7_UI_SECTION, COMP7_PROGRESSION_PAGE_C11N_PROGRESS as COMP7_PROGRESSION_PAGE_C11N_PROGRESS
from adisp import adisp_process as adisp_process
from comp7.gui.event_boards.event_boards_items import DailyVehicleData as DailyVehicleData
from comp7.gui.impl.gen.view_models.views.lobby.enums import Division as Division, MetaRootViews as MetaRootViews, Rank as Rank, SeasonName as SeasonName, StatisticsMode as StatisticsMode
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.customization_tasks_model import CustomizationTasksModel as CustomizationTasksModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.day_statistics_model import DayStatisticsModel as DayStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.top_vehicle_statistics_model import TopVehicleStatisticsModel as TopVehicleStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_model import ProgressionItemModel as ProgressionItemModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.progression_model import ProgressionModel as ProgressionModel, PageState as PageState
from comp7.gui.impl.lobby.comp7_helpers import comp7_model_helpers as comp7_model_helpers, comp7_shared as comp7_shared, comp7_qualification_helpers as comp7_qualification_helpers
from comp7.gui.impl.lobby.comp7_helpers.comp7_c11n_helpers import getComp7ProgressionStyle as getComp7ProgressionStyle, isC11nItemTokenAttainable as isC11nItemTokenAttainable, getVehicleForStyle as getVehicleForStyle, getMaxLevelAndBattlesVehicleSortKey as getMaxLevelAndBattlesVehicleSortKey, selectStyleAndDecalInC11nHangar as selectStyleAndDecalInC11nHangar
from gui.SystemMessages import pushMessage as pushMessage, SM_TYPE as SM_TYPE
from gui.impl.backport import text as text
from gui.impl.backport.backport_tooltip import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from comp7.gui.impl.lobby.comp7_helpers.comp7_gui_helpers import ProgressCacherUI as ProgressCacherUI
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import getDescriptionAndProgressFromC11nDecalQuest as getDescriptionAndProgressFromC11nDecalQuest
from comp7.gui.impl.lobby.meta_view import meta_view_helper as meta_view_helper
from comp7.gui.impl.lobby.meta_view.pages import PageSubModelPresenter as PageSubModelPresenter
from comp7.gui.impl.lobby.tooltips.day_tooltip import DayTooltip as DayTooltip
from comp7.gui.impl.lobby.tooltips.rank_indicator_tooltip import RankIndicatorTooltip as RankIndicatorTooltip
from comp7.gui.impl.lobby.tooltips.battles_indicator_tooltip import BattlesIndicatorTooltip as BattlesIndicatorTooltip
from comp7.gui.impl.lobby.tooltips.wins_indicator_tooltip import WinsIndicatorTooltip as WinsIndicatorTooltip
from comp7.gui.impl.lobby.tooltips.damage_indicator_tooltip import DamageIndicatorTooltip as DamageIndicatorTooltip
from comp7.gui.impl.lobby.tooltips.prestige_indicator_tooltip import PrestigeIndicatorTooltip as PrestigeIndicatorTooltip
from comp7.gui.impl.lobby.tooltips.division_tooltip import DivisionTooltip as DivisionTooltip
from comp7.gui.impl.lobby.tooltips.fifth_rank_tooltip import FifthRankTooltip as FifthRankTooltip
from comp7.gui.impl.lobby.tooltips.general_rank_tooltip import GeneralRankTooltip as GeneralRankTooltip
from comp7.gui.impl.lobby.tooltips.last_update_tooltip import LastUpdateTooltip as LastUpdateTooltip
from comp7.gui.impl.lobby.tooltips.progression_table_tooltip import ProgressionTableTooltip as ProgressionTableTooltip
from comp7.gui.impl.lobby.tooltips.rank_inactivity_tooltip import RankInactivityTooltip as RankInactivityTooltip
from comp7.gui.impl.lobby.tooltips.sixth_rank_tooltip import SixthRankTooltip as SixthRankTooltip
from comp7.gui.shared.event_dispatcher import showComp7MetaRootTab as showComp7MetaRootTab, showComp7SeasonVehiclesStatisticsView as showComp7SeasonVehiclesStatisticsView
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView as VehicleRolesTooltipView
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.notifications import NotificationPriorityLevel as Priority
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round, round_py2_style_int as round_py2_style_int
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from typing import List as List, Iterable as Iterable, Tuple as Tuple, Optional as Optional
from comp7.gui.shared.gui_items.dossier.stats import AccountComp7StatsBlock as AccountComp7StatsBlock
from comp7.gui.shared.gui_items.dossier.stats import Comp7StatsBlock as Comp7StatsBlock
from comp7.gui.event_boards.event_boards_items import AggregatedDailyData as AggregatedDailyData, Comp7PlayerProgression as Comp7PlayerProgression, DailyData as DailyData
from comp7.helpers.comp7_server_settings import Comp7RanksConfig as Comp7RanksConfig
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
CustData: Any
_logger: Any

class ProgressionPage(PageSubModelPresenter):
    __comp7Controller: Any
    __itemsCache: Any
    __c11n: Any
    __lastUpdateTime: Any
    __custProgQuestIDs: Any
    __progressionData: Any
    __selectedDayIndex: Any
    __c11nProgressCacher: Any
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
    def __updateData(self, *_):
        ...
    def __updateQualificationData(self):
        ...
    def __updateProgressionData(self, *_):
        ...
    def __onClientUpdated(self, diff, _):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateSeasonStats(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateDailyStats(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateSeasonVehicleStats(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateDailyVehicleStats(self, dayIndex, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setCurrentScore(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setRanksItems(self, model=None):
        ...
    # decorador original: @adisp_process
    def __setLeaderBoardAsyncData(self):
        ...
    def __onProgressionDataUpdate(self):
        ...
    def __onRankRewardsPageOpen(self):
        ...
    # decorador original: @args2params(...)
    def __onSelectDay(self, index):
        ...
    def __onOpenVehicleStats(self):
        ...
    def __onRefresh(self):
        ...
    def __updateCustomizationTasks(self):
        ...
    def __populateCustomizationTasksModels(self, itemsData):
        ...
    def __onCustomizationProgressShown(self, args):
        ...
    def __onOpenCustomization(self, args):
        ...

def _c11nTaskSortKey(data):
    ...
