# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/battle_results/comp7_team_stats_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/battle_results/comp7_team_stats_model.py
from enum import Enum
from frameworks.wulf import Array
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_player_model import Comp7PlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel

class Comp7ColumnType(Enum):
    SQUAD = 'squad'
    RANK = 'rank'
    PLAYER = 'player'
    DAMAGE = 'damage'
    FRAG = 'frag'
    XP = 'xp'
    VEHICLE = 'tank'
    MEDAL = 'medal'
    PRESTIGEPOINTS = 'prestigePoints'


class Comp7TeamStatsModel(TeamStatsModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(Comp7TeamStatsModel, self).__init__(properties=properties, commands=commands)

    def getAllies(self):
        return self._getArray(5)

    def setAllies(self, value):
        self._setArray(5, value)

    @staticmethod
    def getAlliesType():
        return Comp7PlayerModel

    def getEnemies(self):
        return self._getArray(6)

    def setEnemies(self, value):
        self._setArray(6, value)

    @staticmethod
    def getEnemiesType():
        return Comp7PlayerModel

    def getSortingColumn(self):
        return Comp7ColumnType(self._getString(7))

    def setSortingColumn(self, value):
        self._setString(7, value.value)

    def _initialize(self):
        super(Comp7TeamStatsModel, self)._initialize()
        self._addArrayProperty('allies', Array())
        self._addArrayProperty('enemies', Array())
        self._addStringProperty('sortingColumn', Comp7ColumnType.PLAYER.value)
