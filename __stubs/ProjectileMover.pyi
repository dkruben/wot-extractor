# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ProjectileMover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
import CGF as CGF
from cgf_modules import game_events as game_events
import constants as constants
import TriggersManager as TriggersManager
import helpers as helpers
from TriggersManager import TRIGGER_TYPE as TRIGGER_TYPE
import FlockManager as FlockManager
from items.components.component_constants import INVALID_EFFECT_INDEX as INVALID_EFFECT_INDEX
from vehicle_systems.tankStructure import TankPartNames as TankPartNames, ColliderTypes as ColliderTypes
from helpers import gEffectsDisabled as gEffectsDisabled
from helpers.trajectory_drawer import TrajectoryDrawer as TrajectoryDrawer
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME

class ProjectileMover(object):
    __START_POINT_MAX_DIFF = 20
    __PROJECTILE_HIDING_TIME = 0.05
    __PROJECTILE_TIME_AFTER_DEATH = 2.0
    __AUTO_SCALE_DISTANCE = 180.0
    __projectiles: Any
    __isPaused: Any
    salvo: Any
    __ballistics: Any
    __debugDrawer: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def add(self, shotID, effectsDescr, prefabEffIndex, gravity, refStartPoint, refVelocity, startPoint, maxDistance, shellTypeIdx, shellCaliber, attackerID=0, tracerCameraPos=None, gunInstallationIndex=...):
        ...
    def hide(self, shotID, endPoint):
        ...
    def explode(self, shotID, effectsDescr, prefabEffIndex, effectMaterial, shellType, caliber, endPoint, velocityDir, speed):
        ...
    def hold(self, shotID):
        ...
    def setSpaceID(self, spaceID):
        ...
    def setPause(self, isPause):
        ...
    def __notifyProjectileHit(self, hitPosition, proj):
        ...
    def __addExplosionEffect(self, position, proj, velocityDir, speed):
        ...
    def __killProjectile(self, shotID, position, impactVelDir, velocity, deathType, explode):
        ...
    def __deleteProjectile(self, shotID):
        ...
    def __addWaterRipples(self, position, rippleDiameter, ripplesLeft):
        ...
    def __delProjectile(self, shotID):
        ...
    def __onCameraChanged(self, controlModeName, currentVehicleId=None):
        ...

class EntityCollisionData(object):
    __slots__: tuple
    hitAngleCos: Any
    __isVehicle: Any
    entity: Any
    armor: Any
    def __init__(self, entityID, partIndex, matKind, isVehicle=True):
        ...
    def isVehicle(self):
        ...

def ownVehicleGunShotPositionGetter():
    ...
def collideDynamicAndStatic(startPoint, endPoint, exceptIDs, collisionFlags=128, skipGun=False):
    ...
def collideDynamic(startPoint, endPoint, exceptIDs, skipGun=False):
    ...
def collideVehiclesAndStaticScene(startPoint, endPoint, vehicles, collisionFlags=128, skipGun=False):
    ...
