# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_control/controllers/sound_ctrls/comp7_battle_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from functools import partial as partial
import BigWorld as BigWorld
import WWISE as WWISE
import typing as typing
from enum import Enum as Enum
import SoundGroups as SoundGroups
from IlluminationFlareTargetController import IlluminationFlareTargetController as IlluminationFlareTargetController
from Vehicle import StunInfo as StunInfo
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayersBattleController as SoundPlayersBattleController, VehicleStateSoundPlayer as VehicleStateSoundPlayer, SoundPlayer as SoundPlayer
from helpers import dependency as dependency
from helpers_common import reprSlots as reprSlots
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from points_of_interest_shared import PoiStatus as PoiStatus, ENEMY_VEHICLE_ID as ENEMY_VEHICLE_ID, PoiBlockReasons as PoiBlockReasons
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from shared_utils import nextTick as nextTick, CONST_CONTAINER as CONST_CONTAINER
from vehicle_systems.tankStructure import TankSoundObjectsIndexes as TankSoundObjectsIndexes
_logger: Any
_EQUIPMENT_ACTIVATED_SOUNDS: dict
_EQUIPMENT_DEACTIVATED_SOUNDS: dict
_EQUIPMENT_PREPARING_START_SOUNDS: dict
_EQUIPMENT_PREPARING_CANCEL_SOUNDS: dict
_EQUIPMENT_PRE_DEACTIVATION_SOUNDS: dict
_EQUIPMENT_ARTILLERY_NAMES: list
_PreDeactivationParams: Any
BAN_VIEW_SOUND_SPACE: Any
BAN_PROGRESSION_SOUND_SPACE: Any

class Comp7BattleSoundController(SoundPlayersBattleController):
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def _initializeSoundPlayers(self):
        ...

class SOUNDS(CONST_CONTAINER):
    GENERAL_STATE = 'STATE_gameplay_overlay'
    GENERAL_STATE_ON = 'STATE_gameplay_overlay_on'
    GENERAL_STATE_OFF = 'STATE_gameplay_overlay_off'
    PROGRESSBAR_START = 'comp_7_bans_progressbar_start'
    PROGRESSBAR_STOP = 'comp_7_bans_progressbar_stop'

class _EquipmentStateSoundPlayer(VehicleStateSoundPlayer):
    __sessionProvider: Any
    __POI_EQUIPMENT_ACTIVATED: dict
    __callbackDelayer: Any
    __activeEquipment: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onSwitchViewPoint(self):
        ...
    def __onEquipmentUpdated(self, _, item):
        ...
    def __onPoiEquipmentUsed(self, equipment, vehicleID):
        ...
    def __play2dFromMapping(self, soundsMapping, item=None, itemName=None):
        ...
    def __play2dFromMappingDelayed(self, soundsMapping, item):
        ...
    def __clearActiveEquipment(self):
        ...

class _EquipmentZoneSoundPlayer(VehicleStateSoundPlayer):
    __sessionProvider: Any
    __EQUIPMENT_ZONE_ENTER: dict
    __EQUIPMENT_ZONE_EXIT: dict
    __EQUIPMENT_ZONE_STATE: dict
    __vehicleStates: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onSwitchViewPoint(self):
        ...
    def __stateIsActive(self, value):
        ...
    def __checkSource(self, value):
        ...
    def __setZoneState(self, state, enter):
        ...
    def __clearActiveEquipment(self):
        ...

class _RoleSkillSoundPlayer(SoundPlayer):
    __sessionProvider: Any
    __EQUIPMENT_LEVEL_UP = 'comp_7_ability_levelup'
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onRoleEquipmentStateChanged(self, state, previousState):
        ...

class _ArtilleryAreaParams(object):
    __slots__: tuple
    __repr__ = reprSlots
    position: Any
    radius: Any
    endTime: Any
    threatsCurrentVehicle: Any
    def __init__(self, position, radius, endTime):
        ...

class _ArtillerySoundPlayer(SoundPlayer):
    __sessionProvider: Any
    __ARTILLERY_ENTER = 'comp_7_ability_arty_enter'
    __ARTILLERY_EXIT = 'comp_7_ability_arty_exit'
    __ARTILLERY_DAMAGE_PC = 'imp_artillery_expl_huge_NPC_PC'
    __callbackDelayer: Any
    __artilleryAreas: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onEquipmentAreaCreated(self, equipment, position, endTime, level=None):
        ...
    def __updateAttack(self):
        ...

class _PrebattleSoundPlayer(SoundPlayer):
    __sessionProvider: Any
    __CONFIRM_VEHICLE_SELECTION = 'comp_7_tank_confirm'
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onSelectionConfirmed(self):
        ...
    def _onBattleStarted(self):
        ...

class _PoiVehicleState(Enum):
    DEFAULT = 0
    CAPTURING = 1
    BLOCKED = 2

class _PoiSNSoundPlayer(VehicleStateSoundPlayer):
    __POI_CAPTURE_TIMER_SHOWN = 'comp_7_poi_timer_capture'
    __POI_CAPTURE_BLOCKED = 'comp_7_poi_capture_blocked'
    __poiVehicleState: Any
    def __init__(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def __isCapturing(self, state, value):
        ...
    def __isBlocked(self, state, value):
        ...
    def __setState(self, state):
        ...

class _BuffSNSoundPlayer(VehicleStateSoundPlayer):
    __RESET_ABILITY = 'comp_7_ability_timer_reset'
    __EQUIPMENT_STATE_ACTIVATED: dict
    __vehicleStates: Any
    def __init__(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...

def _getPlayerVehicle():
    ...
def _play2d(soundName):
    ...
def _playVehiclePC(soundName, soundObjectIndex):
    ...
