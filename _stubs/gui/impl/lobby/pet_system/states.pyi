# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/pet_system/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF
from Event import Event as Event
from pet_system_common.pet_constants import PET_CAMERA_NAME as PET_CAMERA_NAME
from wg_async import wg_async as wg_async
from frameworks.wulf import WindowLayer as WindowLayer
from skeletons.gui.game_control import IFadingController as IFadingController
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
from frameworks_common.state_machine import StateFlags as StateFlags, StateIdsObserver as StateIdsObserver
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.battle_results.states import PostBattleResultsEntryState as PostBattleResultsEntryState
from gui.lobby_state_machine.states import LobbyStateDescription as LobbyStateDescription, SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.shared.event_dispatcher import showHangar as showHangar, showPetInfoPage as showPetInfoPage
from gui.subhangar.subhangar_state_groups import CameraMover as CameraMover, SmoothCameraMover as SmoothCameraMover, SubhangarStateGroupConfig as SubhangarStateGroupConfig, SubhangarStateGroupConfigProvider as SubhangarStateGroupConfigProvider, SubhangarStateGroups as SubhangarStateGroups
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine

class PetStorageObserver(StateIdsObserver):
    onStorageEntered: Any
    onStorageExited: Any
    currentState: Any
    def __init__(self):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...
    def clear(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class PetStorageState(SFViewLobbyState, EventsHandler, SubhangarStateGroupConfigProvider):
    STATE_ID = VIEW_ALIAS.PET_STORAGE
    VIEW_KEY: Any
    __petController: Any
    __hangarSpace: Any
    __cameraMover: Any
    def __init__(self, flags=...):
        ...
    def getSubhangarStateGroupConfig(self):
        ...
    def getNavigationDescription(self):
        ...
    def compareParams(self, params, otherParams):
        ...
    @classmethod
    def goTo(cls, moveInstantly=True):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getEvents(self):
        ...
    def __onSpaceChanged(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class PetEventFullscreenWindowState(SFViewLobbyState, EventsHandler):
    STATE_ID = VIEW_ALIAS.PET_EVENT_FULLSCREEN
    VIEW_KEY: Any
    hangarSpace: Any
    fadeManager: Any
    petController: Any
    def addNavigationTransition(self, targetViewState, transitionType=..., record=True):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    # decorador original: @wg_async
    def __switchCamera(self, isExit=False):
        ...
    def _getEvents(self):
        ...
    def __onSpaceChanged(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
