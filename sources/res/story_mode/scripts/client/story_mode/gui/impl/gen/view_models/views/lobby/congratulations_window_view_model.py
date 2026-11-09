# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/congratulations_window_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/congratulations_window_view_model.py
from frameworks.wulf import ViewModel

class CongratulationsWindowViewModel(ViewModel):
    __slots__ = ('onClose', 'onLoaded')

    def __init__(self, properties=5, commands=2):
        super(CongratulationsWindowViewModel, self).__init__(properties=properties, commands=commands)

    def getIsCloseVisible(self):
        return self._getBool(0)

    def setIsCloseVisible(self, value):
        self._setBool(0, value)

    def getIsOnboarding(self):
        return self._getBool(1)

    def setIsOnboarding(self, value):
        self._setBool(1, value)

    def getMedalName(self):
        return self._getString(2)

    def setMedalName(self, value):
        self._setString(2, value)

    def getBadgeId(self):
        return self._getNumber(3)

    def setBadgeId(self, value):
        self._setNumber(3, value)

    def getMissionId(self):
        return self._getNumber(4)

    def setMissionId(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(CongratulationsWindowViewModel, self)._initialize()
        self._addBoolProperty('isCloseVisible', False)
        self._addBoolProperty('isOnboarding', False)
        self._addStringProperty('medalName', '')
        self._addNumberProperty('badgeId', 0)
        self._addNumberProperty('missionId', 0)
        self.onClose = self._addCommand('onClose')
        self.onLoaded = self._addCommand('onLoaded')
