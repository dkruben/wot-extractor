# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/prb_control/__init__.py
from __future__ import absolute_import
from future.utils import viewvalues
import typing
from constants import MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.shared.gui_items.Vehicle import Vehicle
from last_stand_common.last_stand_constants import PREBATTLE_TYPE
from gui.prb_control.prb_helpers import DefaultVehicleAutoSearchHelper
from helpers import dependency
from last_stand.skeletons.ls_controller import ILSController

class LSVehicleAutoSearchHelper(DefaultVehicleAutoSearchHelper):
    __lsCtrl = dependency.descriptor(ILSController)

    @classmethod
    def getVehiclesLevelsChecker(cls):
        prebattleType = cls.platoonCtrl.getPrbEntityType()
        allowedLevels = cls.platoonCtrl.getAllowedTankLevels(prebattleType)
        vehLevels = set()
        criteria = cls.__lsCtrl.getVehiclesCriteria()
        allowedList = [lvl for lvl in range(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1) if allowedLevels & 1 << lvl]
        criteria |= REQ_CRITERIA.VEHICLE.LEVELS(allowedList)
        vehicles = cls.itemsCache.items.getVehicles(criteria)
        for v in viewvalues(vehicles):
            state, vStateLvl = v.getState()
            if state in (Vehicle.VEHICLE_STATE.LOCKED, Vehicle.VEHICLE_STATE.IN_PREBATTLE) and v.checkUndamagedState(Vehicle.VEHICLE_STATE.UNDAMAGED) == Vehicle.VEHICLE_STATE.UNDAMAGED or vStateLvl not in (Vehicle.VEHICLE_STATE_LEVEL.CRITICAL,
             Vehicle.VEHICLE_STATE_LEVEL.WARNING,
             Vehicle.VEHICLE_STATE_LEVEL.ATTENTION) or state == Vehicle.VEHICLE_STATE.AMMO_NOT_FULL:
                vehLevels.add(v.level)

        return vehLevels
