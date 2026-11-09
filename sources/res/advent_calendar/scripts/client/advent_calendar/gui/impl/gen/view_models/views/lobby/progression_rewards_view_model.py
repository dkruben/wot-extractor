# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/progression_rewards_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/progression_rewards_view_model.py
from frameworks.wulf import Array, ViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import ProgressionRewardItemViewModel

class ProgressionRewardsViewModel(ViewModel):
    __slots__ = ('onProgressionRewardCompleted', )

    def __init__(self, properties=2, commands=1):
        super(ProgressionRewardsViewModel, self).__init__(properties=properties, commands=commands)

    def getIsCompleted(self):
        return self._getBool(0)

    def setIsCompleted(self, value):
        self._setBool(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return ProgressionRewardItemViewModel

    def _initialize(self):
        super(ProgressionRewardsViewModel, self)._initialize()
        self._addBoolProperty('isCompleted', False)
        self._addArrayProperty('rewards', Array())
        self.onProgressionRewardCompleted = self._addCommand('onProgressionRewardCompleted')
