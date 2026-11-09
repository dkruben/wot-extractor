# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/rewards_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/rewards_view_model.py
from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class RewardingType(IntEnum):
    COMMON = 0
    ELITE = 1
    ELITE_WITH_VEHICLE = 2


class RewardsViewModel(ViewModel):
    __slots__ = ('onClose', 'onGoToHangar')

    def __init__(self, properties=3, commands=2):
        super(RewardsViewModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return RewardingType(self._getNumber(0))

    def setType(self, value):
        self._setNumber(0, value.value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getAdditionalRewards(self):
        return self._getArray(2)

    def setAdditionalRewards(self, value):
        self._setArray(2, value)

    @staticmethod
    def getAdditionalRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(RewardsViewModel, self)._initialize()
        self._addNumberProperty('type')
        self._addArrayProperty('rewards', Array())
        self._addArrayProperty('additionalRewards', Array())
        self.onClose = self._addCommand('onClose')
        self.onGoToHangar = self._addCommand('onGoToHangar')
