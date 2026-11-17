# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/spotting_indicators_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from enum import Enum as Enum
from functools import partial as partial
import BigWorld as BigWorld
from Event import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from ReplayEvents import g_replayEvents as g_replayEvents
from Vehicle import Vehicle as Vehicle
from constants import DIRECT_DETECTION_TYPE as DIRECT_DETECTION_TYPE
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from helpers.dependency import instance as instance
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Dict as Dict, List as List, Optional as Optional, Tuple as Tuple
from gui.battle_control import BattleSessionSetup as BattleSessionSetup
from gui.battle_control.controllers.vehicle_state_ctrl import VehicleStateController as VehicleStateController
_logger: Any
_TYPE = DIRECT_DETECTION_TYPE
SPOTTING_INDICATORS_PRIORITY: tuple
_PRIORITY_BY_DETECTION_TYPE: dict

class ISpottingIndicator(object):
    __slots__: tuple
    ToggleType: Any
    EnabledType: Any
    def getIndicatorTogglesByType(self):
        ...

class ISpottingIndicatorsController(IBattleController):
    __slots__: tuple
    onSpottingIndicatorAction = None
    def getControllerID(self):
        ...
    def bindSpottingIndicator(self, indicator):
        ...
    def unbindSpottingIndicator(self, indicator):
        ...

class IndicatorAction(Enum):
    SHOW = 'show'
    HIDE = 'hide'
    PASS = 'pass'

class SpottingIndicatorsController(ISpottingIndicatorsController):
    __slots__: tuple
    _vehicleState: Any
    onSpottingIndicatorAction: Any
    __detectionType: Any
    __visToggleByType: Any
    _durationByType: Any
    __enabledByType: Any
    __showTimerID: Any
    __prevControllingVehID: Any
    def __init__(self, vehicleState):
        ...
    def startControl(self):
        ...
    def bindSpottingIndicator(self, indicator):
        ...
    def unbindSpottingIndicator(self, indicator):
        ...
    def stopControl(self):
        ...
    def _getIndicatorAction(self, newDetectionType, isObserved):
        ...
    def _onObservedByEnemy(self, detectionType, isObserved):
        ...
    def _showSpottingIndicator(self, detectionType):
        ...
    def _startShowTimer(self, detectionType, duration=None):
        ...
    def _hideSpottingIndicator(self, detectionType=None, force=False):
        ...
    def _callOnSpottingIndicatorAction(self, detectionType, isVisible):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
    def __onPostMortemSwitched(self, _, __):
        ...
    def __onShowTimerCB(self, detectionType):
        ...
    def _cancelShowTimer(self):
        ...

class _Replay(SpottingIndicatorsController):
    __slots__: tuple
    __stateTransitionEvents: list
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def _getIndicatorAction(self, newDetectionType, isObserved):
        ...
    def _startShowTimer(self, detectionType, duration=None):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
    def _callOnSpottingIndicatorAction(self, detectionType, isVisible):
        ...
    def __onTimeWarpStart(self):
        ...
    def __onTimeWarpFinish(self):
        ...
    def __getLastEventTimeLeft(self):
        ...
    def __recordEvent(self, detectionType, isVisible):
        ...
    def __repr__(self):
        ...

def bindSpottingIndicator(indicator):
    ...
def unbindSpottingIndicator(indicator):
    ...
def createCtrl(setup, state):
    ...
