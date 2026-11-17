# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/rewards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import chain as chain
from typing import TYPE_CHECKING as TYPE_CHECKING
import SoundGroups as SoundGroups
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.rewards_view_model import RewardsViewModel as RewardsViewModel, RewardsViewType as RewardsViewType
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.personal_missions_30.bonus_packers import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData, getBonusPacker as getBonusPacker
from gui.impl.lobby.personal_missions_30.state import PersonalMissions3EntryState as PersonalMissions3EntryState
from gui.impl.lobby.personal_missions_30.views_helpers import getDetailNameByToken as getDetailNameByToken, showRewardVehicleInHangar as showRewardVehicleInHangar, setForceLeavePM3State as setForceLeavePM3State, setVideoOverlayOn as setVideoOverlayOn, setVideoOverlayOff as setVideoOverlayOff, canOpenOperationPage as canOpenOperationPage
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from gui.server_events.finders import NO_AWARD_LIST_FINISHED_QUEST as NO_AWARD_LIST_FINISHED_QUEST, NO_AWARD_LIST_VEHICLE_DETAIL_TOKEN as NO_AWARD_LIST_VEHICLE_DETAIL_TOKEN
from gui.shared.event_dispatcher import showPersonalMissionMainWindow as showPersonalMissionMainWindow
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH, PM_SWITCHES as PM_SWITCHES
from shared_utils import findFirst as findFirst
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Callable as Callable, Dict as Dict, Optional as Optional

class RewardsView(ViewImpl):
    __eventsCache: Any
    __itemsCache: Any
    __lobbyContext: Any
    ctx: Any
    questID: Any
    rewardType: Any
    rewards: Any
    closingCallback: Any
    nextOperationID: Any
    currentOperation: Any
    __tooltipData: Any
    __doStateChange: Any
    def __init__(self, ctx):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onServerSettingsChanged(self, diff=None):
        ...
    def __onClose(self):
        ...
    def __onViewClosed(self):
        ...
    def __onShowOperation(self):
        ...
    def __onDisableVideoOverlaySound(self):
        ...
    def __onShowVehicle(self):
        ...
    def __getVehDetail(self, branchID, operationID):
        ...
    def __isCampaignFinished(self):
        ...
    def __defineCurrentOperation(self):
        ...
    def __defineNextOperationID(self, branchID):
        ...
    def __getOperationName(self, operationID):
        ...
    def __getCampaignName(self, branchID):
        ...
    def __getBonuses(self, rewards):
        ...
    def __fillRewards(self, rewardsModel, packer):
        ...

class RewardsViewWindow(LobbyNotificationWindow):
    def __init__(self, ctx, parent=None):
        ...
