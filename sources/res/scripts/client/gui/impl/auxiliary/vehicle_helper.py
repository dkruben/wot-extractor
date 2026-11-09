# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/auxiliary/vehicle_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/auxiliary/vehicle_helper.py
from __future__ import absolute_import
import math, typing
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS
if typing.TYPE_CHECKING:
    from typing import Optional, Iterable
    from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
    from gui.shared.gui_items.Vehicle import Vehicle

def fillVehicleInfo(vehInfo, vehicle, separateIGRTag=False, tags=None):
    vehInfo.setIsElite(vehicle.isElite)
    vehInfo.setIsPremium(vehicle.isPremium)
    vehInfo.setVehicleLvl(vehicle.level)
    vehInfo.setVehicleType(vehicle.type)
    vehInfo.setVehicleNation(vehicle.nationName)
    vehInfo.setVehicleShortName(vehicle.descriptor.type.shortUserString)
    vehicleTags = set(tags or [])
    vehicleTags.add(VEHICLE_TAGS.PREMIUM_IGR)
    vehInfo.setTags((',').join(vehicleTags & vehicle.tags))
    if separateIGRTag:
        vehInfo.setVehicleName(vehicle.descriptor.type.userString)
    else:
        vehInfo.setVehicleName(vehicle.descriptor.type.shortUserString)
    vehInfo.setVehicleId(vehicle.intCD)
    vehInfo.setInventoryId(vehicle.invID)
    vehInfo.setVehicleLongName(vehicle.descriptor.type.userString)
    vehInfo.setVehicleRole(vehicle.role)
    vehInfo.setRentLeftTime((math.isinf(vehicle.rentLeftTime) or vehicle).rentLeftTime if 1 else -1)
    vehInfo.setRentLeftBattles(vehicle.rentLeftBattles or 0)
    vehInfo.setRentLeftWins(vehicle.rentLeftWins or 0)
    vState, _ = vehicle.getState()
    vehInfo.setState(vState)
    vehInfo.setFromWotPlus(vehicle.isWotPlus)
