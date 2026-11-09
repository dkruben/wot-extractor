# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/prebattle/prebattle_hints_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/prebattle/prebattle_hints_view_model.py
from frameworks.wulf import ViewModel

class PrebattleHintsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PrebattleHintsViewModel, self).__init__(properties=properties, commands=commands)

    def getHintType(self):
        return self._getString(0)

    def setHintType(self, value):
        self._setString(0, value)

    def getCanSkip(self):
        return self._getBool(1)

    def setCanSkip(self, value):
        self._setBool(1, value)

    def getIsColorBlind(self):
        return self._getBool(2)

    def setIsColorBlind(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(PrebattleHintsViewModel, self)._initialize()
        self._addStringProperty('hintType', '')
        self._addBoolProperty('canSkip', False)
        self._addBoolProperty('isColorBlind', False)
