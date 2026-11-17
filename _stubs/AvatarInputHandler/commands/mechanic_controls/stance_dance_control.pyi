# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/stance_dance_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from vehicles.mechanics.mechanic_helpers import getPlayerVehicleMechanicComponent as getPlayerVehicleMechanicComponent
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey

class StanceDanceControl(InputHandlerCommand):
    __mechanic: Any
    def __init__(self, mechanic):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...

def createStanceDanceControl(mechanic, *_, **__):
    ...
