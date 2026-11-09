# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/combined_crew_skill.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional
from math_common import round_py2_style_int as round_py2_style_int
from items import tankmen as tankmen

class CombinedCrewSkill(object):
    __slots__: tuple
    tankmanLevel: Any
    levelIncrease: Any
    skillsEfficiency: Any
    isTankmanActive: Any
    hasActiveTankmanForBooster: Any
    boosterMultiplier: Any
    def __init__(self, tankmanLevel, levelIncrease, skillsEfficiency, isTankmanActive, hasActiveTankmanForBooster=False, boosterMultiplier=None):
        ...
    @property
    def level(self):
        ...
    def _floatLevel(self):
        ...
    @property
    def isActive(self):
        ...
    def __str__(self):
        ...
