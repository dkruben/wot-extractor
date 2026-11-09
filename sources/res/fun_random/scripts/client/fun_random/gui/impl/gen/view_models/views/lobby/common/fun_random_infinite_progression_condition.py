# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_infinite_progression_condition.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_infinite_progression_condition.py
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition

class FunRandomInfiniteProgressionCondition(FunRandomProgressionCondition):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(FunRandomInfiniteProgressionCondition, self).__init__(properties=properties, commands=commands)

    def getCompleteCount(self):
        return self._getNumber(8)

    def setCompleteCount(self, value):
        self._setNumber(8, value)

    def getPrevCompleteCount(self):
        return self._getNumber(9)

    def setPrevCompleteCount(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(FunRandomInfiniteProgressionCondition, self)._initialize()
        self._addNumberProperty('completeCount', -1)
        self._addNumberProperty('prevCompleteCount', -1)
