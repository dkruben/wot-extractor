# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_parameters/shell_mechanics_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Tuple as Tuple, List as List, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING
from enum import Enum as Enum
from gui.shared.items_parameters import params_helper as params_helper
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from items.utils import getVehicleDescriptorWithoutMechanic as getVehicleDescriptorWithoutMechanic
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic
from gui.shared.gui_items.vehicle_modules import Shell as Shell
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from items.vehicles import VehicleDescr as VehicleDescr
_MECHANICS_PARAMS_HANDLERS: dict

class ShellMechanicState(int, Enum):
    UNDEFINED = 0
    ON = 1
    OFF = 2

def getShellParameters(vehicle, shell):
    ...
def _getDefaultShellMechanic(vehicleDescr):
    ...
def _getDefaultShellParams(shell, vehicle):
    ...
def _getLowChargeParams(shell, vehicle):
    ...
def _getSwitchedParams(shell, vehicle):
    ...
def _getShellCalibrationParams(shell, vehicle):
    ...
def _getBustleFeedParams(shell, vehicle):
    ...
