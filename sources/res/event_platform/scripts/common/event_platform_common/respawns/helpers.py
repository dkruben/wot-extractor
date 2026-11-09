# wot-extractor: codigo DESCOMPILADO de sources/res/event_platform/scripts/common/event_platform_common/respawns/helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: event_platform/scripts/common/event_platform_common/respawns/helpers.py
from __future__ import absolute_import
VEHICLE_RESPAWN_COMPONENT = 'VehicleRespawnComponent'

def getVehicleRespawnComponent(vehicle):
    return vehicle.dynamicComponents.get(VEHICLE_RESPAWN_COMPONENT)
