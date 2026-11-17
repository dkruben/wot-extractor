# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/prestige_system/prestige_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import IS_CLIENT as IS_CLIENT
from prestige_system import getCache as getCache, computePrestigeCache as computePrestigeCache
from typing import Dict as Dict, List as List, Optional as Optional
PrestigeGrade: Any

class PrestigeConfig(object):
    _config: Any
    __cache: Any
    class GradeKeys(object):
        LEVEL = 'level'
        MARK_ID = 'prestigeMarkID'
        MAIN = 'main'
    def __init__(self, config):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def prestigeCoefficient(self):
        ...
    @property
    def prestigePoints(self):
        ...
    @property
    def defaultMaxLevel(self):
        ...
    @property
    def grades(self):
        ...
    def getSortedGrades(self, key=...):
        ...
    def getSortedMainGrades(self, key=...):
        ...
    def getVehiclePoints(self, vehCD):
        ...
