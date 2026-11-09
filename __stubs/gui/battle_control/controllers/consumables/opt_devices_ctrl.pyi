# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/consumables/opt_devices_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lmap as lmap
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control import vehicle_getter as vehicle_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.consumables.opt_device_in_battle import createOptDeviceInBattle as createOptDeviceInBattle, DevicesSound as DevicesSound
from gui.battle_control.controllers.consumables.opt_device_sound_ctrl import OptDeviceSoundController as OptDeviceSoundController
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from items import vehicles as vehicles
__all__: tuple

class OptionalDevicesController(IBattleController):
    __slots__: tuple
    __eManager: Any
    onOptionalDeviceAdded: Any
    onOptionalDeviceUpdated: Any
    onOptionalDevicesCleared: Any
    onDescriptorDevicesChanged: Any
    __optionalDevices: Any
    __soundManager: Any
    __sessionProvider: Any
    __order: Any
    __optionalDevicesInDescriptor: Any
    def __init__(self, setup):
        ...
    def __repr__(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    @property
    def soundManager(self):
        ...
    def clear(self, leave=True):
        ...
    def reset(self):
        ...
    def getOptDeviceInBattle(self, deviceID):
        ...
    def isOptionalDeviceOn(self, deviceID):
        ...
    def isOptionalDeviceOnByCD(self, intCD):
        ...
    def getOrderedOptionalDevicesLayout(self):
        ...
    def setOptionalDevice(self, deviceID, isOn):
        ...
    def startVehicleVisual(self, vProxy, isImmediate):
        ...
    def _createSoundManager(self):
        ...
    def _onArenaPeriodChange(self, period, *_):
        ...
    def __onBattleSessionStart(self):
        ...
    def __onBattleSessionStop(self):
        ...
    def __onVehicleChanged(self, vehicle):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onVehicleInfoUpdated(self, vehicleID):
        ...
    def __invalidateOptionalDevices(self, vehicleID):
        ...
