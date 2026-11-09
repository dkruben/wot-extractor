# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_difficulty_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_difficulty_tooltip_model.py
from frameworks.wulf import ViewModel

class MissionDifficultyTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MissionDifficultyTooltipModel, self).__init__(properties=properties, commands=commands)

    def getDifficulty(self):
        return self._getString(0)

    def setDifficulty(self, value):
        self._setString(0, value)

    def getIsAutoCompleteCondition(self):
        return self._getBool(1)

    def setIsAutoCompleteCondition(self, value):
        self._setBool(1, value)

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)

    def getIsLocked(self):
        return self._getBool(3)

    def setIsLocked(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(MissionDifficultyTooltipModel, self)._initialize()
        self._addStringProperty('difficulty', '')
        self._addBoolProperty('isAutoCompleteCondition', False)
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isLocked', False)
