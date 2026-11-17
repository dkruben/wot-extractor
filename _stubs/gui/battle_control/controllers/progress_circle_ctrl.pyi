# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/progress_circle_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from builtins import round as round
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import Event as Event
from constants import REPAIR_POINT_ACTION as REPAIR_POINT_ACTION, SECTOR_BASE_ACTION as SECTOR_BASE_ACTION
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS as EPIC_CONSTS
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, PROGRESS_CIRCLE_TYPE as PROGRESS_CIRCLE_TYPE, VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
REPAIR_COMPLETE_BLOCKED_DELAY = 2

class ProgressTimerPlugin(object):
    _controller: Any
    _type: Any
    _callback: Any
    _cooldown: Any
    _isInPostmortem: Any
    _inCircleIdx: Any
    _sessionProvider: Any
    def __init__(self, controller, sessionProvider):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def getPlayerState(self, idx):
        ...
    def _getTime(self, nextTime):
        ...
    def _cooldownCallback(self):
        ...
    def _startCooldownCallback(self, idx, time):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def _onRespawnVisibility(self, isVisible, fromTab=False):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _stopTimerCallback(self):
        ...
    def _hideAll(self):
        ...

class StepRepairPlugin(ProgressTimerPlugin):
    _type: Any
    __repairPointStates: Any
    __delayedCooldownCB: Any
    __isInFreecam: Any
    _inCircleIdx: Any
    def __init__(self, controller, sessionProvider):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def getPlayerState(self, idx):
        ...
    def _onRespawnVisibility(self, isVisible, fromTab=False):
        ...
    def _action(self, repairPointIndex, action, nextActionTime, percentageHealed):
        ...
    def _hideAll(self):
        ...
    def _stopTimerCallback(self):
        ...
    def __onSpectatorModeChanged(self, mode):
        ...
    def __delayedCooldown(self, repairPointIndex, nextActionTime):
        ...

class SectorBasePlugin(ProgressTimerPlugin):
    _type: Any
    __blockedCB: Any
    _inCircleIdx: Any
    def __init__(self, controller, sessionProvider):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def _action(self, basePointIndex, action, nextActionTime):
        ...
    def _hideAll(self):
        ...
    def __stopBlockState(self):
        ...

class ProgressTimerController(IBattleController):
    __sessionProvider: Any
    __plugins: Any
    __eManager: Any
    onTimerUpdated: Any
    onVehicleEntered: Any
    onVehicleLeft: Any
    onCircleStatusChanged: Any
    onProgressUpdate: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def getPlayerCircleState(self, type_, idx):
        ...
