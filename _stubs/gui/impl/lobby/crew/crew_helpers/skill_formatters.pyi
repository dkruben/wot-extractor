# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/skill_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL

class SkillLvlFormatter(object):
    NDIG = 2
    MIN_FRACTION = 0.01
    MAX_FRACTION: Any
    intSkillLvl: Any
    residualXp: Any
    lvlCostXp: Any
    isSkillLvl: Any
    realSkillLvl: Any
    formattedSkillLvl: Any
    __slots__: tuple
    __hash__ = None
    __skillLvl: Any
    __residual: Any
    __lvlCost: Any
    def __init__(self, skillLvl=..., residual=0, lvlCost=0):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...
    def __add__(self, other):
        ...
    def __sub__(self, other):
        ...
    def __lt__(self, other):
        ...
    def __gt__(self, other):
        ...
    def __eq__(self, other):
        ...
    def __le__(self, other):
        ...
    def __ge__(self, other):
        ...
    def __ne__(self, other):
        ...
    def _cmp(self, other):
        ...
    def makeRealLvl(self):
        ...
    def formatLvl(self):
        ...
    @staticmethod
    def roundLvl(realNumber, ndig):
        ...
