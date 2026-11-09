# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicle_systems/components/vehicle_variable_storage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/components/vehicle_variable_storage.py
from __future__ import absolute_import
import typing, enum, logging, Math, CGF
from cgf_modules.variable_components import VariableStorageComponent
from constants import VEHICLE_CLASSES, VEHICLE_CLASS_INDICES
from vehicle_systems.tankStructure import TankPartIndexes
if typing.TYPE_CHECKING:
    from Vehicle import Vehicle
    from vehicle_appearance.common_tank_appearance import CommonTankAppearance
    from gui.hangar_vehicle_appearance import HangarVehicleAppearance
    from items.vehicles import VehicleDescriptor
    from items.vehicle_items import Gun, Shell
    from cgf_modules.variable_components import VariableType
    TAppearance = typing.Union[(HangarVehicleAppearance, CommonTankAppearance, None)]
_logger = logging.getLogger(__name__)

class VehicleRootVars(enum.Enum):
    TYPE = 'vehicle/type'
    MAX_HEALTH = 'vehicle/maxHealth'


class VehicleGunVars(enum.Enum):
    MUZZLE_BRAKE = 'vehicle/gun/muzzleBrake'
    GUN_LENGTH = 'vehicle/gun/gunLength'
    GUN_CALIBER = 'vehicle/gun/caliber'
    TIME_BETWEEN_SHOTS = 'vehicle/gun/timeBetweenShots'


def createForRoot(vehicle, queue=None):
    vehicleObject = vehicle.entityGameObject
    queue = queue or CGF.CommandQueue(vehicleObject.spaceID)
    vehDescr = vehicle.typeDescriptor
    vehType = set(VEHICLE_CLASSES).intersection(vehDescr.type.tags).pop()
    vehTypeIdx = VEHICLE_CLASS_INDICES[vehType]
    vars = [
     (
      VehicleRootVars.TYPE.value, vehTypeIdx),
     (
      VehicleRootVars.MAX_HEALTH.value, vehicle.maxHealth)]
    queue.removeComponent(vehicleObject, VariableStorageComponent)
    queue.createComponent(vehicleObject, VariableStorageComponent, vars)


def getVariableValuesForGun(appearance):
    shellDescr = appearance.typeDescriptor.shot.shell
    gunDescr = appearance.typeDescriptor.gun
    gunBB = Math.Matrix(appearance.compoundModel.getBoundsForPart(TankPartIndexes.GUN))
    gunLength = gunBB.applyVector(Math.Vector3(0.0, 0.0, 1.0)).length
    timeBetweenShots = gunDescr.clip[1] if 'clip' in gunDescr.tags else gunDescr.reloadTime
    return [
     (
      VehicleGunVars.MUZZLE_BRAKE.value, gunDescr.muzzleBrake.value),
     (
      VehicleGunVars.GUN_LENGTH.value, gunLength),
     (
      VehicleGunVars.GUN_CALIBER.value, shellDescr.caliber),
     (
      VehicleGunVars.TIME_BETWEEN_SHOTS.value, timeBetweenShots)]


def update(go, varName, value):
    varStorage = go.findWrite(VariableStorageComponent)
    if not varStorage:
        _logger.error("Can't find variable storage for: %s", go.name)
        return
    varStorage.modify(go, varName, value)
