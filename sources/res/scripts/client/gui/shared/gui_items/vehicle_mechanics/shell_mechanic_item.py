# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/shell_mechanic_item.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/vehicle_mechanics/shell_mechanic_item.py
from __future__ import absolute_import
from gui.shared.gui_items.vehicle_mechanics.module_mechanic_item import ModuleMechanicItem
from gui.shared.utils.decorators import ReprInjector
from items import vehicles
from items.vehicle_mechanics_types import VehicleMechanicKey, VehicleMechanicKeys
_SHELL_MECHANIC_PRIORITY = {(VehicleMechanicKeys.SHELL_PARAMS_SWITCHER): 1, 
   (VehicleMechanicKeys.SHELL_CALIBRATION): 1, 
   (VehicleMechanicKeys.LOW_CHARGE_SHOT): 1, 
   (VehicleMechanicKeys.BUSTLE_FEED): 1}

@ReprInjector.withParent('rank', 'mechanicSubtype')
class ShellMechanicItem(ModuleMechanicItem):
    __slots__ = ('__rank', '__mechanicSubtype')
    _GUI_SUPPORTED_MECHANICS = {
     VehicleMechanicKeys.SHELL_PARAMS_SWITCHER,
     VehicleMechanicKeys.LOW_CHARGE_SHOT,
     VehicleMechanicKeys.SHELL_CALIBRATION,
     VehicleMechanicKeys.BUSTLE_FEED}

    def __init__(self, mechanic, *args, **kwargs):
        super(ShellMechanicItem, self).__init__(mechanic)
        vehIntCD = kwargs['vehIntCD']
        vehicleMechanicItem = self.itemsFactory.createVehicleMechanicItem(mechanic, vehIntCD)
        self.__rank = vehicleMechanicItem.rank
        shellCD = kwargs.get('shellCD')
        mechanicCache = vehicles.g_cache.vehicleMechanics.get(vehIntCD, {}).get(mechanic.uniqueName, {})
        self.__mechanicSubtype = mechanicCache.get('mechanicSubtypes', {}).get(shellCD, {})

    @property
    def hasVideo(self):
        return False

    @property
    def priority(self):
        return _SHELL_MECHANIC_PRIORITY.get(self._mechanic, 0)

    @property
    def rank(self):
        return self.__rank

    @property
    def mechanicSubtype(self):
        return self.__mechanicSubtype
