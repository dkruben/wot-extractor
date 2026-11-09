# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/tooltips/max_progress_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/tooltips/max_progress_tooltip_model.py
from frameworks.wulf import ViewModel

class MaxProgressTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MaxProgressTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCurrentValue(self):
        return self._getReal(0)

    def setCurrentValue(self, value):
        self._setReal(0, value)

    def getMaxValue(self):
        return self._getReal(1)

    def setMaxValue(self, value):
        self._setReal(1, value)

    def getResourceType(self):
        return self._getString(2)

    def setResourceType(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(MaxProgressTooltipModel, self)._initialize()
        self._addRealProperty('currentValue', 0.0)
        self._addRealProperty('maxValue', 0.0)
        self._addStringProperty('resourceType', '')
