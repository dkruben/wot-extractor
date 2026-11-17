# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/veh_skill_tree/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from uilogging.base.logger import MetricsLogger as MetricsLogger
from uilogging.veh_skill_tree.logging_constants import VehSkillTreeActions as VehSkillTreeActions, VehSkillTreeItems as VehSkillTreeItems, FEATURE_VEH_SKILL_TREE as FEATURE_VEH_SKILL_TREE, VEH_SKILL_TREE_SCREEN as VEH_SKILL_TREE_SCREEN
from wotdecorators import noexcept as noexcept

class SkillTreeUILogger(MetricsLogger):
    def __init__(self):
        ...
    def onSkillTreeOpened(self):
        ...
    def onSkillTreeClosed(self):
        ...
    # decorador original: @noexcept
    def onNodesResearched(self, selectedNodeIDs):
        ...
