# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/components_states/ammo/collections.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
from gui.battle_control.components_states.ammo.constants import AmmoShootPossibility as AmmoShootPossibility
from gui.battle_control.components_states.ammo.shells import DefaultAmmoMode as DefaultAmmoMode
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from shared_utils import findFirst as findFirst
from ChargeableBurstComponent import ChargeableBurstAmmoState as ChargeableBurstAmmoState
from StationaryReloadController import StationaryReloadAmmoState as StationaryReloadAmmoState
from TemperatureGunController import TemperatureGunAmmoState as TemperatureGunAmmoState
from gui.battle_control.components_states.ammo.interfaces import IComponentAmmoState as IComponentAmmoState, IAmmoMode as IAmmoMode

class AmmoStatesROCollection(object):
    _ammoStates: Any
    def __init__(self, ammoStates):
        ...
    @property
    def ammoStates(self):
        ...
    @property
    def chargeableBurstAmmoState(self):
        ...
    @property
    def extraShotReloadState(self):
        ...
    @property
    def stationaryReloadAmmoState(self):
        ...
    @property
    def temperatureGunAmmoState(self):
        ...
    def isReloadingBlocked(self):
        ...
    def canChangeVehicleSetting(self, code):
        ...
    def canShootValidation(self, defaultError):
        ...
    def getSpecialReloadMessage(self):
        ...
    def getAmmoMode(self):
        ...
    def getShotsAmount(self):
        ...
    def getShootPossibility(self, currentShells):
        ...
    def getShellReloadTimes(self, currShell, shellChangeTime, shells):
        ...

class AmmoStatesRWCollection(AmmoStatesROCollection):
    _ammoStates: Any
    @property
    def ammoStates(self):
        ...
    def getReadOnlyCopy(self):
        ...
    def setAmmoStates(self, ammoStates):
        ...
    def clear(self):
        ...
