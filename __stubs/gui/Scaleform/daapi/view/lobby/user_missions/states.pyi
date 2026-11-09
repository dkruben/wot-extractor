# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/user_missions/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import ChallengesMissions as ChallengesMissions
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.challenges.challenges_helpers import getChallengesInfoUrl as getChallengesInfoUrl, getSettings as getSettings, setSettings as setSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.tab_id import TabId as TabId
from gui.impl.gen.view_models.views.lobby.user_missions.info_page_model import InfoPageModel as InfoPageModel
from gui.impl.lobby.common.info_view import getInfoWindowProc as getInfoWindowProc, createContentData as createContentData
from gui.impl.lobby.user_missions.info_page_view import InfoPageView as InfoPageView
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription, LobbyState as LobbyState, getNavigationDescriptionSafe as getNavigationDescriptionSafe
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import UserMissionsEvent as UserMissionsEvent
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from shared_utils import first as first
from skeletons.gui.impl import IGuiLoader as IGuiLoader
MISSION_TABS: tuple

# decorador original: @SubScopeSubLayerState.parentOf
class UserMissionsState(SFViewLobbyState, EventsHandler):
    STATE_ID = VIEW_ALIAS.USER_MISSIONS_HUB_CONTAINER
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    @classmethod
    def goTo(cls, tab=None, subTab=None, eventID=None, groupID=None, marathonPrefix=None, anchor=None, showMissionDetails=None, questId=None, challengeID=None):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def serializeParams(self):
        ...
    def _getListeners(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def compareParams(self, params, otherParams):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def __onTabChanged(self, event):
        ...
    def __findChildState(self, tabID):
        ...

# decorador original: @UserMissionsState.parentOf
class _EntryState(LobbyState):
    STATE_ID = 'entry'

# decorador original: @UserMissionsState.parentOf
class _BasicMissionTab(LobbyState):
    STATE_ID = TabId.BASIC
    TAB_ID = TabId.BASIC
    LOBBY_STATE_DESCR: Any
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @UserMissionsState.parentOf
class _CommonMissionTab(LobbyState):
    STATE_ID = TabId.COMMON
    TAB_ID = TabId.COMMON
    LOBBY_STATE_DESCR: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @UserMissionsState.parentOf
class _ChallengeMissionTab(LobbyState):
    STATE_ID = TabId.CHALLENGES
    TAB_ID = TabId.CHALLENGES
    LOBBY_STATE_DESCR: Any
    __guiLoader: Any
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
def _onMoreInfoRequested():
    ...
