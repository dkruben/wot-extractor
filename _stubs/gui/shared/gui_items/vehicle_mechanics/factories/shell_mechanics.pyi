# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/vehicle_mechanics/factories/shell_mechanics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.shared.items_parameters.functions import getShellParamsSwitcherModifiedShells as getShellParamsSwitcherModifiedShells, getShellCalibrationShells as getShellCalibrationShells, getBustleFeedModifiedShells as getBustleFeedModifiedShells
from gui.shared.gui_items.vehicle_mechanics.factories.base_factory import BaseMechanicFactory as BaseMechanicFactory
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from gui.shared.gui_items.vehicle_modules import Shell as Shell
from items.vehicles import VehicleDescr as VehicleDescr
_SHELL_MODIFICATION_MECHANICS_GETTERS: dict

class ShellMechanicFactory(BaseMechanicFactory):
    @classmethod
    def _getMechanicsChecks(cls, guiItem, vehDescr):
        ...

def _hasShellMechanics(descriptor, shell, mechanic):
    ...
