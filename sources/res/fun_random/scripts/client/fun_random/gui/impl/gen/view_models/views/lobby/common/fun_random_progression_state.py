# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_progression_state.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_progression_state.py
from enum import Enum
from frameworks.wulf import ViewModel

class FunRandomProgressionStatus(Enum):
    DISABLED = 'disabled'
    ACTIVE_FINAL = 'activeFinal'
    ACTIVE_RESETTABLE = 'activeResettable'
    COMPLETED_FINAL = 'completedFinal'
    COMPLETED_RESETTABLE = 'completedResettable'
    ACTIVE_INFINITE_RESETTABLE = 'activeInfiniteResettable'
    ACTIVE_INFINITE_FINAL = 'activeInfiniteFinal'


class FunRandomProgressionState(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FunRandomProgressionState, self).__init__(properties=properties, commands=commands)

    def getStatus(self):
        return FunRandomProgressionStatus(self._getString(0))

    def setStatus(self, value):
        self._setString(0, value.value)

    def getCurrentStage(self):
        return self._getNumber(1)

    def setCurrentStage(self, value):
        self._setNumber(1, value)

    def getMaximumStage(self):
        return self._getNumber(2)

    def setMaximumStage(self, value):
        self._setNumber(2, value)

    def getStatusTimer(self):
        return self._getNumber(3)

    def setStatusTimer(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(FunRandomProgressionState, self)._initialize()
        self._addStringProperty('status')
        self._addNumberProperty('currentStage', -1)
        self._addNumberProperty('maximumStage', -1)
        self._addNumberProperty('statusTimer', -1)
