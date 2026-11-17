# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/skills_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from future.utils import iteritems as iteritems
SKILL_NAMES: tuple
SKILL_INDICES: Any
ORDERED_ROLES: tuple
ROLES: Any
COMMON_SKILL_ROLE_TYPE = 'common'
ROLE_LIMITS: dict
COMMON_SKILLS_ORDERED: tuple
COMMON_SKILLS: Any
ROLES_AND_COMMON_SKILLS: Any
COMMANDER_SKILLS: tuple
GUNNER_SKILLS: tuple
DRIVER_SKILLS: tuple
RADIOMAN_SKILLS: tuple
LOADER_SKILLS: tuple
COMMON_ROLE = 'common'
SKILLS_BY_ROLES_ORDERED: dict
SKILL_NAMES_ORDERED: Any
SKILL_INDICES_ORDERED: Any
SKILLS_BY_ROLES: dict
ROLES_BY_SKILLS: dict
ACTIVE_SKILLS: Any
ACTIVE_NOT_GROUP_SKILLS: Any
ACTIVE_FREE_SKILLS: Any
UNLEARNABLE_SKILLS: tuple
LEARNABLE_ACTIVE_SKILLS: Any
LEARNABLE_COMMANDER_SKILLS: Any
ALL_SKILLS_BY_ROLE_TYPE: Any

class ROLE_NAMES(object):
    COMMANDER = 'commander'
    RADIOMAN = 'radioman'
    DRIVER = 'driver'
    GUNNER = 'gunner'
    LOADER = 'loader'

class ParamMeasureType(object):
    PERCENTS = 'percents'
    SECONDS = 'seconds'
    PERCENT_GAP = 'percentGap'
    MPH = 'mph'
    METERS = 'meters'

class ParamSignType(object):
    PLUS = 'plus'
    MINUS = 'minus'
    SIGN_LESS = 'signLess'

class SkillTypeName(object):
    MAIN = 'main'
    SITUATIONAL = 'situational'
    COMMON = 'common'
    COMMANDER_SPECIAL = 'commanderSpecial'

class SkillUtilization(object):
    FREE_SKILL = 0
    MAJOR_SKILL = 1
    BONUS_SKILL = 2
