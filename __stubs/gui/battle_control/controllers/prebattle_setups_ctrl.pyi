# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_setups_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from account_helpers.settings_core.settings_constants import GAME as GAME
from battle_modifiers_common import EXT_DATA_MODIFIERS_KEY as EXT_DATA_MODIFIERS_KEY
from constants import ARENA_PERIOD as ARENA_PERIOD, VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE
from gui.battle_control.arena_info.interfaces import IPrebattleSetupsController as IPrebattleSetupsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.items_parameters.functions import getVehicleFactors as getVehicleFactors
from gui.shared.utils.MethodsRules import MethodsRules as MethodsRules
from gui.veh_post_progression.battle_cooldown_manager import BattleCooldownManager as BattleCooldownManager
from gui.veh_post_progression.helpers import setFeatures as setFeatures, setDisabledSwitches as setDisabledSwitches, getInstalledShells as getInstalledShells, updateInvInstalled as updateInvInstalled
from gui.veh_post_progression.sounds import playSound as playSound, Sounds as Sounds
from helpers import dependency as dependency
from items import vehicles as vehicles
from items.components.post_progression_components import getActiveModifications as getActiveModifications
from items.utils import getCircularVisionRadius as getCircularVisionRadius, getFirstReloadTime as getFirstReloadTime
from post_progression_common import EXT_DATA_PROGRESSION_KEY as EXT_DATA_PROGRESSION_KEY, EXT_DATA_SLOT_KEY as EXT_DATA_SLOT_KEY, TANK_SETUP_GROUPS as TANK_SETUP_GROUPS, TankSetupLayouts as TankSetupLayouts, TankSetups as TankSetups, VehicleState as VehicleState, unpackActionCDs as unpackActionCDs
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from items.vehicles import VehicleDescr as VehicleDescr
_logger: Any
_SWITCH_SETUPS_ACTION = 0
_EXT_ENHANCEMENTS_KEY = 'extEnhancements'
_EXT_PROGRESSION_MODS = 'extActiveProgression'
_EXT_RESPAWN_BOOST = 'respawnReloadTimeFactor'
_EXT_SIEGE_STATE_KEY = 'extSiegeState'
_SETUP_NAME_TO_LAYOUT: dict

class _States(CONST_CONTAINER):
    IDLE = 0
    VEHICLE_ID = 1
    CREW = 2
    DYN_SLOT = 4
    ENHANCEMENTS = 8
    PROGRESSION = 32
    RESPAWN = 64
    SETUPS = 128
    SETUPS_INDEXES = 256
    DISABLED_SWITCHES = 512
    INIT_COMPLETE = 1024
    SELECTION_STARTED = 2048
    SELECTION_STOPPED = 4096
    SELECTION_ENDED = 8192
    INIT_READY: Any
    SELECTION_AWAIT_HIDING = 16384

class IPrebattleSetupsListener(object):
    def showSetupsView(self, vehicle, isArenaLoaded=False):
        ...
    def updateVehicleParams(self, vehicle, factors):
        ...
    def updateVehicleSetups(self, vehicle):
        ...
    def stopSetupsSelection(self):
        ...
    def hideSetupsView(self):
        ...
    def onArenaLoaded(self):
        ...

class PrebattleSetupsController(MethodsRules, IPrebattleSetupsController):
    __itemsFactory: Any
    __sessionProvider: Any
    __settingsCore: Any
    __slots__: tuple
    __state: Any
    __invData: Any
    __extData: Any
    __playerVehicleID: Any
    __vehicle: Any
    __hasValidCaps: Any
    __cooldown: Any
    __arenaLoaded: Any
    _viewComponents: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def getPrebattleSetupsVehicle(self):
        ...
    def getPrebattleVehicleID(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def isArenaLoaded(self):
        ...
    def isSelectionStarted(self):
        ...
    def isSelectionEnded(self):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setPlayerVehicle(self, vehicleID, vehDescr):
        ...
    def setPeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def stopSelection(self):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setCrew(self, vehicleID, crew):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setDynSlotType(self, vehicleID, dynSlotTypeID):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setEnhancements(self, vehicleID, enhancements):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setPostProgression(self, vehicleID, itemCDs):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setDisabledSwitches(self, vehicleID, groupIDs):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setRespawnReloadFactor(self, vehicleID, reloadFactor):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setSetups(self, vehicleID, setups):
        ...
    def setInvData(self, setups):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setSetupsIndexes(self, vehicleID, setupsIndexes):
        ...
    def updateLayoutIndexes(self, setupsIndexes):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setSiegeState(self, vehicleID, siegeState):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def setVehicleAttrs(self, vehicleID, attrs):
        ...
    def setViewComponents(self, *components):
        ...
    # decorador original: @MethodsRules.delayable(...)
    def onCurrentShellUpdate(self, vehicleID):
        ...
    def arenaLoadCompleted(self):
        ...
    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def switchLayout(self, groupID, layoutIdx):
        ...
    def getSlotItem(self, group, layout, slotId):
        ...
    def __isSelectionAvailable(self):
        ...
    def __isSelectionStopped(self):
        ...
    def __isSelectionShouldEnded(self):
        ...
    def __isSelectionShouldStarted(self):
        ...
    def __onInitStepCompleted(self, stepState):
        ...
    def __onFiniStepCompleted(self):
        ...
    def __onStartSelection(self):
        ...
    def __updateAmmoCtrl(self):
        ...
    def __updateAmmoCtrlParams(self, factors):
        ...
    def __updateFeedbackParams(self, factors):
        ...
    def __updateGuiVehicle(self):
        ...
    def __updatePeriod(self, period):
        ...
    def __updateState(self, addMask):
        ...
    def __updateSetupIndexes(self):
        ...
    def __updateSiegeState(self):
        ...
    @property
    def __postProgressionState(self):
        ...
