# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/battle_gui_controller_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import logging as logging
from Event import EventManager as EventManager, Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from last_stand.gui.battle_control.ls_battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from LSArenaPhasesComponent import LSArenaPhasesComponent as LSArenaPhasesComponent
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
import typing as typing
_logger: Any

class EventBattleGoal(object):
    UNKNOWN = None

class LSBattleGUIControllerBase(IArenaVehiclesController):
    guiSessionProvider: Any
    _TIME_TO_END_NOTIFY = 10
    _UPDATE_PERIOD = 0.5
    _BATTLE_GOALS_WITHOUT_TIMER: list
    _eManager: Any
    onBattleGoalChanged: Any
    onVehicleBuffIconAdded: Any
    onVehicleBuffIconRemoved: Any
    onPhaseChanged: Any
    onHandleEquipmentPressed: Any
    onSoulsContainerReady: Any
    onPhaseTimeChanged: Any
    onInvulnerableStateChanged: Any
    onVehicleInvulnerabilityChanged: Any
    onVehicleFactorsReady: Any
    onBuffUpdate: Any
    _callbackDelayer: Any
    _currentGoal: Any
    _vehicleMarkerIcons: Any
    _hiddenVehicleIDs: Any
    _invulnerableVehiclesIDs: Any
    _pendingHint: Any
    isEventTimerEnabled: Any
    def __init__(self):
        ...
    @property
    def currentGoal(self):
        ...
    @property
    def vehicleMarkerIcons(self):
        ...
    @property
    def battleHintsCtrl(self):
        ...
    @property
    def arenaPhases(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def setVehicleHidden(self, vehicleID, isHidden):
        ...
    def setVehicleInvulnerable(self, vehicleID, isInvulnerable):
        ...
    def isVehicleHidden(self, vehicleID):
        ...
    def isVehicleInvulnerable(self, vehicleID):
        ...
    def addVehicleMarkerIcon(self, vehicleID, iconName):
        ...
    def removeVehicleMarkerIcon(self, vehicleID, iconName):
        ...
    def onFactorsReady(self, vehicleID, diff):
        ...
    def applyBuff(self, data, vehicleID):
        ...
    def unApplyBuff(self, data):
        ...
    def _updateBuff(self, isActive, data):
        ...
    def _onPhaseChanged(self, arenaPhases):
        ...
    def _onPhaseTimeChanged(self, timeLeft, prev, lastPhase, isTimerAlarmEnabled):
        ...
    def _update(self):
        ...
    def _getRelevantGoal(self):
        ...
    def _getAliveAllyVehicles(self):
        ...
    def _showRelevantBattleHint(self, prevGoal, newGoal):
        ...
    def _isPlayerVehicle(self, vehicleID):
        ...
    def _getHintParams(self):
        ...
    def _onHideBattleHint(self, battleHint):
        ...
    def _removeBattleCommunicationMarkers(self):
        ...
