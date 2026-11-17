# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/commands/siege_mode_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from weakref import ref as ref
import CommandMapping as CommandMapping
from constants import ARENA_PERIOD as ARENA_PERIOD, VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE, VEHICLE_SETTING as VEHICLE_SETTING
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand as InputHandlerCommand
from AvatarInputHandler.player_notifications.siege_mode.sound_notifications import playUnavailableSound as playUnavailableSound, playTriggerSound as playTriggerSound
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_helpers import getPlayerVehicleMechanicComponent as getPlayerVehicleMechanicComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class SiegeModeControl(InputHandlerCommand):
    __sessionProvider: Any
    __CANT_SWITCH_ERRORS: dict
    __currentState: Any
    __notifier: Any
    def __init__(self, notifier):
        ...
    def destroy(self):
        ...
    def handleKeyEvent(self, isDown, key, mods, event=None):
        ...
    def __onSiegeStateChanged(self, vehicleID, newState, timeToNextMode):
        ...
    def __switchSiegeMode(self, vehicle):
        ...
