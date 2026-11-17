# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lobby_state_machine/router.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver, visitor as visitor
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.lobby_state_machine.resource_mapping import resLayoutToStateId as resLayoutToStateId, stateIdToResLayout as stateIdToResLayout
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import NavigationEvent as NavigationEvent
from helpers.events_handler import EventsHandler as EventsHandler
from gui.lobby_state_machine.states import UntrackedState as UntrackedState, LobbyState as LobbyState
from frameworks_common.state_machine import State as State
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
_logger: Any
_NAVIGATION_ROUTE_KEY = 'route'
_NAVIGATION_PARAMS_KEY = 'params'

class Router(EventsHandler):
    _routableView: Any
    _routePrefix: Any
    _route: Any
    _params: Any
    def __init__(self, routableView, routePrefix):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    @property
    def routePrefix(self):
        ...
    def setRoute(self, stateId, params):
        ...
    def _getEvents(self):
        ...
    def _encodeRoute(self, stateId):
        ...
    def _encodeParams(self, params):
        ...
    def _decodeStateId(self, route):
        ...
    def _decodeJsonParams(self, jsonParams):
        ...
    def __updateModel(self):
        ...
    def __navigateTo(self, navigationInfo):
        ...
    def __navigateBack(self):
        ...

class SubstateRouter(BaseStateObserver):
    __lsm: Any
    __router: Any
    __rootState: Any
    def __init__(self, lsm, routableView, rootState):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...
