# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_intro_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_intro_view_model.py
from frameworks.wulf import Array, ViewModel

class BattlePassIntroViewModel(ViewModel):
    __slots__ = ('onViewLoaded', )

    def __init__(self, properties=1, commands=1):
        super(BattlePassIntroViewModel, self).__init__(properties=properties, commands=commands)

    def getSlides(self):
        return self._getArray(0)

    def setSlides(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSlidesType():
        return unicode

    def _initialize(self):
        super(BattlePassIntroViewModel, self)._initialize()
        self._addArrayProperty('slides', Array())
        self.onViewLoaded = self._addCommand('onViewLoaded')
