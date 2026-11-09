# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/CapturePointComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import wraps as wraps
import BigWorld as BigWorld
import CGF as CGF
from Event import Event as Event, EventManager as EventManager
from FortRushCapturePointStateMachineComponent import FortRushCapturePointStateMachineComponent as FortRushCapturePointStateMachineComponent
from cgf_script.registration import registerReplicableComponent as registerReplicableComponent, registerComponent as registerComponent
from constants import ARENA_PERIOD as ARENA_PERIOD
from fort_rush.gui.shared.events import CapturePointEvent as CapturePointEvent
from fort_rush_common.cgf.capture_point import FortRushCapturePointComponentDescr as FortRushCapturePointComponentDescr
from fort_rush_common.fort_rush_constants import CaptureStates as CaptureStates
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
_logger: Any

# decorador original: @registerComponent
class CapturePointMarkerAnchor(object):
    category = 'FortRush'
    editorTitle = 'Capture Point Marker Anchor'
    domain = CGF.Domain.ClientEditor

# decorador original: @registerReplicableComponent
class CapturePointComponent(FortRushCapturePointStateMachineComponent, FortRushCapturePointComponentDescr):
    sessionProvider: Any
    _isUiRefreshPending: Any
    _eventManager: Any
    onOwnerTeamChanged: Any
    onCaptureStateChanged: Any
    _isBattleFinished: Any
    _arenaSubscription: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onArenaPeriodChange(self, period, _periodEndTime, _periodLength, _periodAdditionalInfo):
        ...
    def scheduleUiRefresh(self):
        ...
    @property
    def isNeutralizing(self):
        ...
    # decorador original: @capturablePointEventWrapper
    def set_totalInvaders(self, _):
        ...
    # decorador original: @capturablePointEventWrapper
    def set_capturablePointOwnerTeam(self, _):
        ...
    # decorador original: @capturablePointEventWrapper
    def set_invadingTeam(self, _):
        ...
    # decorador original: @capturablePointEventWrapper
    def set_currentPoints(self, _):
        ...
    # decorador original: @capturablePointEventWrapper
    def set_isContested(self, _):
        ...
    # decorador original: @capturablePointEventWrapper
    def set_state(self, prevState):
        ...
    def calculatePercentage(self):
        ...
    def sendEventImmediately(self):
        ...
    def _sendEvent(self):
        ...

def capturablePointEventWrapper(func):
    ...
