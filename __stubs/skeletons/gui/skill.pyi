# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/gui/skill.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Optional as Optional

class ISkill(object):
    @property
    def name(self):
        ...
    @property
    def customName(self):
        ...
    @property
    def crewCustomName(self):
        ...

class ISkillPresenter(ISkill):
    @property
    def userName(self):
        ...
    @property
    def description(self):
        ...
    @property
    def shortDescription(self):
        ...
    @property
    def maxLvlDescription(self):
        ...
    @property
    def currentLvlDescription(self):
        ...
    @property
    def altDescription(self):
        ...
    @property
    def altInfo(self):
        ...
    @property
    def icon(self):
        ...
    @property
    def extensionLessIconName(self):
        ...
    @property
    def bigIconPath(self):
        ...

class ISkillData(ISkill):
    @property
    def level(self):
        ...
    @property
    def roleType(self):
        ...
    @property
    def typeName(self):
        ...
    @property
    def isEnable(self):
        ...
    @property
    def isZero(self):
        ...
    @property
    def isSituational(self):
        ...
    @property
    def isLearned(self):
        ...
    @property
    def isLearnedAsMajor(self):
        ...
    @property
    def isLearnedAsBonus(self):
        ...
    @property
    def isMaxLevel(self):
        ...
    @property
    def isSkillActive(self):
        ...
    @property
    def isRelevant(self):
        ...
    @property
    def learnState(self):
        ...
    @property
    def skillRole(self):
        ...
    @property
    def tankmanRole(self):
        ...
    def setIsSkillActive(self, isSkillActive):
        ...
