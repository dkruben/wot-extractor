# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/stage_reward_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/stage_reward_view_model.py
from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class StageRewardViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=4, commands=1):
        super(StageRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getArtefactNumber(self):
        return self._getNumber(0)

    def setArtefactNumber(self, value):
        self._setNumber(0, value)

    def getIsLastArtefact(self):
        return self._getBool(1)

    def setIsLastArtefact(self, value):
        self._setBool(1, value)

    def getIsQuestReward(self):
        return self._getBool(2)

    def setIsQuestReward(self, value):
        self._setBool(2, value)

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(StageRewardViewModel, self)._initialize()
        self._addNumberProperty('artefactNumber', 0)
        self._addBoolProperty('isLastArtefact', False)
        self._addBoolProperty('isQuestReward', False)
        self._addArrayProperty('rewards', Array())
        self.onClose = self._addCommand('onClose')
