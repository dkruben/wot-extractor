# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/points_of_interest_shared.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/points_of_interest_shared.py
from __future__ import absolute_import
import enum
ENEMY_VEHICLE_ID = -1
INVALID_TIMESTAMP = -1
POI_EQUIPMENT_TAG = 'poiEquipment'

@enum.unique
class PoiType(enum.IntEnum):
    ARTILLERY = 1
    RECON = 2
    ILLUMINATION_FLARE = 3


@enum.unique
class PoiStatus(enum.IntEnum):
    ACTIVE = 1
    CAPTURING = 2
    COOLDOWN = 3


INT_2_POI_STATUS = {int(v): v for k, v in PoiStatus.__members__.items()}

@enum.unique
class PoiBlockReasons(enum.IntEnum):
    DAMAGE = 1
    EQUIPMENT = 2
    OVERTURNED = 3


PoiEquipmentNamesByPoiType = {(PoiType.ARTILLERY): 'poi_artillery_aoe', 
   (PoiType.RECON): 'poi_radar', 
   (PoiType.ILLUMINATION_FLARE): 'poi_illumination_flare'}
PoiTypesByPoiEquipmentName = {name: poiType for poiType, name in PoiEquipmentNamesByPoiType.items()}
