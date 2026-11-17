# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/vehicle_composition.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import enum as enum
import BigWorld as BigWorld
import Compound as Compound
import CGF as CGF
import EntitySync as EntitySync
import Math as Math
import math_utils as math_utils
from constants import IS_UE_EDITOR as IS_UE_EDITOR
from items.components import component_constants as component_constants
from items.components.c11n_constants import HANGER_POSTFIX as HANGER_POSTFIX, AttachmentType as AttachmentType
from vehicle_systems.tankStructure import TankNodeNames as TankNodeNames, TankPartNames as TankPartNames, TankCollisionPartNames as TankCollisionPartNames
from vehicle_appearance.component import VehicleAppearanceComponent as VehicleAppearanceComponent
from helpers import isPlayerAccount as isPlayerAccount
from objects_hierarchy import PrefabsMapItem as PrefabsMapItem, ExtraSlotsMapItem as ExtraSlotsMapItem
from CGF import GameObject as GameObject
from Vehicle import Vehicle as Vehicle
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle as ClientSelectableCameraVehicle
from SimulatedVehicle import SimulatedVehicle as SimulatedVehicle
from vehicle_appearance.common_tank_appearance import CommonTankAppearance as CommonTankAppearance
from gui.hangar_vehicle_appearance import HangarVehicleAppearance as HangarVehicleAppearance
from typing import Iterable as Iterable, List as List, Tuple as Tuple, Optional as Optional
TAppearance: Any
VEHICLE_PART_TO_SLOT: dict
DESTROYED_VEHICLE_PART_TO_SLOT: dict
ATTACHMENT_TYPE_TO_SLOT: dict
_VEHICLE_SLOTS_MAP: dict
_DETACHED_TURRET_SLOTS_MAP: dict

class VehicleSlots(enum.Enum):
    CHASSIS = TankPartNames.CHASSIS
    HULL = TankPartNames.HULL
    TURRET = TankPartNames.TURRET
    GUN_JOINT = TankNodeNames.GUN_JOINT
    GUN = TankPartNames.GUN
    GUN_INCLINATION = TankNodeNames.GUN_INCLINATION
    GUN_FIRE = TankNodeNames.GUN_FIRE
    GUN_RECOIL = TankNodeNames.GUN_RECOIL
    GUN_RECOIL_L = TankNodeNames.GUN_RECOIL_L
    GUN_RECOIL_R = TankNodeNames.GUN_RECOIL_R
    TURRET_COLLISION = TankCollisionPartNames.TURRET
    GUN_COLLISION = TankCollisionPartNames.GUN

def removeComposition(gameObject, queue=None):
    ...
def createVehicleComposition(gameObject, vehicleGameObject=..., prefabMap=None, followNodes=True, extraSlots=None, dynSlotNodes=None, extraSlotComponents=None, queue=None):
    ...
def _getSlotTransform(scale, rotation, position):
    ...
def getExtraSlotMap(vDesc, appearance):
    ...
def createDetachedTurretComposition(gameObject, prefabMap=None, extraSlots=None):
    ...
def findParentVehicle(gameObject):
    ...
def findParentVehicleAppearance(gameObject):
    ...
def getObjectSlots(typeDescriptor):
    ...
