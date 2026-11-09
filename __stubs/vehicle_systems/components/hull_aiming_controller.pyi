# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/hull_aiming_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import registerComponent as registerComponent
from constants import VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE

# decorador original: @registerComponent
class HullAimingController(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False
    __vehicleFilter: Any
    __vehicleDescriptor: Any
    def __init__(self):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def setData(self, vehicleFilter, vehicleDescriptor):
        ...
    def onSiegeStateChanged(self, newState):
        ...

class HullAimingSystem(CGF.System):
    AimingDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def __deactivateAiming(self, aimingComponent):
        ...
