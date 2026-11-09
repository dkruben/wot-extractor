# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/comparison_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/comparison_model.py
from frameworks.wulf import ViewModel

class ComparisonModel(ViewModel):
    __slots__ = ('onAddToComparison', )
    ENABLED = 'enabled'
    DISABLED_FULL_BASKET = 'disabledFullBasket'
    DISABLED_ON_SERVER = 'disabledOnServer'
    CAN_NOT_COMPARE = 'canNotCompare'

    def __init__(self, properties=1, commands=1):
        super(ComparisonModel, self).__init__(properties=properties, commands=commands)

    def getStatus(self):
        return self._getString(0)

    def setStatus(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(ComparisonModel, self)._initialize()
        self._addStringProperty('status', '')
        self.onAddToComparison = self._addCommand('onAddToComparison')
