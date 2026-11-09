# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/sound_ctrls/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from constants import VEHICLE_HIT_FLAGS as VHF
from Event import EventsSubscriber as EventsSubscriber
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.sounds import IShotsResultSoundController as IShotsResultSoundController
from shared_utils import nextTick as nextTick

class SoundPlayersController(object):
    _soundPlayers: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...

class SoundPlayersBattleController(IBattleController):
    __soundPlayers: Any
    __wasStarted: Any
    def __init__(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def _initializeSoundPlayers(self):
        ...
    def _startPlayers(self):
        ...
    def __destroyPlayers(self):
        ...

class SoundPlayer(object):
    def init(self):
        ...
    def destroy(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    @staticmethod
    def _playSound2D(event, checkAlive=False):
        ...

class VehicleStateSoundPlayer(SoundPlayer):
    _sessionProvider: Any
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onSwitchViewPoint(self):
        ...

class BaseEfficiencySoundPlayer(SoundPlayer):
    __sessionProvider: Any
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onEfficiencyReceived(self, events):
        ...

class EquipmentComponentSoundPlayer(object):
    __slots__: tuple
    __sessionProvider: Any
    __eventsSubscriber: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def _onEquipmentComponentUpdated(self, equipmentName, vehicleID, equipmentInfo):
        ...
    def _getEquipmentName(self):
        ...
    def _stopSounds(self):
        ...
    def _getComponentName(self):
        ...
    def __onVehicleControlling(self, vehicle):
        ...

class ShotsResultSoundController(IShotsResultSoundController):
    ENEMY_AND_GUN_DAMAGED_BY_PROJECTILE = 'enemy_hp_damaged_by_projectile_and_gun_damaged_by_player'
    ENEMY_AND_CHASSIS_DAMAGED_BY_PROJECTILE = 'enemy_hp_damaged_by_projectile_and_chassis_damaged_by_player'
    ENEMY_DAMAGED_BY_PROJECTILE = 'enemy_hp_damaged_by_projectile_by_player'
    ENEMY_DAMAGED_BY_NOT_PIERCING = None
    ENEMY_DAMAGED_BY_DIRECT_EXPLOSION = None
    ENEMY_DAMAGED_BY_NEAR_EXPLOSION = 'enemy_hp_damaged_by_near_explosion_by_player'
    ENEMY_NOT_DAMAGED_ATTEMPT_AND_GUN_DAMAGED = 'enemy_no_hp_damage_at_attempt_and_gun_damaged_by_player'
    ENEMY_NOT_DAMAGED_ATTEMPT_AND_CHASSIS_DAMAGED = 'enemy_no_hp_damage_at_attempt_and_chassis_damaged_by_player'
    ENEMY_NOT_DAMAGED_ATTEMPT = 'enemy_no_hp_damage_at_attempt_by_player'
    ENEMY_NOT_DAMAGED_NO_ATTEMPT_AND_GUN_DAMAGED = 'enemy_no_hp_damage_at_no_attempt_and_gun_damaged_by_player'
    ENEMY_NOT_DAMAGED_NO_ATTEMPT_AND_CHASSIS_DAMAGED = 'enemy_no_hp_damage_at_no_attempt_and_chassis_damaged_by_player'
    ENEMY_NOT_DAMAGED_NO_ATTEMPT = 'enemy_no_hp_damage_at_no_attempt_by_player'
    ENEMY_NOT_DAMAGED_BY_NEAR_EXPLOSION = 'enemy_no_hp_damage_by_near_explosion_by_player'
    ENEMY_NOT_DAMAGED_AND_NOT_PIERCED = 'enemy_no_piercing_by_player'
    ENEMY_RICOCHET = 'enemy_ricochet_by_player'
    _DEFAULT_EVENT_PREFIX = ''
    _FREQUENT_EVENT_PREFIX = 'frequent_'
    _SHOT_RESULT_SOUND_PRIORITIES: dict
    _ARMOR_SCREEN_FLAGS: Any
    __sessionProvider: Any
    __eventPrefix: Any
    def __init__(self):
        ...
    def startControl(self, *_):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def getBestSoundEventName(self, bestSound):
        ...
    def getBestShotResultSound(self, currBest, newSoundName, otherData):
        ...
    def getVehicleHitResultSound(self, enemyVehID, hitFlags, enemiesHitCount):
        ...
    def __invalidateCurrentVehicle(self, vehicle):
        ...
