# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/veh_skill_tree/logging_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
FEATURE_VEH_SKILL_TREE = 'veh_skill_tree'
VEH_SKILL_TREE_SCREEN = 'tier_11_progression_screen'

class VehSkillTreeActions(str, Enum):
    CLICK = 'click'
    OPEN = 'open'
    CLOSE = 'close'

class VehSkillTreeItems(str, Enum):
    SKILL_TREE = 'skill_tree'
    RESEARCH_BUTTON = 'research_button'
