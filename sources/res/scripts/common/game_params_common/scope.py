# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/game_params_common/scope.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/game_params_common/scope.py
from __future__ import absolute_import
from enum import IntEnum, unique

@unique
class GameParamsScopeFlags(IntEnum):
    BASE = 1
    CLIENT = 2
    CELL_ARENA = 4


class CellArenaScopeContext(object):
    __slots__ = ('bonusType', 'bonusCapsOverrides', 'gameplayID')

    def __init__(self, bonusType, bonusCapsOverrides, gameplayID):
        self.bonusType = bonusType
        self.bonusCapsOverrides = bonusCapsOverrides
        self.gameplayID = gameplayID


def clientFilter(params):
    return bool(params & GameParamsScopeFlags.CLIENT)


def cellArenaFilter(params):
    return bool(params & GameParamsScopeFlags.CELL_ARENA)
