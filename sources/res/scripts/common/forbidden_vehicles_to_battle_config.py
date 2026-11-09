# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/forbidden_vehicles_to_battle_config.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/forbidden_vehicles_to_battle_config.py
from __future__ import absolute_import
from items.vehicles import makeVehicleTypeCompDescrByName
from realm_utils import ResMgr
CONFIG_FILE = 'scripts/item_defs/vehicles/common/forbidden_vehicles_to_battle_config.xml'
g_forbiddenVehiclesToBattle = None

def readConfig():
    section = ResMgr.openSection(CONFIG_FILE)
    config = set()
    if section is None:
        return frozenset(config)
    else:
        forbiddenVehiclesSection = section['forbiddenVehicles']
        if forbiddenVehiclesSection is not None:
            for vehicleSubsection in forbiddenVehiclesSection.values():
                config.add(makeVehicleTypeCompDescrByName(vehicleSubsection.asString))

        return frozenset(config)


def loadForbiddenVehiclesToBattleCfg():
    global g_forbiddenVehiclesToBattle
    g_forbiddenVehiclesToBattle = readConfig()


def getForbiddenForBattleVehicles():
    if g_forbiddenVehiclesToBattle is None:
        loadForbiddenVehiclesToBattleCfg()
    return g_forbiddenVehiclesToBattle
