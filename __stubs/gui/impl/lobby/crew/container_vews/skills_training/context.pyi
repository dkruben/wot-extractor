# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/skills_training/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import NEW_PERK_SYSTEM as NPS
from gui.impl.lobby.crew.container_vews.common.base_personal_case_context import BasePersonalCaseContext as BasePersonalCaseContext
from gui.impl.lobby.crew.crew_helpers.skill_helpers import getTmanNewSkillCount as getTmanNewSkillCount
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL

class SkillsTrainingViewContext(BasePersonalCaseContext):
    __slots__: tuple
    _role: Any
    _hoveredSkill: Any
    _selectedSkills: Any
    _availableSkillsData: Any
    _activeSkillsForTTC: Any
    def __init__(self, tankmanID, role):
        ...
    @property
    def role(self):
        ...
    @property
    def isMajorQualification(self):
        ...
    @property
    def totalSkillsAmount(self):
        ...
    @property
    def areAllSkillsLearned(self):
        ...
    @property
    def isAnySkillSelected(self):
        ...
    @property
    def selectedSkills(self):
        ...
    @property
    def selectedSkillsCount(self):
        ...
    @property
    def hoveredSkill(self):
        ...
    @property
    def activeSkillsForTTC(self):
        ...
    @property
    def availableSkillsData(self):
        ...
    @property
    def skillsAmount(self):
        ...
    def update(self, tankmanID, updateRole=False):
        ...
    def clearSelection(self):
        ...
    def updateSelectedSkills(self, skillId):
        ...
    def updateHoveredSkill(self, skillId):
        ...
    def _updateActiveSkillsForTTC(self):
        ...
