# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_inputs/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from vehicles.mechanics.mechanic_inputs.mechanic_arl_input import AuxiliaryRocketLauncherInput as AuxiliaryRocketLauncherInput
from vehicles.mechanics.mechanic_inputs.mechanic_single_input import MechanicSingleInput as MechanicSingleInput
from typing import Any as Any, Optional as Optional, Callable as Callable
__all__: tuple

def createMechanicSingleInput(component, profileName, actionName, inputCallback):
    ...
def createAuxiliaryRocketLauncherInput(component, switchModeProfileName, switchModeActionName, activateProfileName, activateActionName, switchModeCallback, activateCallback):
    ...
