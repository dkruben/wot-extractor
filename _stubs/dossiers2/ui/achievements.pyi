# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dossiers2/ui/achievements.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import resource_helper as resource_helper
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from constants import IS_WEB as IS_WEB
from soft_exception import SoftException as SoftException
BATTLE_HERO_TEXTS: dict
BADGES_BLOCK = 'playerBadges'
_AT: tuple
_AS: tuple
_AB: tuple
_AM: tuple
DEFAULT_WEIGHT = -1
MARK_OF_MASTERY = 'markOfMastery'
MARK_ON_GUN = 'marksOnGun'
RARE_STORAGE_RECORD: Any
MARK_OF_MASTERY_RECORD: tuple
MARK_ON_GUN_RECORD: tuple
HONORED_RANK_RECORD: tuple
_MODE_CONVERTER: dict
ACHIEVEMENTS: dict
ACHIEVEMENT_SECTIONS_ORDER: tuple
ACHIEVEMENT_SECTIONS_INDICES: Any
BATTLE_ACHIEVES_WITH_RIBBON: tuple
BATTLE_ACHIEVES_RIGHT: tuple
FORT_BATTLE_ACHIEVES_RIGHT: tuple
BATTLE_APPROACHABLE_ACHIEVES: tuple

class ACHIEVEMENT_BLOCK:
    CLIENT = 'client'
    TOTAL = 'achievements'
    TEAM_7X7 = 'achievements7x7'
    HISTORICAL = 'historicalAchievements'
    UNIQUE = 'uniqueAchievements'
    RARE = 'rareAchievements'
    FORT = 'fortAchievements'
    SINGLE = 'singleAchievements'
    SINGLE_7X7 = 'singleAchievementsRated7x7'
    CLAN = 'clanAchievements'
    RATED_7X7 = 'achievementsRated7x7'
    FALLOUT = 'falloutAchievements'
    EPIC_BATTLE = 'epicBattleAchievements'
    STEAM = 'steamAchievements'
    ALL: tuple

class ACHIEVEMENT_MODE:
    RANDOM = 1
    TEAM_7X7 = 2
    HISTORICAL = 4
    RATED_7X7 = 8
    RANKED = 22
    EPIC_BATTLE = 16
    ALL: Any

class ACHIEVEMENT_TYPE:
    REPEATABLE = 'repeatable'
    CLASS = 'class'
    CUSTOM = 'custom'
    SERIES = 'series'
    SINGLE = 'single'
    ALL: tuple

class ACHIEVEMENT_SECTION:
    EPIC = 'epic'
    BATTLE = 'battle'
    SPECIAL = 'special'
    CLASS = 'class'
    ACTION = 'action'
    MEMORIAL = 'memorial'
    GROUP = 'group'
    ALL: tuple

def makeAchievesStorageName(block):
    ...
def getType(record):
    ...
def getSection(record):
    ...
def getMode(record):
    ...
def getWeight(record):
    ...
def init(achievesMappingXmlPath):
    ...
