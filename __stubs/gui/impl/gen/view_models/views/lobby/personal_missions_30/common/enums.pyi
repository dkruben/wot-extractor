# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/common/enums.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum

class MissionCategory(Enum):
    ASSAULT = 'assault'
    SNIPER = 'sniper'
    SUPPORT = 'support'

class OperationState(Enum):
    COMPLETED_WITH_HONORS = 'completedWithHonors'
    COMPLETED = 'completed'
    ACTIVE = 'active'
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
    LOCKED = 'locked'

class ParamTooltipType(Enum):
    PROGRESSION = 'progression'
    PM3_POINTS = 'pm3_points'
    CUSTOM_SIMPLE = 'custom_simple'
