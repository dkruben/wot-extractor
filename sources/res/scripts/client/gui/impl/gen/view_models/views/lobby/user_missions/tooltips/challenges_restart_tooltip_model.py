# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/tooltips/challenges_restart_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/tooltips/challenges_restart_tooltip_model.py
from frameworks.wulf import ViewModel

class ChallengesRestartTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ChallengesRestartTooltipModel, self).__init__(properties=properties, commands=commands)

    def getRestartCost(self):
        return self._getNumber(0)

    def setRestartCost(self, value):
        self._setNumber(0, value)

    def getCurrency(self):
        return self._getString(1)

    def setCurrency(self, value):
        self._setString(1, value)

    def getFreeRestarts(self):
        return self._getNumber(2)

    def setFreeRestarts(self, value):
        self._setNumber(2, value)

    def getUsedFreeRestarts(self):
        return self._getNumber(3)

    def setUsedFreeRestarts(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(ChallengesRestartTooltipModel, self)._initialize()
        self._addNumberProperty('restartCost', 0)
        self._addStringProperty('currency', '')
        self._addNumberProperty('freeRestarts', 0)
        self._addNumberProperty('usedFreeRestarts', 0)
