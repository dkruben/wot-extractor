# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/simple_activation_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_helpers import getPlayerVehicleMechanicComponent as getPlayerVehicleMechanicComponent
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey

class SimpleActivationControl(InputHandlerCommand):
    _VEHICLE_MECHANIC_KEYS: dict
    __mechanic: Any
    __key: Any
    def __init__(self, mechanic):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...

def createSimpleActivationControl(mechanic, *_, **__):
    ...
