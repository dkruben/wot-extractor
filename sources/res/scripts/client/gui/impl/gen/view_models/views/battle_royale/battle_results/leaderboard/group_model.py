# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/leaderboard/group_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/leaderboard/group_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.battle_royale.battle_results.leaderboard.row_model import RowModel

class GroupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(GroupModel, self).__init__(properties=properties, commands=commands)

    def getPlace(self):
        return self._getString(0)

    def setPlace(self, value):
        self._setString(0, value)

    def getRewardCount(self):
        return self._getNumber(1)

    def setRewardCount(self, value):
        self._setNumber(1, value)

    def getRewardIcon(self):
        return self._getResource(2)

    def setRewardIcon(self, value):
        self._setResource(2, value)

    def getIsPersonalSquad(self):
        return self._getBool(3)

    def setIsPersonalSquad(self, value):
        self._setBool(3, value)

    def getPlayersList(self):
        return self._getArray(4)

    def setPlayersList(self, value):
        self._setArray(4, value)

    @staticmethod
    def getPlayersListType():
        return RowModel

    def _initialize(self):
        super(GroupModel, self)._initialize()
        self._addStringProperty('place', '')
        self._addNumberProperty('rewardCount', 0)
        self._addResourceProperty('rewardIcon', R.invalid())
        self._addBoolProperty('isPersonalSquad', False)
        self._addArrayProperty('playersList', Array())
