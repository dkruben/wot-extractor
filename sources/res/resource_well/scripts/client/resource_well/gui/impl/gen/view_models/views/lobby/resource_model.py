# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resource_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resource_model.py
from frameworks.wulf import ViewModel

class ResourceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ResourceModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getInventoryCount(self):
        return self._getNumber(1)

    def setInventoryCount(self, value):
        self._setNumber(1, value)

    def getLimit(self):
        return self._getNumber(2)

    def setLimit(self, value):
        self._setNumber(2, value)

    def getBalance(self):
        return self._getNumber(3)

    def setBalance(self, value):
        self._setNumber(3, value)

    def getRate(self):
        return self._getReal(4)

    def setRate(self, value):
        self._setReal(4, value)

    def getTooltipId(self):
        return self._getString(5)

    def setTooltipId(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(ResourceModel, self)._initialize()
        self._addStringProperty('type', '')
        self._addNumberProperty('inventoryCount', 0)
        self._addNumberProperty('limit', 0)
        self._addNumberProperty('balance', 0)
        self._addRealProperty('rate', 0.0)
        self._addStringProperty('tooltipId', '')
