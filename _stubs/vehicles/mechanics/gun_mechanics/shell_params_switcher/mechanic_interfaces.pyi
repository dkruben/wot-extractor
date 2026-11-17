# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/shell_params_switcher/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
from items.components.shared_components import ShellSwitcherParams as ShellSwitcherParams

class IShellParamsSwitcherComponentParams(object):
    @classmethod
    def fromMechanicParams(cls, params, vehIntCD):
        ...
    @property
    def shellSubtypes(self):
        ...

class IShellParamsSwitcherMechanicState(IMechanicState):
    @property
    def state(self):
        ...
    @property
    def baseState(self):
        ...
    @property
    def isActive(self):
        ...
    @property
    def lastActiveShotTimestamp(self):
        ...
    @property
    def mechanicSubtype(self):
        ...
    def isNoAmmo(self):
        ...
    def isCritState(self):
        ...
    def timeLeft(self):
        ...
