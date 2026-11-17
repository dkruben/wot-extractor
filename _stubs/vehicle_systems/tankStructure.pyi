# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/tankStructure.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
import Math as Math
from collections import namedtuple as namedtuple
from constants import VehiclePartName as VehiclePartName
from BigWorld import CollisionComponent as CollisionComponent
from typing import Union as Union, Iterable as Iterable, Sized as Sized, Optional as Optional
AABB: Any
_logger: Any
ModelsSetParams: Any
VehiclePartsTuple: Any
UNDAMAGED_SKELETON: Any
CRASHED_SKELETON: Any

class CgfTankNodes(object):
    TANK_ROOT = 'Tank.Root'

class ModelStates(object):
    UNDAMAGED = 'undamaged'
    DESTROYED = 'destroyed'
    EXPLODED = 'exploded'

class TankRenderMode(object):
    NORMAL = 0
    CRASH = 1
    SERVER_COLLISION = 2
    CLIENT_COLLISION = 3
    CRASH_COLLISION = 4
    OVERLAY_COLLISION = 5
    ARMOR_WIDTH_COLLISION = 6
    DISABLE = 7

class TankCollisionPartNames(object):
    CHASSIS = 'chassisCollision'
    HULL = 'hullCollision'
    TURRET = 'turretCollision'
    GUN = 'gunCollision'
    WHEEL = 'wheelCollision'
    ALL: tuple
    @staticmethod
    def getIdx(name):
        ...

class TankPartNames(object):
    CHASSIS = VehiclePartName.CHASSIS
    HULL = VehiclePartName.HULL
    TURRET = VehiclePartName.TURRET
    GUN = VehiclePartName.GUN
    ALL: tuple
    @staticmethod
    def getIdx(name):
        ...
    @staticmethod
    def getActualNodeNameByPartName(partName, isAlive=True):
        ...

class DetachedTurretPartNames(object):
    ALL: tuple
    @staticmethod
    def getIdx(name):
        ...

class DetachedTurretPartIndexes(object):
    TURRET = 0
    GUN = 1
    ALL: tuple
    @staticmethod
    def getName(idx):
        ...

class TankPartIndexes(object):
    CHASSIS = 0
    HULL = 1
    TURRET = 2
    GUN = 3
    ALL: tuple
    @staticmethod
    def getName(idx):
        ...

class TankNodeNames(object):
    TRACK_LEFT_FRONT = 'HP_Track_LFront'
    TRACK_LEFT_REAR = 'HP_Track_LRear'
    TRACK_RIGHT_FRONT = 'HP_Track_RFront'
    TRACK_RIGHT_REAR = 'HP_Track_RRear'
    TRACK_LEFT_UP_FRONT = 'HP_TrackUp_LFront'
    TRACK_LEFT_UP_REAR = 'HP_TrackUp_LRear'
    TRACK_RIGHT_UP_FRONT = 'HP_TrackUp_RFront'
    TRACK_RIGHT_UP_REAR = 'HP_TrackUp_RRear'
    GUI = 'HP_gui'
    HULL_SWINGING = 'V'
    TURRET_JOINT = 'HP_turretJoint'
    HULL_FIRE_1 = 'HP_Fire_1'
    GUN_JOINT = 'HP_gunJoint'
    GUN_INCLINATION = 'Gun'
    GUN_RECOIL = 'G'
    GUN_RECOIL_L = 'G_L'
    GUN_RECOIL_R = 'G_R'
    GUN_FIRE = 'HP_gunFire'
    TRACK_LEFT_MID = 'DM_Track_LMid'
    TRACK_RIGHT_MID = 'DM_Track_RMid'
    CHASSIS_MID_TRAIL = 'DM_Mid_Trail'

class TankSoundObjectsIndexes(object):
    CHASSIS = 0
    ENGINE = 1
    GUN = 2
    HIT = 3
    COUNT = 4

class ColliderTypes(object):
    DYNAMIC_FLAG = 1
    TANK_FLAG = 2
    HANGAR_FLAG = 4
    PLAYER_FLAG = 8
    DYNAMIC_COLLIDER = DYNAMIC_FLAG
    VEHICLE_COLLIDER: Any
    PLATOON_VEHICLE_COLLIDER: Any
    PLAYER_VEHICLE_COLLIDER: Any
    HANGAR_VEHICLE_COLLIDER: Any
    HANGAR_PLAYER_VEHICLE_COLLIDER: Any

def getCrashedSkeleton(vehicleDesc):
    ...
def getPartModelsFromDesc(vehicleDesc, modelsSetParams):
    ...
def getCollisionModelsFromDesc(vehicleDesc, state):
    ...
def getVehicleAABB(collisions):
    ...
def selectItemByTankSize(tankSizeLowerBounds, items, default=None, aabb=None):
    ...
