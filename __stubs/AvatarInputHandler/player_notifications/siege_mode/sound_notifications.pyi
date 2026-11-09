# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/player_notifications/siege_mode/sound_notifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from components_base.component import Component as Component
import SoundGroups as SoundGroups
from constants import VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, DEVICE_STATE_DESTROYED as DEVICE_STATE_DESTROYED
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class SiegeStates(object):
    STARTED = 0
    PAUSED = 1
    STOPPED = 2

class SoundNotifications(object):
    START_TO_SIEGE_MODE = 'start_to_siege_mode_PC'
    START_TO_BASE_MODE = 'start_to_base_mode_PC'
    MOVEMENT_LIMITED_ON = 'strv_siege_mode_movement_limited_on'
    MOVEMENT_LIMITED_OFF = 'strv_siege_mode_movement_limited_off'
    TRANSITION_TIMER = 'siege_mode_transition_timer'
    UI_TURBINE_MODE_ON_STOP = 'ui_turbine_polish_siege_mode_on_stop'
    UI_TURBINE_MODE_OFF_STOP = 'ui_turbine_polish_siege_mode_off_stop'
    UI_TURBINE_MODE_ON = 'ui_turbine_polish_siege_mode_on'
    UI_TURBINE_MODE_OFF = 'ui_turbine_polish_siege_mode_off'
    TWIN_GUN_SWITCH_START = 'gun_rld_dgp_switch_start'
    TWIN_GUN_SWITCH_STOP = 'gun_rld_dgp_switch_stop'

class SiegeModeNotificationsBase(Component):
    _MODE_TYPE = ''
    __vehicleID: Any
    def __init__(self, vehicleID):
        ...
    @property
    def vehicleID(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    @classmethod
    def getModeType(cls):
        ...

class TurboshaftModeSoundNotifications(SiegeModeNotificationsBase):
    _MODE_TYPE = 'turboshaft'
    __sounds: Any
    __lastState: Any
    __engineWasDestroyed: Any
    def __init__(self, vehicleID):
        ...
    def onSiegeStateChanged(self, vehicleID, newState, _):
        ...
    def destroy(self):
        ...

class TwinGunModeSoundNotifications(SiegeModeNotificationsBase):
    _MODE_TYPE = 'twinGun'
    __DEVICE = 'gun'
    __sessionProvider: Any
    __vehicleStateUpdatedHandlers: Any
    __siegeTransitionState: Any
    __startSound: Any
    def __init__(self, vehicleID):
        ...
    def destroy(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def onSiegeStateChanged(self, vehicleID, newState, _):
        ...
    def __clear(self):
        ...
    def __isSwitchingStarted(self):
        ...
    def __isValidDevice(self, device):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __playGunDestroyedSound(self):
        ...
    def __stopSound(self):
        ...
    def __updateDeviceState(self, value):
        ...
    def __updateRepairingDevice(self, value):
        ...

class SiegeModeSoundNotifications(SiegeModeNotificationsBase):
    _MODE_TYPE = 'siege'
    __sounds: Any
    __engineWasDestroyed: Any
    __siegeCallback: Any
    def __init__(self, vehicleID):
        ...
    def stop(self):
        ...
    def destroy(self):
        ...
    def onSiegeStateChanged(self, vehicleID, newState, timeToNextMode):
        ...
    def __onSiegeTimer(self):
        ...
    def __clear(self):
        ...

class PillboxSiegeSoundNotifications(SiegeModeSoundNotifications):
    _PILLBOX_COMPONENT_NAME = 'pillboxSiegeComponent'
    def onSiegeStateChanged(self, vehicleID, newState, timeToNextMode):
        ...

def playTriggerSound(soundStateChange):
    ...
def playUnavailableSound(soundStateChange):
    ...
