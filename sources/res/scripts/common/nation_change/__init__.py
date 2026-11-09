# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/nation_change/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/nation_change/__init__.py
from __future__ import absolute_import
from constants import ITEM_DEFS_PATH
from nation_change.NationChangeSettings import NationChangeSettings
g_settings = None
PDATA_NATION_CHANGE_VEHICLE_DOSSIER_KEY = 'nationChangeVehicleDossier'
CONFIG_XML_PATH = ITEM_DEFS_PATH + 'nation_change.xml'
UNDEFINED_ID = -1

def init(settingsXml=CONFIG_XML_PATH):
    global g_settings
    g_settings = NationChangeSettings(settingsXml)


def findVehicleNationGroupId(vehicleTypeName):
    group = g_settings.findVehicleGroup(vehicleTypeName)
    if group is None:
        return UNDEFINED_ID
    else:
        return group.ID
