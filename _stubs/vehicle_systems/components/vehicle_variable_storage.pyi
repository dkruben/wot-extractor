# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/vehicle_variable_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import enum as enum
import logging as logging
import Math as Math
import CGF as CGF
from cgf_modules.variable_components import VariableStorageComponent as VariableStorageComponent
from constants import VEHICLE_CLASSES as VEHICLE_CLASSES, VEHICLE_CLASS_INDICES as VEHICLE_CLASS_INDICES
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes
from Vehicle import Vehicle as Vehicle
from vehicle_appearance.common_tank_appearance import CommonTankAppearance as CommonTankAppearance
from gui.hangar_vehicle_appearance import HangarVehicleAppearance as HangarVehicleAppearance
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from items.vehicle_items import Gun as Gun, Shell as Shell
from cgf_modules.variable_components import VariableType as VariableType
TAppearance: Any
_logger: Any

class VehicleRootVars(enum.Enum):
    TYPE = 'vehicle/type'
    MAX_HEALTH = 'vehicle/maxHealth'

class VehicleGunVars(enum.Enum):
    MUZZLE_BRAKE = 'vehicle/gun/muzzleBrake'
    GUN_LENGTH = 'vehicle/gun/gunLength'
    GUN_CALIBER = 'vehicle/gun/caliber'
    TIME_BETWEEN_SHOTS = 'vehicle/gun/timeBetweenShots'

def createForRoot(vehicle, queue=None):
    ...
def getVariableValuesForGun(appearance):
    ...
def update(go, varName, value):
    ...
