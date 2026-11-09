# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/challenges/awards_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/challenges/awards_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.challenges.bonus_model import BonusModel

class AwardsViewModel(ViewModel):
    __slots__ = ('onClose', 'onHangar', 'onChallenges')

    def __init__(self, properties=5, commands=3):
        super(AwardsViewModel, self).__init__(properties=properties, commands=commands)

    def getChallengeName(self):
        return self._getString(0)

    def setChallengeName(self, value):
        self._setString(0, value)

    def getMainRewardType(self):
        return self._getString(1)

    def setMainRewardType(self, value):
        self._setString(1, value)

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
        self._setBool(2, value)

    def getIsAvailable(self):
        return self._getBool(3)

    def setIsAvailable(self, value):
        self._setBool(3, value)

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(AwardsViewModel, self)._initialize()
        self._addStringProperty('challengeName', '')
        self._addStringProperty('mainRewardType', '')
        self._addBoolProperty('isCompleted', False)
        self._addBoolProperty('isAvailable', False)
        self._addArrayProperty('rewards', Array())
        self.onClose = self._addCommand('onClose')
        self.onHangar = self._addCommand('onHangar')
        self.onChallenges = self._addCommand('onChallenges')
