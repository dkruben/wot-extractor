# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/GenericComponents.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
COMPOSITION_ROOT_SLOT_NAME = 'compositionRootSlot'

class EHealthGradation(enum.Enum):
    RED_ZONE = 'RED_ZONE'
    YELLOW_ZONE = 'YELLOW_ZONE'
    GREEN_ZONE = 'GREEN_ZONE'

class HealthGradationComponent:
    __redHealth: Any
    __yellowHealth: Any
    def __init__(self, redHealth, yellowHealth):
        ...
    def getHealthZone(self, health, maxHealth):
        ...

class CyclicActivatorComponent(object):
    ...

class VSEComponent(object):
    ...

class StateSwitcherComponent(object):
    NONE_STATE = 0
    NORMAL_STATE = 1
    DAMAGED_STATE = 2
    CRITICAL_STATE = 3
