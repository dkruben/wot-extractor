# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/enums.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, IntEnum as IntEnum

class MetaRootViews(IntEnum):
    PROGRESSION = 0
    RANKREWARDS = 1
    YEARLYREWARDS = 2
    WEEKLYQUESTS = 3
    SHOP = 4
    LEADERBOARD = 5
    YEARLYSTATISTICS = 6

class Rank(IntEnum):
    FIRST = 6
    SECOND = 5
    THIRD = 4
    FOURTH = 3
    FIFTH = 2
    SIXTH = 1

class SeasonName(Enum):
    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'

class Division(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5

class StatisticsMode(IntEnum):
    SEASON = 0
    DAY = 1

class SeasonPointState(Enum):
    ACHIEVED = 'achieved'
    POSSIBLE = 'possible'
    NOTACHIEVED = 'notAchieved'

class TournamentName(Enum):
    WCI = 'wci'
    OLS = 'ols'
