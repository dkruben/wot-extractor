# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/battle/prebattle_window_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/battle/prebattle_window_view_model.py
from frameworks.wulf import ViewModel

class PrebattleWindowViewModel(ViewModel):
    __slots__ = ('onGotoBattle', 'onLoaded')

    def __init__(self, properties=2, commands=2):
        super(PrebattleWindowViewModel, self).__init__(properties=properties, commands=commands)

    def getIsLoading(self):
        return self._getBool(0)

    def setIsLoading(self, value):
        self._setBool(0, value)

    def getMissionNumber(self):
        return self._getNumber(1)

    def setMissionNumber(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(PrebattleWindowViewModel, self)._initialize()
        self._addBoolProperty('isLoading', False)
        self._addNumberProperty('missionNumber', 0)
        self.onGotoBattle = self._addCommand('onGotoBattle')
        self.onLoaded = self._addCommand('onLoaded')
