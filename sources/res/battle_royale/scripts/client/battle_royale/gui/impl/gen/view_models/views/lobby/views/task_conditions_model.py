# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/task_conditions_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/task_conditions_model.py
from frameworks.wulf import ViewModel

class TaskConditionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TaskConditionsModel, self).__init__(properties=properties, commands=commands)

    def getCondition(self):
        return self._getString(0)

    def setCondition(self, value):
        self._setString(0, value)

    def getLastValue(self):
        return self._getNumber(1)

    def setLastValue(self, value):
        self._setNumber(1, value)

    def getCurrentValue(self):
        return self._getNumber(2)

    def setCurrentValue(self, value):
        self._setNumber(2, value)

    def getMaxValue(self):
        return self._getNumber(3)

    def setMaxValue(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(TaskConditionsModel, self)._initialize()
        self._addStringProperty('condition', '')
        self._addNumberProperty('lastValue', 0)
        self._addNumberProperty('currentValue', 0)
        self._addNumberProperty('maxValue', 0)
