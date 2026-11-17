# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/consumables/opt_device_in_battle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
import SoundGroups as SoundGroups
import nations as nations
import functools as functools
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from items import vehicles as vehicles
from items.artefacts import ImprovedConfiguration as ImprovedConfiguration, StillVehicleOptionalDevice as StillVehicleOptionalDevice
from items.vehicles import VEHICLE_DEVICE_INDICES as VEHICLE_DEVICE_INDICES
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
OPT_DEVICE_USED = 'OPT_DEVICE_USED'

class DevicesSound(object):
    __camoNetEvents: tuple
    __stereoEvents: tuple
    __eventsMap: dict
    __resurrectionEventsMap: dict
    __enabled = False
    @classmethod
    def setEnabled(cls, enabled):
        ...
    @classmethod
    def arenaPeriodChange(cls, period):
        ...
    @classmethod
    def playSound(cls, deviceID, isOn):
        ...
    @classmethod
    def playResurrectionSound(cls, resurrectionName):
        ...

class OptDeviceInBattle(object):
    sessionProvider: Any
    _deviceID: Any
    _status: Any
    _lastStatus: Any
    def __init__(self, deviceID, status):
        ...
    def __repr__(self):
        ...
    @property
    def deviceID(self):
        ...
    def isNeedGlow(self):
        ...
    def getStatus(self):
        ...
    def getDescriptor(self):
        ...
    def getIntCD(self):
        ...
    def isUsed(self):
        ...
    def updateStatus(self, status):
        ...
    def getBattleStatus(self):
        ...
    def apply(self):
        ...

class StillStillOptDeviceInBattle(OptDeviceInBattle):
    def apply(self):
        ...

class ResurrectionOptDeviceInBattle(OptDeviceInBattle):
    def getStatus(self):
        ...
    def isResurrectionDeviceEnable(self, deviceName):
        ...
    # decorador original: @skipOnRewind
    def isNeedGlow(self):
        ...
    def isUsed(self):
        ...
    def getBattleStatus(self):
        ...
    # decorador original: @skipOnRewind
    def apply(self):
        ...
    def _getModules(self):
        ...

def _getDescriptor(deviceID):
    ...
def skipOnRewind(func):
    ...
def createOptDeviceInBattle(deviceID, status):
    ...
