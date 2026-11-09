# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/common/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from vehicles.mechanics.common.mechanic_interfaces import IMechanicWithVariants as IMechanicWithVariants
from items.vehicle_mechanics_types import VehicleMechanicVariant as VehicleMechanicVariant

# decorador original: @ReprInjector.simple(...)
class MechanicParamsWithVariants(IMechanicWithVariants):
    _mechanicVariant: Any
    def __init__(self, mechanicVariant):
        ...
    @property
    def mechanicVariant(self):
        ...
