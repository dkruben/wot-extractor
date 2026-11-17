# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/target_designator_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import SoundGroups as SoundGroups
from chat_commands_consts import LocationMarkerSubType as LocationMarkerSubType
from constants import DIRECT_DETECTION_TYPE as DIRECT_DETECTION_TYPE
from helpers import dependency as dependency
from constants import IS_EDITOR as IS_EDITOR
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class VehiclePassengerInfoWatcher(object):
    ...

class TargetDesignatorSoundSystem(CGF.System, VehiclePassengerInfoWatcher):
    _SOUND_SPOTTED_VEHICLE_HIT_PC = 'gui_abl_tda_spotted'
    _SOUND_UNSPOTTED_VEHICLE_HIT_PC = 'gui_abl_tda_blindshot'
    _SOUND3D_UNSPOTTED_VEHICLE_HIT = 'gui_abl_tda_marker'
    _SOUND3D_SPOTTED_VEHICLE_HIT = 'gui_abl_tda_enemy_spotted'
    _STATE_VEHICLE_HIT_PC_GROUP = 'STATE_ext_abl_tda'
    _STATE_VEHICLE_HIT_PC_GROUP_ON = 'STATE_ext_abl_tda_on'
    _STATE_VEHICLE_HIT_PC_GROUP_OFF = 'STATE_ext_abl_tda_off'
    __sessionProvider: Any
    Reactions: Any
    __markers: Any
    __currentVehicle: Any
    def __init__(self):
        ...
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def __onStaticMarkerAdded(self, _, __, position, locationMarkerSubtype, *___):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __onSpottingIndicatorAction(self, detectionType, isVisible):
        ...
    def __onVehiclePassengerUpdating(self, _):
        ...
    def __onVehiclePassengerUpdate(self, vehicle):
        ...
    def __isEnemyVehicle(self, vehicle):
        ...
    @classmethod
    def __playGlobalSound(cls, eventName):
        ...
    @classmethod
    def __play3DSound(cls, eventName, position):
        ...
    @classmethod
    def __setGlobalState(cls, stateGroup, stateName):
        ...
