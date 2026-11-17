# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/spec_boost_mode/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from vehicles.mechanics.common.mechanic_interfaces import IMechanicWithVariants as IMechanicWithVariants
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
from items.components.shared_components import SpecBoostModeParams as SpecBoostModeParams

class ISpecBoostModeMechanicParams(IMechanicWithVariants):
    @classmethod
    def fromMechanicParams(cls, params):
        ...

class ISpecBoostModeMechanicState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status):
        ...
    @property
    def progress(self):
        ...
    @property
    def timeLeft(self):
        ...
    @property
    def state(self):
        ...
