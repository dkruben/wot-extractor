# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/bonus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from epic_constants import EPIC_SKILL_TOKEN_NAME as EPIC_SKILL_TOKEN_NAME, EPIC_SELECT_BONUS_NAME as EPIC_SELECT_BONUS_NAME
from gui.server_events.bonuses import IntegralBonus as IntegralBonus
from gui.server_events.bonuses import SimpleBonus as SimpleBonus

class FrontlineSkillBonus(IntegralBonus):
    def __init__(self, value, ctx=None):
        ...

def isBonusesEqual(lhv, rhv):
    ...
def mergeSelectable(frontlineLevel, startLvl, endLvl, bonuses, bonusesByLvl):
    ...
