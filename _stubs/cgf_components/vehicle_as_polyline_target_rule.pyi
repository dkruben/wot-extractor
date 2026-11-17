# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/vehicle_as_polyline_target_rule.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import registerModule as registerModule
from constants import IS_CLIENT as IS_CLIENT, HAS_DEV_RESOURCES as HAS_DEV_RESOURCES

class Vehicle(object):
    ...

class PolylineDebugTargetComponent(object):
    ...

class VehicleAsPolylineTargetConfiguratorSystem(CGF.System):
    VehicleCreated: Any
    Reactions: Any
    def update(self):
        ...

# decorador original: @registerModule
class VehicleAsPolylineTargetModule(object):
    name = 'PolyLine Debug Target'
    group = 'Fall Tanks'
    systems: list
