# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/ranked/ranked_selectable_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from AccountCommands import RES_SUCCESS as RES_SUCCESS
from frameworks.wulf import WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.ranked.ranked_selectable_reward_view_model import RankedSelectableRewardViewModel as RankedSelectableRewardViewModel
from gui.impl.lobby.common.selectable_reward_base import SelectableRewardBase as SelectableRewardBase
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.ranked_battles.constants import YEAR_AWARDS_ORDER as YEAR_AWARDS_ORDER
from gui.selectable_reward.common import RankedSelectableRewardManager as RankedSelectableRewardManager
from gui.server_events.bonuses import getMergedBonusesFromDicts as getMergedBonusesFromDicts
from gui.shared.event_dispatcher import showRankedYearAwardWindow as showRankedYearAwardWindow
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from gui.SystemMessages import ResultMsg as ResultMsg

class RankedSelectableRewardView(SelectableRewardBase):
    __slots__: tuple
    __rankedController: Any
    __REWARDS_ORDER: list
    _helper = RankedSelectableRewardManager
    __allRewards: Any
    __points: Any
    def __init__(self, receivedRewards=None):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _processReceivedRewards(self, result):
        ...
    def _onCloseClick(self):
        ...
    def _getItemsSortKey(self, _):
        ...
    def __tryToShowRewardsWindow(self, showRemainedSelection=False):
        ...
    def __rewardsSortKey(self, reward):
        ...

class RankedSelectableRewardWindow(LobbyNotificationWindow):
    def __init__(self, rewards):
        ...
