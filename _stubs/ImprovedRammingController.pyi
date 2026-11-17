# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ImprovedRammingController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent

# decorador original: @ReprInjector.withParent(...)
class ImprovedRammingController(VehicleDynamicComponent, IMechanicComponent):
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
