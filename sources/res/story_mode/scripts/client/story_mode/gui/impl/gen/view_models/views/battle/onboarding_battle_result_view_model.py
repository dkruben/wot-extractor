# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/battle/onboarding_battle_result_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/battle/onboarding_battle_result_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class OnboardingBattleResultViewModel(ViewModel):
    __slots__ = ('onContinue', 'onLoaded')

    def __init__(self, properties=2, commands=2):
        super(OnboardingBattleResultViewModel, self).__init__(properties=properties, commands=commands)

    def getCauseText(self):
        return self._getResource(0)

    def setCauseText(self, value):
        self._setResource(0, value)

    def getMissionId(self):
        return self._getNumber(1)

    def setMissionId(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(OnboardingBattleResultViewModel, self)._initialize()
        self._addResourceProperty('causeText', R.invalid())
        self._addNumberProperty('missionId', 0)
        self.onContinue = self._addCommand('onContinue')
        self.onLoaded = self._addCommand('onLoaded')
