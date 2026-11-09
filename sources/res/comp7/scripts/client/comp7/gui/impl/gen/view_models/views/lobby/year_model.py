# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/year_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/year_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class YearState(IntEnum):
    NOTSTARTED = 0
    ACTIVE = 1
    OFFSEASON = 3
    FINISHED = 4


class YearModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(YearModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return YearState(self._getNumber(0))

    def setState(self, value):
        self._setNumber(0, value.value)

    def _initialize(self):
        super(YearModel, self)._initialize()
        self._addNumberProperty('state')
