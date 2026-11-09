# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_setup_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import iteritems as iteritems
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
import Math as Math
import BattleReplay as BattleReplay
import constants as constants
from Event import Event as Event, EventManager as EventManager
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.interfaces import IPrebattleSetupController as IPrebattleSetupController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.gui_vehicle_builder import VehicleBuilder as VehicleBuilder
from gui.veh_post_progression.sounds import playSound as playSound, Sounds as Sounds
from helpers import dependency as dependency
from post_progression_common import TankSetups as TankSetups
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Dict as Dict
_logger: Any

class _SceneController(object):
    __dynObjectsCache: Any
    __spawnPoints: Any
    __config: Any
    __pendingSpawnPoints: Any
    def __init__(self, setup):
        ...
    def createSpawnPoint(self, vehicleID, positionNumber, status):
        ...
    def updateSpawnPoint(self, vehicleID, newStatus):
        ...
    def clear(self):
        ...
    def __onVehicleEnterWorld(self, vehicle):
        ...
    def __createSpawnPointPrefab(self, vehicle, positionNumber, status):
        ...
    def __getAreaColor(self, vehicleID, status):
        ...

class PrebattleSetupController(IPrebattleSetupController):
    __sessionProvider: Any
    __em: Any
    __currentArenaPeriod: Any
    __guiVehicle: Any
    __started: Any
    onVehiclesListUpdated: Any
    onVehicleChanged: Any
    onSelectionConfirmed: Any
    onTeammateSelectionStatuses: Any
    onBattleStarted: Any
    __sceneCtrl: Any
    def __init__(self, setup):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def setPeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def confirmVehicleSelection(self):
        ...
    def isSelectionConfirmed(self):
        ...
    def chooseVehicle(self, newCD):
        ...
    def setAvailableVehicles(self, vehiclesList):
        ...
    @staticmethod
    def getVehiclesList():
        ...
    def _updatePreBattleSetup(self, vehicleInfo):
        ...
    def updateVehicleInfo(self, vehicleInfo):
        ...
    def getCurrentVehicleInfo(self, extendWithDataFromList=False):
        ...
    def updateSpawnPoints(self, spawnPoints):
        ...
    def updateConfirmationStatuses(self, newStatuses):
        ...
    def getCurrentGUIVehicle(self):
        ...
    def switchPrebattleSetup(self, groupID, layoutIdx):
        ...
    def isVehicleStateIndicatorAllowed(self):
        ...
    def getVehicleHealth(self, vehicle):
        ...
    def __extendWithDataFromList(self, info):
        ...
    def __updatePeriod(self, period):
        ...
    @staticmethod
    def __makeGUIVehicle(vehicleInfo):
        ...
