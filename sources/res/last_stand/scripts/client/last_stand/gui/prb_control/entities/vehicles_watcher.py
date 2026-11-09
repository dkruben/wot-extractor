# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/vehicles_watcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/prb_control/entities/vehicles_watcher.py
from __future__ import absolute_import
import typing
from future.utils import viewvalues
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from last_stand.skeletons.ls_controller import ILSController
from last_stand_common.last_stand_constants import FORBIDDEN_VEHICLE_TAGS

class VehiclesWatcher(BaseVehiclesWatcher):
    itemsCache = dependency.descriptor(IItemsCache)
    lsCtrl = dependency.descriptor(ILSController)

    def _getUnsuitableVehicles(self, onClear=False):
        vehConfig = self.lsCtrl.getVehiclesConfig()
        criteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.HAS_ANY_TAG(FORBIDDEN_VEHICLE_TAGS)
        if vehConfig.allowedLevels:
            criteria |= ~REQ_CRITERIA.VEHICLE.LEVELS(vehConfig.allowedLevels)
        if vehConfig.forbiddenClassTags:
            criteria |= REQ_CRITERIA.VEHICLE.CLASSES(vehConfig.forbiddenClassTags)
        if vehConfig.forbiddenVehicles:
            criteria |= REQ_CRITERIA.VEHICLE.SPECIFIC_BY_CD(vehConfig.forbiddenVehicles)
        criteria ^= REQ_CRITERIA.VEHICLE.FORBIDDEN_VEHICLE_TO_BATTLE
        excludeVehicles = self.itemsCache.items.getVehicles(criteria)
        for intCD in vehConfig.allowedVehicles:
            excludeVehicles.pop(intCD, None)

        return viewvalues(excludeVehicles)
