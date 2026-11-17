# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/views/rewards_selection_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from future.utils import viewitems as viewitems
from AccountCommands import RES_SUCCESS as RES_SUCCESS
from epic_constants import EPIC_OFFER_TYPES as EPIC_OFFER_TYPES
from frameworks.wulf import WindowFlags as WindowFlags
from frontline.gui.impl.gen.view_models.views.lobby.views.rewards_selection_view.rewards_selection_view_model import RewardsSelectionViewModel as RewardsSelectionViewModel
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.common.selectable_reward_base import SelectableRewardBase as SelectableRewardBase
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.selectable_reward.common import EpicSelectableRewardManager as EpicSelectableRewardManager
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class RewardsSelectionView(SelectableRewardBase):
    __slots__: tuple
    _helper = EpicSelectableRewardManager
    _epicController: Any
    __onRewardsReceivedCallback: Any
    __onCloseCallback: Any
    __onLoadedCallback: Any
    __isViewLoaded: Any
    __isAutoDestroyWindowsOnReceivedRewards: Any
    def __init__(self, onRewardsReceivedCallback=None, onCloseCallback=None, onLoadedCallback=None, isAutoDestroyWindowsOnReceivedRewards=True, level=0):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onOkClick(self):
        ...
    def _onEpicUpdate(self, diff, *args):
        ...
    @staticmethod
    def _rewardsSortKeyByArtifactName(x):
        ...
    @staticmethod
    def _defaultSortKey(x):
        ...
    def _getTypesSortKey(self):
        ...
    def _getItemsSortKey(self, tabName):
        ...
    def _processReceivedRewards(self, result):
        ...
    def _getReceivedRewards(self, rewardName):
        ...
    def __onViewLoaded(self):
        ...
    @staticmethod
    def __safeCall(callback, *args, **kwargs):
        ...

class RewardsSelectionWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, onRewardsReceivedCallback=None, onCloseCallback=None, onLoadedCallback=None, isAutoDestroyWindowsOnReceivedRewards=True, level=0):
        ...

def _isValidReward(level, tokenID):
    ...
