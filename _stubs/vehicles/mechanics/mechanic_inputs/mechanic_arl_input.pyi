# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_inputs/mechanic_arl_input.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from events_handler import eventHandler as eventHandler
from gui.battle_control import avatar_getter as avatar_getter
from vehicles.mechanics.mechanic_inputs.mechanic_base_input import BaseMechanicInput as BaseMechanicInput
from vehicles.mechanics.mechanic_inputs.mechanic_input_profile import MechanicInputProfile as MechanicInputProfile, PlayerVehicleInputPredicate as PlayerVehicleInputPredicate
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher import AuxiliaryRocketLauncherState as AuxiliaryRocketLauncherState

class AuxiliaryRocketLauncherInputPredicate(PlayerVehicleInputPredicate):
    def __call__(self):
        ...

class AuxiliaryRocketLauncherInput(BaseMechanicInput, IMechanicStatesListenerLogic):
    __activateProfile: Any
    def __init__(self, component, switchModeProfileName, switchModeActionName, activateProfileName, activateActionName, switchModeCallback, activateCallback):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
