# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/game_params_common/scope.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum, unique as unique

# decorador original: @unique
class GameParamsScopeFlags(IntEnum):
    BASE = 1
    CLIENT = 2
    CELL_ARENA = 4

class CellArenaScopeContext(object):
    __slots__: tuple
    bonusType: Any
    bonusCapsOverrides: Any
    gameplayID: Any
    def __init__(self, bonusType, bonusCapsOverrides, gameplayID):
        ...

def clientFilter(params):
    ...
def cellArenaFilter(params):
    ...
