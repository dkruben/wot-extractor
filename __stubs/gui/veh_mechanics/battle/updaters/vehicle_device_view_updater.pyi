# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/vehicle_device_view_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, VEHICLE_DEVICE_IN_COMPLEX_ITEM as VEHICLE_DEVICE_IN_COMPLEX_ITEM
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Dict as Dict, List as List

class IVehicleDeviceStatusView(object):
    def vehicleDeviceStatusChanged(self, devicesStatuses):
        ...

class VehicleDeviceStatusUpdater(ViewUpdater):
    __sessionProvider: Any
    __observed: Any
    __devicesStatuses: Any
    def __init__(self, observed, view):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def __onVehicleStateUpdated(self, stateID, value):
        ...
    def __onVehicleDeviceStatusChanged(self, deviceName, status):
        ...

def makeUIDeviceState(devicesStatuses):
    ...
