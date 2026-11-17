# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/presenters/personal_missions_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from future.utils import itervalues as itervalues, viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
from constants import ROLE_TYPE_TO_COMMON_ROLE as ROLE_TYPE_TO_COMMON_ROLE
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.personal_missions_list_model import PersonalMissionsListModel as PersonalMissionsListModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.personal_mission_model import PersonalMissionModel as PersonalMissionModel
from gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import OverlapCtrlMixin as OverlapCtrlMixin
from gui.impl.lobby.user_missions.hangar_widget.presenters.constants import UserMissionGroups as UserMissionGroups
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.services import IPersonalMissionsService as IPersonalMissionsService
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.lobby.personal_missions_30.tooltips.umg_tooltip import UmgPersonalMissionsTooltip as UmgPersonalMissionsTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.PERSONAL_MISSIONS_30 import PERSONAL_MISSIONS_30 as PERSONAL_MISSIONS_30
from gui.server_events.events_dispatcher import showPersonalMission as showPersonalMission, showPersonalMissionOperationsPage as showPersonalMissionOperationsPage
from gui.shared.event_dispatcher import showPersonalMissionCampaignSelectorWindow as showPersonalMissionCampaignSelectorWindow, showPersonalMissionMainWindow as showPersonalMissionMainWindow
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
import nations as nations
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from typing import Optional as Optional
from items.vehicles import VehicleType as VehicleType
from gui.server_events.event_items import PersonalMission as PersonalMission
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

# base nao representavel no stub: ViewComponent[...]
class PersonalMissionsPresenter(UserMissionChildPresenter, TooltipPositionerMixin, OverlapCtrlMixin):
    GROUP = UserMissionGroups.PERSONAL_MISSIONS
    eventsCache: Any
    hangarSpace: Any
    lobbyContext: Any
    personalMissionsService: Any
    _onClicks: Any
    _showTierMismatch: Any
    _showNoMissions: Any
    _showUnavailable: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onEventsUpdated(self):
        ...
    def _onClick(self, args):
        ...
    def _onMarkAsViewed(self, _):
        ...
    def _rawUpdate(self):
        ...
    def _updateMissions(self, vm):
        ...
    def _getCardTierMismatch(self):
        ...
    def _getCardNoMissions(self):
        ...
    def _addWarningClick(self, branchID):
        ...
    def _getCardUnavailable(self):
        ...
    def _getCard(self, campaignName):
        ...
    def _fillCardInProgress(self, missionVM, quest, vehType):
        ...
    def _fillCardCompleted(self, missionVM, branchID, operationId, vehType):
        ...
    def _updateVisibility(self):
        ...
    def isVisible(self):
        ...
    @staticmethod
    def _icons():
        ...
    @classmethod
    def _getClassifier(cls, branchID, vehType):
        ...
    def _update(self, *_):
        ...
    @classmethod
    def _isUnsuitableForPM(cls, vehicle):
        ...
    @classmethod
    def _hasProperVehicleTier(cls, operationID):
        ...
    @classmethod
    def _pickMissionState(cls, quest, vehType):
        ...
