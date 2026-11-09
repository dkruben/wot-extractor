# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/shared/timer_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/shared/timer_model.py
from frameworks.wulf import ViewModel

class TimerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TimerModel, self).__init__(properties=properties, commands=commands)

    def getStartTimestamp(self):
        return self._getNumber(0)

    def setStartTimestamp(self, value):
        self._setNumber(0, value)

    def getElapsed(self):
        return self._getReal(1)

    def setElapsed(self, value):
        self._setReal(1, value)

    def getDuration(self):
        return self._getReal(2)

    def setDuration(self, value):
        self._setReal(2, value)

    def _initialize(self):
        super(TimerModel, self)._initialize()
        self._addNumberProperty('startTimestamp', 0)
        self._addRealProperty('elapsed', 0.0)
        self._addRealProperty('duration', 0.0)
