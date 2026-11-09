# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/ls_vehicle_params_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/lobby/ls_vehicle_params_view.py
from __future__ import absolute_import
from gui.impl.lobby.hangar.presenters.hangar_vehicle_params_presenter import HangarVehicleParamsPresenter
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class LSVehicleParamsPresenter(HangarVehicleParamsPresenter):
    __itemsCache = dependency.descriptor(IItemsCache)

    def _getVehicle(self):
        vehicle = super(LSVehicleParamsPresenter, self)._getVehicle()
        if vehicle:
            return self._removeConsumables(vehicle)
        else:
            return

    def _getDefaultVehicle(self):
        vehicle = super(LSVehicleParamsPresenter, self)._getVehicle()
        if vehicle:
            return self._removeConsumables(vehicle)
        else:
            return

    def _removeConsumables(self, vehicle):
        vehicle = self.__itemsCache.items.getLayoutsVehicleCopy(vehicle)
        vehicle.consumables.setLayout(*([None] * len(vehicle.consumables.layout)))
        vehicle.consumables.setInstalled(*([None] * len(vehicle.consumables.installed)))
        return vehicle
