# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/armor_flashlight/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/armor_flashlight/utils.py
import typing
from items import vehicles
from vehicle_systems.tankStructure import TankPartNames
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor
    from items.components.shared_components import MaterialInfo

def _convertMatInfo(matInfo):
    return (
     matInfo.kind,
     matInfo.armor if matInfo.armor is not None else 0.0,
     matInfo.vehicleDamageFactor,
     matInfo.useHitAngle | matInfo.mayRicochet << 1 | matInfo.collideOnceOnly << 2 | matInfo.checkCaliberForRicochet << 3 | matInfo.checkCaliberForHitAngleNorm << 4 | bool(matInfo.extra) << 5)


def getAllMatInfos(typeDescriptor):
    partDescriptors = {(TankPartNames.CHASSIS): (typeDescriptor.chassis), 
       (TankPartNames.HULL): (typeDescriptor.hull), 
       (TankPartNames.TURRET): (typeDescriptor.turret), 
       (TankPartNames.GUN): (typeDescriptor.gun)}
    materialsAll = {}
    for partName, partDesc in partDescriptors.items():
        materialList = [_convertMatInfo(matInfo) for matInfo in partDesc.materials.itervalues()]
        materialsAll[partName] = materialList

    if typeDescriptor.type.isWheeledVehicle:
        for key, matInfo in typeDescriptor.chassis.wheelsArmor.iteritems():
            materialsAll[key] = [
             _convertMatInfo(matInfo)]

    commonMaterials = [_convertMatInfo(matInfo) for matInfo in vehicles.g_cache.commonConfig['materials'].itervalues()]
    materialsAll['common'] = commonMaterials
    return materialsAll


class ArmorFlashlightHideReason(object):
    USER_HIDDEN = 1
    HE_ROCKET_AIMING_MODE = 2
