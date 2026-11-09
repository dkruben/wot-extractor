# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import typing as typing
from functools import partial as partial
import BigWorld as BigWorld
import adisp as adisp
from BWUtil import AsyncReturn as AsyncReturn
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags, visitor as visitor
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey, ViewKeyDynamic as ViewKeyDynamic
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams as GuiImplViewLoadParams
from gui.impl import backport as backport
from gui.lobby_state_machine.states import LobbyState as LobbyState, SFViewLobbyState as SFViewLobbyState, GuiImplViewLobbyState as GuiImplViewLobbyState, UntrackedState as UntrackedState, SubScopeSubLayerState as SubScopeSubLayerState, SubScopeTopLayerState as SubScopeTopLayerState, TopScopeTopLayerState as TopScopeTopLayerState, LobbyStateDescription as LobbyStateDescription
from gui.lobby_state_machine.transitions import NavigationTransition as NavigationTransition, GuardTransition as GuardTransition
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.dialogs.builders import ResPureDialogBuilder as ResPureDialogBuilder
from gui.impl.gen import R as R
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.events import NavigationEvent as NavigationEvent, LoadGuiImplViewEvent as LoadGuiImplViewEvent
from gui.subhangar.subhangar_state_groups import SubhangarStateGroupConfigProvider as SubhangarStateGroupConfigProvider, SubhangarStateGroups as SubhangarStateGroups, SubhangarStateGroupConfig as SubhangarStateGroupConfig
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from wg_async import wg_await as wg_await, wg_async as wg_async, BrokenPromiseError as BrokenPromiseError
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
_logger: Any

# decorador original: @SubScopeSubLayerState.parentOf
class CustomizationState(LobbyState, EventsHandler, SubhangarStateGroupConfigProvider):
    STATE_ID = 'customization'
    __CAMERA_NAME = 'Customization'
    __ENVIRONMENT_NAME = 'Customization'
    __hangarSpace: Any
    __c11n: Any
    @classmethod
    def goTo(cls, vehInvID=None, callback=None, season=None, modeId=None, tabId=None, itemCD=None):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def getSubhangarStateGroupConfig(self):
        ...
    def makeTransition(self, transitionType, record):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _getListeners(self):
        ...
    def _getEvents(self):
        ...
    @staticmethod
    def __showHangar(event):
        ...
    def __onSpaceChanged(self):
        ...

class _CustomizationTransition(NavigationTransition):
    __lobbyContext: Any
    __itemsCache: Any
    def execute(self, event):
        ...

# decorador original: @CustomizationState.parentOf
class _LoadingState(LobbyState, EventsHandler):
    STATE_ID = 'loading'
    __hangarSpace: Any
    __params: Any
    def __init__(self, flags=...):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getEvents(self):
        ...
    def __onVehicleChanged(self):
        ...
    def __onSpaceChanged(self):
        ...
    def __goToMain(self):
        ...

# decorador original: @CustomizationState.parentOf
class _MainState(SFViewLobbyState, EventsHandler):
    STATE_ID = 'main'
    VIEW_KEY: Any
    __CAMERA_NAME = 'Customization'
    __GUN_PITCH_ANGLE = 0.0
    __TURRET_YAW_ANGLE = 0.0
    __RESTRICTED_EVENTS: list
    __lobbyContext: Any
    __hangarSpace: Any
    __c11n: Any
    proceedWithoutSave: Any
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    def mustConfirmExit(self, event):
        ...
    def getNavigationDescription(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getRestrictions(self):
        ...
    def _onViewExternallyDestroyed(self):
        ...
    def __cleanup(self, _=None):
        ...
    def __setupTankTransformation(self):
        ...
    # decorador original: @wg_async
    def __handleRestrictedEvent(self, event=None):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @wg_async
    def __confirmatorWrapper(self, callback):
        ...

# decorador original: @CustomizationState.parentOf
class _ExitState(LobbyState):
    STATE_ID = 'exit'
    def _onEntered(self, event):
        ...

class _ExitTransition(GuardTransition):
    def getPriority(self):
        ...

# decorador original: @TopScopeTopLayerState.parentOf
class _CustomizationTopState(LobbyState):
    STATE_ID = 'customization'
    def registerStates(self):
        ...

# decorador original: @_CustomizationTopState.parentOf
class _ConfirmLeaveState(LobbyState):
    STATE_ID = 'confirmLeave'
    __c11n: Any
    __dialog: Any
    __waitFuture: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    # decorador original: @wg_async
    def waitForResult(self):
        ...
    # decorador original: @wg_async
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class _CustomizationMidState(LobbyState):
    STATE_ID = 'customization'
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def mustConfirmExit(self, event):
        ...
    def _onEntered(self, event):
        ...
    def __shouldRedirectToExit(self, event):
        ...

# decorador original: @_CustomizationMidState.parentOf
class _CustomizationEditState(LobbyState):
    STATE_ID = 'edit'
    def getNavigationDescription(self):
        ...

# decorador original: @_CustomizationMidState.parentOf
class CustomizationCartState(LobbyState):
    STATE_ID = 'cart'
    VIEW_KEY: Any
    def _getViewLoadCtx(self, event):
        ...
    def _onEntered(self, event):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @_CustomizationMidState.parentOf
class ProgressiveItemsState(GuiImplViewLobbyState):
    STATE_ID = 'progressiveItems'
    VIEW_KEY: Any
    def __init__(self, flags=...):
        ...
    @classmethod
    def goTo(cls, itemIntCD=None):
        ...
    def _onExited(self):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def _getViewLoadCtx(self, event, appLoader=None):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
