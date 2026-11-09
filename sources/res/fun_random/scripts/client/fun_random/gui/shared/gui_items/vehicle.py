# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/shared/gui_items/vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/shared/gui_items/vehicle.py
from __future__ import absolute_import
import typing
from fun_random.gui.fun_gui_constants import VEHICLE_TAGS
from gui.shared.gui_items import checkForTags
from gui.shared.utils.requesters import REQ_CRITERIA
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

def isOnlyFunRandomVehicle(vehicle):
    return checkForTags(vehicle.tags, VEHICLE_TAGS.FUN_RANDOM)


ONLY_FUN_RANDOM_VEHICLE_CRITERIA = REQ_CRITERIA.CUSTOM(isOnlyFunRandomVehicle)
