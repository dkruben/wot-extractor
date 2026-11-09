# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/state.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
import SoundGroups as SoundGroups
from cgf_components.pm30_hangar_components import PERSONAL_MISSIONS_SUB_HANGAR_IS_READY as PERSONAL_MISSIONS_SUB_HANGAR_IS_READY
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from frameworks.wulf import ViewStatus as ViewStatus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.user_missions.states import UserMissionsState as UserMissionsState
from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import StylePreviewState as StylePreviewState
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import OperationState as OperationState, MissionCategory as MissionCategory
from gui.impl.gen.view_models.views.lobby.personal_missions_30.main_view_model import MainScreenState as MainScreenState, AnimationState as AnimationState
from gui.impl.lobby.hangar.states import HangarState as HangarState
from gui.impl.lobby.personal_missions_30.hangar_helpers import AssemblingManager as AssemblingManager
from gui.impl.lobby.personal_missions_30.personal_mission_constants import SoundsKeys as SoundsKeys, IntroKeys as IntroKeys
from gui.impl.lobby.personal_missions_30.views_helpers import openInfoPageScreen as openInfoPageScreen, isIntroShown as isIntroShown, getOperationStatus as getOperationStatus, getBranchSortedPmOperations as getBranchSortedPmOperations, getCurrentOperationLastInstalledDetail as getCurrentOperationLastInstalledDetail, canOpenOperationPage as canOpenOperationPage
from gui.impl.lobby.vehicle_hub.states import OverviewState as OverviewState
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription, LobbyState as LobbyState, ViewLobbyState as ViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition, NavigationTransition as NavigationTransition
from gui.server_events.finders import getBranchByOperationId as getBranchByOperationId
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showHangar, showPM30IntroWindow as showPM30IntroWindow, showWithoutAwardListOperationIntroWindow as showWithoutAwardListOperationIntroWindow
from gui.subhangar.subhangar_state_groups import SubhangarStateGroupConfigProvider as SubhangarStateGroupConfigProvider, SubhangarStateGroupConfig as SubhangarStateGroupConfig, SubhangarStateGroups as SubhangarStateGroups
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.impl.lobby.personal_missions_30.main_view import MainView as MainView
from gui.shared.events import NavigationEvent as NavigationEvent
_logger: Any
_OPAQUE_BACKGROUND_ALPHA = 1.0

# decorador original: @SubScopeSubLayerState.parentOf
class CampaignSelectorState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.CAMPAIGN_SELECTOR
    VIEW_KEY: Any
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def getBackNavigationDescription(self, params):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class PersonalMissions3EntryState(LobbyState, EventsHandler, SubhangarStateGroupConfigProvider):
    STATE_ID = 'personalMissions3Entry'
    __eventsCache: Any
    __hangarSpace: Any
    assemblingManager: Any
    def __init__(self, flags=...):
        ...
    def getSubhangarStateGroupConfig(self):
        ...
    def registerStates(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getEvents(self):
        ...
    def __onSpaceChanged(self):
        ...

# decorador original: @PersonalMissions3EntryState.parentOf
class PersonalMissions3State(ViewLobbyState, EventsHandler):
    STATE_ID = VIEW_ALIAS.PERSONAL_MISSIONS_3
    VIEW_KEY: Any
    __appLoader: Any
    __eventsCache: Any
    __cachedParams: Any
    __isForcedLeave: Any
    __canOpenOperationPage: Any
    def __init__(self, flags=...):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def serializeParams(self):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def setForceLeave(self):
        ...
    def _getEvents(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def isAnimationPlayed(self, *_):
        ...
    def __onAssemblingAnimationStarted(self):
        ...
    def __onAssemblingVideoFinished(self, stageNumber):
        ...
    def __onAssemblingAnimationFinished(self):
        ...
    def __onEventsCacheSync(self, *_):
        ...
    def __onCameraFlightStarted(self):
        ...
    def __onCameraFlightFinished(self):
        ...

class _PersonalMissionsChildState(LobbyState):
    _cachedParams: Any
    _canOpenOperationPage: Any
    def __init__(self, flags=...):
        ...
    @property
    def assemblingManager(self):
        ...
    def registerTransitions(self):
        ...
    def readyToEnter(self):
        ...
    def getNavigationDescription(self):
        ...
    def goBack(self):
        ...
    def _onEntered(self, event):
        ...
    def _getNavigationDescriptionTitle(self):
        ...
    def __onMoreInfoRequested(self):
        ...

class _SpecialPM3Transition(NavigationTransition):
    def getPriority(self):
        ...

# decorador original: @PersonalMissions3State.parentOf
class _LoadingState(_PersonalMissionsChildState, EventsHandler):
    STATE_ID = 'loading'
    __appLoader: Any
    __uiLoader: Any
    __eventsCache: Any
    def getNavigationDescription(self):
        ...
    def _getNavigationDescriptionTitle(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __onSubHangarReady(self, _):
        ...
    def onLoaded(self):
        ...
    def __onWindowStatusChanged(self, _, status):
        ...
    def __moveCamera(self):
        ...
    def __initAssemblingManager(self):
        ...

# decorador original: @PersonalMissions3State.parentOf
class ProgressionState(_PersonalMissionsChildState):
    STATE_ID = 'progression'
    __eventsCache: Any
    @classmethod
    def goTo(cls, operationID=None, category=..., state=None):
        ...
    def registerTransitions(self):
        ...
    def _getNavigationDescriptionTitle(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @PersonalMissions3State.parentOf
class MissionsState(_PersonalMissionsChildState):
    STATE_ID = 'missions'
    @classmethod
    def goTo(cls, operationID=None, category=..., state=None):
        ...
    def serializeParams(self):
        ...
    def registerTransitions(self):
        ...
    def _getNavigationDescriptionTitle(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def _onEntered(self, event):
        ...

# decorador original: @PersonalMissions3State.parentOf
class AssemblingState(_PersonalMissionsChildState):
    STATE_ID = 'assembling'
    _cachedParams: Any
    @classmethod
    def goTo(cls, operationID=None, category=..., state=None):
        ...
    def _getNavigationDescriptionTitle(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
