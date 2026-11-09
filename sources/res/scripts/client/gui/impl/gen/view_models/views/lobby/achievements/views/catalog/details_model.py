# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/catalog/details_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/catalog/details_model.py
from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.rewards_model import RewardsModel

class ProgressType(Enum):
    PERCENTAGE = 'percentage'
    STEPPED = 'stepped'


class DetailsModel(AdvancedAchievementModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(DetailsModel, self).__init__(properties=properties, commands=commands)

    def getProgressType(self):
        return ProgressType(self._getString(15))

    def setProgressType(self, value):
        self._setString(15, value.value)

    def getSpecificItemLevel(self):
        return self._getNumber(16)

    def setSpecificItemLevel(self, value):
        self._setNumber(16, value)

    def getRewards(self):
        return self._getArray(17)

    def setRewards(self, value):
        self._setArray(17, value)

    @staticmethod
    def getRewardsType():
        return RewardsModel

    def _initialize(self):
        super(DetailsModel, self)._initialize()
        self._addStringProperty('progressType')
        self._addNumberProperty('specificItemLevel', 0)
        self._addArrayProperty('rewards', Array())
