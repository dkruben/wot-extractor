# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/vehicle_health_observer_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import logging as logging
from collections import defaultdict as defaultdict
from constants import SPECIAL_VEHICLE_HEALTH as SPECIAL_VEHICLE_HEALTH, IS_EDITOR as IS_EDITOR, IS_CGF_DUMP as IS_CGF_DUMP
from GenericComponents import StateSwitcherComponent as StateSwitcherComponent
from cgf_components_common.state_components import VehicleHealthObserverComponent as VehicleHealthObserverComponent
_logger: Any

class Vehicle(object):
    ...

class VehicleHealthObserverSystem(CGF.System):
    ObserverActivated: Any
    ObserverDeactivated: Any
    SwitcherAccess: Any
    VehicleAccess: Any
    Reactions: Any
    __switchersGroupedByVehicle: Any
    __switchersToVehiclesMap: Any
    def __init__(self):
        ...
    def update(self):
        ...
    @staticmethod
    def __determineState(health):
        ...
    def __onHealthChanged(self, vehicleID, newHealth, _):
        ...
