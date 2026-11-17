# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/battle_result_view/battle_result_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from collections import OrderedDict as OrderedDict
from future.utils import viewvalues as viewvalues, viewitems as viewitems
from typing import Any as Any, Dict as Dict, TYPE_CHECKING as TYPE_CHECKING
import SoundGroups as SoundGroups
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from battle_royale.gui.impl.lobby.tooltips.reward_currency_tooltip_view import RewardCurrencyTooltipView as RewardCurrencyTooltipView
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from frameworks.wulf import WindowFlags as WindowFlags
from gui.impl import backport as backport
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.battle_result_view_model import BattleResultViewModel as BattleResultViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.tooltip_constants_model import TooltipConstantsModel as TooltipConstantsModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.stat_item_model import StatItemModel as StatItemModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.leaderboard.leaderboard_constants import LeaderboardConstants as LeaderboardConstants
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.battle_reward_item_model import BattleRewardItemModel as BattleRewardItemModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.place_model import PlaceModel as PlaceModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.row_model import RowModel as RowModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.battle_pass_progress import BattlePassProgress as BattlePassProgress
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import event_dispatcher as event_dispatcher, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import BattleRoyalePlatoonEvent as BattleRoyalePlatoonEvent
from gui.server_events.battle_royale_formatters import BRSections as BRSections
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS as HANGAR_HEADER_QUESTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController, IPlatoonController as IPlatoonController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from shared_utils import first as first
from soft_exception import SoftException as SoftException
from gui.sounds.ambients import BattleResultsEnv as BattleResultsEnv
from battle_royale.gui.battle_control.controllers.br_battle_sounds import BREvents as BREvents
from battle_royale.gui.constants import BattleRoyaleSubMode as BattleRoyaleSubMode
from gui.impl.backport.backport_context_menu import BackportContextMenuWindow as BackportContextMenuWindow
from gui.impl.backport.backport_context_menu import createContextMenuData as createContextMenuData
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from messenger.storage import UsersStorage as UsersStorage, MessengerStorageDescriptor as MessengerStorageDescriptor
from messenger.formatters.service_channel_helpers import parseTokenBonusCount as parseTokenBonusCount
from gui.impl.gen.view_models.views.battle_royale.battle_results.player_battle_type_status_model import BattleType as BattleType
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.impl.gen.view_models.views.battle_royale.battle_results.player_battle_type_status_model import PlayerBattleTypeStatusModel as PlayerBattleTypeStatusModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_result_view.leaderboard_model import LeaderboardModel as LeaderboardModel
_THE_BEST_PLACE = 1
_BR_POINTS_ICON: _Any
_BATTLE_REWARD_TYPES: list
_HIDDEN_BONUSES_WITH_ZERO_VALUES: _Any
_TOURNAMENT_ARENA_BONUS_TYPES: tuple
_INVALID_PREBATTLE_ID = 0

class BattleRoyaleBattleResultsWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...

# base nao representavel no stub: ViewComponent[...]
class BattleRoyaleBattleResultsView(IPrbListener):
    __slots__: tuple
    __battleResults: _Any
    __brController: _Any
    __lobbyContext: _Any
    __connectionMgr: _Any
    __brProgressionController: _Any
    __platoonCtrl: _Any
    usersStorage: _Any
    __sound_env__ = BattleResultsEnv
    __arenaUniqueID: _Any
    __data: _Any
    __isObserverResult: _Any
    __arenaBonusType: _Any
    __tooltipsData: _Any
    __tooltipParametersCreator: _Any
    __ally: _Any
    __squadCreatedByInvite: _Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def arenaUniqueID(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def createContextMenu(self, event):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def __update(self):
        ...
    def __onBattlePassClick(self):
        ...
    def __updateBattlePass(self):
        ...
    def __updateSquadState(self):
        ...
    def __onInviteToPlatoonClick(self):
        ...
    def __onLeavedPlatoon(self, *_):
        ...
    def __setPlayerBattleTypeStatus(self, statusModel):
        ...
    def __setPersonalResult(self, personalModel):
        ...
    def __setLeaderboard(self, leaderboardModel):
        ...
    def __getFinishReason(self):
        ...
    def __isSquadMode(self):
        ...
    def __hasPremium(self):
        ...
    def __getStats(self):
        ...
    def __getFinancialData(self, section):
        ...
    def __getBattlePassPointsTotal(self):
        ...
    def __setFinishResult(self, personalResultsModel):
        ...
    def __setStats(self, statsModel):
        ...
    def __setBattleRewards(self, rewardsModel):
        ...
    def __setBattleRewardsWithPremium(self, rewardsModel):
        ...
    def __setIsPlatoonWindowOpen(self, isOpen):
        ...
    def __getBrProgressionTokenCount(self):
        ...
    def __getEarnedRewards(self, section):
        ...
    def __setCommonInfo(self):
        ...
    def __setMapName(self):
        ...
    def __setCompletedQuests(self, personalModel):
        ...
    def __getTooltipParametersCreator(self):
        ...
    def __getAchievementTooltipParameters(self, event):
        ...
    def __getQuestsTooltipParameters(self, _):
        ...
    def __getBonusTooltipParameters(self, event):
        ...
    @staticmethod
    def __normalizeTooltipID(tooltipID):
        ...
    def __parseProgressionTokenCount(self, tokens):
        ...
    @staticmethod
    def __setUserName(model, info):
        ...
    def __isCommander(self):
        ...
    def __isTournament(self):
        ...
