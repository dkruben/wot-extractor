# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/prestige_system/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from builtins import zip as zip
from copy import copy as copy
from future.utils import lrange as lrange, viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV, LOG_DEBUG as LOG_DEBUG
from dossiers2.custom.cache import getCache as getDossiers2Cache, buildCache as buildDossiers2Cache
from typing import Optional as Optional, Dict as Dict, List as List, Set as Set
_g_cache: dict

class PrestigeConstants(object):
    GRADE_MIN_LEVEL = 1
    GRADES_NUMBER = 20
    PRESTIGE_MAX_LEVEL = 1000
    MAX_GRADE_MARK_ID = -1

def getCache():
    ...
def computePrestigeCache(config, cache=None, dossiers2Cache=None):
    ...
def computeAllPrestigePoints(defaultLevels, overrideItems, allVehicleDescrs, defaultLevelCostArgs):
    ...
def computePrestigePoints(override):
    ...
def preprocessLevels(levels):
    ...
def computeLevelCost(levelCostArgs, levels):
    ...
def applyOverridePoints(prestigePointsDict, overridePoints, vehicles, defaultLevelCostArgs, newMaxLevel=None):
    ...
