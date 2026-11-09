# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/tooltips/difficulty_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/tooltips/difficulty_tooltip_view_model.py
from frameworks.wulf import Array
from last_stand.gui.impl.gen.view_models.views.lobby.tooltips.difficulty_wave_rewards_model import DifficultyWaveRewardsModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel

class DifficultyTooltipViewModel(DifficultyItemModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(DifficultyTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getIsHangar(self):
        return self._getBool(7)

    def setIsHangar(self, value):
        self._setBool(7, value)

    def getMaxCompletedMissions(self):
        return self._getNumber(8)

    def setMaxCompletedMissions(self, value):
        self._setNumber(8, value)

    def getModifier(self):
        return self._getNumber(9)

    def setModifier(self, value):
        self._setNumber(9, value)

    def getRewardsByWave(self):
        return self._getArray(10)

    def setRewardsByWave(self, value):
        self._setArray(10, value)

    @staticmethod
    def getRewardsByWaveType():
        return DifficultyWaveRewardsModel

    def _initialize(self):
        super(DifficultyTooltipViewModel, self)._initialize()
        self._addBoolProperty('isHangar', False)
        self._addNumberProperty('maxCompletedMissions', 0)
        self._addNumberProperty('modifier', 0)
        self._addArrayProperty('rewardsByWave', Array())
