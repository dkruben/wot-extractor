# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/shell_mechanics.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/shell_mechanics.py
from __future__ import absolute_import
import typing
from gui.shared.items_parameters.functions import getShellParamsSwitcherModifiedShells, getShellCalibrationShells, getBustleFeedModifiedShells
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory
from items.vehicle_mechanics_types import VehicleMechanicKeys
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor
    from items.vehicle_mechanics_types import VehicleMechanicKey
    from gui.shared.gui_items.vehicle_modules import Shell
    from items.vehicles import VehicleDescr
_SHELL_MODIFICATION_MECHANICS_GETTERS = {(VehicleMechanicKeys.SHELL_PARAMS_SWITCHER): getShellParamsSwitcherModifiedShells, 
   (VehicleMechanicKeys.SHELL_CALIBRATION): getShellCalibrationShells, 
   (VehicleMechanicKeys.BUSTLE_FEED): getBustleFeedModifiedShells}

def _hasShellMechanics(descriptor, shell, mechanic):
    getter = _SHELL_MODIFICATION_MECHANICS_GETTERS.get(mechanic)
    if getter is None or not hasVehicleDescrMechanic(descriptor, mechanic):
        return False
    return shell.intCD in getter(descriptor)


class ShellMechanicFactory(BaseMechanicFactory):

    @classmethod
    def _getMechanicsChecks(cls, guiItem, vehDescr):
        return [
         (
          hasVehicleDescrMechanic(vehDescr, VehicleMechanicKeys.LOW_CHARGE_SHOT), VehicleMechanicKeys.LOW_CHARGE_SHOT),
         (
          _hasShellMechanics(vehDescr, guiItem, VehicleMechanicKeys.SHELL_CALIBRATION), VehicleMechanicKeys.SHELL_CALIBRATION),
         (
          _hasShellMechanics(vehDescr, guiItem, VehicleMechanicKeys.BUSTLE_FEED), VehicleMechanicKeys.BUSTLE_FEED),
         (
          _hasShellMechanics(vehDescr, guiItem, VehicleMechanicKeys.SHELL_PARAMS_SWITCHER),
          VehicleMechanicKeys.SHELL_PARAMS_SWITCHER)]
