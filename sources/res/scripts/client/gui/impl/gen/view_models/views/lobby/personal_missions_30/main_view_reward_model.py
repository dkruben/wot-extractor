# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/main_view_reward_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/main_view_reward_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.style_bonus_model import StyleBonusModel

class RewardsType(Enum):
    MAIN = 'main'
    OPERATION = 'operation'
    CAMPAIGN = 'campaign'


class MainViewRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MainViewRewardModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)

    @staticmethod
    def getItemsType():
        return StyleBonusModel

    def getRewardsType(self):
        return RewardsType(self._getString(1))

    def setRewardsType(self, value):
        self._setString(1, value.value)

    def getCompletedTasks(self):
        return self._getNumber(2)

    def setCompletedTasks(self, value):
        self._setNumber(2, value)

    def getTasksNumber(self):
        return self._getNumber(3)

    def setTasksNumber(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(MainViewRewardModel, self)._initialize()
        self._addArrayProperty('items', Array())
        self._addStringProperty('rewardsType')
        self._addNumberProperty('completedTasks', 0)
        self._addNumberProperty('tasksNumber', 0)
