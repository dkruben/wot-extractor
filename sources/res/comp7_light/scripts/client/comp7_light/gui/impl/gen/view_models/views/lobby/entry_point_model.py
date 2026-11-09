# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/entry_point_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/entry_point_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class ProgressionState(Enum):
    INPROGRESS = 'inProgress'
    COMPLETED = 'completed'


class EntryPointModel(ViewModel):
    __slots__ = ('onOpenProgression', 'onAnimationEnd', 'onEntryPointAnimationSeen')

    def __init__(self, properties=6, commands=3):
        super(EntryPointModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return ProgressionState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def getCurProgressPoints(self):
        return self._getNumber(1)

    def setCurProgressPoints(self, value):
        self._setNumber(1, value)

    def getPrevProgressPoints(self):
        return self._getNumber(2)

    def setPrevProgressPoints(self, value):
        self._setNumber(2, value)

    def getPointsForLevel(self):
        return self._getNumber(3)

    def setPointsForLevel(self, value):
        self._setNumber(3, value)

    def getCurrentStage(self):
        return self._getNumber(4)

    def setCurrentStage(self, value):
        self._setNumber(4, value)

    def getIsEntryPointAnimationSeen(self):
        return self._getBool(5)

    def setIsEntryPointAnimationSeen(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(EntryPointModel, self)._initialize()
        self._addStringProperty('state')
        self._addNumberProperty('curProgressPoints', 0)
        self._addNumberProperty('prevProgressPoints', 0)
        self._addNumberProperty('pointsForLevel', 0)
        self._addNumberProperty('currentStage', 0)
        self._addBoolProperty('isEntryPointAnimationSeen', False)
        self.onOpenProgression = self._addCommand('onOpenProgression')
        self.onAnimationEnd = self._addCommand('onAnimationEnd')
        self.onEntryPointAnimationSeen = self._addCommand('onEntryPointAnimationSeen')
