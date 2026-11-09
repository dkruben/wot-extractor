# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crystals_promo/condition_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crystals_promo/condition_model.py
from frameworks.wulf import ViewModel

class ConditionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ConditionModel, self).__init__(properties=properties, commands=commands)

    def getPosition(self):
        return self._getNumber(0)

    def setPosition(self, value):
        self._setNumber(0, value)

    def getForWin(self):
        return self._getNumber(1)

    def setForWin(self, value):
        self._setNumber(1, value)

    def getForDefeat(self):
        return self._getNumber(2)

    def setForDefeat(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(ConditionModel, self)._initialize()
        self._addNumberProperty('position', 0)
        self._addNumberProperty('forWin', 0)
        self._addNumberProperty('forDefeat', 0)
