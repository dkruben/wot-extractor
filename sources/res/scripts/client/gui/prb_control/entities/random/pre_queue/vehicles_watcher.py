# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/random/pre_queue/vehicles_watcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/random/pre_queue/vehicles_watcher.py
from constants import BATTLE_MODE_VEH_TAGS_EXCEPT_REGULAR
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher

class RegularVehiclesWatcher(BaseVehiclesWatcher):
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_REGULAR
