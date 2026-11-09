# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_pass_completed_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_pass_completed_tooltip_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class ChapterType(Enum):
    COMMON = 'common'
    EXTRA = 'extra'
    HOLIDAY = 'holiday'


class BattlePassCompletedTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BattlePassCompletedTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getIsBattlePassPurchased(self):
        return self._getBool(0)

    def setIsBattlePassPurchased(self, value):
        self._setBool(0, value)

    def getNotChosenRewardCount(self):
        return self._getNumber(1)

    def setNotChosenRewardCount(self, value):
        self._setNumber(1, value)

    def getIsAvailableTankmen(self):
        return self._getBool(2)

    def setIsAvailableTankmen(self, value):
        self._setBool(2, value)

    def getChapterType(self):
        return ChapterType(self._getString(3))

    def setChapterType(self, value):
        self._setString(3, value.value)

    def _initialize(self):
        super(BattlePassCompletedTooltipViewModel, self)._initialize()
        self._addBoolProperty('isBattlePassPurchased', False)
        self._addNumberProperty('notChosenRewardCount', 0)
        self._addBoolProperty('isAvailableTankmen', False)
        self._addStringProperty('chapterType')
