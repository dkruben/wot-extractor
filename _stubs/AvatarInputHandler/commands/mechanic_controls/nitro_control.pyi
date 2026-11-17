# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/nitro_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
import BigWorld as BigWorld
import CommandMapping as CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.mechanic_helpers import getPlayerVehicleMechanicComponent as getPlayerVehicleMechanicComponent
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
_logger: Any
CLICK_THRESHOLD = 0.75

class NitroActivationControl(InputHandlerCommand):
    __sessionProvider: Any
    __mechanic: Any
    __startTime: Any
    __stopTime: Any
    def __init__(self, mechanic):
        ...
    def __alternateNitro(self):
        ...
    def __cancelNitro(self):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...

def createNitroActivationControl(mechanic, *_, **__):
    ...
