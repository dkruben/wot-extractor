# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_inputs/mechanic_input_profile.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
import Input as Input
from Input import TriggerEvent as TriggerEvent
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
_logger: Any

class PlayerVehicleInputPredicate(object):
    _entityRef: Any
    def __init__(self, entity):
        ...
    def __call__(self):
        ...

class MechanicInputProfile(object):
    __vehicleRef: Any
    __profileName: Any
    __actionName: Any
    __callback: Any
    __predicateFactory: Any
    __activateOnAttach: Any
    def __init__(self, vehicle, profileName, actionName, callback, predicateFactory=..., activateOnAttach=True):
        ...
    def attach(self):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
