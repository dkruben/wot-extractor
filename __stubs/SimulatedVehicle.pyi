# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SimulatedVehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from copy import copy as copy
from functools import partial as partial
import BigWorld as BigWorld
import Math as Math
import CGF as CGF
from cgf_network import C_INVALID_NETWORK_OBJECT_ID as C_INVALID_NETWORK_OBJECT_ID
from Event import Event as Event
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from common_tank_structure import VehicleAppearanceCacheInfo as VehicleAppearanceCacheInfo
from constants import DEFAULT_GUN_INSTALLATION_INDEX as DEFAULT_GUN_INSTALLATION_INDEX, VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE, SPECIAL_VEHICLE_HEALTH as SPECIAL_VEHICLE_HEALTH, VEHICLE_HIT_EFFECT as VEHICLE_HIT_EFFECT
from gui.battle_control import vehicle_getter as vehicle_getter
from gui.shared.items_parameters import isAutoShootGun as isAutoShootGun
from helpers import dependency as dependency
from items import vehicles as vehicles
from shared_utils.vehicle_utils import createWheelFilters as createWheelFilters
from skeletons.vehicle_appearance_cache import IAppearanceCache as IAppearanceCache
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes
from helpers_common import setDamageSticker as setDamageSticker
_logger: Any
_UNSPOTTED_CONE_WIDTH_SCALE = 1
_UNSPOTTED_CONE_LENGTH_SCALE = 1

class _SimulatedVehicleSpeedProvider(object):
    __slots__: tuple
    __value: Any
    @property
    def value(self):
        ...
    def __init__(self):
        ...
    def set(self, val):
        ...
    def reset(self):
        ...

class VehicleBase(object):
    _wheelsScrollFilter: Any
    _wheelsSteeringFilter: Any
    _isCrewActive: Any
    _speedInfo: Any
    typeDescriptor: Any
    _isEnteringWorld: Any
    wheelsState: Any
    burnoutLevel: Any
    isStrafing: Any
    def __init__(self):
        ...
    def _initAdditionalFilters(self, typeDescriptor):
        ...
    @property
    def isEnteringWorld(self):
        ...
    @property
    def isWheeledTech(self):
        ...
    @property
    def wheelsScrollSmoothed(self):
        ...
    @property
    def wheelsScrollFilters(self):
        ...
    @property
    def wheelsSteeringFilters(self):
        ...
    @property
    def wheelsSteeringSmoothed(self):
        ...
    @property
    def speedInfo(self):
        ...
    @property
    def isCrewActive(self):
        ...
    def getSpeed(self):
        ...
    def isAlive(self):
        ...
    def isOnFire(self):
        ...
    def showCollisionEffect(self, hitPos, collisionEffectName='collisionVehicle', collisionNormal=None, isTracks=False, damageFactor=0, impulse=None, pcEnergy=None):
        ...
    def getOptionalDevices(self):
        ...

class SimulatedVehicle(BigWorld.Entity, VehicleBase):
    __appearanceCache: Any
    _CONE_SIZE = 2
    isStarted: Any
    typeDescriptor: Any
    appearance: Any
    __appearanceCacheID: Any
    __appearanceCacheInfo: Any
    onAppearanceLoaded: Any
    extras: Any
    __prereqs: Any
    turretMatrix: Any
    gunMatrix: Any
    __prevDamageStickers: Any
    __brokenTrackVisible: Any
    __turretDetachmentConfirmed: Any
    __damageDecalEffectId: Any
    _isEnteringWorld: Any
    def __init__(self):
        ...
    @property
    def isTurretDetached(self):
        ...
    @property
    def isTurretMarkedForDetachment(self):
        ...
    @property
    def turretYaw(self):
        ...
    @property
    def gunPitch(self):
        ...
    @property
    def health(self):
        ...
    @property
    def maxHealth(self):
        ...
    @property
    def appearanceCacheID(self):
        ...
    def getSimulatedSteeringDataLink(self):
        ...
    def gunOriginMatrix(self, gunInstallationIndex=..., gunIndex=0):
        ...
    def gunFireMatrix(self, gunInstallationIndex=..., gunIndex=0):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def stopVisual(self):
        ...
    def addModel(self, model):
        ...
    def delModel(self, model):
        ...
    def getMatinfo(self, partIndex, matKind):
        ...
    def showKillingSticker(self, shellCompactDescr, isArmorPierced, hitPoints):
        ...
    def _createAppearance(self, entityID, forceReloading):
        ...
    def getDynAttachments(self):
        ...
    def __onAppearanceReady(self, appearance):
        ...
    def __startVisual(self):
        ...
    def __stopExtras(self):
        ...
    def getMaxComponentIndex(self, skipWheels=False):
        ...
    def __calcMaxHitEffectAndHasPiercedShot(self, shotPoints):
        ...
    def __showDamageStickers(self, stickers):
        ...
    def __decodeAndAddSticker(self, hitPoint):
        ...
    def updateBrokenTracks(self, trackStates):
        ...
    def __onActivateAppearance(self):
        ...
    def __resetAppearance(self):
        ...
