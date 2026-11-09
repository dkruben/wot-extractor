# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/common/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from vehicles.components.component_interfaces import IVehicleSlotComponent as IVehicleSlotComponent
from items.vehicle_mechanics_types import VehicleMechanicVariant as VehicleMechanicVariant, VehicleMechanicKey as VehicleMechanicKey

class IMechanicComponentLogic(object):
    @property
    def isValid(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...

class IMechanicComponent(IVehicleSlotComponent, IMechanicComponentLogic):
    ...

class IMechanicWithVariants(object):
    @property
    def mechanicVariant(self):
        ...
