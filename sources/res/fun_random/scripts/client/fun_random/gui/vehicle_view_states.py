# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/vehicle_view_states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/vehicle_view_states.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.vehicle_view_states import SelectedViewState

class FunRandomVehicleViewState(SelectedViewState, FunSubModesWatcher):

    @classmethod
    def isSuitableVehicle(cls, vehicle):
        return cls._funRandomCtrl.isOnlyFunRandomVehicle(vehicle.item)

    def setCustomizationVisible(self, customizationVisible):
        self._isCustomizationVisible = customizationVisible

    def setEliteShown(self, eliteShown):
        self._isEliteShown = eliteShown

    def setLevelShown(self, levelShown):
        self._isLevelShown = levelShown

    def setMaintenanceVisible(self, maintenanceVisible):
        self._isMaintenanceVisible = maintenanceVisible

    def setRoleShown(self, roleShown):
        self._isRoleShown = roleShown

    def _resolveVehicleState(self, vehicle):
        super(FunRandomVehicleViewState, self)._resolveVehicleState(vehicle)
        self.__resolveStateByCurrentSubMode(vehicle)

    @hasDesiredSubMode()
    def __resolveStateByCurrentSubMode(self, vehicle):
        self.getDesiredSubMode().resolveVehicleViewState(self, vehicle)
