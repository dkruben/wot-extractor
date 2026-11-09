# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/poi_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/poi_helpers.py
from __future__ import absolute_import, division
import typing, BigWorld
from items import vehicles
from points_of_interest_shared import PoiEquipmentNamesByPoiType, PoiTypesByPoiEquipmentName
if typing.TYPE_CHECKING:
    from items.artefacts import Equipment
    from points_of_interest.components import PoiStateComponent

def getPoiCooldownProgress(poiState):
    status = poiState.status
    duration = status.endTime - status.startTime
    progress = (BigWorld.serverTime() - status.startTime) / duration * 100
    return progress


def getPoiEquipmentByType(poiType):
    cache = vehicles.g_cache
    name = PoiEquipmentNamesByPoiType[poiType]
    equipmentID = cache.equipmentIDs().get(name)
    if equipmentID is not None:
        return cache.equipments()[equipmentID]
    else:
        return


def getPoiTypeByEquipment(equipment):
    return PoiTypesByPoiEquipmentName.get(equipment.name, None)
