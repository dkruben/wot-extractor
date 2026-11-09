# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/battle_control/arena_info/arena_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from comp7_core.gui.battle_control.arena_info.arena_vos import Comp7CoreKeys as Comp7CoreKeys
_DEFAULT_ROLE_SKILL_LEVEL = 0
_DEFAULT_PLAYER_RANK = 0
_DEFAULT_PLAYER_DIVISION = 0

class Comp7Keys(Enum):
    RANK = 'rank'
    IS_QUAL_ACTIVE = 'isQualActive'
    @staticmethod
    def getKeys(static=True):
        ...
    @staticmethod
    def getSortingKeys(static=True):
        ...

class TournamentComp7Keys(Enum):
    @staticmethod
    def getKeys(static=True):
        ...
    @staticmethod
    def getSortingKeys(static=True):
        ...
