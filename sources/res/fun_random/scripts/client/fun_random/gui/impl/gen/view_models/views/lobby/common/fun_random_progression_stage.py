# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_progression_stage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_progression_stage.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class Rarity(Enum):
    ORDINARY = 'ordinary'
    UNUSUAL = 'unusual'
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'


class FunRandomProgressionStage(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FunRandomProgressionStage, self).__init__(properties=properties, commands=commands)

    def getCurrentPoints(self):
        return self._getNumber(0)

    def setCurrentPoints(self, value):
        self._setNumber(0, value)

    def getRequiredPoints(self):
        return self._getNumber(1)

    def setRequiredPoints(self, value):
        self._setNumber(1, value)

    def getMaximumPoints(self):
        return self._getNumber(2)

    def setMaximumPoints(self, value):
        self._setNumber(2, value)

    def getIsCompleted(self):
        return self._getBool(3)

    def setIsCompleted(self, value):
        self._setBool(3, value)

    def getRarity(self):
        return Rarity(self._getString(4))

    def setRarity(self, value):
        self._setString(4, value.value)

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(FunRandomProgressionStage, self)._initialize()
        self._addNumberProperty('currentPoints', -1)
        self._addNumberProperty('requiredPoints', -1)
        self._addNumberProperty('maximumPoints', -1)
        self._addBoolProperty('isCompleted', False)
        self._addStringProperty('rarity')
        self._addArrayProperty('rewards', Array())
