# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/random/random_team_stats_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/random/random_team_stats_model.py
from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_player_model import RandomPlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel

class RandomColumnType(Enum):
    SQUAD = 'squad'
    PLAYER = 'player'
    DAMAGE = 'damage'
    FRAG = 'frag'
    XP = 'xp'
    VEHICLE = 'tank'
    MEDAL = 'medal'


class RandomTeamStatsModel(TeamStatsModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(RandomTeamStatsModel, self).__init__(properties=properties, commands=commands)

    def getAllies(self):
        return self._getArray(5)

    def setAllies(self, value):
        self._setArray(5, value)

    @staticmethod
    def getAlliesType():
        return RandomPlayerModel

    def getEnemies(self):
        return self._getArray(6)

    def setEnemies(self, value):
        self._setArray(6, value)

    @staticmethod
    def getEnemiesType():
        return RandomPlayerModel

    def getSortingColumn(self):
        return RandomColumnType(self._getString(7))

    def setSortingColumn(self, value):
        self._setString(7, value.value)

    def _initialize(self):
        super(RandomTeamStatsModel, self)._initialize()
        self._addArrayProperty('allies', Array())
        self._addArrayProperty('enemies', Array())
        self._addStringProperty('sortingColumn', RandomColumnType.PLAYER.value)
