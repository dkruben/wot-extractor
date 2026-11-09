# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tooltips/rest_bonus_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tooltips/rest_bonus_tooltip_model.py
from frameworks.wulf import ViewModel

class RestBonusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RestBonusTooltipModel, self).__init__(properties=properties, commands=commands)

    def getMultiplier(self):
        return self._getNumber(0)

    def setMultiplier(self, value):
        self._setNumber(0, value)

    def getResetTimestamp(self):
        return self._getNumber(1)

    def setResetTimestamp(self, value):
        self._setNumber(1, value)

    def getEndTimestamp(self):
        return self._getNumber(2)

    def setEndTimestamp(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(RestBonusTooltipModel, self)._initialize()
        self._addNumberProperty('multiplier', 0)
        self._addNumberProperty('resetTimestamp', 0)
        self._addNumberProperty('endTimestamp', 0)
