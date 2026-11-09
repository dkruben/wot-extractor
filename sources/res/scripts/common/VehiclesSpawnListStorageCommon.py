# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/VehiclesSpawnListStorageCommon.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/VehiclesSpawnListStorageCommon.py
from __future__ import absolute_import
from collections import namedtuple
VehicleSpawnData = namedtuple('VehicleSpawnData', ['vehicleCD', 'outfitCD'])

def convertVehicleSpawnDataToTuples(spawnData):
    return {(data.vehicleCD, data.outfitCD) for data in spawnData}


def convertTuplesToVehicleSpawnData(tuples):
    return {VehicleSpawnData(data[0], data[1]) for data in tuples}
