# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/enums.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/enums.py
from enum import Enum, IntEnum

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
