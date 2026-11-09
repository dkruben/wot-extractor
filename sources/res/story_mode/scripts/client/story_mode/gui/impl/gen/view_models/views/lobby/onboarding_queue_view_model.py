# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/onboarding_queue_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/onboarding_queue_view_model.py
from frameworks.wulf import ViewModel

class OnboardingQueueViewModel(ViewModel):
    __slots__ = ('onQuit', 'onLoaded')

    def __init__(self, properties=1, commands=2):
        super(OnboardingQueueViewModel, self).__init__(properties=properties, commands=commands)

    def getIsVisibleButton(self):
        return self._getBool(0)

    def setIsVisibleButton(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(OnboardingQueueViewModel, self)._initialize()
        self._addBoolProperty('isVisibleButton', False)
        self.onQuit = self._addCommand('onQuit')
        self.onLoaded = self._addCommand('onLoaded')
