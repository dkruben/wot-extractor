# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/ranked/year_leaderboard_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/ranked/year_leaderboard_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class YearLeaderboardViewModel(ViewModel):
    __slots__ = ('onLeaderboardBtnClick', )

    def __init__(self, properties=6, commands=1):
        super(YearLeaderboardViewModel, self).__init__(properties=properties, commands=commands)

    def getPlayerName(self):
        return self._getString(0)

    def setPlayerName(self, value):
        self._setString(0, value)

    def getPlayerClan(self):
        return self._getString(1)

    def setPlayerClan(self, value):
        self._setString(1, value)

    def getPositionsTotal(self):
        return self._getNumber(2)

    def setPositionsTotal(self, value):
        self._setNumber(2, value)

    def getPosition(self):
        return self._getNumber(3)

    def setPosition(self, value):
        self._setNumber(3, value)

    def getRewardId(self):
        return self._getNumber(4)

    def setRewardId(self, value):
        self._setNumber(4, value)

    def getBgImage(self):
        return self._getResource(5)

    def setBgImage(self, value):
        self._setResource(5, value)

    def _initialize(self):
        super(YearLeaderboardViewModel, self)._initialize()
        self._addStringProperty('playerName', '')
        self._addStringProperty('playerClan', '')
        self._addNumberProperty('positionsTotal', 0)
        self._addNumberProperty('position', 0)
        self._addNumberProperty('rewardId', 0)
        self._addResourceProperty('bgImage', R.invalid())
        self.onLeaderboardBtnClick = self._addCommand('onLeaderboardBtnClick')
