# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/battle_result_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.builtins import range as range
import WWISE as WWISE
import ArenaType as ArenaType
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.pub import WindowImpl as WindowImpl
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, TokensBonus as TokensBonus
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.impl.gen import R as R
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.money import Currency as Currency
from last_stand.gui.game_control.ls_artefacts_controller import getBonusPriority as getBonusPriority
from last_stand.gui.game_control.ls_difficulty_missions_controller import getFormattedMissionsList as getFormattedMissionsList
from last_stand.gui.impl.gen.view_models.views.common.base_team_member_model import TeamMemberBanType as TeamMemberBanType
from last_stand.gui.impl.gen.view_models.views.lobby.battle_result_view_model import BattleResultViewModel as BattleResultViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel as BonusItemViewModel
from last_stand.gui.impl.lobby.ls_helpers.bonuses_formatters import LSBonusesAwardsComposer as LSBonusesAwardsComposer, getLSBattleResultAwardFormatter as getLSBattleResultAwardFormatter, getImgName as getImgName
from last_stand.gui.impl.lobby.tooltips.points_tooltip import PointsTooltipView as PointsTooltipView
from last_stand.gui.impl.lobby.tooltips.difficulty_tooltip import DifficultyTooltipView as DifficultyTooltipView
from last_stand.gui.impl.lobby.widgets.battle_result_stats import BattleResultStats as BattleResultStats
from last_stand.gui.sounds import playSound as playSound
from last_stand.gui.sounds.sound_constants import PBS_ENTER as PBS_ENTER, PBS_EXIT as PBS_EXIT, LastStandVO as LastStandVO, DifficultyState as DifficultyState
from last_stand.gui.shared.event_dispatcher import showLootBoxMainViewInQueue as showLootBoxMainViewInQueue
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController as ILSArtefactsController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_difficulty_missions_controller import ILSDifficultyMissionsController as ILSDifficultyMissionsController
from last_stand.skeletons.ls_quests_ui_cache import ILSQuestsUICache as ILSQuestsUICache
from last_stand_common.last_stand_constants import ProgressPointsSettings as ProgressPointsSettings, ARENA_BONUS_TYPE_TO_LEVEL as ARENA_BONUS_TYPE_TO_LEVEL, LS_VEHILCE_DAILY_QUEST as LS_VEHILCE_DAILY_QUEST
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from helpers import dependency as dependency
from skeletons.gui.game_control import IEventBattlesController as IEventBattlesController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from last_stand.gui.impl.lobby.base_view import BaseView as BaseView
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from gui.sounds.ambients import BattleResultsEnv as BattleResultsEnv
from skeletons.gui.shared import IItemsCache as IItemsCache
_R_BACKPORT_TOOLTIP: Any
_R_POINTS_TOOLTIP: Any

class BattleResultView(BaseView):
    __slots__: tuple
    battleResults: Any
    lobbyContext: Any
    eventBattlesController: Any
    settingsCore: Any
    lsCtrl: Any
    lsArtifactsCtrl: Any
    itemsCache: Any
    lsDifficultyMissionsCtrl: Any
    questsCache: Any
    _MAX_BONUSES_IN_VIEW = 7
    __sound_env__ = BattleResultsEnv
    __idGen: Any
    __bonusCache: Any
    __tooltipCtx: Any
    __arenaUniqueID: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createContextMenu(self, event):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __fillViewModel(self):
        ...
    def __fillCommonInfo(self, model, totalVO):
        ...
    def __fillPlayerInfo(self, playerInfo, totalVO):
        ...
    def __fillRewardsInfo(self, model, totalVO):
        ...
    def __playVoiceover(self, totalVO):
        ...
    def __getLeaderboardPosition(self, players, personal, field):
        ...
    def __getCreditsBonus(self, credits):
        ...
    def __getProgressPointsBonus(self, points):
        ...
    def __getQuestBonuses(self, quests):
        ...
    def __checkLootBox(self, bonuses):
        ...
    def __geProgressPointsCountFromTokens(self, tokens):
        ...
    def __getDailyProgressPoints(self, bonuses):
        ...
    def __getPersonalVO(self, totalVO):
        ...
    def __filterBonuses(self, bonuses, exclude=None):
        ...

class BattleResultWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
