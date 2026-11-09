# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/campaign_selector_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from adisp import adisp_process as adisp_process
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, ViewStatus as ViewStatus, WindowFlags as WindowFlags
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getSuitableVehicles as getSuitableVehicles, processPMOperation as processPMOperation, switchCampaign as switchCampaign
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.campaign_model import CampaignModel as CampaignModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.campaign_selector_model import CampaignSelectorModel as CampaignSelectorModel, CampaignSelectorViewState as CampaignSelectorViewState
from gui.impl.gen.view_models.views.lobby.personal_missions_30.operation_model import OperationState as OperationState
from gui.impl.gen.view_models.views.lobby.personal_missions_30.select_operation_model import SelectOperationModel as SelectOperationModel
from gui.impl.lobby.personal_missions_30.personal_mission_constants import PERSONAL_MISSIONS_CAMPAIGN_SELECTOR_SPACE as PERSONAL_MISSIONS_CAMPAIGN_SELECTOR_SPACE, IntroKeys as IntroKeys
from gui.impl.lobby.personal_missions_30.views_helpers import getOperationStatus as getOperationStatus, isIntroShown as isIntroShown, isPMCampaignsStarted as isPMCampaignsStarted, firstUnclaimedOperation as firstUnclaimedOperation, getBranchSortedPmOperations as getBranchSortedPmOperations
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.server_events.events_dispatcher import showPersonalMissionOperationsPage as showPersonalMissionOperationsPage
from gui.server_events.finders import getBranchByOperationId as getBranchByOperationId
from gui.shared.event_dispatcher import showPersonalMissionMainWindow as showPersonalMissionMainWindow, showPM30IntroWindow as showPM30IntroWindow
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH, PM_SWITCHES as PM_SWITCHES
from shared_utils import first as first
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, List as List, Optional as Optional
from gui.server_events.event_items import PMOperation as PMOperation
ACTIVATE_WAITING_ID = 'activateCampaign'
SWITCH_WAITING_ID = 'switchCampaign'

class CampaignSelectorView(ViewImpl):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_CAMPAIGN_SELECTOR_SPACE
    __eventsCache: Any
    __itemsCache: Any
    __lobbyContext: Any
    _personalMissions: Any
    _activeSeason: Any
    _progressInFirstTwoSeasons: Any
    _progressInWithoutAwardListSeasons: Any
    _firstTwoSeasonsAreCompletedWithHonors: Any
    _suitableVehicles: Any
    _isFirstTimeEntrance: Any
    _campaigns: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    def _finalize(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onServerSettingsChanged(self, diff=None):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onEventCacheSyncCompleted(self, *_):
        ...
    def __onItemsSyncCompleted(self, _, diff=None):
        ...
    def __onClose(self):
        ...
    def _onEnterTheOperation(self, data):
        ...
    # decorador original: @adisp_process
    def _switchCampaign(self, data):
        ...
    def _fillModel(self):
        ...
    def _getSeasonState(self, isAllOperationsWithHonors, activeCampaigns, isFirstTimeEntrance):
        ...
    @staticmethod
    def _getLastUncompletedOperation(operations):
        ...
    def _isLockedByVeh(self, activeCampaigns):
        ...
    def _isOperationActive(self, operation, isBranchWithAwardListActive, activeCampaigns, lastActiveOperationID):
        ...

class CampaignSelectorWindow(WindowImpl):
    _OPAQUE_BACKGROUND_ALPHA = 1.0
    __background_alpha__: Any
    def __init__(self, layer, **kwargs):
        ...
