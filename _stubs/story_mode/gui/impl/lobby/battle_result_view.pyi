# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/battle_result_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from logging import getLogger as getLogger
import typing as typing
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import DISPLAY_ALL_AWARDS as DISPLAY_ALL_AWARDS
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.impl import backport as backport
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from story_mode.gui.impl.gen.view_models.views.lobby.battle_result_stat_tooltip_model import StatEnum as StatEnum
from story_mode.gui.impl.gen.view_models.views.lobby.battle_result_view_model import BattleResultViewModel as BattleResultViewModel
from story_mode.gui.impl.gen.view_models.views.lobby.progress_level_model import ProgressLevelModel as ProgressLevelModel
from story_mode.gui.impl.lobby.battle_result_stat_tooltip import BattleResultStatTooltip as BattleResultStatTooltip
from story_mode.gui.impl.mixins import DestroyWindowOnDisconnectMixin as DestroyWindowOnDisconnectMixin
from story_mode.gui.shared.event_dispatcher import showCongratulationsWindow as showCongratulationsWindow
from story_mode.gui.shared.utils import getTasksCount as getTasksCount, formatAndFillRewards as formatAndFillRewards
from story_mode.gui.sound_constants import POST_BATTLE_MUSIC_WIN as POST_BATTLE_MUSIC_WIN, POST_BATTLE_MUSIC_LOSE as POST_BATTLE_MUSIC_LOSE
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.skeletons.story_mode_fading_controller import IStoryModeFadingController as IStoryModeFadingController
from story_mode.uilogging.story_mode.consts import LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import PostBattleWindowLogger as PostBattleWindowLogger
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME, MissionType as MissionType
from wg_async import wg_async as wg_async
_logger: Any

class BattleResultView(ViewImpl):
    __slots__: tuple
    _MAX_OBJECTIVES_COUNT = 1
    _MAX_BONUSES_IN_VIEW = 7
    _ICON_OBJECTIVES = 'icon_battle_condition_win'
    _ICON_KILLS = 'icon_battle_condition_kill_vehicles'
    _ICON_DAMAGE = 'icon_battle_condition_damage'
    _ICON_ASSIST = 'icon_battle_condition_assist'
    _ICON_DAMAGE_BLOCKED = 'icon_battle_condition_damage_block'
    _MAIN_REWARDS: tuple
    _battleResultsService: Any
    _storyModeCtrl: Any
    _lobbyContext: Any
    _fadeManager: Any
    _battlePass: Any
    __arenaUniqueId: Any
    __idGen: Any
    _uiLogger: Any
    __bonusCache: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def __getDetailedStatsForStatTooltip(self, stat):
        ...
    def __getInfoListFotStatTooltip(self, stat):
        ...
    def __fillViewModel(self):
        ...
    def __fillProgressLevels(self, missionProgressModel, progressLevelsModels, battleResults):
        ...
    def __createProgressModel(self, value, icon, name, stat):
        ...
    def __fillRewards(self, mainRewardsModel, otherRewardsModel):
        ...
    # decorador original: @wg_async
    def __onClose(self):
        ...

class BattleResultsWindow(DestroyWindowOnDisconnectMixin, WindowImpl):
    __slots__: tuple
    def __init__(self, layer, **kwargs):
        ...
