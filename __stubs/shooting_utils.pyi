# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/shooting_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WGAI as WGAI
import math as math
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, SHELL_TRAJECTORY_EPSILON_SERVER as SHELL_TRAJECTORY_EPSILON_SERVER
__DIST_LIMIT_TAGS: list
__STEEP_AIMING_TAGS: list
__MIXED_AIMING_TAGS: list

class TrajectoryMode(object):
    FLAT_AIMING = 0
    STEEP_AIMING = 1
    MIXED_AIMING = 2

class ShootingTest(object):
    __impl: Any
    def __init__(self, spaceID, vehicleDescr):
        ...
    def updateVehicleMatrix(self, vehicleMatrix):
        ...
    def setTargetEntity(self, targetEntity):
        ...
    def setEntitiesToAvoid(self, entitiesToAvoid):
        ...
    def setEntityCollisionCallback(self, entityCollisionCallback):
        ...
    def getCurTrajectoryMode(self):
        ...
    def setDestructibleHealthCallback(self, destructibleHealthCallback):
        ...
    def canShootAtPoint(self, targetPosition):
        ...
    def canShootAtPointFixedAngles(self, targetPosition, turretYaw, gunPitch):
        ...

def getMaxShotDistance(height, vehicleDescr):
    ...
def getPyShootingTest(spaceID, vehicleDescr):
    ...
def _getPyShootingTestYawLimits(spaceID, vehicleDescr):
    ...
