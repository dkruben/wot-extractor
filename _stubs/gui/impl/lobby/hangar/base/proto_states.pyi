# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/base/proto_states.pyc (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import adisp as adisp
from BWUtil import AsyncReturn as AsyncReturn
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.game_control.loadout_controller import updateInteractor as updateInteractor
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.easy_tank_equip_state import generateEasyTankEquipStates as generateEasyTankEquipStates, EasyTankEquipStatePrototype as EasyTankEquipStatePrototype
from gui.impl.lobby.hangar.random.sound_manager import ALL_VEHICLES_SOUND_SPACE as ALL_VEHICLES_SOUND_SPACE
from gui.impl.lobby.tank_setup.tank_setup_sounds import playEnterTankSetupView as playEnterTankSetupView, playExitTankSetupView as playExitTankSetupView
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription, TopScopeTopLayerState as TopScopeTopLayerState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateFlags as LobbyStateFlags
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from skeletons.gui.game_control import ILoadoutController as ILoadoutController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from sound_gui_manager import ViewSoundExtension as ViewSoundExtension
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.lobby_state_machine.transitions import ConditionalTransition as ConditionalTransition
from wg_async import await_callback as await_callback, wg_async as wg_async, BrokenPromiseError as BrokenPromiseError, wg_await as wg_await
from gui.shared.events import NavigationEvent as NavigationEvent
absolute_import: Any
_logger: Any

# gerado do bytecode: classes base desconhecidas
class _HangarStatePrototype:
    VIEW_KEY: Any

# gerado do bytecode: classes base desconhecidas
class _DefaultHangarStatePrototype:
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...

# gerado do bytecode: classes base desconhecidas
class _AllVehiclesStatePrototype:
    _AllVehiclesStatePrototype__soundExtension: Any
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def getNavigationDescription(self):
        ...

# gerado do bytecode: classes base desconhecidas
class _LoadoutStatePrototype:
    _LoadoutStatePrototype__loadoutController: Any
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# gerado do bytecode: classes base desconhecidas
class _LoadoutConfirmStatePrototype:
    _LoadoutConfirmStatePrototype__loadoutController: Any
    _LoadoutConfirmStatePrototype__forwardEvent: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def waitForResult(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __forwardEvent(self, event):
        ...

# gerado do bytecode: classes base desconhecidas
class _LoadoutSectionStatePrototype:
    _LoadoutSectionStatePrototype__loadoutController: Any
    _LoadoutSectionStatePrototype__lobbyContext: Any
    _LoadoutSectionStatePrototype__RESTRICTED_EVENTS: Any
    _LoadoutSectionStatePrototype__handleRestrictedEvent: Any
    _LoadoutSectionStatePrototype__confirmatorWrapper: Any
    def __init__(self, flags=...):
        ...
    def serializeParams(self):
        ...
    def _getRestrictions(self):
        ...
    def _interactorConfirm(self, event):
        ...
    def _getConfirmationState(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __handleRestrictedEvent(self, event=...):
        ...
    def __confirmatorWrapper(self, callback):
        ...

# gerado do bytecode: classes base desconhecidas
class _ShellsLoadoutStatePrototype:
    def isStateReachable(self, event):
        ...
    def getNavigationDescription(self):
        ...

# gerado do bytecode: classes base desconhecidas
class _EquipmentLoadoutStatePrototype:
    def isStateReachable(self, event):
        ...
    def getNavigationDescription(self):
        ...

# gerado do bytecode: classes base desconhecidas
class _InstructionsLoadoutStatePrototype:
    def isStateReachable(self, event):
        ...
    def getNavigationDescription(self):
        ...

# gerado do bytecode: classes base desconhecidas
class _ConsumablesLoadoutStatePrototype:
    def isStateReachable(self, event):
        ...
    def getNavigationDescription(self):
        ...

def generateBasicLoadoutStateClasses(parentHangarStateCls, loadoutResource, loadoutStatePrototypeCls=..., confirmStatePrototypeCls=..., sectionStatePrototypeCls=..., shellsStatePrototypeCls=..., equipmentStatePrototypeCls=..., instructionsStatePrototypeCls=..., consumablesStatePrototypeCls=...):
    ...
def generateBasicHangarStateClasses(parentStateCls, hangarResource, hangarPrototypeCls=..., defaultHangarPrototypeCls=..., allVehiclesPrototypeCls=..., easyTankEquipPrototypeCls=...):
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
