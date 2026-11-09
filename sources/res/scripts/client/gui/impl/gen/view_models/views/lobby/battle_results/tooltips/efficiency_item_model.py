# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/tooltips/efficiency_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/tooltips/efficiency_item_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class Unit(Enum):
    SEC = 'sec'
    COUNT = 'count'


class EfficiencyItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(EfficiencyItemModel, self).__init__(properties=properties, commands=commands)

    def getLabel(self):
        return self._getResource(0)

    def setLabel(self, value):
        self._setResource(0, value)

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)

    def getValueType(self):
        return self._getResource(2)

    def setValueType(self, value):
        self._setResource(2, value)

    def _initialize(self):
        super(EfficiencyItemModel, self)._initialize()
        self._addResourceProperty('label', R.invalid())
        self._addRealProperty('value', 0.0)
        self._addResourceProperty('valueType', R.invalid())
