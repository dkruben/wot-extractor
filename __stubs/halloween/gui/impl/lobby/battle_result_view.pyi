# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/battle_result_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from gui.impl import backport as backport
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.pub import WindowImpl as WindowImpl, ToolTipWindow as ToolTipWindow
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, TokensBonus as TokensBonus
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.impl.gen import R as R
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.shared.money import Currency as Currency
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import DISPLAY_ALL_AWARDS as DISPLAY_ALL_AWARDS
from halloween.gui.impl.gen.view_models.views.common.base_team_member_model import TeamMemberBanType as TeamMemberBanType
from halloween.gui.impl.gen.view_models.views.lobby.battle_result_view_model import BattleResultViewModel as BattleResultViewModel
from halloween.gui.impl.gen.view_models.views.lobby.reward_bonus_item_view_model import RewardBonusItemViewModel as RewardBonusItemViewModel
from halloween.gui.impl.lobby.hw_helpers.bonuses_formatters import HalloweenBonusesAwardsComposer as HalloweenBonusesAwardsComposer, getHWBattleResultAwardFormatter as getHWBattleResultAwardFormatter, getImgName as getImgName, formatTokenBonusName as formatTokenBonusName
from halloween.gui.impl.lobby.tooltips.key_tooltip import KeyTooltipView as KeyTooltipView
from halloween.gui.impl.lobby.widgets.battle_result_stats import BattleResultStats as BattleResultStats
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import PBS_ENTER as PBS_ENTER, PBS_EXIT as PBS_EXIT, VO as VO, VOObjects as VOObjects, DifficultyState as DifficultyState
from halloween.gui.game_control.halloween_artefacts_controller import getBonusPriority as getBonusPriority
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween_common.configs.halloween_loot import lootConfigSchema as lootConfigSchema
from halloween_common.halloween_constants import ArtefactsSettings as ArtefactsSettings, ARENA_BONUS_TYPE_TO_LEVEL as ARENA_BONUS_TYPE_TO_LEVEL
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from halloween.gui.impl.lobby.tooltips.ability_tooltip import AbilityTooltipView as AbilityTooltipView
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from helpers import dependency as dependency
from skeletons.gui.game_control import IEventBattlesController as IEventBattlesController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from halloween.gui.impl.lobby.base_view import BaseView as BaseView
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from gui.sounds.ambients import BattleResultsEnv as BattleResultsEnv
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
_R_BACKPORT_TOOLTIP: Any
_R_KEY_TOOLTIP: Any
_CURRENCIES: Any

class BattleResultView(BaseView):
    __slots__: tuple
    battleResults: Any
    lobbyContext: Any
    eventBattlesController: Any
    settingsCore: Any
    hwArtefactCtrl: Any
    eventsCache: Any
    itemsCache: Any
    _MAX_BONUSES_IN_VIEW = 6
    __sound_env__ = BattleResultsEnv
    __idGen: Any
    __bonusCache: Any
    __tooltipCtx: Any
    __arenaUniqueID: Any
    __totalVO: Any
    def __init__(self, **kwargs):
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
    def __getKeysBonus(self, keys):
        ...
    def __getHangarLootBonuses(self, hangarLoot):
        ...
    def __getHangarLootKeysAmount(self, hangarLootBonuses):
        ...
    def __getQuestBonuses(self, quests):
        ...
    def __getKeyCountFromTokens(self, tokens):
        ...

class BattleResultWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
