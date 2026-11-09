# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/components_states/ammo/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, IntEnum as IntEnum
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys

class AmmoShootPossibility(IntEnum):
    NOT_DEFINED = 0
    ALLOWED = 1
    DENIED = 2

class ActiveAmmoMode(IntEnum):
    NOT_DEFINED = 0
    DEFAULT_SHELLS = 1
    MODIFIED_SHELLS = 2

class ShellMode(Enum):
    NOT_DEFINED = ''
    LOW_CHARGE_SHOT = VehicleMechanicKeys.LOW_CHARGE_SHOT.uniqueName
    BUSTLE_FEED = VehicleMechanicKeys.BUSTLE_FEED.uniqueName
    SHELL_PARAMS_SWITCHER = VehicleMechanicKeys.SHELL_PARAMS_SWITCHER.uniqueName
    AUXILIARY_ROCKET_LAUNCHER = VehicleMechanicKeys.AUXILIARY_ROCKET_LAUNCHER.uniqueName
    SHELL_CALIBRATION = VehicleMechanicKeys.SHELL_CALIBRATION.uniqueName
