# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/skill_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import copy as copy
from typing import Tuple as Tuple
from constants import NEW_PERK_SYSTEM as NPS
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.Vehicle import sortCrew as sortCrew
from gui.shared.skill_parameters.skills_packers import g_skillPackers as g_skillPackers, packBase as packBase
from gui.shared.utils.skill_presenter_helper import getSkillDescrArgs as getSkillDescrArgs
from items import tankmen as tankmen
from items.components import perks_constants as perks_constants
from items.components.component_constants import EMPTY_STRING as EMPTY_STRING
from items.components.skills_constants import ROLES_BY_SKILLS as ROLES_BY_SKILLS
from items.tankmen import COMMON_SKILLS as COMMON_SKILLS, MAX_SKILLS_EFFICIENCY as MAX_SKILLS_EFFICIENCY, MAX_SKILLS_EFFICIENCY_XP as MAX_SKILLS_EFFICIENCY_XP, MAX_SKILL_LEVEL as MAX_SKILL_LEVEL, generateCompactDescr as generateCompactDescr, SKILLS_BY_ROLES as SKILLS_BY_ROLES
from .skill_formatters import SkillLvlFormatter as SkillLvlFormatter

def isTankmanSkillIrrelevant(tankman, skill):
    ...
def getSkillsLevelsForXp(tankman, possibleXp=0):
    ...
def getTmanNewSkillCount(tankman, useOnlyFull=False, withFree=False):
    ...
def quickEarnTmanSkills(tankman, possibleXp, ignoreEfficiency=False):
    ...
def quickEarnCrewSkills(crew, selectedTankmanID, personalXP, commonXP):
    ...
def getTmanWithSkill(tankman, tankmanVehicle, skill, itemsFactory, isBonus=False):
    ...
def getMaxSkillsEffAndLikeOwnVehTman(tankman, tankmanVehicle, itemsFactory, removeSkillCopies=False):
    ...
def getVehicleWithSkilledTman(skilledTman, tankman, tankmanVehicle, skillName=''):
    ...
def getSkillParams(tankman, tankmanVehicle, skillBooster, skill, skillName, skillLevel, isFakeSkill, isIrrelevant=False, isBonusSkill=False):
    ...
def getSkillDescription(tankman, skill, skillLevel, skillBooster, isCmpSkill, isFakeSkillLvl, isIrrelevant):
    ...
def formatDescription(description, params):
    ...
def getRoleBySkillName(skillName, **__):
    ...
