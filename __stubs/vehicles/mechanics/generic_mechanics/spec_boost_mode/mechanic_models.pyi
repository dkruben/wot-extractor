# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/spec_boost_mode/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from items.vehicle_mechanics_types import SpecBoostModeMechanicVariant as SpecBoostModeMechanicVariant
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from vehicles.mechanics.generic_mechanics.spec_boost_mode.mechanic_interfaces import ISpecBoostModeMechanicState as ISpecBoostModeMechanicState, ISpecBoostModeMechanicParams as ISpecBoostModeMechanicParams
from vehicles.mechanics.common.mechanic_models import MechanicParamsWithVariants as MechanicParamsWithVariants
from items.components.shared_components import SpecBoostModeParams as SpecBoostModeParams

# decorador original: @ReprInjector.withParent(...)
class SpecBoostModeMechanicParams(ISpecBoostModeMechanicParams, MechanicParamsWithVariants):
    @classmethod
    def fromMechanicParams(cls, params):
        ...

class SpecBoostModeMechanicState(ISpecBoostModeMechanicState):
    __state: Any
    __baseTime: Any
    __endTime: Any
    def __init__(self, state, baseTime, endTime):
        ...
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
    def isTransition(self, other):
        ...
