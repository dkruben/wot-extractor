# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/reward_points_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/reward_points_model.py
from frameworks.wulf import ViewModel

class RewardPointsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RewardPointsModel, self).__init__(properties=properties, commands=commands)

    def getTopCount(self):
        return self._getNumber(0)

    def setTopCount(self, value):
        self._setNumber(0, value)

    def getPointsWin(self):
        return self._getNumber(1)

    def setPointsWin(self, value):
        self._setNumber(1, value)

    def getPointsLose(self):
        return self._getNumber(2)

    def setPointsLose(self, value):
        self._setNumber(2, value)

    def getExternalPointsWin(self):
        return self._getNumber(3)

    def setExternalPointsWin(self, value):
        self._setNumber(3, value)

    def getExternalPointsLose(self):
        return self._getNumber(4)

    def setExternalPointsLose(self, value):
        self._setNumber(4, value)

    def getIsSpecial(self):
        return self._getBool(5)

    def setIsSpecial(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(RewardPointsModel, self)._initialize()
        self._addNumberProperty('topCount', 0)
        self._addNumberProperty('pointsWin', 0)
        self._addNumberProperty('pointsLose', 0)
        self._addNumberProperty('externalPointsWin', 0)
        self._addNumberProperty('externalPointsLose', 0)
        self._addBoolProperty('isSpecial', False)
