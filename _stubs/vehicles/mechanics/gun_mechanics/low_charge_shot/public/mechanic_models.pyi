# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/public/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import LowChargeShotVisualState as LowChargeShotVisualState
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState

# base nao representavel no stub: typing.NamedTuple(...)
# decorador original: @ReprInjector.simple(...)
class LowChargeShotPublicMechanicState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, state, params):
        ...
    def isTransition(self, other):
        ...
