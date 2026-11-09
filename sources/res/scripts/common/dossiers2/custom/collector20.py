# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dossiers2/custom/collector20.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/collector20.py
from __future__ import absolute_import
import ResMgr, typing
from items.vehicles import makeVehicleTypeCompDescrByName
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import FrozenSet
    VehCD = int
COLLECTOR20_CONFIG_PATH = 'scripts/item_defs/collector20.xml'
CONFIG_SECTION = 'collector20Vehicles'
COLLECTOR20_MEDAL_ID = 'twoPointZeroCollectorMedal'
COLLECTOR20_BADGE_IDS = (215, 216)
_g_collector20Config = frozenset()

def _readConfig():
    section = ResMgr.openSection(COLLECTOR20_CONFIG_PATH)
    if section is None:
        raise SoftException('Collector20 vehicles config is not found at %s!' % COLLECTOR20_CONFIG_PATH)
    vehiclesSection = section[CONFIG_SECTION]
    if vehiclesSection is None:
        raise SoftException('%s section is not found in %s!' % (CONFIG_SECTION, COLLECTOR20_CONFIG_PATH))
    result = set()
    vehicleNames = vehiclesSection.readString('').split()
    for vehicleName in vehicleNames:
        vehTypeCompDescr = makeVehicleTypeCompDescrByName(vehicleName)
        if vehTypeCompDescr in result:
            raise SoftException('%r specified more than once in %s!' % (vehicleName, COLLECTOR20_CONFIG_PATH))
        result.add(vehTypeCompDescr)

    return frozenset(result)


def loadCollector20Config():
    global _g_collector20Config
    if not _g_collector20Config:
        _g_collector20Config = _readConfig()


def getCollector20Config():
    if not _g_collector20Config:
        loadCollector20Config()
    return _g_collector20Config
