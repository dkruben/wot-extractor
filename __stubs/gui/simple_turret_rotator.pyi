# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/simple_turret_rotator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import Math as Math
import Event as Event
import math_utils as math_utils
from vehicle_systems.tankStructure import TankNodeNames as TankNodeNames
from VehicleGunRotator import VehicleGunRotator as VehicleGunRotator, MatrixAnimator as MatrixAnimator
logger: Any

class SimpleTurretRotator(object):
    __slots__: tuple
    __ROTATION_TICK_LENGTH = 0.05
    turretMatrix: Any
    turretYaw: Any
    isStarted: Any
    __isStarted: Any
    __turretYaw: Any
    __targetTurretYaw: Any
    __turretTranslation: Any
    __turretPitch: Any
    __rotationTime: Any
    __timerID: Any
    __turretMatrixAnimator: Any
    __easingCls: Any
    __easing: Any
    _eventsManager: Any
    onTurretRotationStarted: Any
    onTurretRotated: Any
    def __init__(self, compoundModel=None, currTurretYaw=0.0, turretTranslation=..., turretPitch=0.0, easingCls=...):
        ...
    def destroy(self):
        ...
    def start(self, targetTurretYaw, rotationTime=None):
        ...
    def setEasing(self, easingCls):
        ...
    def stop(self):
        ...
    def reset(self):
        ...
    def __onTick(self):
        ...
    def __updateTurretMatrix(self, yaw, time):
        ...
