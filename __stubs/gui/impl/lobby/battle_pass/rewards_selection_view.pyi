# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/rewards_selection_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from functools import partial as partial
from future.utils import viewitems as viewitems
from AccountCommands import RES_SUCCESS as RES_SUCCESS
from frameworks.wulf import WindowFlags as WindowFlags
from gui import SystemMessages as SystemMessages
from gui.battle_pass.rewards_sort import getTypesSortKey as getTypesSortKey, getItemsSortKey as getItemsSortKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.rewards_selection_view_model import RewardsSelectionViewModel as RewardsSelectionViewModel
from gui.impl.lobby.common.selectable_reward_base import SelectableRewardBase as SelectableRewardBase
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.selectable_reward.common import BattlePassSelectableRewardManager as BattlePassSelectableRewardManager
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

class RewardsSelectionView(SelectableRewardBase):
    __slots__: tuple
    __battlePass: Any
    _helper = BattlePassSelectableRewardManager
    __chapterID: Any
    __level: Any
    __onRewardsReceivedCallback: Any
    __onCloseCallback: Any
    def __init__(self, chapterID=0, level=0, onRewardsReceivedCallback=None, onCloseCallback=None):
        ...
    def _getReceivedRewards(self, rewardName):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _sortContent(self):
        ...
    def _sortCart(self):
        ...
    def _processReceivedRewards(self, result):
        ...
    @staticmethod
    def __safeCall(callback, *args, **kwargs):
        ...

class RewardsSelectionWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, chapterID=0, level=0, onRewardsReceivedCallback=None, onCloseCallback=None):
        ...

def _isValidReward(chapterID, level, tokenID):
    ...
