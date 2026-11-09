# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/winback/winback_reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_tooltip import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.winback.winback_reward_view_model import RewardName as RewardName, RewardWindowType as RewardWindowType, WinbackRewardViewModel as WinbackRewardViewModel
from gui.impl.lobby.user_missions.hub.hub_view import DailyTabs as DailyTabs
from gui.impl.lobby.winback.sounds import SOUNDS as SOUNDS
from gui.impl.lobby.winback.tooltips.selectable_reward_tooltip import SelectableRewardTooltip as SelectableRewardTooltip
from gui.impl.lobby.winback.winback_bonus_packer import getWinbackBonusPacker as getWinbackBonusPacker, getWinbackBonuses as getWinbackBonuses
from gui.impl.lobby.winback.winback_bonuses import WinbackVehicleBonus as WinbackVehicleBonus
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.events_dispatcher import showDailyQuests as showDailyQuests
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar, showHangar as showHangar, showWinbackSelectRewardView as showWinbackSelectRewardView
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst, first as first
from skeletons.gui.game_control import IWinbackController as IWinbackController
from skeletons.gui.shared import IItemsCache as IItemsCache
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from typing import List as List
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
_logger: Any
_AWARDS_ORDER: list

class WinbackRewardView(ViewImpl):
    __slots__: tuple
    _itemsCache: Any
    _winbackController: Any
    _COMMON_SOUND_SPACE: Any
    __questIDs: Any
    __tooltipData: Any
    __selectedRewards: Any
    __isOnlyDaily: Any
    __isLastWindow: Any
    __bonuses: Any
    def __init__(self, ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onClose(self):
        ...
    @staticmethod
    def _onSelectReward():
        ...
    def _showInHangar(self):
        ...
    def _showQuests(self):
        ...
    @staticmethod
    def __sortBonusesByKey(bonus):
        ...
    def __packRewards(self, bonuses, model):
        ...
    def __getState(self):
        ...

class WinbackRewardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, parent=None, ctx=None):
        ...

def _selectablesSort(bonuses):
    ...
