# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_components_common/managers/state_managers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import logging as logging
from GenericComponents import HealthGradationComponent as HealthGradationComponent, EHealthGradation as EHealthGradation, StateSwitcherComponent as StateSwitcherComponent
from functools import partial as partial
from constants import IS_UNKNOWN as IS_UNKNOWN
_logger: Any

class HealthComponent(object):
    ...

class StateSwitcherSystem(CGF.System):
    StateActivated: Any
    StateDeactivated: Any
    StateAccess: Any
    GradationAccess: Any
    Reactions: Any
    __switcherCallbacks: Any
    def __init__(self):
        ...
    def update(self):
        ...
    def __onHealthChanged(self, go, old, health, maxHealth):
        ...
