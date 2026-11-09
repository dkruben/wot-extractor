# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/__init__.py
from __future__ import absolute_import
from gui import GUI_NATIONS_ORDER_INDEX
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES

def vehicleComparisonKey(vehicle):
    return (
     not vehicle.isFavorite,
     GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
     VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
     vehicle.level,
     vehicle.userName)
