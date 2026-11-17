# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/rewards_selection_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from helpers import dependency as dependency
from AccountCommands import RES_SUCCESS as RES_SUCCESS
from comp7_common_const import COMP7_OFFER_YEARLY_REWARD_TOKEN_PREFIX as COMP7_OFFER_YEARLY_REWARD_TOKEN_PREFIX, offerRewardCategoryToken as offerRewardCategoryToken
from comp7.gui.impl.gen.view_models.views.lobby.rewards_selection_screen_model import RewardsSelectionScreenModel as RewardsSelectionScreenModel
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import getComp7OfferWeeklyQuestsRewardTokenPrefix as getComp7OfferWeeklyQuestsRewardTokenPrefix
from comp7.gui.selectable_reward.common import Comp7SelectableRewardManager as Comp7SelectableRewardManager
from comp7.gui.shared.event_dispatcher import showComp7SelectedRewardsScreen as showComp7SelectedRewardsScreen
from frameworks.wulf import WindowFlags as WindowFlags
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.common.selectable_reward_base import SelectableRewardBase as SelectableRewardBase
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from typing import Callable as Callable, Optional as Optional
from gui.SystemMessages import ResultMsg as ResultMsg
WEEKLY_TAB_PARTIAL = 'weekly:'
YEARLY_TAB_PARTIAL = 'yearly:'
TABS_PRIORITY: tuple

class Comp7SelectableRewardType(Enum):
    NONE = 0
    YEARLY = 1
    WEEKLY_QUESTS = 2

class Comp7RewardsSelectionView(SelectableRewardBase):
    _helper = Comp7SelectableRewardManager
    def __init__(self, tokenCondition):
        ...
    def _processReceivedRewards(self, result):
        ...
    def _getTypesSortKey(self):
        ...
    def _getRewardType(self, reward):
        ...
    def _getDefaultTab(self):
        ...
    @staticmethod
    # decorador original: @dependency.replace_none_kwargs(...)
    def __getSelectedMetaTabId(uiLoader=None):
        ...

class Comp7RewardsSelectionWindow(LobbyWindow):
    __slots__: tuple
    __rewardTokens: Any
    def __init__(self, rewardSelectionType=..., category=None):
        ...
    def tokenCondition(self, token):
        ...
