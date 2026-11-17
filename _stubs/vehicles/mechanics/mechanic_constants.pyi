# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from items.vehicle_mechanics_types import VehicleMechanic as VehicleMechanic, VehicleMechanicKeys as VehicleMechanicKeys, ALL_VEHICLE_MECHANIC_KEYS as ALL_VEHICLE_MECHANIC_KEYS
VEHICLE_MECHANIC_DYN_COMPONENT_NAMES: dict
TRACKABLE_VEHICLE_MECHANICS: Any
VEHICLE_MECHANIC_TAGS: dict
VEHICLE_MECHANIC_USED_COMMANDS: dict

class VehicleMechanicCommand(Enum):
    PREPARING = 'preparing'
    CANCELLED = 'cancelled'
    ACTIVATE = 'activate'
    ALTERNATIVE_ACTIVATE = 'altActivate'
    DEACTIVATE = 'deactivate'
    SWITCH = 'switch'
    MANUAL_RELOAD = 'manual_reload'
