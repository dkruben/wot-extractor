# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/tankman_skill.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.gui_item import GUIItem as GUIItem
from gui.shared.utils import skill_presenter_helper as skill_presenter_helper
from items.components.component_constants import EMPTY_STRING as EMPTY_STRING
from items.components.skills_constants import SKILLS_BY_ROLES as SKILLS_BY_ROLES, SkillTypeName as SkillTypeName
from items.special_crew import CustomSkills as CustomSkills
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL, ROLES_BY_SKILLS as ROLES_BY_SKILLS, getSkillRoleType as getSkillRoleType
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.skill import ISkill as ISkill, ISkillData as ISkillData, ISkillPresenter as ISkillPresenter
from typing import Optional as Optional, Sequence as Sequence
from items.tankmen import TankmanDescr as TankmanDescr
from gui.shared.gui_items.Tankman import Tankman as Tankman
BROTHERHOOD_SKILL_NAME = 'brotherhood'
COMMANDER_BONUS = 'commander_bonus'

class SkillLearnState(CONST_CONTAINER):
    UNLEARNED = 0
    MAJOR = 1
    BONUS = 2

class _Skill(GUIItem, ISkill):
    __slots__: tuple
    _name: Any
    _customName: Any
    _crewCustomName: Any
    def __init__(self, skillName, customName=..., crewCustomName=..., proxy=None, **_):
        ...
    @property
    def name(self):
        ...
    @property
    def customName(self):
        ...
    @property
    def crewCustomName(self):
        ...

class _SkillPresenter(_Skill, ISkillPresenter):
    __slots__: tuple
    def __init__(self, skillName, customName=..., crewCustomName=..., proxy=None, **kwargs):
        ...
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

class _SkillData(_Skill, ISkillData):
    __slots__: tuple
    _skillRole: Any
    _tankmanRole: Any
    _level: Any
    _isSkillActive: Any
    _isZero: Any
    _isEnable: Any
    _learnState: Any
    _roleType: Any
    _isRelevant: Any
    _typeName: Any
    def __init__(self, skillName, skillRole, tankmanRole=None, level=0, isSkillActive=False, isZero=False, isEnable=False, learnState=..., customName=..., crewCustomName=..., proxy=None, **kwargs):
        ...
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
    def isSituational(self):
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
    def skillRole(self):
        ...
    @property
    def tankmanRole(self):
        ...
    @property
    def isEnable(self):
        ...
    @property
    def isZero(self):
        ...
    @property
    def learnState(self):
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
    def setIsSkillActive(self, isSkillActive):
        ...

class TankmanSkill(_SkillData, _SkillPresenter):
    __slots__: tuple
    def __init__(self, skillName, skillRole, tankmanRole=None, level=0, isSkillActive=False, isZero=False, isEnable=False, learnState=..., customName=..., crewCustomName=..., proxy=None):
        ...
    def __repr__(self):
        ...
    def __ne__(self, other):
        ...
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...

def getIsSkillEnable(skillName, roles):
    ...
def getSkilLevel(skillName, tdescr, skillLevel=None):
    ...
def getSkillLearnedState(skillName, skillRole, tankmanRole, skills, bonusSkills):
    ...
def getIsRelevantForRole(skillName, role):
    ...
def getSkillStates(skillName, skillRole, tankman, tdescr):
    ...
def getTankmanSkill(skillName, skillRole, tankman=None, proxy=None, customCrewName=..., level=None, tankmanRole=None, **kwargs):
    ...
