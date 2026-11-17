# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/personal_missions_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.settings_core.settings_constants import PersonalMission3 as PersonalMission3
from gui.impl.gen.view_models.views.lobby.personal_missions_30.operation_status_model import OperationStatus as OperationStatus
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.personal_missions_30.views_helpers import getDetailNameByToken as getDetailNameByToken, getVehicleDetails as getVehicleDetails, getDetailedOperationStatus as getDetailedOperationStatus, getBranchesSortedPmOperations as getBranchesSortedPmOperations, getPersonalMissionData as getPersonalMissionData, getCheckedPMPointsKey as getCheckedPMPointsKey, setPersonalMissionData as setPersonalMissionData, getCurrentOperationLastInstalledDetail as getCurrentOperationLastInstalledDetail
from gui.shared.event_dispatcher import showPersonalMissionMainWindow as showPersonalMissionMainWindow, showPersonalMissionCampaignSelectorWindow as showPersonalMissionCampaignSelectorWindow
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH, PM_SWITCHES as PM_SWITCHES
from shared_utils import first as first
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.personal_missions_model import PersonalMissionsModel as PersonalMissionsModel, State as State
from gui.impl.gen import R as R
from typing import Tuple as Tuple, Optional as Optional
from collections import OrderedDict as OrderedDict
from gui.server_events.event_items import PMOperation as PMOperation
UnpackedOp: Any
MIN_PM_POINTS = 0
_OP_NOT_COMPLETE: set
_NEXT_OP_AVAILABLE = OperationStatus.NEXT_OPERATION_AVAILABLE

# base nao representavel no stub: ViewComponent[...]
class PersonalMissionsWindgetPresenter:
    LAYOUT_ID: Any
    __lobbyContext: Any
    __eventsCache: Any
    __settingsCore: Any
    __pmCache: Any
    __currentOperation: Any
    __linkedOperation: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def __onCacheSyncCompleted(self, *_):
        ...
    def __goToOperation(self):
        ...
    def __goToCampaigns(self):
        ...
    def __findAndUnpackFirstInProgressOperation(self, opsByID):
        ...
    def __findAndUnpackNextOpIfNoCurrent(self, isWithoutAwardListBranchActivated, opsByID, unpackedOp):
        ...
    def __fillModel(self):
        ...
    def __fillDetailProgress(self, model, operation):
        ...
